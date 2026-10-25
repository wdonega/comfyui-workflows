# LTX 2.3 · Foley (sound for silent video)

[comfyui-workflows](../../README.md) › **LTX 2.3 · Foley (sound for silent video)**

Lightricks' official workflow for the **Foley V2A** LoRA: the video goes in as a fixed latent and only the audio is generated (time mask), with ComfyUI-LTXVideo's multimodal guider (CFG 6 on audio, 30 steps). Uses the **dev** transformer (the LoRA was trained on it).

| | |
|---|---|
| Status | ✅ tested |
| Family | LTX 2.3 |
| License | [LTX-2 Community License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE) |
| Total download | 39.07 GB |
| Test | 7 s silent video (169 frames, a boy running in the rain) + rain and footsteps prompt: 7 s 48 kHz audio, continuous from start to end (mean −10 to −15 dB); footstep sync has to be checked by ear |
| Time | **32min 09s** (RTX 5060 Ti 16 GB, 2026-10-24) |
| Peak VRAM | 15621 MiB |

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
| ComfyUI-LTXVideo | `220e1d4` | https://github.com/Lightricks/ComfyUI-LTXVideo |
| VideoHelperSuite | 1.7.9 | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `ltx-2.3-22b-dev_transformer_only_int8_convrot.safetensors` | LTX 2.3 22B dev, transformer only (INT8) | 21.51 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/diffusion_models/ltx-2.3-22b-dev_transformer_only_int8_convrot.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_video_vae_bf16.safetensors` | video VAE | 1.45 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_video_vae_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_audio_vae_bf16.safetensors` | audio VAE | 0.36 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_audio_vae_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `text_encoders/` | `gemma_3_12B_it_fp8_scaled.safetensors` | Gemma 3 12B text encoder (FP8) | 13.21 GB | [download](https://huggingface.co/Comfy-Org/ltx-2/resolve/ccde4ba417d7900669fd56dd292a883cee11ff37/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) | [page](https://huggingface.co/Comfy-Org/ltx-2) |
| `text_encoders/` | `ltx-2.3_text_projection_bf16.safetensors` | LTX 2.3 text projection | 2.31 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | [page](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `loras/` | `ltx-2.3-22b-lora-foley-v2a-1.0.safetensors` | Foley V2A 1.0 LoRA (gated: accept the license) | 0.23 GB | [download](https://huggingface.co/Lightricks/LTX-2.3-22b-LoRA-Foley-V2A/resolve/4f42751a30658d79595a27258ea9fb4f4308dcb5/ltx-2.3-22b-lora-foley-v2a-1.0.safetensors) | [page](https://huggingface.co/Lightricks/LTX-2.3-22b-LoRA-Foley-V2A) |

<details><summary>SHA-256</summary>

```
6f4b86bd840cb83179e9021306a63119c3b4e664248292c4103613a2d4a4484c  models/diffusion_models/ltx-2.3-22b-dev_transformer_only_int8_convrot.safetensors
01ea62d09bc139f95c5dee7b5c062ad6a3e6cd8be910a1983ac02e7eb5b8ee3b  models/vae/LTX23_video_vae_bf16.safetensors
5bc10fa4adecf99dda132d916e23048cbd56797702c5fa50eb5d2079048a38c3  models/vae/LTX23_audio_vae_bf16.safetensors
60216ce97c01c3a8753c2dfd0a89fc76e16fbe446d1a32ef8f1b528ac8bae466  models/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors
911d59bb4cb7708179c9a0045ea0fe41212ecfb77aed3a02702b7c0a8274911f  models/text_encoders/ltx-2.3_text_projection_bf16.safetensors
1bc16020f3937f1dc4957b24c713bc04ec550d6502db8c3e1dd822c412e1fb85  models/loras/ltx-2.3-22b-lora-foley-v2a-1.0.safetensors
```

</details>

## How to use

1. **VHS LoadVideo**: the video **without audio** (`muted_video.mp4`); the frame count is rounded to 8k+1.
2. Positive prompt: describe the sounds and when they happen ("footsteps in sync with each stride"); the example's negative already excludes music and speech.
3. LoRA strength 0.8–1.0. The video comes out with the generated audio.

## License

Free personal and commercial use for individuals and companies with annual revenue under US$ 10M; above that, a paid commercial license from Lightricks. **No territory restrictions.** Lightricks claims no rights over the outputs (they are yours). Outputs may not be used to train competing models. The Gemma 3 text encoder follows Google's Gemma Terms of Use (prohibited-use policy; outputs are free).

## Notes

- Slow: 30 steps on the dev model, ~32 min for 7 s.
- Changes from the official workflow: Kijai's model stack (dev INT8 + VAEs + FP8 Gemma) instead of the full checkpoint; the two `ArbitraryCode` nodes (which run Python typed into the workflow) replaced by native `ComfyMathExpression` + `ImageFromBatch`; `VideoSave_LTX` replaced by `CreateVideo` + `SaveVideo`.
- ComfyUI-LTXVideo pip dependencies: only `OpenImageIO` and `ninja` were missing (`PIP_USER=true python3.13 -m pip install OpenImageIO ninja`).
