# SeedVR2 v2 · video upscale (GGUF)

[comfyui-workflows](../../README.md) › **SeedVR2 v2 · video upscale (GGUF)**

Second version of [SeedVR2](../42-seedvr2-upscale/README.md): instead of ComfyUI's native support (INT8), it uses numz's [ComfyUI-SeedVR2_VideoUpscaler](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler) v2.5 custom node with the 3B model in GGUF Q8_0. Same model and the same quality by eye; on the same VHS clip it took 134 s against ~410 s for the native one. It processes the video in batches of 21 frames (`batch_size`, always 4n+1) and sets the final height in `resolution` (shortest edge).

| | |
|---|---|
| Status | ✅ tested |
| Family | SeedVR2 |
| License | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Total download | 4.16 GB |
| Test | 3 s of VHS cleaned with ffmpeg (632x468, 90 frames) → 972x720: 90 frames and audio kept, no jumps between batches |
| Time | **2min 14s** (RTX 5060 Ti 16 GB, 2026-10-26) |
| Peak VRAM | 7887 MiB |

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
| ComfyUI-SeedVR2_VideoUpscaler (v2.5.23) | `5a4bf42` | https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `SEEDVR2/` | `seedvr2_ema_3b-Q8_0.gguf` | SeedVR2 3B (GGUF Q8_0) | 3.66 GB | [download](https://huggingface.co/cmeka/SeedVR2-GGUF/resolve/de058a1261f2fc4bb41f39e9ddf313877e4ebf0d/seedvr2_ema_3b-Q8_0.gguf) | [page](https://huggingface.co/cmeka/SeedVR2-GGUF) |
| `SEEDVR2/` | `ema_vae_fp16.safetensors` | SeedVR2 VAE | 0.50 GB | [download](https://huggingface.co/numz/SeedVR2_comfyUI/resolve/09ced71023636e9bc8cdf9cdecfb2625d1e691e8/ema_vae_fp16.safetensors) | [page](https://huggingface.co/numz/SeedVR2_comfyUI) |

<details><summary>SHA-256</summary>

```
be0d60083a2051a265eb4b77f28edf494e6db67ffc250216f32b72292e5cbd96  models/SEEDVR2/seedvr2_ema_3b-Q8_0.gguf
20678548f420d98d26f11442d3528f8b8c94e57ee046ef93dbb7633da8612ca1  models/SEEDVR2/ema_vae_fp16.safetensors
```

</details>

## How to use

1. After `install.sh`, install the custom node's dependency in ComfyUI's Python: `pip install rotary-embedding-torch==0.9.1` (the rest of `requirements.txt` already ships with ComfyUI) and restart ComfyUI.
2. Video in **LoadVideo** (`input.mp4`).
3. Final height in the **SeedVR2VideoUpscaler** `resolution` (720; it is the shortest edge). `batch_size` 21: bigger batches need more VRAM (93 frames ran out of 16 GB without `blocks_to_swap`).
4. For long videos, split them into chunks (the [VHS v2 use case](../../usecases/vhs-upscale-v2/README.md) does it for you): every frame of the video is kept in RAM.

## License

Apache-2.0 (GGUF models, VAE and custom node): free personal and commercial use, with no revenue or territory limits; just keep the license notices when redistributing. The outputs are yours.

## Notes

### Comparison (2026-10-26, same 3 s of VHS, 720p, `lab` color correction)

| Version | Time | Peak VRAM |
|---|---|---|
| [v1](../42-seedvr2-upscale/README.md) native 3B INT8 | 411 s | 7.0 GB |
| v2 3B Q8_0, `batch_size` 21 | 150 s | 8.1 GB |
| v2 3B Q4_K_M, `batch_size` 21 | 148 s | 8.0 GB |
| v2 3B Q8_0, `batch_size` 93 | out of VRAM (OOM) | — |
| v2 3B Q8_0, `batch_size` 93, `blocks_to_swap` 16 | 142 s | 15.6 GB |

Raw source (no cleanup), to measure only the upscale. By eye the versions came out the same (Q4 too); bigger batches gave no visible gain and no version had a jump between batches. `torch.compile` (the **SeedVR2TorchCompileSettings** node) was not used or tested.

### 7B model (optional)

[`seedvr2_ema_7b-Q8_0.gguf`](https://huggingface.co/cmeka/SeedVR2-GGUF/resolve/de058a1261f2fc4bb41f39e9ddf313877e4ebf0d/seedvr2_ema_7b-Q8_0.gguf) (8.84 GB, Apache-2.0), into `models/SEEDVR2/`. It is not in `install.sh`; change the **SeedVR2LoadDiTModel** `model`. Test (same 3 s of cleaned VHS, 720p): 160 s and 12.1 GB peak VRAM (3B: 134 s, 7.9 GB), but sharpness 108 against 174 for the 3B: on a source this degraded the 7B keeps the blur instead of rebuilding it, as in [v1](../42-seedvr2-upscale/README.md). At 1080p: 347 s, 15.4 GB.
