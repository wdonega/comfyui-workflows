# Chatterbox Multilingual · TTS with cloning (23 languages)

[comfyui-workflows](../../README.md) › **Chatterbox Multilingual · TTS with cloning (23 languages)**

The **FL Chatterbox Multilingual TTS** node (ResembleAI) cloning a reference voice in Portuguese (`Portuguese (pt)`). Uses ~3.7 GB VRAM.

| | |
|---|---|
| Status | ✅ tested |
| Family | Chatterbox |
| License | [MIT](https://opensource.org/license/mit) |
| Total download | 3.21 GB |
| Test | temperature 0.6: 8.6 s with just the sentence. With the default temperature (0.8) the model kept going ~30 s of babble after the sentence. The PT sentence was transcribed back by Qwen3-ASR and came out right (only "ComfyUI" turns into something like "Confiuí", normal for an English name). |
| Time | **11s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 3729 MiB |

## Files in this folder

| File | What it is |
|---|---|
| `workflow.json` | Workflow to drag into the ComfyUI interface |
| `workflow.api.json` | Same workflow in API format (test parameters, example inputs) |
| `install.sh` | Installs custom nodes and downloads the models into the right folders |
| `components.json` | Source of this README and of install.sh |

## Installation

```bash
# on the ComfyUI machine (the script checks that the folder is the ComfyUI root)
bash install.sh /path/to/ComfyUI

# ComfyUI in Docker (container "comfyui")
docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh
```

Files that already exist with the right size are skipped. New downloads have their SHA-256 checked (`VERIFY_EXISTING=1` also checks the existing ones).

## Custom nodes

| Node | Tested version | Page |
|---|---|---|
| ComfyUI_Fill-ChatterBox | `f7d7a16` | https://github.com/filliptm/ComfyUI_Fill-ChatterBox |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `chatterbox/chatterbox_multilingual/` | `t3_mtl23ls_v2.safetensors` | Multilingual T3 v2 (text → speech tokens) | 2.14 GB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/t3_mtl23ls_v2.safetensors) | [page](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `s3gen.pt` | S3Gen (tokens → audio) | 1.06 GB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/s3gen.pt) | [page](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `ve.pt` | Voice encoder | 6 MB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/ve.pt) | [page](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `conds.pt` | Default voice | 0 MB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/conds.pt) | [page](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `Cangjie5_TC.json` | config / tokenizer | 2 MB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/Cangjie5_TC.json) | [page](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `grapheme_mtl_merged_expanded_v1.json` | config / tokenizer | 0 MB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/grapheme_mtl_merged_expanded_v1.json) | [page](https://huggingface.co/ResembleAI/chatterbox) |

<details><summary>SHA-256</summary>

```
b1237586127ce98e7800a68e49938eb5092846862aabcb6e17b2fda7889a6c75  models/chatterbox/chatterbox_multilingual/t3_mtl23ls_v2.safetensors
9b9ff07e60b20c136e2b1b3d7563a24604e8d2c4c267888d1ee929dd0151d2a3  models/chatterbox/chatterbox_multilingual/s3gen.pt
4b16d836bc598509860f6fa068165a8bb5e9ac84f05582dfcf278a5a372879f1  models/chatterbox/chatterbox_multilingual/ve.pt
6552d70568833628ba019c6b03459e77fe71ca197d5c560cef9411bee9d87f4e  models/chatterbox/chatterbox_multilingual/conds.pt
```

</details>

## How to use

1. The models download themselves on first use to `models/chatterbox/chatterbox_multilingual/` ([ResembleAI/chatterbox](https://huggingface.co/ResembleAI/chatterbox)).
2. Pip dependencies from the node's `requirements.txt` (`PIP_USER=true python3.13 -m pip install --no-deps` só do que faltar; veja `requirements.txt` do nó. Não instalar `onnxruntime-openvino` se já houver `onnxruntime`.).
3. Use **temperature 0.6**; at 0.8 it hallucinated after the end of the sentence.

## License

MIT: free personal and commercial use, no limits; just keep the copyright notice when redistributing the weights.

## Notes

- The node repository declares no license.
- The test reference voice is synthetic (Qwen3-TTS "Serena" voice, 12.8 s in PT); no real voice was cloned. Cloning someone's voice requires that person's consent.
