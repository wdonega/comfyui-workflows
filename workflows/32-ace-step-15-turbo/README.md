# ACE-Step 1.5 Turbo · music

[comfyui-workflows](../../README.md) › **ACE-Step 1.5 Turbo · music**

The official `audio_ace_step_1_5_split` template (turbo model + two Qwen text encoders + VAE). Generates songs with vocals from style tags and lyrics in 8 steps. MIT license: the free option for soundtracks of published projects.

| | |
|---|---|
| Status | ✅ tested |
| Family | ACE-Step 1.5 |
| License | [MIT](https://opensource.org/license/mit) |
| Total download | 10.03 GB |
| Test | template example (K-pop with lyrics) shortened to 30 s |
| Time | **16s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 11267 MiB |

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
| `diffusion_models/` | `acestep_v1.5_turbo.safetensors` | ACE-Step 1.5 Turbo | 4.79 GB | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/6707deb277e9e0907fd9c14ce6b6f1d695c6a3fc/split_files/diffusion_models/acestep_v1.5_turbo.safetensors) | [page](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files) |
| `text_encoders/` | `qwen_0.6b_ace15.safetensors` | Qwen 0.6B text encoder | 1.19 GB | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/6707deb277e9e0907fd9c14ce6b6f1d695c6a3fc/split_files/text_encoders/qwen_0.6b_ace15.safetensors) | [page](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files) |
| `text_encoders/` | `qwen_1.7b_ace15.safetensors` | Qwen 1.7B text encoder (lyrics) | 3.71 GB | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/6707deb277e9e0907fd9c14ce6b6f1d695c6a3fc/split_files/text_encoders/qwen_1.7b_ace15.safetensors) | [page](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files) |
| `vae/` | `ace_1.5_vae.safetensors` | audio VAE | 0.34 GB | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/6707deb277e9e0907fd9c14ce6b6f1d695c6a3fc/split_files/vae/ace_1.5_vae.safetensors) | [page](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files) |

<details><summary>SHA-256</summary>

```
3f6e0797fad420a39bd33979eb6e840e30989e34a3794e843d23b60ec6e422d7  models/diffusion_models/acestep_v1.5_turbo.safetensors
fd4590c82153b8ddb67e15a2e7aaa8afa8b83a858c8a9b82a4831063156aa7a7  models/text_encoders/qwen_0.6b_ace15.safetensors
ed63e9247d1f55f3ace04fa11e95b085fc82d459c82c5626f0b2e37b91ebd710  models/text_encoders/qwen_1.7b_ace15.safetensors
6de92e3a862acd287e08b024ac90f0783a8635451b728721a33ff03565bcb2bb  models/vae/ace_1.5_vae.safetensors
```

</details>

## How to use

In **TextEncodeAceStepAudio1.5**: style tags and lyrics with sections. Length in seconds in **EmptyAceStep1.5LatentAudio** (120 in the template). XL (4B) variants exist among the ComfyUI templates and need ≥ 12 GB with offload.

## License

MIT: free personal and commercial use, no limits; just keep the copyright notice when redistributing the weights.

## Notes

- Very fast: 30 s of music in 16 s.
