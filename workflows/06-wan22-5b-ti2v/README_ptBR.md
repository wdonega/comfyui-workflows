# Wan 2.2 5B · texto/imagem para vídeo

[comfyui-workflows](../../README_ptBR.md) › **Wan 2.2 5B · texto/imagem para vídeo**

O template oficial `video_wan2_2_5B_ti2v` sem mudanças: o modelo TI2V de 5B em fp16 (10 GB) gera 121 frames em 1280x704 a 24 fps. Funciona como texto-para-vídeo ou, ligando uma imagem inicial no `Wan22ImageToVideoLatent`, imagem-para-vídeo. Sem áudio.

| | |
|---|---|
| Status | ✅ testado |
| Família | Wan 2.2 |
| Licença | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Download total | 18.14 GB |
| Teste | prompt do template (músico no metrô), 1280x704, 121 frames, 20 steps uni_pc, CFG 5: cena coerente e fiel ao prompt |
| Tempo | **9min 10s** (RTX 5060 Ti 16 GB, 2026-10-23) |
| Pico de VRAM | 15465 MiB |

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
| `diffusion_models/` | `wan2.2_ti2v_5B_fp16.safetensors` | Wan 2.2 TI2V 5B (fp16) | 10.00 GB | [download](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/ee6f4a40737a995bf5818954cfce6d59443b0f04/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors) | [página](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) |
| `text_encoders/` | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | text encoder UMT5-XXL (FP8) | 6.74 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | [página](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `vae/` | `wan2.2_vae.safetensors` | VAE do Wan 2.2 | 1.41 GB | [download](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/ee6f4a40737a995bf5818954cfce6d59443b0f04/split_files/vae/wan2.2_vae.safetensors) | [página](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) |

<details><summary>SHA-256</summary>

```
456f901338bd9eadbded3828b819109a9b68e8a525ca5cf8d0049a69fcfeca1e  models/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors
c3355d30191f1f066b26d93fba017ae9809dce6c627dda5f6a66eaa651204f68  models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
e40321bd36b9709991dae2530eb4ac303dd168276980d3e9bc4b6e2b75fed156  models/vae/wan2.2_vae.safetensors
```

</details>

## Como usar

1. Prompt positivo no primeiro **CLIPTextEncode**; o negativo (em chinês, do template) pode ficar.
2. Resolução e duração no **Wan22ImageToVideoLatent** (121 frames = 5 s a 24 fps).
3. Para imagem-para-vídeo, ligue um **LoadImage** na entrada `start_image` do Wan22ImageToVideoLatent.

## Licença

Apache-2.0: uso pessoal e comercial livres, sem limite de receita nem de território; basta manter os avisos de licença ao redistribuir os pesos. As saídas são suas.

## Observações

- Plano original sugeria GGUF para 16 GB; o 5B em fp16 roda nativo (pico de 15,5 GB), sem custom node.
- O `umt5_xxl_fp8_e4m3fn_scaled` é o mesmo arquivo usado pelo Wan Animate 2 e pelo Bernini-R (SHA-256 idêntico).
