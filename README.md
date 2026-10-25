<p align="center"><img src="assets/logo.svg" alt="ComfyUI Workflows" width="100%"></p>

Language: **English** · [Português](README_ptBR.md)

# comfyui-workflows

**Tested** ComfyUI workflows from my homelab, each with everything needed to run it again on another
install: the workflow (UI and API), the list of components with destination folder, commit-pinned
download link and page, and an `install.sh` that installs everything on its own.

Test environment: ComfyUI v0.42.4 (`3f438ca6`) in Docker (`yanwk/comfyui-boot` cu130), Python 3.13,
torch 2.13 + CUDA 13.0, **RTX 5060 Ti 16 GB**, 61 GB of RAM. The GPU was dedicated to ComfyUI during the tests:
nothing else was running on it. The first workflows were built on v0.37.0 and all of them were run again on v0.42.4
(regression test); the times shown are from the latest run.

## What's here

```
workflows/<folder>/
├── README.md          components, folders, links, usage, license, test result (README_ptBR.md: Portuguese)
├── workflow.json      drag into the ComfyUI interface
├── workflow.api.json  API format (POST /prompt)
├── install.sh         installs custom nodes and models (self-contained)
└── components.json    data source for the READMEs and install.sh
lib/comfy_install.sh   install.sh functions (embedded into each one by the generator)
tools/                 generator and converters (see tools/README.md)
```

## Workflows

Every workflow below was tested on the setup described above; times are from those runs.

### Image

| Workflow | Family | What it does | Test time | Download | License |
|---|---|---|---|---|---|
| [Qwen-Image 2.1 Turbo](workflows/37-qwen-image-21-turbo/README.md) | Qwen-Image 2.1 | Turbo Qwen-Image 2.1: same quality, 2.4x faster | 10s · 1024² | 17.28 GB | Qwen Research (research only) |
| [Krea 2 Turbo](workflows/38-krea2-turbo/README.md) | Krea 2 | Text to image with a cinematic look, 8 steps | 23s · 1024² | 18.61 GB | Krea 2 Community (free < US$ 1M) |
| [Flux 3 Klein (distilled)](workflows/39-flux3-klein/README.md) | Flux 3 | Detail-rich text to image, with a prompt upsampler | 21s · 1024² | 17.75 GB | FLUX Kommunity (free < US$ 5M) |
| [MOSS-Image (SFT)](workflows/40-moss-image/README.md) | MOSS-Image | Text to image with a free license (Apache-2.0) | 35s · 1024² | 13.01 GB | Apache-2.0 (free) |
| [SeedVR2 · 4x upscale](workflows/42-seedvr2-upscale/README.md) | SeedVR2 | 4x image upscale in 1 step (a video version exists too) | 23s · 1024² → 4096² | 3.96 GB | Apache-2.0 (free) |
| [Qwen-Image 2.1 · instruction editing](workflows/qwen-image-21-edit/README.md) | Qwen-Image 2.1 | Edits a photo from text, with up to 10 reference images | 1min 17s · 896x1152 | 17.28 GB | Qwen Research (research only) |
| [Qwen-Image 2.1 · text to image](workflows/qwen-image-21-t2i/README.md) | Qwen-Image 2.1 | The official Qwen-Image 2.1 template (25 steps) | 26s · 1024² | 17.28 GB | Qwen Research (research only) |
| [Qwen-Image 2.1 · Viggle 4-step (editing)](workflows/qwen-image-21-viggle-edit/README.md) | Qwen-Image 2.1 | Instruction editing in 4 steps, up to 3 references, up to 4 MP output | 1min 23s · 2752x1536 | 17.62 GB | Qwen Research (research only) |
| [Qwen-Image 2.1 · Viggle 4-step (text to image)](workflows/qwen-image-21-viggle-t2i/README.md) | Qwen-Image 2.1 | Qwen-Image 2.1 in 4 steps with Viggle's turbo LoRA, up to 2 MP | 11s · 1920x1088 | 17.62 GB | Qwen Research (research only) |

### Video

| Workflow | Family | What it does | Test time | Download | License |
|---|---|---|---|---|---|
| [H3 Turbo v4 (larryvrh)](workflows/02-h3-turbo-v4/README.md) | MiniMax H3 | 4–8 step turbo LoRA with its own sampler (TaoMate alternative) | 16min 34s · 15 s | 40.85 GB | MiniMax H3 Community (⚠️ territory) |
| [LTX 2.3 · image to video with audio](workflows/04-ltx23-i2v/README.md) | LTX 2.3 | Image → video with audio and speech in 2 stages (fast) | 1min 35s · 4.8 s | 43.35 GB | LTX-2 Community (free < US$ 10M) |
| [Wan 2.2 5B · text/image to video](workflows/06-wan22-5b-ti2v/README.md) | Wan 2.2 | 5 s 720p video from text (or image), fits natively in 16 GB | 9min 10s · 5 s | 18.14 GB | Apache-2.0 (free) |
| [H3 Character Swap (Relay 2.0)](workflows/14-h3-character-swap/README.md) | MiniMax H3 | Swaps the character in a video while keeping performance, scene and audio | 12min 56s · 4 s | 46.33 GB | MiniMax H3 Community (⚠️ territory) |
| [Wan Animate 2 · animate a character with a video's motion](workflows/15-wan-animate-2/README.md) | Wan 2.2 (Animate 2) | Transfers pose, body motion and expressions from a driving video to a character image | 7min 02s · 3.4 s | 24.91 GB | Apache-2.0 (free) |
| [Bernini-R · style transfer (anime / real life)](workflows/16-bernini-r-style-transfer/README.md) | Wan 2.2 (Bernini-R) | Video editing with Bernini-R; anime and real-life style LoRAs | 18min 33s · 4,9 s | 39.15 GB | Apache-2.0 (free) |
| [LTX 2.3 · Face Swap (head swap)](workflows/17-ltx23-face-swap/README.md) | LTX 2.3 | Swaps a person's head/face in a video keeping body, clothing, motion and audio | 6min 45s · 4 s | 44.71 GB | LTX-2 Community (free < US$ 10M) |
| [H3 HR Endless Sampler (Gemma 4 directs the chunks)](workflows/23-h3-hr-endless-sampler/README.md) | MiniMax H3 | Long video in chunks; a local Gemma 4 plans the production and writes each chunk's prompt | 16min 36s · 6.6 s | 50.11 GB | MiniMax H3 Community (⚠️ territory) |
| [H3 Long Video (LLM-split prompt)](workflows/24-h3-long-video/README.md) | MiniMax H3 | Long videos from chained segments, with the prompt split by an LLM | 11min 26s · 16 s | 44.43 GB | MiniMax H3 Community (⚠️ territory) |
| [Herrgott's H3 Infinite Continuation (v1.4)](workflows/25-h3-infinite-continuation/README.md) | MiniMax H3 | Chains FL2VA clips with safe handover and joins them without visible seams | 22min 31s · 8.7 s (2 clips) | 42.47 GB | MiniMax H3 Community (⚠️ territory) |
| [LTX 2.3 · Foley (sound for silent video)](workflows/33-ltx23-foley-v2a/README.md) | LTX 2.3 | Generates synchronized sound effects for a silent video | 32min 09s · 7 s | 39.07 GB | LTX-2 Community (free < US$ 10M) |
| [H3 Realism People](workflows/59-h3-realism-people/README.md) | MiniMax H3 | Realism LoRA for people (trigger r34l1sm) | 1min 55s · 5 s | 42.69 GB | MiniMax H3 Community (⚠️ territory) |
| [LTX 2.3 · Clean Plate (removes people from video)](workflows/60-ltx23-clean-plate/README.md) | LTX 2.3 | Erases people and moving objects and returns the empty background | 3min 39s · 4 s | 42.68 GB | LTX-2 Community (free < US$ 10M) |
| [H3 Director · TaoMate 3-step (timeline)](workflows/h3-director-3step/README.md) | MiniMax H3 | 15 s video with audio, built on a timeline of segments | 10min 10s · 15 s | 63.53 GB | MiniMax H3 Community (⚠️ territory) |
| [H3 Ref2VA · TaoMate 3 steps](workflows/h3-ref2va-taomate-3step/README.md) | MiniMax H3 | Video+audio from a reference image in 3 steps | 8min 39s · 15 s | 42.55 GB | MiniMax H3 Community (⚠️ territory) |

### Audio

| Workflow | Family | What it does | Test time | Download | License |
|---|---|---|---|---|---|
| [ACE-Step 1.5 Turbo · music](workflows/32-ace-step-15-turbo/README.md) | ACE-Step 1.5 | Songs with lyrics in 8 steps; 30 s in 16 s | 16s · 30 s | 10.03 GB | MIT (free) |
| [Fish Audio Drama 3 · voice cloning](workflows/46-fish-drama3-voice-clone/README.md) | Fish Audio Drama 3 | Expressive 35B TTS with cloning, cues like [laughs] and multiple speakers | 1min 04s · 8.6 s | 44.34 GB | Fish Audio Community (commercial < US$ 500K) |
| [VoxCPM2 · TTS, voice design and cloning](workflows/47-voxcpm2/README.md) | VoxCPM2 | 2B TTS in 30 languages, 48 kHz: voice from a description or cloned | 1min 33s · 2 × ~8 s | 4.96 GB | Apache-2.0 (free) |
| [Chatterbox Multilingual · TTS with cloning (23 languages)](workflows/48-chatterbox-multilingual/README.md) | Chatterbox | Light, fast TTS with cloning, Portuguese included | 11s · 8.6 s | 3.21 GB | MIT (free) |
| [Qwen3-TTS · built-in voices and cloning](workflows/49-qwen3-tts/README.md) | Qwen3-TTS | 1.7B TTS in 10 languages (PT included): 9 built-in voices, cloning and voice design | 1min 29s · 12.8 s + 7.5 s | 9.75 GB | Apache-2.0 (free) |
| [MiniMax Music 3 · songs with lyrics](workflows/minimax-music3/README.md) | MiniMax Music 3 | Generates a song of up to a few minutes from style + lyrics | 2min 26s · 60 s | 14.33 GB | MiniMax-Music3 Community |

Times measured on the RTX 5060 Ti 16 GB with the parameters described in each folder's README
(execution inside ComfyUI, without queue; peak VRAM is in each folder's README). "Download" is the workflow's total model size,
counting files shared with other workflows.

## Use cases and scripts

Complete jobs that combine workflows from this repo with ffmpeg and a script. Each folder has the script, the workflow it sends to ComfyUI and a README with the decisions and tests behind it.

| Use case | What it does | Workflows used | Script |
|---|---|---|---|
| [VHS tape restoration](usecases/vhs-upscale/README.md) | Cleans old captures (borders, noise, color, audio) with ffmpeg and upscales them with SeedVR2, in batch | [SeedVR2 · 4x upscale](workflows/42-seedvr2-upscale/README.md) | [`restore_vhs.py`](usecases/vhs-upscale/restore_vhs.py) |

## Installing a workflow

```bash
# on the ComfyUI machine
bash workflows/<folder>/install.sh /path/to/ComfyUI

# ComfyUI in Docker (container "comfyui"): the script goes through standard input
docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < workflows/<folder>/install.sh
```

The script only runs if the folder is the **ComfyUI root** (`main.py`, `folder_paths.py`, `models/`,
`custom_nodes/`). If you point it at a subfolder (for example `models/`), it tells you where the root is.
Existing files with the right size are skipped; new downloads have their SHA-256 checked.
Gated repositories need the license accepted on Hugging Face and `HF_TOKEN` in the environment.

## Licenses

The content of this repository (scripts, `lib/`, `tools/`, READMEs and the workflows assembled here) is
under **[0BSD](LICENSE)**: use, copy and modify it freely, no credit required.
Redistributed third-party workflows (noted in the folder's README) keep their author's license, and the
**models** downloaded by the `install.sh` scripts have their own licenses, summarized in each folder (not
legal advice). Pay special attention to:

- **MiniMax H3**: prohibited in the US, EU, UK and South Korea, **including the outputs**.
  Do not use the videos in globally published projects.
- **Qwen-Image 2.1**: research and evaluation only.

## Maintenance

```bash
python3 tools/gen.py      # regenerates README.md, README_ptBR.md and install.sh from components.json
```

To add a workflow: create `workflows/<folder>/` with `workflow.json`, `workflow.api.json` and
`components.json` (copy an existing one as a template; translatable texts are `{"pt": ..., "en": ...}`; `kind` is `image`, `video` or `audio`)
and run the generator.

---

Independent project, not affiliated with or endorsed by Comfy Org. The logo uses original lettering; "ComfyUI" is used only to say what these workflows are for.

To add a use case: create `usecases/<folder>/` with the script, its README.md/README_ptBR.md (written by hand) and a
`usecase.json` (`title`, `short`, `workflows` with the folder names used, `script`); the generator adds it to the table above.
