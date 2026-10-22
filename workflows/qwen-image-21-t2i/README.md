# Qwen-Image 2.1 · text to image

[comfyui-workflows](../../README.md) › **Qwen-Image 2.1 · text to image**

The official `image_qwen_image_2_1_t2i` template, with the original example prompt (fashion editorial portrait). The optional prompt-rewriting branch (off in the template) was removed.

| | |
|---|---|
| Status | ✅ tested |
| Family | Qwen-Image 2.1 |
| License | [Qwen Research License](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE) |
| Total download | 17.28 GB |
| Test | original template prompt, 1024x1024, 25 `euler` steps |
| Time | **26s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | not measured |

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
| `diffusion_models/` | `qwen_image_2.1_int8_convrot.safetensors` | Qwen-Image 2.1 (INT8) | 7.26 GB | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/5dc5850eb514a3685f6a03a2641728a8f7549c69/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) |
| `text_encoders/` | `qwen3vl_8b_int8_convrot.safetensors` | Qwen3-VL 8B text encoder (INT8) | 9.35 GB | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/5dc5850eb514a3685f6a03a2641728a8f7549c69/text_encoders/qwen3vl_8b_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) |
| `vae/` | `qwen_image_2.1_vae_bf16.safetensors` | Qwen-Image 2.1 VAE | 0.68 GB | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/5dc5850eb514a3685f6a03a2641728a8f7549c69/vae/qwen_image_2.1_vae_bf16.safetensors) | [page](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) |

<details><summary>SHA-256</summary>

```
cb74113cb03faecd79611b01fd7fd642f0aa60d6f0b95086abee214d75eaa57d  models/diffusion_models/qwen_image_2.1_int8_convrot.safetensors
8bfd0f6e12abf2d2d697ecc888e5e90b0d6741d6708f05799f53afa560452e8f  models/text_encoders/qwen3vl_8b_int8_convrot.safetensors
bb21f7473051e1ac368515dd3f2e15cd44d7a11748ee8823e1ddca3e4876b7c9  models/vae/qwen_image_2.1_vae_bf16.safetensors
```

</details>

## How to use

Prompt in the text node; size in **ResolutionSelector** (the model natively supports up to 2048x2048).

## License

**Research and evaluation only.** Any commercial use (including assets of a free published product) needs a license from Alibaba (model-business@notice.qwencloud.com). Keep the license notice when redistributing the weights.

## Notes

Same seed/prompt comparison (RTX 5060 Ti): Qwen 2.1 24 s · Qwen 2.1 Turbo 10 s · Krea 2 Turbo 23 s · Flux 3 Klein 21 s · MOSS-Image 35 s. All rendered the sign text correctly.
