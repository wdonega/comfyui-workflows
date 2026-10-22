# LTX 2.3 · imagem para vídeo com áudio

[comfyui-workflows](../../README_ptBR.md) › **LTX 2.3 · imagem para vídeo com áudio**

O template oficial do ComfyUI `video_ltx2_3_i2v` (nós nativos, sem custom node obrigatório) com a pilha de modelos separada do Kijai: transformer **destilado** em FP8, VAEs e Gemma 3 em FP8. Gera em meia resolução, faz upscale x2 no latente e refina; o áudio sai junto, com fala.

| | |
|---|---|
| Status | ✅ testado |
| Família | LTX 2.3 |
| Licença | [LTX-2 Community License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE) |
| Download total | 43.35 GB |
| Teste | 704x1280, 25 fps, 121 frames (4,8 s), imagem de referência + prompt com fala: identidade mantida, fala audível; corte do retrato de estúdio para a praia porque imagem e prompt mostram cenários diferentes |
| Tempo | **1min 51s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15845 MiB |

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

## Custom nodes

| Nó | Versão testada | Página |
|---|---|---|
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors` | LTX 2.3 22B destilado, só transformer (FP8 com escala de ativação) | 25.02 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_video_vae_bf16.safetensors` | VAE de vídeo | 1.45 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_video_vae_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_audio_vae_bf16.safetensors` | VAE de áudio | 0.36 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_audio_vae_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `text_encoders/` | `gemma_3_12B_it_fp8_scaled.safetensors` | text encoder Gemma 3 12B (FP8) | 13.21 GB | [download](https://huggingface.co/Comfy-Org/ltx-2/resolve/ccde4ba417d7900669fd56dd292a883cee11ff37/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) | [página](https://huggingface.co/Comfy-Org/ltx-2) |
| `text_encoders/` | `ltx-2.3_text_projection_bf16.safetensors` | projeção de texto do LTX 2.3 | 2.31 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `latent_upscale_models/` | `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | upscaler espacial x2 (2º estágio) | 1.00 GB | [download](https://huggingface.co/Lightricks/LTX-2.3/resolve/c1521179de480464f366a98a9d9b2acc4cc097b9/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) | [página](https://huggingface.co/Lightricks/LTX-2.3) |

<details><summary>SHA-256</summary>

```
7327111e298066af8032f573d8db187986229ed2d4c926818ebf02041cfac8cf  models/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors
01ea62d09bc139f95c5dee7b5c062ad6a3e6cd8be910a1983ac02e7eb5b8ee3b  models/vae/LTX23_video_vae_bf16.safetensors
5bc10fa4adecf99dda132d916e23048cbd56797702c5fa50eb5d2079048a38c3  models/vae/LTX23_audio_vae_bf16.safetensors
60216ce97c01c3a8753c2dfd0a89fc76e16fbe446d1a32ef8f1b528ac8bae466  models/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors
911d59bb4cb7708179c9a0045ea0fe41212ecfb77aed3a02702b7c0a8274911f  models/text_encoders/ltx-2.3_text_projection_bf16.safetensors
5f416311fa8172b65af67530758964708d29a317b830d689a51143b7f91913ed  models/latent_upscale_models/ltx-2.3-spatial-upscaler-x2-1.1.safetensors
```

</details>

## Como usar

1. Imagem inicial no **LoadImage**; prompt no **PrimitiveStringMultiline** (inclua falas entre aspas e os sons).
2. Largura/altura e duração (segundos) nos **PrimitiveInt**; fps no outro PrimitiveInt (25).
3. As sigmas manuais do template (8 + 3 steps) já servem para o modelo destilado.
4. Para uma transição contínua, use uma imagem que já esteja no cenário descrito no prompt.

## Licença

Uso pessoal e comercial grátis para pessoas e empresas com receita anual abaixo de US$ 10 mi; acima disso, licença comercial paga da Lightricks. **Sem restrição de território.** A Lightricks não reivindica as saídas (são suas). Não pode usar saídas para treinar modelos concorrentes. O text encoder Gemma 3 segue os Gemma Terms of Use do Google (política de uso proibido; saídas livres).

## Observações

- Diferenças para o template oficial: em vez do checkpoint `ltx-2.3-22b-dev-fp8` + LoRA destilado + Gemma FP4, usa o transformer destilado do Kijai, os VAEs separados e o Gemma FP8 (a mesma pilha do Face Swap #17, para baixar uma vez só). O ramo opcional que melhora o prompt com o Gemma (desligado no template) foi removido.
- KJNodes entra só pelo `VAELoaderKJ`.
- Muito mais rápido que o MiniMax H3: 111 s para ~5 s de vídeo.
