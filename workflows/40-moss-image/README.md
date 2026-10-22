# MOSS-Image (SFT)

[comfyui-workflows](../../README.md) › **MOSS-Image (SFT)**

The official `image_moss_image_t2i` template with MOSS-Image SFT in INT8 (25 steps, `er_sde`, CFG 2.5) and Qwen3.5 9B W4A8 as text encoder and prompt expander. Needs ComfyUI ≥ 0.42. **Apache-2.0**: the best option on this list for assets of published projects.

| | |
|---|---|
| Status | ✅ tested |
| Family | MOSS-Image |
| License | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Total download | 13.01 GB |
| Test | Test prompt (same for every image model compared): bookstore café with a calico cat and a sign reading "OPEN DAILY 8-20", seed 20261022, 1024x1024. |
| Time | **35s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 13045 MiB |

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
| `diffusion_models/` | `moss_image_sft_int8_convrot.safetensors` | MOSS-Image SFT (INT8) | 5.41 GB | [download](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/24147db865fcdc207270f844777587223fed8d6e/diffusion_models/moss_image_sft_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MOSS-Image) |
| `text_encoders/` | `qwen3.5_9b_w4a8_gptq.safetensors` | Qwen3.5 9B text encoder (W4A8) | 7.34 GB | [download](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/24147db865fcdc207270f844777587223fed8d6e/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) | [page](https://huggingface.co/Comfy-Org/MOSS-Image) |
| `vae/` | `flux2-vae_small.safetensors` | Flux 2 VAE (small) | 0.25 GB | [download](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/24147db865fcdc207270f844777587223fed8d6e/vae/flux2-vae_small.safetensors) | [page](https://huggingface.co/Comfy-Org/MOSS-Image) |

<details><summary>SHA-256</summary>

```
b4d1475bc7eeffd7b809e82ea13a1fba1fb85c4e18365af3813722faa5c0fe4f  models/diffusion_models/moss_image_sft_int8_convrot.safetensors
4cc6a1543ad2061806da46f35f90cadb4801dcba246c44782cf42ec0feb6407c  models/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors
d8d52ba036475f5fb07c8b435e176d3d97ebfa82f0d1a1c317f9cc1e25bd013b  models/vae/flux2-vae_small.safetensors
```

</details>

## How to use

Prompt in **PrimitiveStringMultiline**; the template expands the prompt (designed for short requests, including in Chinese). There is a community 8-step fast version (`lodestones/MOSS-Image-SFT-8-steps-dmd`), not tested here.

## License

Apache-2.0: free personal and commercial use, with no revenue or territory limits; just keep the license notices when redistributing the weights. The outputs are yours.

## Notes

Same seed/prompt comparison (RTX 5060 Ti): Qwen 2.1 24 s · Qwen 2.1 Turbo 10 s · Krea 2 Turbo 23 s · Flux 3 Klein 21 s · MOSS-Image 35 s. All rendered the sign text correctly.
