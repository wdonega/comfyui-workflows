[comfyui-workflows](../../README.md) › **H3 Realism People**

Language: **English** · [Português](README_ptBR.md)

# H3 Realism People

The base Ref2VA + TaoMate with fal's **Realism People** LoRA chained after TaoMate. Makes people look more natural and cinematic (less AI sheen). Prompt trigger: `r34l1sm`.

| | |
|---|---|
| Plan item | #59 |
| Status | ✅ tested |
| Family | MiniMax H3 |
| License | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Total download | 42.69 GB |
| Test | 736x1280, 122 frames (5 s), 3 steps; LoRA applied with no skipped keys (208/208) |
| Time | **2min 14s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 15577 MiB |

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
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |
| VideoHelperSuite | 1.7.9 | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | Ref2VA model (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | Qwen3-VL 32B text encoder (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_int8_convrot.safetensors` | video VAE | 2.81 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | audio VAE | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors` | TaoMate 3-step LoRA | 2.48 GB | [download](https://huggingface.co/drbaph/MiniMax-H3-Turbo-Lora-ComfyUI/resolve/633e6c48cd05f7800e2cb2c007b5c9023b92c576/experimental/minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors) | [page](https://huggingface.co/TaoLiveAIGC/TaoMate-H3-FL2VA) |
| `loras/` | `h3-realism-people-t2v-i2v-r2v.safetensors` | Realism People LoRA (strength 1.0) | 0.13 GB | [download](https://huggingface.co/fal/MiniMax-H3-Realism-People-LoRA/resolve/039cc8579d7aa357a882d7f4111b25da4f72dccc/h3-realism-people-t2v-i2v-r2v.safetensors) | [page](https://huggingface.co/fal/MiniMax-H3-Realism-People-LoRA) |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
52a2c8c73583c86e4f41cdcce3a6ad0ea562987bc0bf3d60a0cef5f5c8e60c0e  models/vae/minimax_h3_video_vae_int8_convrot.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
6b119983683b265ad65224a9a643eea1714efe5b8bcb93799999635ccc455c73  models/loras/minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors
acc529601d2da117fb81179e76c56e488a3beab1171659d305f04fa3655b787e  models/loras/h3-realism-people-t2v-i2v-r2v.safetensors
```

</details>

## How to use

Same as the base workflow, with the **Realism People LoRA (#59)** node after TaoMate. Start the prompt with `r34l1sm,`. Works for T2V, I2V and R2V according to the author.

## License

Personal and commercial use allowed up to US$ 20M/year in revenue (above that, MiniMax's authorization). **Prohibited in the US, EU, UK and South Korea, including displaying or distributing the outputs there (clause V.4)**: do not use the videos in globally published projects. Published content must be labeled as AI-generated; impersonating real people without consent is prohibited; commercial products must display "MiniMax H3". Third-party LoRAs inherit these terms.

## Notes

- In the short test (5 s) the result looked more natural and less saturated than the base, with no artifacts.
