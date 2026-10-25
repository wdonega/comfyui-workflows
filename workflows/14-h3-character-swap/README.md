# H3 Character Swap (Relay 2.0)

[comfyui-workflows](../../README.md) › **H3 Character Swap (Relay 2.0)**

The author's (akatz-ai) official workflow with **H3 Relay 2.0**: SAM 3.1 masks the described person, and Ref2VA with the Character Swap v1.5 LoRA + FL2V Turbo 8-step swaps the identity for the reference image. Keeps motion, camera, set and the original soundtrack. Long videos are processed in windows.

| | |
|---|---|
| Status | ✅ tested |
| Family | MiniMax H3 |
| License | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Total download | 46.33 GB |
| Test | 4 s source (96 frames, 736x1280, 24 fps), subject `boy`, author's recipe (8 steps, er_sde, CFG 1, LoRAs 1.0): identity swapped, pose/scene/timing preserved; clothing did not follow the reference |
| Time | **12min 56s** (RTX 5060 Ti 16 GB, 2026-10-22) |
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

## Custom nodes

| Node | Tested version | Page |
|---|---|---|
| H3 Relay | `e2a7665` | https://github.com/akatz-ai/h3-relay |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | Ref2VA model (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | Qwen3-VL 32B text encoder (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_fp16.safetensors` | video VAE fp16 (author's recipe) | 5.21 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_fp16.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | audio VAE | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [page](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_fl2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors` | FL2V Turbo 8-step LoRA (required) | 1.96 GB | [download](https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/30f485ed874aa44c8183348ad361c5eabad318da/minimax_h3_fl2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors) | [page](https://huggingface.co/lightx2v/Minimax-h3-Turbo) |
| `loras/` | `h3_character_swap_v1.5.safetensors` | Character Swap v1.5 LoRA | 0.16 GB | [download](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/resolve/96ea3407b230b6f7df71c58c70e31df96bd7e533/h3_character_swap_v1.5.safetensors) | [page](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA) |
| `checkpoints/` | `sam3.1_multiplex_fp16.safetensors` | SAM 3.1 (person mask) | 1.75 GB | [download](https://huggingface.co/Comfy-Org/sam3.1/resolve/7bb8374780a725b4353ed31f3a9395c9742b5621/checkpoints/sam3.1_multiplex_fp16.safetensors) | [page](https://huggingface.co/Comfy-Org/sam3.1) |
| `loras/` | `h3-v2-challenge-eval-20261013/v2-1000.safetensors` | link → `../h3_character_swap_v1.5.safetensors` (name used by the author's workflow) | — | — | — |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
7c1f131492e7eddacaac9069a61b81bdd39de5cc96561e677c5eab1cdce5e522  models/vae/minimax_h3_video_vae_fp16.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
08cfe946033af7d27719b964b6e0a0e50c32138daabbd6ce4137e23df6bf9980  models/loras/minimax_h3_fl2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors
8f2c3c3eba161df8d0c6099598b4730f641f5ce01e04cd16d2427cff8a35218f  models/loras/h3_character_swap_v1.5.safetensors
9ba99c92703c2e8b4f47de2d34a539bb8e18923049e238b780d70dbe6368eb03  models/checkpoints/sam3.1_multiplex_fp16.safetensors
```

</details>

## How to use

1. Load `workflow.json`. In **LoadVideo**, one continuous shot (`source.mp4`); in **LoadImage**, the character reference (`reference.png`).
2. In **Prepare Source**: `duration_seconds` 0 = the whole video (normalized to 24 fps and multiples of 32 px).
3. In the SAM text (`subject`), describe the person to swap (e.g. `the man on the left`); check the mask in the preview.
4. Keep 8 steps, `er_sde`, `normal` scheduler, CFG 1 and both LoRAs at 1.0.
5. One person at a time: to swap two, run again using the output as the source.

## License

Personal and commercial use allowed up to US$ 20M/year in revenue (above that, MiniMax's authorization). **Prohibited in the US, EU, UK and South Korea, including displaying or distributing the outputs there (clause V.4)**: do not use the videos in globally published projects. Published content must be labeled as AI-generated; impersonating real people without consent is prohibited; commercial products must display "MiniMax H3". Third-party LoRAs inherit these terms.

## Notes

- Slow on 16 GB: ~76 s per step (8 steps per window of up to 124 frames) because the recipe targets 24 GB and offloads. 4 s of video took ~13 min.
- **Do not stack it with TaoMate** (the author's recipe uses only the 8-step Turbo).
- License: impersonating real people without consent is prohibited by the H3 license.
- **Credits:** `workflow.json` and `workflow.api.json` are Akatz Labs' official examples ([akatz-ai/MiniMax-H3-Character-Swap-LoRA](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/tree/main/examples)), redistributed unchanged; parts derived from ComfyUI templates are MIT (Comfy Org). The LoRA and H3 Relay belong to their authors.
