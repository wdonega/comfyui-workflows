# Bernini-R · transferência de estilo (anime / real)

[comfyui-workflows](../../README_ptBR.md) › **Bernini-R · transferência de estilo (anime / real)**

O template oficial `video_bernini_r_video_editing` (edição de vídeo por instrução, ByteDance Bernini-R sobre o Wan 2.2 14B, high + low noise) em INT8 convrot, com o LoRA de velocidade lightx2v (6 steps) e os LoRAs de estilo do **tarn59** encadeados nos dois ramos. Modo "Video Editing (Style / Motion)" e prompt-gatilho `Anime style transfer.`

| | |
|---|---|
| Status | ✅ testado |
| Família | Wan 2.2 (Bernini-R) |
| Licença | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Download total | 39.15 GB |
| Teste | fonte 4,9 s (117 frames, 480x832), LoRA de anime 1.0: personagem convertido para anime (rosto e olhos), movimento e enquadramento idênticos; o fundo ficou quase fotográfico |
| Tempo | **18min 45s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 11663 MiB |

## Arquivos desta pasta

| Arquivo | O que é |
|---|---|
| `workflow.json` | Workflow para arrastar na interface do ComfyUI |
| `workflow.api.json` | Mesmo workflow no formato da API (parâmetros do teste, entradas de exemplo) |
| `install.sh` | Instala custom nodes e baixa os modelos para as pastas certas |
| `components.json` | Fonte dos dados deste README e do install.sh |

## Instalação

```bash
# na máquina com o ComfyUI (o script confere se a pasta é a raiz do ComfyUI)
bash install.sh /path/to/ComfyUI

# ComfyUI em Docker (container "comfyui")
docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh
```

Arquivos que já existem com o tamanho certo são pulados. Downloads novos têm o SHA-256 conferido (`VERIFY_EXISTING=1` confere também os que já existiam).

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `wan2.2_bernini_r_high_noise_int8_convrot.safetensors` | Bernini-R high noise (INT8) | 14.54 GB | [download](https://huggingface.co/Comfy-Org/Bernini-R/resolve/8e6d2ce0c2ead4dd237482c504ea9e4ae5b15347/diffusion_models/wan2.2_bernini_r_high_noise_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/Bernini-R) |
| `diffusion_models/` | `wan2.2_bernini_r_low_noise_int8_convrot.safetensors` | Bernini-R low noise (INT8) | 14.54 GB | [download](https://huggingface.co/Comfy-Org/Bernini-R/resolve/8e6d2ce0c2ead4dd237482c504ea9e4ae5b15347/diffusion_models/wan2.2_bernini_r_low_noise_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/Bernini-R) |
| `text_encoders/` | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | text encoder UMT5-XXL (FP8) | 6.74 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | [página](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `vae/` | `Wan2_1_VAE_bf16.safetensors` | VAE do Wan 2.1 | 0.25 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/vae/Wan2_1_VAE_bf16.safetensors) | [página](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `loras/` | `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors` | LoRA de velocidade lightx2v (Apache-2.0) | 0.63 GB | [download](https://huggingface.co/Kijai/WanVideo_comfy/resolve/8260d429d19fd7a72304cad059160b95d843913f/Lightx2v/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors) | [página](https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill) |
| `loras/` | `bernini_r_anime_style_transfer_high_noise.safetensors` | #56 estilo anime (high noise) | 0.61 GB | [download](https://huggingface.co/tarn59/bernini_r_anime_style_transfer_lora/resolve/9c8244d055585c82755186b9c4ac892f646d26f7/bernini_r_anime_style_transfer_high_noise.safetensors) | [página](https://huggingface.co/tarn59/bernini_r_anime_style_transfer_lora) |
| `loras/` | `bernini_r_anime_style_transfer_low_noise.safetensors` | #56 estilo anime (low noise) | 0.61 GB | [download](https://huggingface.co/tarn59/bernini_r_anime_style_transfer_lora/resolve/9c8244d055585c82755186b9c4ac892f646d26f7/bernini_r_anime_style_transfer_low_noise.safetensors) | [página](https://huggingface.co/tarn59/bernini_r_anime_style_transfer_lora) |
| `loras/` | `bernini_r_real_life_style_transfer_v3_high_noise.safetensors` | #56 estilo real-life v3 (high noise) | 0.61 GB | [download](https://huggingface.co/tarn59/bernini_r_real_life_style_transfer_lora/resolve/b48438d22e40dff00d7e585d66c96ff9dd1c11d6/bernini_r_real_life_style_transfer_v3_high_noise.safetensors) | [página](https://huggingface.co/tarn59/bernini_r_real_life_style_transfer_lora) |
| `loras/` | `bernini_r_real_life_style_transfer_v3_low_noise.safetensors` | #56 estilo real-life v3 (low noise) | 0.61 GB | [download](https://huggingface.co/tarn59/bernini_r_real_life_style_transfer_lora/resolve/b48438d22e40dff00d7e585d66c96ff9dd1c11d6/bernini_r_real_life_style_transfer_v3_low_noise.safetensors) | [página](https://huggingface.co/tarn59/bernini_r_real_life_style_transfer_lora) |

<details><summary>SHA-256</summary>

```
9d9a84f6e70032bd8f1dab40f5b0270fefd259ac5111a52b4acb752773c119b3  models/diffusion_models/wan2.2_bernini_r_high_noise_int8_convrot.safetensors
98fe00c6e38a745929cd7770a84ae3814c834d2ed7bef6b8a0a526c896fe8e5c  models/diffusion_models/wan2.2_bernini_r_low_noise_int8_convrot.safetensors
c3355d30191f1f066b26d93fba017ae9809dce6c627dda5f6a66eaa651204f68  models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
1ab9a32cc2c740f6e39d80d367ce5dcc28db8c71b79b28670546b8973e9d75f9  models/vae/Wan2_1_VAE_bf16.safetensors
37d49218544b9e0bfb8e831d1399f451fbc5068aff6474f42a90c928363c3573  models/loras/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors
b5b5cf67a67345fb37de4da7bb5967c75496606081ba7e743b67b862a172b26f  models/loras/bernini_r_anime_style_transfer_high_noise.safetensors
c944b81911c97897e451da5b12236a2d2aa6f46797a4948b2e671ef466eba5ed  models/loras/bernini_r_anime_style_transfer_low_noise.safetensors
047080ab2333fd69a0188bdb8fb7d8f24f23bd37fc0d62d95df8ffe082790ed0  models/loras/bernini_r_real_life_style_transfer_v3_high_noise.safetensors
45d87cb48ecafd2b72143d418127abc42316cb92604f50f262acdfdb2aae93e9  models/loras/bernini_r_real_life_style_transfer_v3_low_noise.safetensors
```

</details>

## Como usar

1. **LoadVideo**: o vídeo a editar (`source.mp4`; o **Video Slice** usa os primeiros 5 s).
2. Modo no combo de tarefa: **Video Editing (Style / Motion)**.
3. Prompt = gatilho do LoRA: `Anime style transfer.` (anime) ou `Real life style transfer.` (real-life; troque os dois LoRAs pelos `real_life_..._v3`).
4. Os LoRAs de estilo ficam **depois** do lightx2v, um no ramo high noise e outro no low noise, força 1.0.
5. Sem estilo: tire os dois nós de LoRA de estilo e escreva a edição no prompt (ex.: trocar o fundo).

## Licença

Apache-2.0: uso pessoal e comercial livres, sem limite de receita nem de território; basta manter os avisos de licença ao redistribuir os pesos. As saídas são suas.

## Observações

- O template original usa os pesos FP8 (15,6 GB cada); aqui foram usados os INT8 convrot (14,5 GB cada).
- O LoRA de real-life foi baixado, mas só o de anime foi testado.
- Bernini-R tem suporte nativo no core do ComfyUI v0.37 (não precisa de custom node).
