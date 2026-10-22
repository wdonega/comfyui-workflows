# Fish Audio Drama 3 · voice cloning

[comfyui-workflows](../../README.md) › **Fish Audio Drama 3 · voice cloning**

The node's `drama3_voice_clone` example: Qwen3-ASR transcribes the reference voice, Drama 3 encodes the voice and speaks the text (accepts cues like `[laughs]`, `[whispers]`). **int8experts** variant: ~6 GB of the model on the GPU and the experts in **RAM** (~48 GB free RAM).

| | |
|---|---|
| Status | ✅ tested |
| Family | Fish Audio Drama 3 |
| License | [Fish Audio Community License](https://huggingface.co/fishaudio/drama-3) |
| Total download | 44.34 GB |
| Test | cloning the synthetic voice with the PT sentence (8.6 s, 44.1 kHz). The PT sentence was transcribed back by Qwen3-ASR and came out right (only "ComfyUI" turns into something like "Confiuí", normal for an English name). |
| Time | **1min 04s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 14215 MiB |

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
| ComfyUI-Drama3 | `67a733a` | https://github.com/PedroMarinhoDev/ComfyUI-Drama3 |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `drama3_int8experts_bf16.safetensors` | Drama 3 (INT8 experts; fastest under 24 GB) | 38.70 GB | [download](https://huggingface.co/PedroMarinhoDev/Drama-3-ComfyUI/resolve/681e2fae64af1f12e64b9c19c82930a5f3bba1a4/drama3_int8experts_bf16.safetensors) | [page](https://huggingface.co/PedroMarinhoDev/Drama-3-ComfyUI) |
| `vae/` | `drama3_codec.safetensors` | audio codec | 1.57 GB | [download](https://huggingface.co/PedroMarinhoDev/Drama-3-ComfyUI/resolve/681e2fae64af1f12e64b9c19c82930a5f3bba1a4/drama3_codec.safetensors) | [page](https://huggingface.co/PedroMarinhoDev/Drama-3-ComfyUI) |
| `asr/` | `qwen3_asr_1.7b_bf16.safetensors` | Qwen3-ASR 1.7B (transcribes the reference) | 4.08 GB | [download](https://huggingface.co/PedroMarinhoDev/Qwen3-ASR-ComfyUI/resolve/6ad8c9be026925839479a8d97749068a4202fbe9/qwen3_asr_1.7b_bf16.safetensors) | [page](https://huggingface.co/PedroMarinhoDev/Qwen3-ASR-ComfyUI) |

<details><summary>SHA-256</summary>

```
f407996b17583ba857ace14e0330a13788cf89f4d47cfdcd4766ad5106576899  models/diffusion_models/drama3_int8experts_bf16.safetensors
4fecf102907a48414230da9a74d72d07c3a92368eab53fab655797837bddf5ae  models/vae/drama3_codec.safetensors
958ac49a7015ad546206e87fbcf390ac567b81d1cc7d613a1255a41033b8345f  models/asr/qwen3_asr_1.7b_bf16.safetensors
```

</details>

## How to use

1. **LoadAudio**: 5 to 15 s of the voice to clone (`reference_voice.flac`).
2. **Drama3Generate**: the text; cues in brackets (`[sighs]`, `[laughs]`). `speakers` = `one take per line` for one voice.
3. **Drama3Decode**: `shorten_long_pauses` on trims long pauses.

## License

Free research and non-commercial use; free commercial use for those under US$ 500K/year in revenue. **A hosted service (generating voices for others) needs a separate license.** Imitating an identifiable person's voice without prior consent is prohibited, as is using the outputs to train other speech models. The outputs are yours.

## Notes

- **RAM:** needs ~48 GB of free RAM (~32 GB with the W4A8 variant, which fails more often with real voices). In the test another service using 48 GB had to be paused.
- The node is newer than its example: `speakers` and `shorten_long_pauses` were added.
- No extra pip dependencies.
- The test reference voice is synthetic (Qwen3-TTS "Serena" voice, 12.8 s in PT); no real voice was cloned. Cloning someone's voice requires that person's consent.
