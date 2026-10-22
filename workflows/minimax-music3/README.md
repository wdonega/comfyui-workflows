# MiniMax Music 3 · songs with lyrics

[comfyui-workflows](../../README.md) › **MiniMax Music 3 · songs with lyrics**

The official `audio_minimax_music_3` template with the original example (lo-fi hip-hop, 78 BPM, with lyrics). Generates the whole track, vocals included, from a style description and lyrics with section tags.

| | |
|---|---|
| Status | ✅ tested |
| Family | MiniMax Music 3 |
| License | [MiniMax-Music3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-Music3/blob/main/LICENSE) |
| Total download | 14.33 GB |
| Test | template example: 60 s stereo MP3 at 44.1 kHz, consistent loudness (−16 to −20 dB) |
| Time | **2min 26s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 14859 MiB |

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
| `diffusion_models/` | `minimax_music3_dit_fp16.safetensors` | Music 3 DiT (fp16) | 4.91 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/9e364ccd290a401561091fb441ed19cd7de92550/diffusion_models/minimax_music3_dit_fp16.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-Music-3) |
| `text_encoders/` | `minimax_music3_text_encoder_pruned_int8_convrot.safetensors` | text encoder (INT8) | 9.20 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/9e364ccd290a401561091fb441ed19cd7de92550/text_encoders/minimax_music3_text_encoder_pruned_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-Music-3) |
| `vae/` | `minimax_music3_dav.safetensors` | audio VAE (DAV) | 0.22 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/9e364ccd290a401561091fb441ed19cd7de92550/vae/minimax_music3_dav.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-Music-3) |

<details><summary>SHA-256</summary>

```
45494a2b6b69af115902ff28eaf54118d19067aa54da01000f3e3efce7ba0e34  models/diffusion_models/minimax_music3_dit_fp16.safetensors
010b7416d2336a08c711bc22ee65849c9623069ddb7d89bec011a75699e52014  models/text_encoders/minimax_music3_text_encoder_pruned_int8_convrot.safetensors
2a32155b769be01445fcc2a8663b910fc9e1751e18dc1c3ec528064512d9ef0c  models/vae/minimax_music3_dav.safetensors
```

</details>

## How to use

In **MiniMaxMusic3TextEncode**: the style description (genre, BPM, key, mood) and the lyrics with sections (`[Intro]`, `[Verse]`, `[Chorus]`…). Length comes from the text itself; 30 steps, CFG 1.7.

## License

Personal and commercial use; **no territory restriction**. Commercial products must display "MiniMax-Music3" and there is a revenue cap for use without authorization. MiniMax claims no rights over the generated music (it is yours). A service generating music for others needs safeguards against misuse.

## Notes

- The original license is the MiniMax-Music3 Community License (the Comfy-Org card says Apache-2.0, but the MiniMax repository's LICENSE applies).
