Language: **English** · [Português](README_ptBR.md)

# H3 Turbo v4 (larryvrh)

The base Ref2VA with the **MiniMax-H3 Turbo LoRA** (checkpoint `v4_step600_ema`, the author's recommendation) and the **MiniMax-H3 Turbo Sampler** instead of TaoMate. The sampler handles the separate video and audio schedules. Useful range: 4 to 8 steps, `simple` scheduler.

| | |
|---|---|
| Plan item | #2 |
| Status | ✅ tested |
| Family | MiniMax H3 |
| License | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Total download | 40.85 GB |
| Test | 736x1280, 362 frames (15 s), 6 steps, same scene/seed as the base workflow: coherent video, no artifacts, darker cinematography and more dramatic expressions; ~2x slower than TaoMate 3 steps |
| Time | **16min 48s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 15603 MiB |

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
| ComfyUI-MiniMax-H3-Turbo | `4274783` | https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | Ref2VA model (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | Qwen3-VL 32B text encoder (NVFP4, Blackwell) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_int8_convrot.safetensors` | video VAE | 2.81 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | audio VAE | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_turbo_v4_step600_ema.safetensors` | Turbo v4-600 LoRA (Apache-2.0; inherits the H3 terms) | 0.78 GB | [download](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora/resolve/43a74557ac3f6539db8e0f2a959d03feb7a81480/minimax_h3_turbo_v4_step600_ema.safetensors) | [page](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora) |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
52a2c8c73583c86e4f41cdcce3a6ad0ea562987bc0bf3d60a0cef5f5c8e60c0e  models/vae/minimax_h3_video_vae_int8_convrot.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
5f3a626cd72c93a8b9318d6760c510bc5092d2ab13aaba1f932c5bab07a416d3  models/loras/minimax_h3_turbo_v4_step600_ema.safetensors
```

</details>

## How to use

1. Same as the base workflow; the model goes through **MiniMax-H3 Turbo LoRA** (strength 1.0) and `SamplerCustomAdvanced` gets the **MiniMax-H3 Turbo Sampler**.
2. Steps in **BasicScheduler** (`simple`): 4 is the minimum, 6–8 look noticeably better; above 8 it starts to over-sharpen.
3. `low_vram` off (bypass) is the sharpest; on (merge) uses less VRAM but is softer on INT8 bases.

## License

Personal and commercial use allowed up to US$ 20M/year in revenue (above that, MiniMax's authorization). **Prohibited in the US, EU, UK and South Korea, including displaying or distributing the outputs there (clause V.4)**: do not use the videos in globally published projects. Published content must be labeled as AI-generated; impersonating real people without consent is prohibited; commercial products must display "MiniMax H3". Third-party LoRAs inherit these terms.

## Notes

- Compared with TaoMate 3 steps on the same scene: 1008 s vs 524 s. Worth it as an aesthetic alternative, not for speed.
- The author warns that at 4 steps with fast motion v4 can leave trails; 6–8 steps fix it.
- The LoRA was made for T2V/I2V; here it was applied to Ref2VA and worked.
