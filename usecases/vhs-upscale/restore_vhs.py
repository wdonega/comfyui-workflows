#!/usr/bin/env python3
"""Restore VHS captures (and other old videos): ffmpeg cleanup + optional SeedVR2 upscale in ComfyUI.

Usage:
  restore_vhs.py [options] FILE... [-o FOLDER]
  restore_vhs.py birthday*.mpg                   # wildcard (expanded by the shell, or by the script when quoted)
  restore_vhs.py -r ~/tapes -o ~/restored        # whole folder, recursive
  restore_vhs.py a.mpg --color mild --upscale 1080 --model 7b
  restore_vhs.py a.mpg --upscale none            # ffmpeg cleanup only (fast)
  restore_vhs.py birthday*.mpg -t 5              # quick test: only the first 5 seconds of each video

Steps for each file:
  1. ffprobe: format, resolution, pixel aspect ratio, audio.
  2. Measurements: black borders (cropdetect), interlacing (idet).
  3. ffmpeg: crops borders and the head-switching noise at the bottom, deinterlaces if needed, smooths compression
     blocks, reduces noise, corrects color, converts to square pixels; audio: cuts hum and hiss, normalizes loudness.
  4. Upscale (default 720p, SeedVR2 3B): the video goes to ComfyUI in chunks and is joined at the end.
  5. Output: FOLDER/<name>_restored.mp4 (H.264 + AAC). The original is never modified.
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
import uuid
from collections import Counter
from pathlib import Path

COMFY_URL = os.environ.get('COMFY_URL', 'http://localhost:8188').rstrip('/')
COMFY_CONTAINER = os.environ.get('COMFY_CONTAINER')   # optional: local Docker container, used only to delete used chunks
TEMPLATE = Path(__file__).with_name('seedvr2_video.api.json')
EXTS = {'.mpg', '.mpeg', '.vob', '.avi', '.dv', '.mov', '.mp4', '.m4v', '.mkv', '.wmv', '.3gp', '.ts', '.m2ts', '.flv'}

COLORS = {
    'normalize': 'normalize=blackpt=black:whitept=white:smoothing=24:independence=0.6:strength=0.7',
    'mild': 'colortemperature=temperature=8500:mix=0.6,eq=saturation=1.05',
    'strong': 'colortemperature=temperature=10000:mix=0.7,eq=saturation=1.05',
    'auto': 'grayworld',
    'auto45': 'split[cx][cy];[cy]grayworld[cg];[cx][cg]blend=all_mode=normal:all_opacity=0.45',
    'colorcorrect': 'colorcorrect=analyze=median',
    'none': None,
}
MODELS = {'3b': 'seedvr2_3b_int8_convrot.safetensors', '7b': 'seedvr2_7b_int8_convrot.safetensors'}
CHUNK_S = {720: 20, 1080: 10}                                  # seconds per ComfyUI chunk (RAM limit)
FACTOR = {('3b', 720): 110, ('3b', 1080): 160, ('7b', 720): 130, ('7b', 1080): 200}  # GPU s per video s (measured/estimated)


def log(msg):
    print(f'[{time.strftime("%H:%M:%S")}] {msg}', flush=True)


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def ffmpeg(*args):
    run(['ffmpeg', '-v', 'error', '-y', *args])


# ---------- input ----------

def collect(inputs, recursive):
    files, errors = [], []
    for e in inputs:
        matches = sorted(glob.glob(os.path.expanduser(e))) if glob.has_magic(e) else [os.path.expanduser(e)]
        if not matches:
            errors.append(f'nothing matches "{e}"')
        for m in matches:
            p = Path(m)
            if p.is_dir():
                if not recursive:
                    errors.append(f'"{m}" is a folder: use -r to process the videos inside it')
                    continue
                files += sorted(f for f in p.rglob('*') if f.is_file() and f.suffix.lower() in EXTS)
            elif p.is_file():
                files.append(p)
            else:
                errors.append(f'"{m}" does not exist')
    return files, errors


# ---------- analysis ----------

def probe(f):
    d = json.loads(run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(f)]).stdout)
    v = next(s for s in d['streams'] if s['codec_type'] == 'video')
    sar = v.get('sample_aspect_ratio', '1:1')
    n, m = (int(x) for x in sar.split(':')) if re.fullmatch(r'\d+:\d+', sar) and not sar.startswith('0') else (1, 1)
    return {'w': v['width'], 'h': v['height'], 'sar': n / m, 'codec': v['codec_name'],
            'dur': float(d['format'].get('duration', 0)), 'audio': any(s['codec_type'] == 'audio' for s in d['streams'])}


def detect_borders(f, info):
    out = subprocess.run(['ffmpeg', '-v', 'info', '-t', '120', '-i', str(f), '-vf', 'cropdetect=limit=24:round=2', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    crops = re.findall(r'crop=(\d+):(\d+):(\d+):(\d+)', out)
    w, h, x, y = (int(v) for v in Counter(crops).most_common(1)[0][0]) if crops else (info['w'], info['h'], 0, 0)
    x += 2; w -= 4                                     # margin for the ragged VHS edge
    if info['h'] <= 576:                               # SD analog capture: head-switching noise at the bottom
        h = min(h, info['h'] - y - 12)
    return w - w % 2, h - h % 2, x, y


def interlaced(f):
    out = subprocess.run(['ffmpeg', '-v', 'info', '-t', '120', '-i', str(f), '-vf', 'idet', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    m = re.findall(r'Multi frame detection: TFF:\s*(\d+) BFF:\s*(\d+) Progressive:\s*(\d+)', out)
    if not m:
        return False
    tff, bff, prog = (int(v) for v in m[-1])
    return (tff + bff) > 0.25 * (tff + bff + prog)


# ---------- ffmpeg stage ----------

def clean(f, info, color, out_file, crf, start, duration):
    cw, ch, cx, cy = detect_borders(f, info)
    il = interlaced(f)
    sw = round(cw * info['sar'] / 2) * 2
    vf = [f'crop={cw}:{ch}:{cx}:{cy}']
    if il:
        vf.append('bwdif=mode=send_field:parity=auto')
    if info['codec'] in ('mpeg2video', 'mpeg1video', 'mpeg4', 'msmpeg4v3', 'wmv2', 'wmv3'):
        vf.append('deblock=filter=weak:block=8')
    vf.append('nlmeans=s=2.5:p=7:r=11')
    if COLORS[color]:
        vf.append(COLORS[color])
    vf += [f'scale={sw}:{ch}:flags=lanczos', 'setsar=1']
    cut = (['-ss', str(start)] if start else []) + (['-t', str(duration)] if duration else [])
    a = ['-af', 'highpass=f=60,afftdn=nf=-30,loudnorm=I=-18:TP=-1.5', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000'] if info['audio'] else ['-an']
    log(f'  borders {cw}x{ch}+{cx}+{cy}, {"interlaced → deinterlacing" if il else "progressive"}, color: {color}, output {sw}x{ch}')
    ffmpeg(*cut, '-i', str(f), '-vf', ','.join(vf), *a, '-c:v', 'libx264', '-crf', str(crf), '-preset', 'slow',
           '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(out_file))
    return sw, ch


# ---------- ComfyUI stage ----------

def comfy(path, data=None):
    req = urllib.request.Request(COMFY_URL + path, data=json.dumps(data).encode() if data else None,
                                 headers={'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())


def upload(path, name):
    """Sends a file to ComfyUI's input/vhs_restore folder (the /upload/image endpoint accepts any file)."""
    b = uuid.uuid4().hex
    body = b''.join([
        f'--{b}\r\nContent-Disposition: form-data; name="subfolder"\r\n\r\nvhs_restore\r\n'.encode(),
        f'--{b}\r\nContent-Disposition: form-data; name="overwrite"\r\n\r\ntrue\r\n'.encode(),
        f'--{b}\r\nContent-Disposition: form-data; name="image"; filename="{name}"\r\n'
        f'Content-Type: video/mp4\r\n\r\n'.encode(), Path(path).read_bytes(), f'\r\n--{b}--\r\n'.encode()])
    req = urllib.request.Request(COMFY_URL + '/upload/image', data=body,
                                 headers={'Content-Type': f'multipart/form-data; boundary={b}'})
    d = json.loads(urllib.request.urlopen(req, timeout=300).read())
    return f"{d['subfolder']}/{d['name']}" if d.get('subfolder') else d['name']


def download(out, dest):
    q = urllib.parse.urlencode({'filename': out['filename'], 'subfolder': out['subfolder'], 'type': out.get('type', 'output')})
    with urllib.request.urlopen(f'{COMFY_URL}/view?{q}', timeout=300) as r, open(dest, 'wb') as f:
        shutil.copyfileobj(r, f)


def cleanup(*paths):
    """The ComfyUI API cannot delete files; with COMFY_CONTAINER set, removes the used chunks through docker exec."""
    if COMFY_CONTAINER:
        try:
            run(['docker', 'exec', COMFY_CONTAINER, 'rm', '-f', *paths])
        except (OSError, subprocess.CalledProcessError):
            pass


def upscale_chunk(seg, name, W, H, model, dest):
    remote = upload(seg, f'{name}.mp4')
    p = json.loads(TEMPLATE.read_text())
    p['73']['inputs']['file'] = remote
    p['76']['inputs']['filename_prefix'] = f'vhs_restore/{name}'
    r = p['66:57']['inputs']
    for k in [k for k in r if k.startswith('resize_type.')]:
        del r[k]
    r.update({'resize_type': 'scale dimensions', 'resize_type.width': W, 'resize_type.height': H, 'resize_type.crop': 'disabled'})
    p['66:105']['inputs']['value'] = True            # automatic temporal chunks (fit in VRAM)
    p['66:99']['inputs']['temporal_overlap'] = 1
    p['66:59']['inputs']['color_correction_method'] = 'lab'
    p['66:52']['inputs']['unet_name'] = MODELS[model]
    d = comfy('/prompt', {'prompt': p, 'client_id': 'restore_vhs'})
    if d.get('node_errors'):
        raise RuntimeError(f'ComfyUI rejected the workflow: {d["node_errors"]}')
    pid, t0 = d['prompt_id'], time.time()
    while True:
        h = comfy(f'/history/{pid}').get(pid)
        if h and h['status'].get('status_str') in ('success', 'error'):
            break
        time.sleep(5)
    if h['status']['status_str'] != 'success':
        cleanup(f'/root/ComfyUI/input/{remote}')
        msg = [m[1].get('exception_message', '') for m in h['status']['messages'] if m[0] == 'execution_error']
        raise RuntimeError(f'ComfyUI error: {msg}')
    out = h['outputs']['76']['images'][0]
    download(out, dest)
    cleanup(f'/root/ComfyUI/input/{remote}', f"/root/ComfyUI/output/{out['subfolder']}/{out['filename']}")
    return time.time() - t0


def frame_count(f):
    return int(run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v', '-show_entries', 'stream=nb_read_packets',
                    '-of', 'csv=p=0', str(f)]).stdout.strip())


def upscale(cleaned, tmp, name, aspect, height, model, dur, crf, target):
    W = round(height * aspect / 16) * 16
    total = frame_count(cleaned)
    per = int(os.environ.get('RESTORE_VHS_CHUNK_FRAMES', CHUNK_S[height] * 30 + 1))  # 4n+1 (601 / 301): SeedVR2 keeps every frame
    assert per % 4 == 1, 'chunk size must be 4n+1 frames'
    n = -(-total // per)
    log(f'  upscale to {W}x{height} with SeedVR2 {model.upper()}: {total} frames in {n} chunk(s), '
        f'estimate ~{dur * FACTOR[(model, height)] / 3600:.1f} h of GPU (plus any ComfyUI queue)')
    parts = []
    for i in range(n):
        s, e = i * per, min((i + 1) * per, total)
        real = e - s
        pad = (-(real - 1)) % 4                        # repeat the last frame up to 4n+1; cut back after the upscale
        seg = tmp / f'seg_{i:04d}.mp4'
        ffmpeg('-i', str(cleaned), '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo',
               '-vf', f'trim=start_frame={s}:end_frame={e},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop={pad}',
               '-map', '0:v', '-map', '1:a', '-shortest', '-c:v', 'libx264', '-crf', '12', '-preset', 'fast',
               '-pix_fmt', 'yuv420p', '-c:a', 'aac', str(seg))
        res = tmp / f'res_{i:04d}.mp4'
        spent = upscale_chunk(seg, f'{name}_{os.getpid()}_{i:04d}', W, height, model, res)
        local = tmp / f'up_{i:04d}.mp4'
        ffmpeg('-i', str(res), '-frames:v', str(real), '-an', '-c:v', 'libx264', '-crf', '12', '-preset', 'fast',
               '-pix_fmt', 'yuv420p', str(local))
        got = frame_count(local)
        if got != real:
            raise RuntimeError(f'chunk {i + 1}: expected {real} frames, SeedVR2 returned {got}')
        seg.unlink()
        res.unlink()
        parts.append(local)
        log(f'  chunk {i + 1}/{n} done in {spent:.0f} s')
    lst = tmp / 'list.txt'
    lst.write_text(''.join(f"file '{p}'\n" for p in parts))
    audio = ['-i', str(cleaned), '-map', '0:v', '-map', '1:a?', '-c:a', 'copy']
    ffmpeg('-f', 'concat', '-safe', '0', '-i', str(lst), *audio, '-c:v', 'libx264', '-crf', str(crf), '-preset', 'slow',
           '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(target))   # no -shortest: it drops the last frame
    if frame_count(target) != total:
        raise RuntimeError(f'joined video has {frame_count(target)} frames, expected {total}')


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description='Restore VHS captures: ffmpeg cleanup + SeedVR2 upscale (ComfyUI).',
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__.split('Steps')[0])
    ap.add_argument('inputs', nargs='+', help='files, wildcards (birthday*.mpg) or folders (with -r)')
    ap.add_argument('-o', '--output', default='restored', help='output folder (default: ./restored)')
    ap.add_argument('-r', '--recursive', action='store_true', help='process folders, including subfolders')
    ap.add_argument('--color', choices=list(COLORS), default='normalize', help='color correction (default: normalize)')
    ap.add_argument('--upscale', choices=['720', '1080', 'none'], default='720', help='final upscale height (default: 720)')
    ap.add_argument('--model', choices=list(MODELS), default='3b', help='SeedVR2 model (default: 3b)')
    ap.add_argument('--start', type=float, metavar='SECONDS', help='start at this second (to test a section)')
    ap.add_argument('-t', '--max', dest='duration', type=float, metavar='SECONDS',
                    help='maximum length of each video, in seconds (default: the whole video); handy for a quick test')
    ap.add_argument('--overwrite', action='store_true', help='redo files that already exist in the output folder')
    ap.add_argument('--keep-temp', action='store_true', help='do not delete intermediate files')
    a = ap.parse_args()

    files, errors = collect(a.inputs, a.recursive)
    for e in errors:
        print(f'warning: {e}', file=sys.stderr)
    if not files:
        sys.exit('no videos to process')
    dest = Path(os.path.expanduser(a.output))
    if dest.exists() and not dest.is_dir():
        sys.exit(f'"{dest}" exists and is not a folder')
    dest.mkdir(parents=True, exist_ok=True)
    height = None if a.upscale == 'none' else int(a.upscale)
    if height:
        try:
            comfy('/system_stats')
        except Exception as e:
            sys.exit(f'ComfyUI does not answer at {COMFY_URL} ({e}); use --upscale none to only clean up')

    failures = 0
    for i, f in enumerate(files, 1):
        final = dest / f'{f.stem}_restored.mp4'
        log(f'[{i}/{len(files)}] {f}')
        if final.exists() and not a.overwrite:
            log(f'  already exists: {final} (use --overwrite to redo it)')
            continue
        tmp = Path(tempfile.mkdtemp(prefix=f'.{f.stem}_', dir=dest))
        t0 = time.time()
        try:
            info = probe(f)
            dur = a.duration or max(0.0, info['dur'] - (a.start or 0))
            if height:
                cleaned = tmp / 'cleaned.mp4'
                w, h = clean(f, info, a.color, cleaned, 14, a.start, a.duration)
                upscale(cleaned, tmp, re.sub(r'[^\w-]', '_', f.stem), w / h, height, a.model, dur, 18, final)
            else:
                clean(f, info, a.color, final, 18, a.start, a.duration)
            log(f'  ok: {final} ({time.time() - t0:.0f} s)')
        except Exception as e:
            failures += 1
            final.unlink(missing_ok=True)
            log(f'  ERROR: {e}' + (f' (intermediate files in {tmp})' if a.keep_temp else ''))
        finally:
            if not a.keep_temp:
                shutil.rmtree(tmp, ignore_errors=True)
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
