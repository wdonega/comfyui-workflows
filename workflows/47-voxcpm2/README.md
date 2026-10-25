# VoxCPM2 · TTS, voice design and cloning

[comfyui-workflows](../../README.md) › **VoxCPM2 · TTS, voice design and cloning**

The node's example with both modes: **VoxCPM2_TTS** creates the voice from a text description; **VoxCPM2_Clone** clones a reference (with its transcript in `prompt_text`). 48 kHz output.

| | |
|---|---|
| Status | ✅ tested |
| Family | VoxCPM2 |
| License | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Total download | 4.96 GB |
| Test | clone (9.4 s) and a voice described as "calm man, deep voice, Brazilian Portuguese" (7.0 s). The PT sentence was transcribed back by Qwen3-ASR and came out right (only "ComfyUI" turns into something like "Confiuí", normal for an English name). |
| Time | **1min 33s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 6581 MiB |

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
| ComfyUI-VoxCPM2 | `0e52a6c` | https://github.com/Saganaki22/ComfyUI-VoxCPM2 |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `tts/VoxCPM/VoxCPM2/` | `model.safetensors` | VoxCPM2 2B (weights) | 4.58 GB | [download](https://huggingface.co/openbmb/VoxCPM2/resolve/32279effe8c19989596f05d353d1447f51d9e915/model.safetensors) | [page](https://huggingface.co/openbmb/VoxCPM2) |
| `tts/VoxCPM/VoxCPM2/` | `audiovae.pth` | Audio VAE | 0.38 GB | [download](https://huggingface.co/openbmb/VoxCPM2/resolve/32279effe8c19989596f05d353d1447f51d9e915/audiovae.pth) | [page](https://huggingface.co/openbmb/VoxCPM2) |
| `tts/VoxCPM/VoxCPM2/` | `tokenizer.json` | config / tokenizer | 4 MB | [download](https://huggingface.co/openbmb/VoxCPM2/resolve/32279effe8c19989596f05d353d1447f51d9e915/tokenizer.json) | [page](https://huggingface.co/openbmb/VoxCPM2) |
| `tts/VoxCPM/VoxCPM2/` | `config.json` | config / tokenizer | 0 MB | [download](https://huggingface.co/openbmb/VoxCPM2/resolve/32279effe8c19989596f05d353d1447f51d9e915/config.json) | [page](https://huggingface.co/openbmb/VoxCPM2) |
| `tts/VoxCPM/VoxCPM2/` | `special_tokens_map.json` | config / tokenizer | 0 MB | [download](https://huggingface.co/openbmb/VoxCPM2/resolve/32279effe8c19989596f05d353d1447f51d9e915/special_tokens_map.json) | [page](https://huggingface.co/openbmb/VoxCPM2) |
| `tts/VoxCPM/VoxCPM2/` | `tokenization_voxcpm2.py` | config / tokenizer | 0 MB | [download](https://huggingface.co/openbmb/VoxCPM2/resolve/32279effe8c19989596f05d353d1447f51d9e915/tokenization_voxcpm2.py) | [page](https://huggingface.co/openbmb/VoxCPM2) |
| `tts/VoxCPM/VoxCPM2/` | `tokenizer_config.json` | config / tokenizer | 0 MB | [download](https://huggingface.co/openbmb/VoxCPM2/resolve/32279effe8c19989596f05d353d1447f51d9e915/tokenizer_config.json) | [page](https://huggingface.co/openbmb/VoxCPM2) |

<details><summary>SHA-256</summary>

```
f7f964cfa9da23653baec6e6f7750719977ad944ed9f95fe52fe3a620506891d  models/tts/VoxCPM/VoxCPM2/model.safetensors
94b5d51e107e0507d4acc976cfdadb64edd6fd06d1f751dadbf2fd1594274bf1  models/tts/VoxCPM/VoxCPM2/audiovae.pth
```

</details>

## How to use

1. The model (~5 GB) downloads itself on first use to `models/tts/VoxCPM/VoxCPM2/` ([openbmb/VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)).
2. Pip dependencies: `wetext inflect simplejson sortedcontainers soundfile` (`PIP_USER=true python3.13 -m pip install --no-deps` só do que faltar; veja `requirements.txt` do nó. Não instalar `onnxruntime-openvino` se já houver `onnxruntime`.). Do **not** install the `voxcpm` PyPI package (conflicts with `dill`); the node ships the code in `src/`.
3. `enable_denoiser` and `enable_asr` need `modelscope`/`funasr` (not installed); keep them off.

## License

Apache-2.0: free personal and commercial use, with no revenue or territory limits; just keep the license notices when redistributing the weights. The outputs are yours.

## Notes

- The test reference voice is synthetic (Qwen3-TTS "Serena" voice, 12.8 s in PT); no real voice was cloned. Cloning someone's voice requires that person's consent.
