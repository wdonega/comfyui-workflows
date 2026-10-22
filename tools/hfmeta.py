"""Resolve arquivos do Hugging Face para URLs fixadas em commit, com SHA-256 e tamanho.

Uso: python3 hfmeta.py repo:caminho[@revisao] ...  -> JSON na saída padrão
Ex.: python3 hfmeta.py Comfy-Org/MiniMax-H3:vae/minimax_h3_audio_vae_fp32.safetensors
Repositórios gated precisam de HF_TOKEN no ambiente.
"""
import json
import sys

from huggingface_hub import HfApi

api = HfApi()
out = []
cache = {}
for arg in sys.argv[1:]:
    spec, _, rev = arg.partition("@")
    repo, _, path = spec.partition(":")
    key = (repo, rev or None)
    if key not in cache:
        cache[key] = api.model_info(repo, revision=rev or None, files_metadata=True)
    info = cache[key]
    sib = next(s for s in info.siblings if s.rfilename == path)
    out.append({
        "repo": repo,
        "path": path,
        "revision": info.sha,
        "url": f"https://huggingface.co/{repo}/resolve/{info.sha}/{path}",
        "page": f"https://huggingface.co/{repo}",
        "sha256": sib.lfs.sha256 if sib.lfs else None,
        "size": sib.size,
    })
json.dump(out, sys.stdout, indent=1)
