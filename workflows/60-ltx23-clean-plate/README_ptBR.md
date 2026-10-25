# LTX 2.3 · Clean Plate (remove pessoas do vídeo)

[comfyui-workflows](../../README_ptBR.md) › **LTX 2.3 · Clean Plate (remove pessoas do vídeo)**

O IC-LoRA **Clean Plate** da Lightricks no workflow vídeo-para-vídeo oficial do ComfyUI-LTXVideo: o vídeo original entra como referência e sai regenerado sem os elementos em movimento, mantendo o fundo estático. Sem máscara: é um modelo de quadro inteiro.

| | |
|---|---|
| Status | ✅ testado |
| Família | LTX 2.3 |
| Licença | [LTX-2 Community License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE) |
| Download total | 42.68 GB |
| Teste | 4 s (97 frames) de um garoto correndo numa rua com um monstro e fumaça ao fundo: garoto, monstro e fumaça removidos; rua, carros, árvores, reflexos e movimento de câmera preservados |
| Tempo | **3min 39s** (RTX 5060 Ti 16 GB, 2026-10-24) |
| Pico de VRAM | 15791 MiB |

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
| ComfyUI-LTXVideo | `220e1d4` | https://github.com/Lightricks/ComfyUI-LTXVideo |
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors` | LTX 2.3 22B destilado, só transformer (FP8 com escala de ativação) | 25.02 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_video_vae_bf16.safetensors` | VAE de vídeo | 1.45 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_video_vae_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_audio_vae_bf16.safetensors` | VAE de áudio | 0.36 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_audio_vae_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `text_encoders/` | `gemma_3_12B_it_fp8_scaled.safetensors` | text encoder Gemma 3 12B (FP8) | 13.21 GB | [download](https://huggingface.co/Comfy-Org/ltx-2/resolve/ccde4ba417d7900669fd56dd292a883cee11ff37/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) | [página](https://huggingface.co/Comfy-Org/ltx-2) |
| `text_encoders/` | `ltx-2.3_text_projection_bf16.safetensors` | projeção de texto do LTX 2.3 | 2.31 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `loras/` | `ltx-2.3-22b-ic-lora-clean-plate-1.0.safetensors` | IC-LoRA Clean Plate 1.0 (gated: aceite a licença) | 0.33 GB | [download](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Clean-Plate/resolve/c2ab69ffe3e21410293bdee99d7d8ca0bc5a9ad0/ltx-2.3-22b-ic-lora-clean-plate-1.0.safetensors) | [página](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Clean-Plate) |

<details><summary>SHA-256</summary>

```
7327111e298066af8032f573d8db187986229ed2d4c926818ebf02041cfac8cf  models/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors
01ea62d09bc139f95c5dee7b5c062ad6a3e6cd8be910a1983ac02e7eb5b8ee3b  models/vae/LTX23_video_vae_bf16.safetensors
5bc10fa4adecf99dda132d916e23048cbd56797702c5fa50eb5d2079048a38c3  models/vae/LTX23_audio_vae_bf16.safetensors
60216ce97c01c3a8753c2dfd0a89fc76e16fbe446d1a32ef8f1b528ac8bae466  models/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors
911d59bb4cb7708179c9a0045ea0fe41212ecfb77aed3a02702b7c0a8274911f  models/text_encoders/ltx-2.3_text_projection_bf16.safetensors
a1b573a9649df549901ae6c5571a6d305d0620aed8953f39536e34da4ca01d6a  models/loras/ltx-2.3-22b-ic-lora-clean-plate-1.0.safetensors
```

</details>

## Como usar

1. **LoadVideo**: o vídeo original (`source.mp4`) **com trilha de áudio** (o workflow codifica o áudio; acrescente uma muda se não houver). Dimensões múltiplas de 32 e frames 8k+1.
2. Prompt positivo: descreva a **cena vazia** desejada, não "remova X"; cite o que não pode aparecer. Negativo: as pessoas/objetos a remover.
3. O ramo de imagem inicial (`first_frame.png`) vem em bypass; o arquivo só precisa existir.

## Licença

Uso pessoal e comercial grátis para pessoas e empresas com receita anual abaixo de US$ 10 mi; acima disso, licença comercial paga da Lightricks. **Sem restrição de território.** A Lightricks não reivindica as saídas (são suas). Não pode usar saídas para treinar modelos concorrentes. O text encoder Gemma 3 segue os Gemma Terms of Use do Google (política de uso proibido; saídas livres).

## Observações

- Mudanças em relação ao workflow oficial (que usa o IC-LoRA "instant shave" de exemplo): pilha do Kijai com o transformer **destilado** (sem o LoRA de destilação), Gemma FP8 local e o LoRA Clean Plate.
- Não serve quando a pessoa ocupa quase todo o quadro (ex.: pernas em primeira pessoa).
- Dependências pip do ComfyUI-LTXVideo: só `OpenImageIO` e `ninja` faltavam (`PIP_USER=true python3.13 -m pip install OpenImageIO ninja`).
