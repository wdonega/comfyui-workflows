# Qwen-Image 2.1 · Viggle 4 steps (texto para imagem)

[comfyui-workflows](../../README_ptBR.md) › **Qwen-Image 2.1 · Viggle 4 steps (texto para imagem)**

Workflow de Tensor Alchemist com o LoRA turbo de 4 steps da Viggle: imagens de 2 MP (1920x1088) em ~11 s.

| | |
|---|---|
| Status | ✅ testado |
| Família | Qwen-Image 2.1 |
| Licença | [Qwen Research License](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE) |
| Download total | 17.62 GB |
| Teste | faroleiro num penhasco ao pôr do sol, 1920x1088, 4 steps |
| Tempo | **11s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15503 MiB |

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
| `diffusion_models/` | `qwen_image_2.1_int8_convrot.safetensors` | Qwen-Image 2.1 (INT8) | 7.26 GB | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/5dc5850eb514a3685f6a03a2641728a8f7549c69/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) |
| `text_encoders/` | `qwen3vl_8b_int8_convrot.safetensors` | text encoder Qwen3-VL 8B (INT8) | 9.35 GB | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/5dc5850eb514a3685f6a03a2641728a8f7549c69/text_encoders/qwen3vl_8b_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) |
| `vae/` | `qwen_image_2.1_vae_bf16.safetensors` | VAE do Qwen-Image 2.1 | 0.68 GB | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/5dc5850eb514a3685f6a03a2641728a8f7549c69/vae/qwen_image_2.1_vae_bf16.safetensors) | [página](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) |
| `loras/` | `Qwen-Image-2.1-viggle-turbo-4step-lora-r64.safetensors` | LoRA Viggle turbo 4 steps | 0.34 GB | [download](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/bafc91e4cc934f5fb1406b22496a0bed9b99c548/Qwen-Image-2.1-viggle-turbo-4step-lora-r64.safetensors) | [página](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo) |

<details><summary>SHA-256</summary>

```
cb74113cb03faecd79611b01fd7fd642f0aa60d6f0b95086abee214d75eaa57d  models/diffusion_models/qwen_image_2.1_int8_convrot.safetensors
8bfd0f6e12abf2d2d697ecc888e5e90b0d6741d6708f05799f53afa560452e8f  models/text_encoders/qwen3vl_8b_int8_convrot.safetensors
bb21f7473051e1ac368515dd3f2e15cd44d7a11748ee8823e1ddca3e4876b7c9  models/vae/qwen_image_2.1_vae_bf16.safetensors
5c494dce662a95898d0988831af733b203ceced9116a82aa099c997f96ea1a3a  models/loras/Qwen-Image-2.1-viggle-turbo-4step-lora-r64.safetensors
```

</details>

## Como usar

Prompt no **TextEncodeQwenImage21**; proporção e megapixels no **ResolutionSelector** (16:9, 2 MP).

## Licença

**Só pesquisa e avaliação.** Qualquer uso comercial (inclusive assets de produto grátis publicado) exige licença da Alibaba (model-business@notice.qwencloud.com). Ao redistribuir os pesos, manter o aviso de licença.

## Observações

- No arquivo de origem o LoRA estava em bypass (rodava como Qwen puro com 25 steps); aqui foi reativado com 4 steps, a receita do LoRA.
- Créditos: layout e testes do workflow por Tensor Alchemist; LoRA da Viggle (licença de pesquisa da Qwen).
