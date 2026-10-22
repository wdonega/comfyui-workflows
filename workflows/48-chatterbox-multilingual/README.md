# Chatterbox Multilingual · TTS with cloning (23 languages)

[comfyui-workflows](../../README.md) › **Chatterbox Multilingual · TTS with cloning (23 languages)**

The **FL Chatterbox Multilingual TTS** node (ResembleAI) cloning a reference voice in Portuguese (`Portuguese (pt)`). Uses ~3.7 GB VRAM.

| | |
|---|---|
| Status | ✅ tested |
| Family | Chatterbox |
| License | [MIT](https://opensource.org/license/mit) |
| Total download | 0 MB |
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

<details><summary>SHA-256</summary>

```
```

</details>

## How to use

1. The models download themselves on first use to `models/chatterbox/chatterbox_multilingual/` ([ResembleAI/chatterbox](https://huggingface.co/ResembleAI/chatterbox)).
2. Pip dependencies from the node's `requirements.txt` (`PIP_USER=true python3.13 -m pip install --no-deps` só do que faltar; veja `requirements.txt` do nó. Não instalar `onnxruntime-openvino` se já houver `onnxruntime`.).
3. Use **temperature 0.6**; at 0.8 it hallucinated after the end of the sentence.

## License

MIT: free personal and commercial use, no limits; just keep the copyright notice when redistributing the weights.

## Notes

- The automatic download leaves a ~3 GB copy in `~/.cache/huggingface/hub/models--ResembleAI--chatterbox` besides the `models/chatterbox` folder; the cache copy can be deleted.
- The node repository declares no license.
- The test reference voice is synthetic (Qwen3-TTS "Serena" voice, 12.8 s in PT); no real voice was cloned. Cloning someone's voice requires that person's consent.
