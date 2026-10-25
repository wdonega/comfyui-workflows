# LTX 2.3 · Foley (som para vídeo mudo)

[comfyui-workflows](../../README_ptBR.md) › **LTX 2.3 · Foley (som para vídeo mudo)**

O workflow oficial da Lightricks para o LoRA **Foley V2A**: o vídeo entra como latente fixo e só o áudio é gerado (máscara por tempo), com o guiador multimodal do ComfyUI-LTXVideo (CFG 6 no áudio, 30 steps). Usa o transformer **dev** (o LoRA foi treinado nele).

| | |
|---|---|
| Status | ✅ testado |
| Família | LTX 2.3 |
| Licença | [LTX-2 Community License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE) |
| Download total | 39.07 GB |
| Teste | vídeo mudo de 7 s (169 frames, garoto correndo na chuva) + prompt de chuva e passos: áudio de 7 s a 48 kHz, contínuo do início ao fim (média −10 a −15 dB); a sincronia dos passos precisa ser conferida ouvindo |
| Tempo | **32min 09s** (RTX 5060 Ti 16 GB, 2026-10-24) |
| Pico de VRAM | 15621 MiB |

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
| VideoHelperSuite | 1.7.9 | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `ltx-2.3-22b-dev_transformer_only_int8_convrot.safetensors` | LTX 2.3 22B dev, só transformer (INT8) | 21.51 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/diffusion_models/ltx-2.3-22b-dev_transformer_only_int8_convrot.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_video_vae_bf16.safetensors` | VAE de vídeo | 1.45 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_video_vae_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_audio_vae_bf16.safetensors` | VAE de áudio | 0.36 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_audio_vae_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `text_encoders/` | `gemma_3_12B_it_fp8_scaled.safetensors` | text encoder Gemma 3 12B (FP8) | 13.21 GB | [download](https://huggingface.co/Comfy-Org/ltx-2/resolve/ccde4ba417d7900669fd56dd292a883cee11ff37/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) | [página](https://huggingface.co/Comfy-Org/ltx-2) |
| `text_encoders/` | `ltx-2.3_text_projection_bf16.safetensors` | projeção de texto do LTX 2.3 | 2.31 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `loras/` | `ltx-2.3-22b-lora-foley-v2a-1.0.safetensors` | LoRA Foley V2A 1.0 (gated: aceite a licença) | 0.23 GB | [download](https://huggingface.co/Lightricks/LTX-2.3-22b-LoRA-Foley-V2A/resolve/4f42751a30658d79595a27258ea9fb4f4308dcb5/ltx-2.3-22b-lora-foley-v2a-1.0.safetensors) | [página](https://huggingface.co/Lightricks/LTX-2.3-22b-LoRA-Foley-V2A) |

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

## Como usar

1. **VHS LoadVideo**: o vídeo **sem áudio** (`muted_video.mp4`); o número de frames é arredondado para 8k+1.
2. Prompt positivo: descreva os sons e quando acontecem ("passos em sincronia com cada passada"); o negativo do exemplo já exclui música e fala.
3. LoRA com força 0,8–1,0. O vídeo sai com o áudio gerado.

## Licença

Uso pessoal e comercial grátis para pessoas e empresas com receita anual abaixo de US$ 10 mi; acima disso, licença comercial paga da Lightricks. **Sem restrição de território.** A Lightricks não reivindica as saídas (são suas). Não pode usar saídas para treinar modelos concorrentes. O text encoder Gemma 3 segue os Gemma Terms of Use do Google (política de uso proibido; saídas livres).

## Observações

- Lento: 30 steps no modelo dev, ~32 min para 7 s.
- Mudanças em relação ao workflow oficial: pilha de modelos do Kijai (dev INT8 + VAEs + Gemma FP8) no lugar do checkpoint completo; os dois nós `ArbitraryCode` (que executam Python digitado no workflow) trocados por `ComfyMathExpression` + `ImageFromBatch` nativos; `VideoSave_LTX` trocado por `CreateVideo` + `SaveVideo`.
- Dependências pip do ComfyUI-LTXVideo: só `OpenImageIO` e `ninja` faltavam (`PIP_USER=true python3.13 -m pip install OpenImageIO ninja`).
