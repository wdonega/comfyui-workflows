Language: **English** · [Português](README_ptBR.md)

# Herrgott's H3 Infinite Continuation (v1.4)

Makes videos of any length clip by clip: **Start** creates clip 1 (T2VA/I2VA/FL2VA) and saves the latent with *handover* metadata; each **Continue** loads the previous one, protects the last 39 safe frames as context (native Masked AV) and generates the next; **Stitch** decodes the saved chain and joins it at the safe points, with a short video and audio crossfade.

| | |
|---|---|
| Plan item | #25 |
| Status | ✅ tested |
| Family | MiniMax H3 |
| License | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Total download | 42.47 GB |
| Test | 736x1280, 15 steps: Start 5 s (553 s) + Continue 5 s (732 s) + Stitch (115 s) = 8.7 s final. Auto Handover detected the forced ending and handed over the safe point: seamless join. The reference was used as first/last frame, hence the portrait at the end |
| Time | **23min 20s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 15651 MiB |

## Files in this folder

| File | What it is |
|---|---|
| `01-start.json` | Clip 1: drag into the UI |
| `01-start.api.json` | Clip 1 (API) |
| `02-continue.json` | Clips 2, 3, …: bump `clip_index` in Load/Save for each clip |
| `02-continue.api.json` | Continue (API) |
| `03-stitch.json` | Joins the saved chain into one final video |
| `03-stitch.api.json` | Stitch (API) |
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
| Herrgotts-H3-Infinite-Continuation-Suite | `4b1edd6` | https://github.com/HerrgottMargott/Herrgotts-H3-Infinite-Continuation-Suite |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | FL2VA model (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | Qwen3-VL 32B text encoder (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_fp16.safetensors` | video VAE fp16 | 5.21 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_fp16.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | audio VAE | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |

<details><summary>SHA-256</summary>

```
e889202c41dafb67b10d67b97f0d8541508036a6090af23425a5c2615d03c47a  models/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
7c1f131492e7eddacaac9069a61b81bdd39de5cc96561e677c5eab1cdce5e522  models/vae/minimax_h3_video_vae_fp16.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
```

</details>

## How to use

1. **01-start**: first and last frames are optional (the author recommends repeating the same frame at both ends as a quality "reset"); the Qwen reference becomes `<Picture 2>`. Run it and it saves `output/h3_continuous/clip_00001`.
2. **02-continue**: Load's `clip_index` = previous, Save's = current. `duration_mode` `Net New Content` makes the requested duration new content only.
3. Repeat Continue as many times as you like.
4. **03-stitch**: `first_clip`/`last_clip` (0 = up to the last) and it renders the final video.

## License

Personal and commercial use allowed up to US$ 20M/year in revenue (above that, MiniMax's authorization). **Prohibited in the US, EU, UK and South Korea, including displaying or distributing the outputs there (clause V.4)**: do not use the videos in globally published projects. Published content must be labeled as AI-generated; impersonating real people without consent is prohibited; commercial products must display "MiniMax H3". Third-party LoRAs inherit these terms.

## Notes

- The author's examples use **SageAttention** (`PathchSageAttentionKJ`), which was not installed; here it was replaced by comfy-kitchen attention + MiniMax LowVRAM Attention + Chunk FeedForward (KJNodes), and it worked on 16 GB.
- Do not use the same studio portrait as the last frame if you want the scene to end on location: the clip is forced to reach it (that is what happened in the test).
- The time in the table adds up the three steps (553 + 732 + 115 s).
