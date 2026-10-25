# H3 HR Endless Sampler (Gemma 4 directs the chunks)

[comfyui-workflows](../../README.md) › **H3 HR Endless Sampler (Gemma 4 directs the chunks)**

Replaces `SamplerCustomAdvanced` with a chunked sampler with latent continuation. A local **Gemma 4 12B** (llama.cpp) analyzes the prompt and references, plans the shots and writes each chunk's prompt; `[Shot N] At MM:SS.mmm,` cuts land on the exact frame. Ref2VA without LoRA, 20 steps.

| | |
|---|---|
| Status | ✅ tested |
| Family | MiniMax H3 |
| License | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Total download | 50.11 GB |
| Test | 6 s, 0.5 MP (960x544), 39-frame chunks (5 chunks), 20 steps, 1 reference, 2 shots with a cut at 00:03.000 (landed on frame 72); identity kept. Of the total: H3 508 s, Gemma 377 s |
| Time | **18min 38s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 15583 MiB |

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
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |
| VideoHelperSuite | 1.7.9 | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |
| ComfyUI-HR-Endless-Sampler | `1681f89` | https://github.com/hradec/ComfyUI-HR-Endless-Sampler |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | Ref2VA model (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | Qwen3-VL 32B text encoder (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_fp16.safetensors` | video VAE fp16 | 5.21 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_fp16.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | audio VAE | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `llama_cpp/gemma-4-12b-it-qat-q4_0/` | `gemma-4-12b-it-qat-q4_0.gguf` | Gemma 4 12B QAT Q4_0 (director; Apache-2.0) | 6.98 GB | [download](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf/resolve/29d097773436b69ff9feafd636ab4cf873786537/gemma-4-12b-it-qat-q4_0.gguf) | [page](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf) |
| `llama_cpp/gemma-4-12b-it-qat-q4_0/` | `mmproj-gemma-4-12b-it-qat-q4_0.gguf` | Gemma vision projector | 0.18 GB | [download](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf/resolve/29d097773436b69ff9feafd636ab4cf873786537/mmproj-gemma-4-12b-it-qat-q4_0.gguf) | [page](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf) |
| `llama_cpp/gemma-4-12b-it-qat-q4_0/` | `gemma-4-12B-it-qat-assistant-MTP-Q8_0.gguf` | MTP drafter (speeds up Gemma) | 0.47 GB | [download](https://huggingface.co/Janvitos/gemma-4-12B-it-qat-assistant-MTP-Q8_0-GGUF/resolve/f5fdc2cdfa1a1257cf6d979fb17f1c94f9852ec4/gemma-4-12B-it-qat-assistant-MTP-Q8_0.gguf) | [page](https://huggingface.co/Janvitos/gemma-4-12B-it-qat-assistant-MTP-Q8_0-GGUF) |
| `vae_approx/` | `taeh3.safetensors` | TAEH3: lightweight chunk preview (MIT, optional) | 23 MB | [download](https://github.com/madebyollin/taehv/raw/011dfc2112197741c540e0bdd5b7b67bcc930771/safetensors/taeh3.safetensors) | [page](https://github.com/madebyollin/taehv) |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
7c1f131492e7eddacaac9069a61b81bdd39de5cc96561e677c5eab1cdce5e522  models/vae/minimax_h3_video_vae_fp16.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b  models/llama_cpp/gemma-4-12b-it-qat-q4_0/gemma-4-12b-it-qat-q4_0.gguf
cb018338a7538a9814d994bfe54644c71eb7ed54e31eae2f721e45fd3c260da7  models/llama_cpp/gemma-4-12b-it-qat-q4_0/mmproj-gemma-4-12b-it-qat-q4_0.gguf
13331068b6af643c3dc75e619373b674c1f75a1958e7c82e2020d96a17c63809  models/llama_cpp/gemma-4-12b-it-qat-q4_0/gemma-4-12B-it-qat-assistant-MTP-Q8_0.gguf
4fd022bfcab08772fe0536b17ea1a3bbb5625be11e397868d1c5d891863d4c13  models/vae_approx/taeh3.safetensors
```

</details>

## How to use

1. Write the prompt with shots in the node's format: `[Shot 1] ...` and, from the second one on, `[Shot 2] At 00:03.000, ...` (time as MM:SS.mmm at 24 fps). Without `At`, the node stops with an error.
2. Duration in seconds in the **PrimitiveFloat** feeding the `length` math; resolution in **ResolutionSelector** (`megapixels`).
3. `chunk_frames`: 39 is a good starting point on 16 GB (less VRAM, more joins).
4. References go through **ImageScaleBy** (the author's template uses 0.3 for 4K images; with ~800 px images use 1.0).

## License

Personal and commercial use allowed up to US$ 20M/year in revenue (above that, MiniMax's authorization). **Prohibited in the US, EU, UK and South Korea, including displaying or distributing the outputs there (clause V.4)**: do not use the videos in globally published projects. Published content must be labeled as AI-generated; impersonating real people without consent is prohibited; commercial products must display "MiniMax H3". Third-party LoRAs inherit these terms.

## Notes

- **Requires `llama-cpp-python` 0.3.35 with CUDA** in ComfyUI's Python. The official wheel (cu125) is built with AVX-512 and crashes with *Illegal instruction* on CPUs without AVX-512; here it was built from source with `-DGGML_CUDA=on -DCMAKE_CUDA_ARCHITECTURES=120 -DGGML_NATIVE=OFF -DGGML_AVX2=ON -DGGML_AVX512=OFF` against CUDA 13 (ComfyUI's cu13 libs). Install with `--no-deps` so torch is left alone.
- The author's template uses the **Spectrum** node (`comfyui-spectrum-minimax-h3`, optional accelerator). Its latest version is Flagged in the ComfyUI registry; this workflow was tested **without** it.
- Gemma shares the GPU with H3: in this test it took 377 s of the 1118 s. `cache_gemma_preproduction` reuses the planning when only the seed changes.
- The node downloads Gemma by itself if missing; install.sh already puts it in place.
- **Side effect:** `pytorch_memory_fraction` (0.85) stays in effect for the **whole** ComfyUI process after the workflow finishes. In the regression run, Wan Animate 2 run afterwards ran out of memory (13.2 GB limit on a 16 GB card). Restart ComfyUI after using HR Endless, or use 1.0.
