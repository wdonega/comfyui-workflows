"""Gera README.md + install.sh de cada workflow e o README geral a partir dos components.json.

Uso: python3 tools/gen.py
Fonte única: workflows/<pasta>/components.json. Metadados do Hugging Face (URL fixada em commit,
SHA-256, tamanho) vêm de tools/.hf_cache.json; o que faltar é resolvido com tools/hfmeta.py
(precisa de huggingface_hub; em repos gated, HF_TOKEN).
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "tools" / ".hf_cache.json"
LIB = (ROOT / "lib" / "comfy_install.sh").read_text()

STATUS = {
    "testado": "✅ testado",
    "parcial": "⚠️ parcial",
    "falhou": "❌ falhou",
    "pendente": "⏳ pendente",
}


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


def build(folder):
    c = json.loads((folder / "components.json").read_text())
    meta = hf_meta([m["hf"] for m in c.get("models", []) if "hf" in m])
    models = []
    for m in c.get("models", []):
        if "hf" in m:
            x = meta[m["hf"]]
            models.append({**m, "file": m.get("file", x["path"].split("/")[-1]), "url": x["url"], "page": m.get("page", x["page"]),
                           "sha256": x["sha256"], "size": x["size"]})
        else:
            models.append(m)
    c["_models"] = models
    total = sum(m.get("size") or 0 for m in models)

    # ---- install.sh (autocontido: a lib vai embutida) ----
    lines = [
        "#!/usr/bin/env bash",
        f"# {c['title']}: instala custom nodes e modelos no ComfyUI.",
        "# Gerado por tools/gen.py a partir de components.json. Não edite à mão.",
        "#",
        "# Uso:  bash install.sh /caminho/do/ComfyUI        (ou COMFYUI_DIR=... bash install.sh)",
        "# Docker: docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh",
        "",
        LIB.strip(),
        "",
        'comfy_root "${1:-}"',
    ]
    for n in c.get("nodes", []):
        if n.get("registry"):
            lines.append(f"registry_node {n['registry']} {n['version']}")
        else:
            lines.append(f"clone_node {n['url']} {n['commit']}")
    for m in models:
        lines.append(f"fetch_model {m['dest']} {m['file']} {m['url']} {m.get('sha256') or '-'} {m.get('size') or '-'}")
    for lk in c.get("links", []):
        lines.append(f"link_model {lk['dest']} {lk['link']} {lk['target']}")
    lines += ['log "pronto. Reinicie o ComfyUI se instalou custom nodes novos."', ""]
    sh = folder / "install.sh"
    sh.write_text("\n".join(lines))
    sh.chmod(0o755)

    # ---- README.md da pasta ----
    t = c.get("test", {})
    r = [f"# {c['title']}", "", c["summary"], ""]
    r += ["| | |", "|---|---|",
          f"| Item do plano | {c.get('plan', '—')} |",
          f"| Status | {STATUS.get(c['status'], c['status'])} |",
          f"| Família | {c.get('family', '—')} |",
          f"| Licença | [{c['license']['name']}]({c['license']['url']}) |",
          f"| Download total | {gb(total)} |"]
    if t:
        r += [f"| Teste | {t['what']} |",
              f"| Tempo | **{fmt_time(t['time_s'])}** ({t['gpu']}, {t['date']}) |",
              f"| Pico de VRAM | {str(t['vram_mib']) + ' MiB' if t.get('vram_mib') else 'não medido'} |"]
    files = c.get("files") or {
        "workflow.json": "Workflow para arrastar na interface do ComfyUI",
        "workflow.api.json": "Mesmo workflow no formato da API (parâmetros do teste, entradas de exemplo)",
    }
    r += ["", "## Arquivos desta pasta", "", "| Arquivo | O que é |", "|---|---|"]
    r += [f"| `{f}` | {d} |" for f, d in files.items()]
    r += ["| `install.sh` | Instala custom nodes e baixa os modelos para as pastas certas |",
          "| `components.json` | Fonte dos dados deste README e do install.sh |", ""]
    r += ["## Instalação", "", "```bash", "# na máquina com o ComfyUI (o script confere se a pasta é a raiz do ComfyUI)",
          "bash install.sh /caminho/do/ComfyUI", "", "# ComfyUI em Docker (container \"comfyui\")",
          "docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh", "```", "",
          "Arquivos que já existem com o tamanho certo são pulados. Downloads novos têm o SHA-256 conferido "
          "(`VERIFY_EXISTING=1` confere também os que já existiam).", ""]
    if c.get("nodes"):
        r += ["## Custom nodes", "", "| Nó | Versão testada | Página |", "|---|---|---|"]
        for n in c["nodes"]:
            ver = n["version"] if n.get("registry") else f"`{n['commit'][:7]}`"
            r.append(f"| {n['name']} | {ver} | {n['page']} |")
        r.append("")
    r += ["## Modelos", "", "| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |", "|---|---|---|---|---|---|"]
    for m in models:
        r.append(f"| `{m['dest']}/` | `{m['file']}` | {m.get('role', '')} | {gb(m['size']) if m.get('size') else '—'} "
                 f"| [download]({m['url']}) | [página]({m['page']}) |")
    for lk in c.get("links", []):
        r.append(f"| `{lk['dest']}/` | `{lk['link']}` | link → `{lk['target']}` ({lk.get('why', '')}) | — | — | — |")
    r += ["", "<details><summary>SHA-256</summary>", "", "```"]
    r += [f"{m['sha256']}  models/{m['dest']}/{m['file']}" for m in models if m.get("sha256")]
    r += ["```", "", "</details>", ""]
    if c.get("usage"):
        r += ["## Como usar", "", c["usage"].strip(), ""]
    r += ["## Licença", "", c["license"]["summary"].strip(), ""]
    if c.get("notes"):
        r += ["## Observações", "", c["notes"].strip(), ""]
    (folder / "README.md").write_text("\n".join(r))
    return c, total


def main():
    rows = []
    for folder in sorted((ROOT / "workflows").iterdir()):
        if (folder / "components.json").exists():
            c, total = build(folder)
            rows.append((folder.name, c, total))
            print(f"ok  {folder.name}")
    head = (ROOT / "tools" / "README.head.md").read_text().strip()
    table = ["| Workflow | Item | Família | O que faz | Status | Tempo do teste | VRAM | Download | Licença |",
             "|---|---|---|---|---|---|---|---|---|"]
    for name, c, total in rows:
        t = c.get("test", {})
        table.append(
            f"| [{c['title']}](workflows/{name}/) | {c.get('plan', '—')} | {c.get('family', '—')} | {c['short']} "
            f"| {STATUS.get(c['status'], c['status'])} | {fmt_time(t['time_s']) + ' · ' + t['clip'] if t else '—'} "
            f"| {str(round(t['vram_mib'] / 1024, 1)) + ' GB' if t.get('vram_mib') else '—'} | {gb(total)} | {c['license']['short']} |")
    tail = (ROOT / "tools" / "README.tail.md").read_text().strip()
    (ROOT / "README.md").write_text(head + "\n\n" + "\n".join(table) + "\n\n" + tail + "\n")
    print("ok  README.md")


if __name__ == "__main__":
    main()
