# H3 Long Video (LLM-split prompt)

[comfyui-workflows](../../README.md) › **H3 Long Video (LLM-split prompt)**

Generates videos longer than a single H3 sampling by chaining segments that continue motion and audio. An LLM (any OpenAI-compatible server; in the test, a local llama.cpp on another GPU) splits the story into per-segment prompts with the right timing. Uses Ref2VA + Ref2V Turbo 8-step LoRA and sparse attention (`BlockSparseAttention`).

| | |
|---|---|
| Status | ✅ tested |
| Family | MiniMax H3 |
| License | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Total download | 44.43 GB |
| Test | 16 s in 2 segments of 8 s, 960x544, 8 steps, 1 reference; qwen3.8-flash-next (local llama.cpp, another GPU) split the story correctly (dialogue in segment 2); continuous join, consistent identity, continuous audio |
| Time | **11min 26s** (RTX 5060 Ti 16 GB, 2026-10-25) |
| Peak VRAM | 15659 MiB |

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
| ComfyUI-H3-Long-Video | `7499153` | https://github.com/ooizj/ComfyUI-H3-Long-Video |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | Ref2VA model (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | Qwen3-VL 32B text encoder (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_fp16.safetensors` | video VAE fp16 | 5.21 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_fp16.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | audio VAE | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_ref2v_turbo_8step_v1.1_768p_comfyui_bf16.safetensors` | Ref2V Turbo 8-step v1.1 LoRA (strength 0.8) | 1.96 GB | [download](https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/30f485ed874aa44c8183348ad361c5eabad318da/minimax_h3_ref2v_turbo_8step_v1.1_768p_comfyui_bf16.safetensors) | [page](https://huggingface.co/lightx2v/Minimax-h3-Turbo) |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
7c1f131492e7eddacaac9069a61b81bdd39de5cc96561e677c5eab1cdce5e522  models/vae/minimax_h3_video_vae_fp16.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
e56863a7524e0300729cbb7b64cc8b548d90698c1abbf7d83898b0122fbe1e81  models/loras/minimax_h3_ref2v_turbo_8step_v1.1_768p_comfyui_bf16.safetensors
```

</details>

## How to use

1. In **Ref Prompt Builder**, pick the reference images (`pictures`) and write the whole story; refer to `<Picture 1>` etc.
2. In **H3 Prompt API**: `api_url` = an OpenAI-compatible server (`http://localhost:8080/v1` in this file; DeepSeek in the author's original), `model` from that server. Give `max_tokens` headroom if the model "thinks" before answering.
3. In **H3 Long Video**: `total_seconds` (final length) and `segment_seconds` (length of each segment). More than one segment requires the Prompt API connected.
4. `local_llm` = `auto`: it only unloads ComfyUI's models when the URL is localhost. If your LLM runs on another machine or GPU, use its address and nothing is unloaded.

## License

Personal and commercial use allowed up to US$ 20M/year in revenue (above that, MiniMax's authorization). **Prohibited in the US, EU, UK and South Korea, including displaying or distributing the outputs there (clause V.4)**: do not use the videos in globally published projects. Published content must be labeled as AI-generated; impersonating real people without consent is prohibited; commercial products must display "MiniMax H3". Third-party LoRAs inherit these terms.

## Notes

- The log with each segment's prompts goes to `output/h3_prompt_logs/`.
- The author recommends strong LLMs (27B dense or DeepSeek) to split timed dialogue; qwen3.8-flash-next (local llama.cpp) got it right in the test.
- For the UI workflow with the author's original layout (subgraph), see `example_workflows/` in the node's repository.
- Time measured on v0.42.4 with the card limited to 165 W (default 180 W). On this machine, at 180 W, the card (on a riser) fell off the bus three times in this workflow, the one with the longest sustained load in the repo.
