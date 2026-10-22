# Qwen-Image 2.1 Turbo

[comfyui-workflows](../../README_ptBR.md) › **Qwen-Image 2.1 Turbo**

O template oficial `image_qwen_image_2_1_turbo_t2i` com o modelo turbo em INT8 da Comfy-Org. Reaproveita o text encoder e o VAE do Qwen-Image 2.1. O ramo opcional que reescreve o prompt com o Qwen3.5 9B (desligado no template) foi removido.

| | |
|---|---|
| Status | ✅ testado |
| Família | Qwen-Image 2.1 |
| Licença | [Qwen Research License](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE) |
| Download total | 17.28 GB |
| Teste | Prompt do teste (igual nos modelos de imagem da comparação): café-livraria com um gato tricolor e uma placa escrita "OPEN DAILY 8-20", seed 20261022, 1024x1024. |
| Tempo | **10s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15647 MiB |

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
| `diffusion_models/` | `qwen_image_2.1_turbo_int8_convrot.safetensors` | Qwen-Image 2.1 Turbo (INT8) | 7.26 GB | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/0217efd1d9c9452e84f6448903d6e21bfa171ffd/diffusion_models/qwen_image_2.1_turbo_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) |
| `text_encoders/` | `qwen3vl_8b_int8_convrot.safetensors` | text encoder Qwen3-VL 8B (INT8) | 9.35 GB | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/5dc5850eb514a3685f6a03a2641728a8f7549c69/text_encoders/qwen3vl_8b_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) |
| `vae/` | `qwen_image_2.1_vae_bf16.safetensors` | VAE do Qwen-Image 2.1 | 0.68 GB | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/5dc5850eb514a3685f6a03a2641728a8f7549c69/vae/qwen_image_2.1_vae_bf16.safetensors) | [página](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) |

<details><summary>SHA-256</summary>

```
8144a0182964aa8403ad6dbc011db837304167d235161b9aabaa8532e967314c  models/diffusion_models/qwen_image_2.1_turbo_int8_convrot.safetensors
8bfd0f6e12abf2d2d697ecc888e5e90b0d6741d6708f05799f53afa560452e8f  models/text_encoders/qwen3vl_8b_int8_convrot.safetensors
bb21f7473051e1ac368515dd3f2e15cd44d7a11748ee8823e1ddca3e4876b7c9  models/vae/qwen_image_2.1_vae_bf16.safetensors
```

</details>

## Como usar

1. Prompt no nó de texto; resolução no **ResolutionSelector**.
2. Para reativar o reescritor de prompt do template original, baixe `qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors` (Comfy-Org/Qwen-Image-2.1) e use o template do ComfyUI.

## Licença

**Só pesquisa e avaliação.** Qualquer uso comercial (inclusive assets de produto grátis publicado) exige licença da Alibaba (model-business@notice.qwencloud.com). Ao redistribuir os pesos, manter o aviso de licença.

## Observações

Comparação na mesma seed/prompt (RTX 5060 Ti): Qwen 2.1 24 s · Qwen 2.1 Turbo 10 s · Krea 2 Turbo 23 s · Flux 3 Klein 21 s · MOSS-Image 35 s. Todos acertaram o texto da placa.
