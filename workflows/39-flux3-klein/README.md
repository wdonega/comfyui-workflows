# Flux 3 Klein (distilled)

[comfyui-workflows](../../README.md) › **Flux 3 Klein (distilled)**

The official `image_flux3_klein_distilled_t2i` template in INT8, with the prompt upsampler (Qwen3.5 9B W4A8) on as in the original. Needs ComfyUI ≥ 0.42 (Flux 3 Image support). The template's optional layout editor was removed from the API version.

| | |
|---|---|
| Status | ✅ tested |
| Family | Flux 3 |
| License | [FLUX Kommunity License](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |
| Total download | 17.75 GB |
| Test | Test prompt (same for every image model compared): bookstore café with a calico cat and a sign reading "OPEN DAILY 8-20", seed 20261022, 1024x1024. |
| Time | **21s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 15421 MiB |

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
| `diffusion_models/` | `flux3-image-klein-int8-convrot.safetensors` | Flux 3 Image Klein (INT8) | 5.83 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/diffusion_models/flux3-image-klein-int8-convrot.safetensors) | [page](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |
| `text_encoders/` | `qwen3vl_4b_int8_convrot.safetensors` | Qwen3-VL 4B text encoder (INT8) | 4.86 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/text_encoders/qwen3vl_4b_int8_convrot.safetensors) | [page](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |
| `text_encoders/` | `qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors` | Qwen3.5 9B prompt upsampler (W4A8) | 6.72 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors) | [page](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |
| `vae/` | `flux2-vae.safetensors` | Flux 2 VAE | 0.34 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/vae/flux2-vae.safetensors) | [page](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |

<details><summary>SHA-256</summary>

```
847d8933548afd93df4af2cac2498e70891bf28d9dae06d695f536992e168fe2  models/diffusion_models/flux3-image-klein-int8-convrot.safetensors
32de113cbf8282b02cbff0794b637b9d6676da09314a1db5a30bcea9bf4ee01c  models/text_encoders/qwen3vl_4b_int8_convrot.safetensors
e5d85a7421d197bf5a12474511936ecabce19a833252f16e9310a983194a4458  models/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors
868fe7b343cc8f3a19dbcfcafbc3d5f888802be3f89bd81b65b3621a066ce8f3  models/vae/flux2-vae.safetensors
```

</details>

## How to use

1. Short prompt in **PrimitiveStringMultiline**; the upsampler turns it into a detailed caption.
2. 16 steps, CFG 1, `euler`. To turn the upsampler off, flip the template's switch (saves time and VRAM).

## License

Free non-commercial use; free commercial use for "Qualifying Users" (annual revenue < US$ 5M) who keep content filters. BFL claims no rights over the outputs. Outputs may not be used to train competing models. Gated repository: accept the terms on Hugging Face and use HF_TOKEN.

## Notes

Same seed/prompt comparison (RTX 5060 Ti): Qwen 2.1 24 s · Qwen 2.1 Turbo 10 s · Krea 2 Turbo 23 s · Flux 3 Klein 21 s · MOSS-Image 35 s. All rendered the sign text correctly.
