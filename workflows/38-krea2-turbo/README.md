# Krea 2 Turbo

[comfyui-workflows](../../README.md) › **Krea 2 Turbo**

The official `image_krea2_turbo_t2i_int8` template (8 steps, CFG 1). The text encoder itself (Qwen3-VL 4B) expands the prompt before generating. Uses Qwen3-VL 4B in INT8 (the same file as Flux 3 Klein) instead of the template's FP8.

| | |
|---|---|
| Status | ✅ tested |
| Family | Krea 2 |
| License | [Krea 2 Community License](https://huggingface.co/krea/Krea-2-Turbo) |
| Total download | 18.61 GB |
| Test | Test prompt (same for every image model compared): bookstore café with a calico cat and a sign reading "OPEN DAILY 8-20", seed 20261022, 1024x1024. |
| Time | **23s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 15477 MiB |

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
| `diffusion_models/` | `krea2_turbo_int8_convrot.safetensors` | Krea 2 Turbo (INT8) | 13.49 GB | [download](https://huggingface.co/Comfy-Org/Krea-2/resolve/1171f4dc7e325bf3734586942e737872506c73e1/diffusion_models/krea2_turbo_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/Krea-2) |
| `text_encoders/` | `qwen3vl_4b_int8_convrot.safetensors` | Qwen3-VL 4B text encoder (INT8; BFL gated repo, same file as in Krea-2) | 4.86 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/text_encoders/qwen3vl_4b_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/Krea-2) |
| `vae/` | `qwen_image_vae.safetensors` | Qwen-Image VAE | 0.25 GB | [download](https://huggingface.co/Comfy-Org/Krea-2/resolve/1171f4dc7e325bf3734586942e737872506c73e1/vae/qwen_image_vae.safetensors) | [page](https://huggingface.co/Comfy-Org/Krea-2) |

<details><summary>SHA-256</summary>

```
8e4eeda70dd5037ab1ba2bef6b417f9f901e26093117cf397f741fc1fdaaf3f1  models/diffusion_models/krea2_turbo_int8_convrot.safetensors
32de113cbf8282b02cbff0794b637b9d6676da09314a1db5a30bcea9bf4ee01c  models/text_encoders/qwen3vl_4b_int8_convrot.safetensors
a70580f0213e67967ee9c95f05bb400e8fb08307e017a924bf3441223e023d1f  models/vae/qwen_image_vae.safetensors
```

</details>

## How to use

1. Prompt in the user **PrimitiveStringMultiline**; the prompt expansion switch is on.
2. The 9 official style LoRAs (`Comfy-Org/Krea-2/loras`: watercolor, retro anime, kids' drawing, tarot…) go in a **LoraLoaderModelOnly** after the model; the template had one, switched off, which was removed.

## License

Free personal and commercial use for those under US$ 1M/year in revenue (company and affiliates); above that, an Enterprise License. Deployments reachable by others need content filtering and an AI-generated disclosure. The outputs are yours.

## Notes

Same seed/prompt comparison (RTX 5060 Ti): Qwen 2.1 24 s · Qwen 2.1 Turbo 10 s · Krea 2 Turbo 23 s · Flux 3 Klein 21 s · MOSS-Image 35 s. All rendered the sign text correctly.
