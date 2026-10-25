# LTX 2.3 · Clean Plate (removes people from video)

[comfyui-workflows](../../README.md) › **LTX 2.3 · Clean Plate (removes people from video)**

Lightricks' **Clean Plate** IC-LoRA in ComfyUI-LTXVideo's official video-to-video workflow: the original video goes in as reference and comes out regenerated without the moving elements, keeping the static background. No mask: it is a full-frame model.

| | |
|---|---|
| Status | ✅ tested |
| Family | LTX 2.3 |
| License | [LTX-2 Community License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE) |
| Total download | 42.68 GB |
| Test | 4 s (97 frames) of a boy running down a street with a monster and smoke behind him: boy, monster and smoke removed; street, cars, trees, reflections and camera motion kept |
| Time | **3min 39s** (RTX 5060 Ti 16 GB, 2026-10-24) |
| Peak VRAM | 15791 MiB |

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
| ComfyUI-LTXVideo | `220e1d4` | https://github.com/Lightricks/ComfyUI-LTXVideo |
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors` | LTX 2.3 22B distilled, transformer only (FP8 with activation scales) | 25.02 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_video_vae_bf16.safetensors` | video VAE | 1.45 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_video_vae_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_audio_vae_bf16.safetensors` | audio VAE | 0.36 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_audio_vae_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `text_encoders/` | `gemma_3_12B_it_fp8_scaled.safetensors` | Gemma 3 12B text encoder (FP8) | 13.21 GB | [download](https://huggingface.co/Comfy-Org/ltx-2/resolve/ccde4ba417d7900669fd56dd292a883cee11ff37/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) | [page](https://huggingface.co/Comfy-Org/ltx-2) |
| `text_encoders/` | `ltx-2.3_text_projection_bf16.safetensors` | LTX 2.3 text projection | 2.31 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `loras/` | `ltx-2.3-22b-ic-lora-clean-plate-1.0.safetensors` | Clean Plate 1.0 IC-LoRA (gated: accept the license) | 0.33 GB | [download](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Clean-Plate/resolve/c2ab69ffe3e21410293bdee99d7d8ca0bc5a9ad0/ltx-2.3-22b-ic-lora-clean-plate-1.0.safetensors) | [page](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Clean-Plate) |

<details><summary>SHA-256</summary>

```
7327111e298066af8032f573d8db187986229ed2d4c926818ebf02041cfac8cf  models/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors
01ea62d09bc139f95c5dee7b5c062ad6a3e6cd8be910a1983ac02e7eb5b8ee3b  models/vae/LTX23_video_vae_bf16.safetensors
5bc10fa4adecf99dda132d916e23048cbd56797702c5fa50eb5d2079048a38c3  models/vae/LTX23_audio_vae_bf16.safetensors
60216ce97c01c3a8753c2dfd0a89fc76e16fbe446d1a32ef8f1b528ac8bae466  models/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors
911d59bb4cb7708179c9a0045ea0fe41212ecfb77aed3a02702b7c0a8274911f  models/text_encoders/ltx-2.3_text_projection_bf16.safetensors
a1b573a9649df549901ae6c5571a6d305d0620aed8953f39536e34da4ca01d6a  models/loras/ltx-2.3-22b-ic-lora-clean-plate-1.0.safetensors
```

</details>

## How to use

1. **LoadVideo**: the original video (`source.mp4`) **with an audio track** (the workflow encodes audio; add a silent one if there is none). Dimensions divisible by 32 and 8k+1 frames.
2. Positive prompt: describe the desired **empty scene**, not "remove X"; name what must not appear. Negative: the people/objects to remove.
3. The first-frame branch (`first_frame.png`) is bypassed; the file just has to exist.

## License

Free personal and commercial use for individuals and companies with annual revenue under US$ 10M; above that, a paid commercial license from Lightricks. **No territory restrictions.** Lightricks claims no rights over the outputs (they are yours). Outputs may not be used to train competing models. The Gemma 3 text encoder follows Google's Gemma Terms of Use (prohibited-use policy; outputs are free).

## Notes

- Changes from the official workflow (which uses the example "instant shave" IC-LoRA): Kijai stack with the **distilled** transformer (no distillation LoRA), local FP8 Gemma and the Clean Plate LoRA.
- Not for cases where the person fills most of the frame (e.g. first-person legs).
- ComfyUI-LTXVideo pip dependencies: only `OpenImageIO` and `ninja` were missing (`PIP_USER=true python3.13 -m pip install OpenImageIO ninja`).
