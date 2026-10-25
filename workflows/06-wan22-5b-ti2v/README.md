# Wan 2.2 5B · text/image to video

[comfyui-workflows](../../README.md) › **Wan 2.2 5B · text/image to video**

The official `video_wan2_2_5B_ti2v` template unchanged: the 5B TI2V model in fp16 (10 GB) generates 121 frames at 1280x704, 24 fps. Works as text-to-video or, by connecting a start image to `Wan22ImageToVideoLatent`, image-to-video. No audio.

| | |
|---|---|
| Status | ✅ tested |
| Family | Wan 2.2 |
| License | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Total download | 18.14 GB |
| Test | template prompt (subway musician), 1280x704, 121 frames, 20 steps uni_pc, CFG 5: coherent scene, faithful to the prompt |
| Time | **9min 10s** (RTX 5060 Ti 16 GB, 2026-10-23) |
| Peak VRAM | 15465 MiB |

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
| `diffusion_models/` | `wan2.2_ti2v_5B_fp16.safetensors` | Wan 2.2 TI2V 5B (fp16) | 10.00 GB | [download](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/ee6f4a40737a995bf5818954cfce6d59443b0f04/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors) | [page](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) |
| `text_encoders/` | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | UMT5-XXL text encoder (FP8) | 6.74 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | [page](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `vae/` | `wan2.2_vae.safetensors` | Wan 2.2 VAE | 1.41 GB | [download](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/ee6f4a40737a995bf5818954cfce6d59443b0f04/split_files/vae/wan2.2_vae.safetensors) | [page](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) |

<details><summary>SHA-256</summary>

```
456f901338bd9eadbded3828b819109a9b68e8a525ca5cf8d0049a69fcfeca1e  models/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors
c3355d30191f1f066b26d93fba017ae9809dce6c627dda5f6a66eaa651204f68  models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
e40321bd36b9709991dae2530eb4ac303dd168276980d3e9bc4b6e2b75fed156  models/vae/wan2.2_vae.safetensors
```

</details>

## How to use

1. Positive prompt in the first **CLIPTextEncode**; the negative one (Chinese, from the template) can stay.
2. Resolution and length in **Wan22ImageToVideoLatent** (121 frames = 5 s at 24 fps).
3. For image-to-video, connect a **LoadImage** to the `start_image` input of Wan22ImageToVideoLatent.

## License

Apache-2.0: free personal and commercial use, with no revenue or territory limits; just keep the license notices when redistributing the weights. The outputs are yours.

## Notes

- The original plan suggested GGUF for 16 GB; the 5B in fp16 runs natively (15.5 GB peak), no custom node.
- `umt5_xxl_fp8_e4m3fn_scaled` is the same file used by Wan Animate 2 and Bernini-R (identical SHA-256).
