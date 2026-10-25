# Wan Animate 2 · animate a character with a video's motion

[comfyui-workflows](../../README.md) › **Wan Animate 2 · animate a character with a video's motion**

The official `video_wan_animate2_distilled` template (distilled, 10 `lcm` steps, CFG 1) in INT8 convrot with the native `WanAnimate2ToVideo` and `WanAnimate2Cache` nodes. Takes a character image and a driving video; the character repeats the video's pose, body motion and expressions. Keeps the driving video's audio.

| | |
|---|---|
| Status | ✅ tested |
| Family | Wan 2.2 (Animate 2) |
| License | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Total download | 24.91 GB |
| Test | full-body character + driving video of a child running, 480x848, 81 frames, 10 steps: the character runs with the same legs, arms and approach to the camera as the guide; the background is the character image's. With a bust-only reference, only the expressions and head motion were transferred |
| Time | **7min 02s** (RTX 5060 Ti 16 GB, 2026-10-23) |
| Peak VRAM | 15345 MiB |

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

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `wan_animate_2_distill_int8_convrot.safetensors` | Wan Animate 2 distilled (INT8) | 16.65 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/diffusion_models/wan_animate_2_distill_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `text_encoders/` | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | UMT5-XXL text encoder (FP8) | 6.74 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | [page](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `clip_vision/` | `clip_vision_h.safetensors` | CLIP Vision H | 1.26 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/clip_vision/clip_vision_h.safetensors) | [page](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `vae/` | `Wan2_1_VAE_bf16.safetensors` | Wan 2.1 VAE | 0.25 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/vae/Wan2_1_VAE_bf16.safetensors) | [page](https://huggingface.co/Comfy-Org/Wan-Animate-2) |

<details><summary>SHA-256</summary>

```
d2e566ecac3f164cb1a6b63dc7d868d6678c9affa49fbceb3abe4f9458f89c8a  models/diffusion_models/wan_animate_2_distill_int8_convrot.safetensors
c3355d30191f1f066b26d93fba017ae9809dce6c627dda5f6a66eaa651204f68  models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
64a7ef761bfccbadbaa3da77366aac4185a6c58fa5de5f589b42a65bcc21f161  models/clip_vision/clip_vision_h.safetensors
1ab9a32cc2c740f6e39d80d367ce5dcc28db8c71b79b28670546b8973e9d75f9  models/vae/Wan2_1_VAE_bf16.safetensors
```

</details>

## How to use

1. **LoadImage**: the character (`character.png`), **full body** if the driving video has body motion (with a bust, only head and expressions are transferred).
2. **LoadVideo**: the driving video (`driving.mp4`).
3. Two prompts: the action (e.g. `A man running down a rainy street`) and the character's appearance.
4. Resolution in the video's **ResizeImageMaskNode** (480x854 in the template) and `length` in **WanAnimate2ToVideo** (81 frames).

## License

Apache-2.0: free personal and commercial use, with no revenue or territory limits; just keep the license notices when redistributing the weights. The outputs are yours.

## Notes

- The plan warned that the default **GGUF** loader silently ignores the driving video; here INT8 convrot with the native loader was used and the guide's motion showed up in the result.
- The template also saves a side-by-side comparison video (result + guide).
- The character stays in its own image's setting; inserting it into the driving video would be the replacement mode (not tested).
