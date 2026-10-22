"""Gera os READMEs (inglês e português) e o install.sh de cada workflow, e os READMEs gerais.

Uso: python3 tools/gen.py
Fonte única: workflows/<pasta>/components.json. Textos traduzíveis ficam como {"pt": ..., "en": ...}.
Saídas: README.md (inglês, principal) e README_ptBR.md (português), com seletor de idioma no topo.
Metadados do Hugging Face (URL fixada em commit, SHA-256, tamanho) vêm de tools/.hf_cache.json; o que
faltar é resolvido com tools/hfmeta.py (precisa de huggingface_hub; em repos gated, HF_TOKEN).
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "tools" / ".hf_cache.json"
LIB = (ROOT / "lib" / "comfy_install.sh").read_text()

LANGS = {"en": "README.md", "pt": "README_ptBR.md"}

L = {
    "en": {
        "switch": "Language: **English** · [Português](README_ptBR.md)",
        "status": {"testado": "✅ tested", "parcial": "⚠️ partial", "falhou": "❌ failed", "pendente": "⏳ pending"},
        "plan": "Plan item", "family": "Family", "license": "License", "download": "Total download",
        "test": "Test", "time": "Time", "vram": "Peak VRAM", "not_measured": "not measured",
        "files": "Files in this folder", "file": "File", "what": "What it is",
        "wf_ui": "Workflow to drag into the ComfyUI interface",
        "wf_api": "Same workflow in API format (test parameters, example inputs)",
        "install_sh": "Installs custom nodes and downloads the models into the right folders",
        "components": "Source of this README and of install.sh",
        "install": "Installation",
        "install_cmt1": "# on the ComfyUI machine (the script checks that the folder is the ComfyUI root)",
        "install_cmt2": "# ComfyUI in Docker (container \"comfyui\")",
        "install_txt": "Files that already exist with the right size are skipped. New downloads have their SHA-256 checked "
                       "(`VERIFY_EXISTING=1` also checks the existing ones).",
        "nodes": "Custom nodes", "node": "Node", "tested_ver": "Tested version", "page": "Page",
        "models": "Models", "folder": "Folder (`models/…`)", "role": "Role", "size": "Size",
        "link": "link", "page_lnk": "page",
        "usage": "How to use", "notes": "Notes",
        "tbl": ["Workflow", "Item", "Family", "What it does", "Status", "Test time", "VRAM", "Download", "License"],
    },
    "pt": {
        "switch": "Idioma: [English](README.md) · **Português**",
        "status": {"testado": "✅ testado", "parcial": "⚠️ parcial", "falhou": "❌ falhou", "pendente": "⏳ pendente"},
        "plan": "Item do plano", "family": "Família", "license": "Licença", "download": "Download total",
        "test": "Teste", "time": "Tempo", "vram": "Pico de VRAM", "not_measured": "não medido",
        "files": "Arquivos desta pasta", "file": "Arquivo", "what": "O que é",
        "wf_ui": "Workflow para arrastar na interface do ComfyUI",
        "wf_api": "Mesmo workflow no formato da API (parâmetros do teste, entradas de exemplo)",
        "install_sh": "Instala custom nodes e baixa os modelos para as pastas certas",
        "components": "Fonte dos dados deste README e do install.sh",
        "install": "Instalação",
        "install_cmt1": "# na máquina com o ComfyUI (o script confere se a pasta é a raiz do ComfyUI)",
        "install_cmt2": "# ComfyUI em Docker (container \"comfyui\")",
        "install_txt": "Arquivos que já existem com o tamanho certo são pulados. Downloads novos têm o SHA-256 conferido "
                       "(`VERIFY_EXISTING=1` confere também os que já existiam).",
        "nodes": "Custom nodes", "node": "Nó", "tested_ver": "Versão testada", "page": "Página",
        "models": "Modelos", "folder": "Pasta (`models/…`)", "role": "Papel", "size": "Tamanho",
        "link": "link", "page_lnk": "página",
        "usage": "Como usar", "notes": "Observações",
        "tbl": ["Workflow", "Item", "Família", "O que faz", "Status", "Tempo do teste", "VRAM", "Download", "Licença"],
    },
}


def tr(x, lang):
    """Texto no idioma pedido; aceita string simples (igual nos dois) ou {"pt":…, "en":…}."""
    return x.get(lang) or x.get("pt") if isinstance(x, dict) else x


def hf_meta(specs):
    cache = {f"{x['repo']}:{x['path']}@{x['revision']}": x for x in json.loads(CACHE.read_text())} if CACHE.exists() else {}
    by_short = {f"{x['repo']}:{x['path']}": x for x in cache.values()}

    def lookup(spec):
        return cache.get(spec) or (by_short.get(spec) if "@" not in spec else None) or next(
            (x for k, x in cache.items() if k.startswith(spec.split("@")[0] + "@") and spec.split("@")[1] in x["revision"]), None)

    missing = [s for s in specs if lookup(s) is None]
    if missing:
        res = subprocess.run([sys.executable, str(ROOT / "tools" / "hfmeta.py"), *missing], capture_output=True, text=True, check=True)
        for x in json.loads(res.stdout):
            cache[f"{x['repo']}:{x['path']}@{x['revision']}"] = x
        CACHE.write_text(json.dumps(list(cache.values()), indent=1))
        by_short.update({f"{x['repo']}:{x['path']}": x for x in cache.values()})
    return {s: lookup(s) for s in specs}


def gb(size):
    return f"{size / 1e9:.2f} GB" if size >= 1e8 else f"{size / 1e6:.0f} MB"


def fmt_time(s):
    return f"{s // 60}min {s % 60:02d}s" if s >= 60 else f"{s}s"


def resolve_models(c):
    meta = hf_meta([m["hf"] for m in c.get("models", []) if "hf" in m])
    models = []
    for m in c.get("models", []):
        if "hf" in m:
            x = meta[m["hf"]]
            models.append({**m, "file": m.get("file", x["path"].split("/")[-1]), "url": x["url"], "page": m.get("page", x["page"]),
                           "sha256": x["sha256"], "size": x["size"]})
        else:
            models.append(m)
    return models


def write_install(folder, c, models):
    lines = [
        "#!/usr/bin/env bash",
        f"# {tr(c['title'], 'en')}: installs custom nodes and models into ComfyUI.",
        "# Generated by tools/gen.py from components.json. Do not edit by hand.",
        "#",
        "# Usage:  bash install.sh /path/to/ComfyUI        (or COMFYUI_DIR=... bash install.sh)",
        "# Docker: docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh",
        "",
        LIB.strip(),
        "",
        'comfy_root "${1:-}"',
    ]
    for n in c.get("nodes", []):
        lines.append(f"registry_node {n['registry']} {n['version']}" if n.get("registry") else f"clone_node {n['url']} {n['commit']}")
    for m in models:
        lines.append(f"fetch_model {m['dest']} {m['file']} {m['url']} {m.get('sha256') or '-'} {m.get('size') or '-'}")
    for lk in c.get("links", []):
        lines.append(f"link_model {lk['dest']} {lk['link']} {lk['target']}")
    lines += ['log "pronto / done. Reinicie o ComfyUI se instalou custom nodes novos / restart ComfyUI if new custom nodes were installed."', ""]
    sh = folder / "install.sh"
    sh.write_text("\n".join(lines))
    sh.chmod(0o755)


def readme(c, models, total, lang):
    s = L[lang]
    t = c.get("test", {})
    lic = c["license"]
    r = [s["switch"], "", f"# {tr(c['title'], lang)}", "", tr(c["summary"], lang), ""]
    r += ["| | |", "|---|---|",
          f"| {s['plan']} | {c.get('plan', '—')} |",
          f"| Status | {s['status'].get(c['status'], c['status'])} |",
          f"| {s['family']} | {c.get('family', '—')} |",
          f"| {s['license']} | [{lic['name']}]({lic['url']}) |",
          f"| {s['download']} | {gb(total)} |"]
    if t:
        r += [f"| {s['test']} | {tr(t['what'], lang)} |",
              f"| {s['time']} | **{fmt_time(t['time_s'])}** ({t['gpu']}, {t['date']}) |",
              f"| {s['vram']} | {str(t['vram_mib']) + ' MiB' if t.get('vram_mib') else s['not_measured']} |"]
    files = c.get("files") or {"workflow.json": s["wf_ui"], "workflow.api.json": s["wf_api"]}
    r += ["", f"## {s['files']}", "", f"| {s['file']} | {s['what']} |", "|---|---|"]
    r += [f"| `{f}` | {tr(d, lang)} |" for f, d in files.items()]
    r += [f"| `install.sh` | {s['install_sh']} |", f"| `components.json` | {s['components']} |", ""]
    r += [f"## {s['install']}", "", "```bash", s["install_cmt1"], "bash install.sh /path/to/ComfyUI", "",
          s["install_cmt2"], "docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh", "```", "",
          s["install_txt"], ""]
    if c.get("nodes"):
        r += [f"## {s['nodes']}", "", f"| {s['node']} | {s['tested_ver']} | {s['page']} |", "|---|---|---|"]
        for n in c["nodes"]:
            ver = n["version"] if n.get("registry") else f"`{n['commit'][:7]}`"
            r.append(f"| {n['name']} | {ver} | {n['page']} |")
        r.append("")
    r += [f"## {s['models']}", "", f"| {s['folder']} | {s['file']} | {s['role']} | {s['size']} | Download | {s['page']} |",
          "|---|---|---|---|---|---|"]
    for m in models:
        r.append(f"| `{m['dest']}/` | `{m['file']}` | {tr(m.get('role', ''), lang)} | {gb(m['size']) if m.get('size') else '—'} "
                 f"| [download]({m['url']}) | [{s['page_lnk']}]({m['page']}) |")
    for lk in c.get("links", []):
        r.append(f"| `{lk['dest']}/` | `{lk['link']}` | {s['link']} → `{lk['target']}` ({tr(lk.get('why', ''), lang)}) | — | — | — |")
    r += ["", "<details><summary>SHA-256</summary>", "", "```"]
    r += [f"{m['sha256']}  models/{m['dest']}/{m['file']}" for m in models if m.get("sha256")]
    r += ["```", "", "</details>", ""]
    if c.get("usage"):
        r += [f"## {s['usage']}", "", tr(c["usage"], lang).strip(), ""]
    r += [f"## {s['license']}", "", tr(lic["summary"], lang).strip(), ""]
    if c.get("notes"):
        r += [f"## {s['notes']}", "", tr(c["notes"], lang).strip(), ""]
    return "\n".join(r)


def main():
    rows = []
    for folder in sorted((ROOT / "workflows").iterdir()):
        if not (folder / "components.json").exists():
            continue
        c = json.loads((folder / "components.json").read_text())
        models = resolve_models(c)
        total = sum(m.get("size") or 0 for m in models)
        write_install(folder, c, models)
        for lang, fname in LANGS.items():
            (folder / fname).write_text(readme(c, models, total, lang))
        rows.append((folder.name, c, total))
        print(f"ok  {folder.name}")
    for lang, fname in LANGS.items():
        s = L[lang]
        table = ["| " + " | ".join(s["tbl"]) + " |", "|" + "---|" * len(s["tbl"])]
        for name, c, total in rows:
            t = c.get("test", {})
            table.append(
                f"| [{tr(c['title'], lang)}](workflows/{name}/{fname}) | {c.get('plan', '—')} | {c.get('family', '—')} "
                f"| {tr(c['short'], lang)} | {s['status'].get(c['status'], c['status'])} "
                f"| {fmt_time(t['time_s']) + ' · ' + tr(t['clip'], lang) if t else '—'} "
                f"| {str(round(t['vram_mib'] / 1024, 1)) + ' GB' if t.get('vram_mib') else '—'} | {gb(total)} "
                f"| {tr(c['license']['short'], lang)} |")
        head = (ROOT / "tools" / f"README.head.{lang}.md").read_text().strip()
        tail = (ROOT / "tools" / f"README.tail.{lang}.md").read_text().strip()
        (ROOT / fname).write_text(s["switch"] + "\n\n" + head + "\n\n" + "\n".join(table) + "\n\n" + tail + "\n")
        print(f"ok  {fname}")


if __name__ == "__main__":
    main()
