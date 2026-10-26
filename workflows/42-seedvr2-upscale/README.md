# SeedVR2 · 4x upscale

[comfyui-workflows](../../README.md) › **SeedVR2 · 4x upscale**

The official `utility_seedvr2_3b_int8_upscale_image` template, natively supported in ComfyUI (the planned custom node was not needed). Restores and upscales 4x in a single diffusion step, with a tiled VAE.

| | |
|---|---|
| Status | ✅ tested |
| Family | SeedVR2 |
| License | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Total download | 3.96 GB |
| Test | 1024x1024 MOSS-Image image → 4096x4096: sharp fur and whiskers, no artifacts |
| Time | **23s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 7831 MiB |

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
| `diffusion_models/` | `seedvr2_3b_int8_convrot.safetensors` | SeedVR2 3B (INT8) | 3.46 GB | [download](https://huggingface.co/Comfy-Org/SeedVR2/resolve/df48879708206a403d2a61acd55578c2e80fd233/diffusion_models/seedvr2_3b_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/SeedVR2) |
| `vae/` | `seedvr2_ema_vae_fp16.safetensors` | SeedVR2 VAE | 0.50 GB | [download](https://huggingface.co/Comfy-Org/SeedVR2/resolve/df48879708206a403d2a61acd55578c2e80fd233/vae/seedvr2_ema_vae_fp16.safetensors) | [page](https://huggingface.co/Comfy-Org/SeedVR2) |

<details><summary>SHA-256</summary>

```
c3dec8bcc5916843a8a858572970597462e1f2dc598d6dfd818f6cd40f53a157  models/diffusion_models/seedvr2_3b_int8_convrot.safetensors
20678548f420d98d26f11442d3528f8b8c94e57ee046ef93dbb7633da8612ca1  models/vae/seedvr2_ema_vae_fp16.safetensors
```

</details>

## How to use

1. Image in **LoadImage** (`input.png`).
2. Factor in **ResizeImageMaskNode** (`multiplier` 4). For video, use the `utility_seedvr2_3b_int8_upscale_video` template.

## License

Apache-2.0: free personal and commercial use, with no revenue or territory limits; just keep the license notices when redistributing the weights. The outputs are yours.

## Notes

- The template's `ImageCompare` node (a UI-only visual comparer) was removed from the API version.
- Only 7.8 GB peak VRAM: fits comfortably in 16 GB.

### 7B models (optional)

The [Comfy-Org/SeedVR2](https://huggingface.co/Comfy-Org/SeedVR2) repo (Apache-2.0) also has SeedVR2 **7B**, regular and *sharp*. They work in this same workflow by changing the **UNETLoader** `unet_name`; they are not in `install.sh`. To download, into `models/diffusion_models/`:

| File | Size | SHA-256 |
|---|---|---|
| [`seedvr2_7b_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/SeedVR2/resolve/df48879708206a403d2a61acd55578c2e80fd233/diffusion_models/seedvr2_7b_int8_convrot.safetensors) | 8.33 GB | `5aa0d25fc9d35e449b659d0c9a5dcb22e2a4fa04032101b95a39da42b32c1be6` |
| [`seedvr2_7b_sharp_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/SeedVR2/resolve/df48879708206a403d2a61acd55578c2e80fd233/diffusion_models/seedvr2_7b_sharp_int8_convrot.safetensors) | 8.33 GB | `db48be2f1cc7e36b01a2aa529810f5d9c6a971edd29be225cf1b0eb18d51c366` |

Test (2026-10-25, official video template `utility_seedvr2_3b_int8_upscale_video`, 3 s of a VHS capture 640x480 → 960x720, `lab` color correction, automatic temporal chunks):

| Model | Time | Peak VRAM | Sharpness (Laplacian variance) |
|---|---|---|---|
| input (lanczos) | — | — | 65 |
| 3B INT8 | 329 s | 7.5 GB | **221** |
| 7B INT8 | 392 s | 10.8 GB | 119 |
| 7B *sharp* INT8 | 438 s | 10.9 GB | 109 |

On a heavily degraded source (VHS), the 7B models were more conservative than the 3B: they keep the blur instead of rebuilding detail. The 3B was the best here, and faster. The 7B models may do better on less degraded sources (not tested).

Second pass (the 3B output run through the 3B again): 354 s keeping 960x720 and 384 s going to 1440x1080. It gets sharper, but faces get worse: hard outlines, darkened eyes and made-up shadows. One pass is the limit.

### v2

For video, [v2](../42-seedvr2-upscale-v2/README.md) uses numz's custom node with the 3B in GGUF Q8_0: ~3x faster on the same clip.
