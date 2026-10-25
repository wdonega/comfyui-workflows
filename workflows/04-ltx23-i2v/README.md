# LTX 2.3 · image to video with audio

[comfyui-workflows](../../README.md) › **LTX 2.3 · image to video with audio**

The official ComfyUI template `video_ltx2_3_i2v` (native nodes, no required custom node) with Kijai's split model stack: **distilled** FP8 transformer, VAEs and Gemma 3 in FP8. Generates at half resolution, upscales the latent x2 and refines; audio comes out together, speech included.

| | |
|---|---|
| Status | ✅ tested |
| Family | LTX 2.3 |
| License | [LTX-2 Community License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE) |
| Total download | 43.35 GB |
| Test | 704x1280, 25 fps, 121 frames (4.8 s), reference image + prompt with speech: identity kept, speech audible; cut from the studio portrait to the beach because image and prompt show different settings |
| Time | **1min 35s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 15845 MiB |

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

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors` | LTX 2.3 22B distilled, transformer only (FP8 with activation scales) | 25.02 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_video_vae_bf16.safetensors` | video VAE | 1.45 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_video_vae_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_audio_vae_bf16.safetensors` | audio VAE | 0.36 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_audio_vae_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `text_encoders/` | `gemma_3_12B_it_fp8_scaled.safetensors` | Gemma 3 12B text encoder (FP8) | 13.21 GB | [download](https://huggingface.co/Comfy-Org/ltx-2/resolve/ccde4ba417d7900669fd56dd292a883cee11ff37/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) | [page](https://huggingface.co/Comfy-Org/ltx-2) |
| `text_encoders/` | `ltx-2.3_text_projection_bf16.safetensors` | LTX 2.3 text projection | 2.31 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `latent_upscale_models/` | `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | x2 spatial upscaler (stage 2) | 1.00 GB | [download](https://huggingface.co/Lightricks/LTX-2.3/resolve/c1521179de480464f366a98a9d9b2acc4cc097b9/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) | [page](https://huggingface.co/Lightricks/LTX-2.3) |

<details><summary>SHA-256</summary>

```
7327111e298066af8032f573d8db187986229ed2d4c926818ebf02041cfac8cf  models/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors
01ea62d09bc139f95c5dee7b5c062ad6a3e6cd8be910a1983ac02e7eb5b8ee3b  models/vae/LTX23_video_vae_bf16.safetensors
5bc10fa4adecf99dda132d916e23048cbd56797702c5fa50eb5d2079048a38c3  models/vae/LTX23_audio_vae_bf16.safetensors
60216ce97c01c3a8753c2dfd0a89fc76e16fbe446d1a32ef8f1b528ac8bae466  models/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors
911d59bb4cb7708179c9a0045ea0fe41212ecfb77aed3a02702b7c0a8274911f  models/text_encoders/ltx-2.3_text_projection_bf16.safetensors
5f416311fa8172b65af67530758964708d29a317b830d689a51143b7f91913ed  models/latent_upscale_models/ltx-2.3-spatial-upscaler-x2-1.1.safetensors
```

</details>

## How to use

1. Starting image in **LoadImage**; prompt in **PrimitiveStringMultiline** (put dialogue in quotes and describe the sounds).
2. Width/height and duration (seconds) in the **PrimitiveInt** nodes; fps in the other PrimitiveInt (25).
3. The template's manual sigmas (8 + 3 steps) already work for the distilled model.
4. For a continuous transition, use an image that already shows the setting described in the prompt.

## License

Free personal and commercial use for individuals and companies with annual revenue under US$ 10M; above that, a paid commercial license from Lightricks. **No territory restrictions.** Lightricks claims no rights over the outputs (they are yours). Outputs may not be used to train competing models. The Gemma 3 text encoder follows Google's Gemma Terms of Use (prohibited-use policy; outputs are free).

## Notes

- Differences from the official template: instead of the `ltx-2.3-22b-dev-fp8` checkpoint + distilled LoRA + FP4 Gemma, it uses Kijai's distilled transformer, the split VAEs and FP8 Gemma (the same stack as Face Swap #17, so it is downloaded once). The optional Gemma prompt-enhancer branch (off in the template) was removed.
- KJNodes is only needed for `VAELoaderKJ`.
- Much faster than MiniMax H3: 111 s for ~5 s of video.
