# Bernini-R · style transfer (anime / real life)

[comfyui-workflows](../../README.md) › **Bernini-R · style transfer (anime / real life)**

The official `video_bernini_r_video_editing` template (instruction-based video editing, ByteDance Bernini-R on Wan 2.2 14B, high + low noise) in INT8 convrot, with the lightx2v speed LoRA (6 steps) and **tarn59**'s style LoRAs chained in both branches. "Video Editing (Style / Motion)" mode and trigger prompt `Anime style transfer.`

| | |
|---|---|
| Status | ✅ tested |
| Family | Wan 2.2 (Bernini-R) |
| License | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Total download | 39.15 GB |
| Test | 4.9 s source (117 frames, 480x832), anime LoRA 1.0: character converted to anime (face and eyes), identical motion and framing; the background stayed mostly photographic |
| Time | **18min 45s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 11663 MiB |

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
| `diffusion_models/` | `wan2.2_bernini_r_high_noise_int8_convrot.safetensors` | Bernini-R high noise (INT8) | 14.54 GB | [download](https://huggingface.co/Comfy-Org/Bernini-R/resolve/8e6d2ce0c2ead4dd237482c504ea9e4ae5b15347/diffusion_models/wan2.2_bernini_r_high_noise_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/Bernini-R) |
| `diffusion_models/` | `wan2.2_bernini_r_low_noise_int8_convrot.safetensors` | Bernini-R low noise (INT8) | 14.54 GB | [download](https://huggingface.co/Comfy-Org/Bernini-R/resolve/8e6d2ce0c2ead4dd237482c504ea9e4ae5b15347/diffusion_models/wan2.2_bernini_r_low_noise_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/Bernini-R) |
| `text_encoders/` | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | UMT5-XXL text encoder (FP8) | 6.74 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | [page](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `vae/` | `Wan2_1_VAE_bf16.safetensors` | Wan 2.1 VAE | 0.25 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/vae/Wan2_1_VAE_bf16.safetensors) | [page](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `loras/` | `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors` | lightx2v speed LoRA (Apache-2.0) | 0.63 GB | [download](https://huggingface.co/Kijai/WanVideo_comfy/resolve/8260d429d19fd7a72304cad059160b95d843913f/Lightx2v/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors) | [page](https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill) |
| `loras/` | `bernini_r_anime_style_transfer_high_noise.safetensors` | #56 anime style (high noise) | 0.61 GB | [download](https://huggingface.co/tarn59/bernini_r_anime_style_transfer_lora/resolve/9c8244d055585c82755186b9c4ac892f646d26f7/bernini_r_anime_style_transfer_high_noise.safetensors) | [page](https://huggingface.co/tarn59/bernini_r_anime_style_transfer_lora) |
| `loras/` | `bernini_r_anime_style_transfer_low_noise.safetensors` | #56 anime style (low noise) | 0.61 GB | [download](https://huggingface.co/tarn59/bernini_r_anime_style_transfer_lora/resolve/9c8244d055585c82755186b9c4ac892f646d26f7/bernini_r_anime_style_transfer_low_noise.safetensors) | [page](https://huggingface.co/tarn59/bernini_r_anime_style_transfer_lora) |
| `loras/` | `bernini_r_real_life_style_transfer_v3_high_noise.safetensors` | #56 real-life style v3 (high noise) | 0.61 GB | [download](https://huggingface.co/tarn59/bernini_r_real_life_style_transfer_lora/resolve/b48438d22e40dff00d7e585d66c96ff9dd1c11d6/bernini_r_real_life_style_transfer_v3_high_noise.safetensors) | [page](https://huggingface.co/tarn59/bernini_r_real_life_style_transfer_lora) |
| `loras/` | `bernini_r_real_life_style_transfer_v3_low_noise.safetensors` | #56 real-life style v3 (low noise) | 0.61 GB | [download](https://huggingface.co/tarn59/bernini_r_real_life_style_transfer_lora/resolve/b48438d22e40dff00d7e585d66c96ff9dd1c11d6/bernini_r_real_life_style_transfer_v3_low_noise.safetensors) | [page](https://huggingface.co/tarn59/bernini_r_real_life_style_transfer_lora) |

<details><summary>SHA-256</summary>

```
9d9a84f6e70032bd8f1dab40f5b0270fefd259ac5111a52b4acb752773c119b3  models/diffusion_models/wan2.2_bernini_r_high_noise_int8_convrot.safetensors
98fe00c6e38a745929cd7770a84ae3814c834d2ed7bef6b8a0a526c896fe8e5c  models/diffusion_models/wan2.2_bernini_r_low_noise_int8_convrot.safetensors
c3355d30191f1f066b26d93fba017ae9809dce6c627dda5f6a66eaa651204f68  models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
1ab9a32cc2c740f6e39d80d367ce5dcc28db8c71b79b28670546b8973e9d75f9  models/vae/Wan2_1_VAE_bf16.safetensors
37d49218544b9e0bfb8e831d1399f451fbc5068aff6474f42a90c928363c3573  models/loras/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors
b5b5cf67a67345fb37de4da7bb5967c75496606081ba7e743b67b862a172b26f  models/loras/bernini_r_anime_style_transfer_high_noise.safetensors
c944b81911c97897e451da5b12236a2d2aa6f46797a4948b2e671ef466eba5ed  models/loras/bernini_r_anime_style_transfer_low_noise.safetensors
047080ab2333fd69a0188bdb8fb7d8f24f23bd37fc0d62d95df8ffe082790ed0  models/loras/bernini_r_real_life_style_transfer_v3_high_noise.safetensors
45d87cb48ecafd2b72143d418127abc42316cb92604f50f262acdfdb2aae93e9  models/loras/bernini_r_real_life_style_transfer_v3_low_noise.safetensors
```

</details>

## How to use

1. **LoadVideo**: the video to edit (`source.mp4`; **Video Slice** takes the first 5 s).
2. Task combo mode: **Video Editing (Style / Motion)**.
3. Prompt = LoRA trigger: `Anime style transfer.` (anime) or `Real life style transfer.` (real-life; swap both LoRAs for the `real_life_..._v3` ones).
4. The style LoRAs go **after** lightx2v, one in the high noise branch and one in the low noise branch, strength 1.0.
5. No style: remove both style LoRA nodes and write the edit in the prompt (e.g. replace the background).

## License

Apache-2.0: free personal and commercial use, with no revenue or territory limits; just keep the license notices when redistributing the weights. The outputs are yours.

## Notes

- The original template uses the FP8 weights (15.6 GB each); the INT8 convrot ones (14.5 GB each) were used here.
- The real-life LoRA was downloaded, but only the anime one was tested.
- Bernini-R is natively supported in ComfyUI v0.37 core (no custom node needed).
