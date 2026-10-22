# LTX 2.3 · Face Swap (head swap)

[comfyui-workflows](../../README.md) › **LTX 2.3 · Face Swap (head swap)**

Head swap workflow with the distilled LTX 2.3 and @Alissonerdx's **BFS head swap v3** LoRA. `ReservedRegionFrameComposer` (BFSNodes) builds each frame with the reference face in a reserved strip next to the video; LTX generates the video with the swapped head and the original audio is kept. It also saves a side-by-side comparison video.

| | |
|---|---|
| Plan item | #17 |
| Status | ✅ tested |
| Family | LTX 2.3 |
| License | [LTX-2 Community License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE) |
| Total download | 44.71 GB |
| Test | 4 s source (97 frames, 736x1280, 24 fps) + 1 face image, 8 steps (euler_ancestral_cfg_pp + bong_tangent): head swapped, pose/camera/set/clothing kept; background elements missing from the prompt (monster, smoke) disappeared |
| Time | **8min 42s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 15821 MiB |

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
| ComfyUI-BFSNodes | `64be9ce` | https://github.com/alisson-anjos/ComfyUI-BFSNodes |
| RES4LYF | `56e4475` | https://github.com/ClownsharkBatwing/RES4LYF |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors` | LTX 2.3 22B distilled, transformer only (FP8 with activation scales) | 25.02 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_video_vae_bf16.safetensors` | video VAE | 1.45 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_video_vae_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_audio_vae_bf16.safetensors` | audio VAE | 0.36 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_audio_vae_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `text_encoders/` | `gemma_3_12B_it_fp8_scaled.safetensors` | Gemma 3 12B text encoder (FP8) | 13.21 GB | [download](https://huggingface.co/Comfy-Org/ltx-2/resolve/ccde4ba417d7900669fd56dd292a883cee11ff37/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) | [page](https://huggingface.co/Comfy-Org/ltx-2) |
| `text_encoders/` | `ltx-2.3_text_projection_bf16.safetensors` | LTX 2.3 text projection | 2.31 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `latent_upscale_models/` | `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | x2 spatial upscaler (stage 2) | 1.00 GB | [download](https://huggingface.co/Lightricks/LTX-2.3/resolve/c1521179de480464f366a98a9d9b2acc4cc097b9/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) | [page](https://huggingface.co/Lightricks/LTX-2.3) |
| `loras/` | `ltx23-head_swap_v3_rank_adaptive_fro_098.safetensors` | BFS head swap v3 LoRA (renamed as the workflow expects) | 1.36 GB | [download](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap-Video/resolve/d0adb5394c6a1b05f2245ec33cb91051a8000853/ltx-2.3/head_swap_v3_rank_adaptive_fro_098.safetensors) | [page](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap-Video) |

<details><summary>SHA-256</summary>

```
7327111e298066af8032f573d8db187986229ed2d4c926818ebf02041cfac8cf  models/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors
01ea62d09bc139f95c5dee7b5c062ad6a3e6cd8be910a1983ac02e7eb5b8ee3b  models/vae/LTX23_video_vae_bf16.safetensors
5bc10fa4adecf99dda132d916e23048cbd56797702c5fa50eb5d2079048a38c3  models/vae/LTX23_audio_vae_bf16.safetensors
60216ce97c01c3a8753c2dfd0a89fc76e16fbe446d1a32ef8f1b528ac8bae466  models/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors
911d59bb4cb7708179c9a0045ea0fe41212ecfb77aed3a02702b7c0a8274911f  models/text_encoders/ltx-2.3_text_projection_bf16.safetensors
5f416311fa8172b65af67530758964708d29a317b830d689a51143b7f91913ed  models/latent_upscale_models/ltx-2.3-spatial-upscaler-x2-1.1.safetensors
78083ede0004c500ac0ae7b8fee43d28a1c3b503bac4a21edfeba7c60da8460d  models/loras/ltx23-head_swap_v3_rank_adaptive_fro_098.safetensors
```

</details>

## How to use

1. **VHS LoadVideo**: the source video (`source.mp4`); duration in seconds is in the **PrimitiveFloat** (5 in the original) and fps in the other one (24).
2. **LoadImage**: the face/head to insert (`face.png`), frontal and well lit.
3. **Prompt**: describe the person who should appear **and the rest of the scene** (background, props, lighting). Anything not in the prompt may disappear.
4. Keep 8 steps, `euler_ancestral_cfg_pp` sampler and `bong_tangent` scheduler (RES4LYF); head swap LoRA at 1.0.

## License

Free personal and commercial use for individuals and companies with annual revenue under US$ 10M; above that, a paid commercial license from Lightricks. **No territory restrictions.** Lightricks claims no rights over the outputs (they are yours). Outputs may not be used to train competing models. The Gemma 3 text encoder follows Google's Gemma Terms of Use (prohibited-use policy; outputs are free).

## Notes

- **Credits:** original workflow by Rob on [comfy.org](https://comfy.org/workflows/download/bed989744195.json?filename=bed989744195), LoRA by [@Alissonerdx](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap-Video). This folder holds the tested version, converted to API and automatically re-laid-out (the original layout is at the link).
- **BFSNodes and RES4LYF:** RES4LYF needs `PyWavelets` (`pip install --no-deps PyWavelets` in ComfyUI's Python). Recent BFSNodes versions show up as *Flagged* in the ComfyUI registry; the tested commit's code was reviewed (`subprocess` only for ffmpeg, downloads only from OpenCV Zoo and Comfy-Org, the Wan patch stays inactive when core already supports Bernini).
- The same author publishes a head swap LoRA for **MiniMax H3** (`h3/minimax_h3_head_swap_v1.0_r32.safetensors`).
- Faster than H3 Character Swap (#14: 868 s for 4 s) and keeps the original clothing; #14 swaps the whole character.
- License: swapping real people's faces without consent may violate image rights; use people who agreed or fictional faces.
