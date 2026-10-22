# Qwen-Image 2.1 · edição por instrução

[comfyui-workflows](../../README_ptBR.md) › **Qwen-Image 2.1 · edição por instrução**

O template oficial `image_qwen_image_2_1_image_edit` com o exemplo original: vestir a pessoa da imagem 1 com a camisa da imagem 2 ("Replace costumes for the character"). As imagens de exemplo vêm do repositório Comfy-Org/workflow_templates.

| | |
|---|---|
| Status | ✅ testado |
| Família | Qwen-Image 2.1 |
| Licença | [Qwen Research License](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE) |
| Download total | 17.28 GB |
| Teste | exemplo original: roupa trocada pela camisa jeans de referência, rosto e pose preservados |
| Tempo | **1min 17s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15583 MiB |

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

<details><summary>SHA-256</summary>

```
cb74113cb03faecd79611b01fd7fd642f0aa60d6f0b95086abee214d75eaa57d  models/diffusion_models/qwen_image_2.1_int8_convrot.safetensors
8bfd0f6e12abf2d2d697ecc888e5e90b0d6741d6708f05799f53afa560452e8f  models/text_encoders/qwen3vl_8b_int8_convrot.safetensors
bb21f7473051e1ac368515dd3f2e15cd44d7a11748ee8823e1ddca3e4876b7c9  models/vae/qwen_image_2.1_vae_bf16.safetensors
```

</details>

## Como usar

1. Imagem a editar no primeiro **LoadImage** (`image_1`); referências nos seguintes, citadas no prompt como `<image1>`, `<image2>`…
2. Imagens de exemplo: [portrait_model_denim.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/portrait_model_denim.png) e [clothing_light_blue_denim_shirt.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/clothing_light_blue_denim_shirt.png) → coloque em `ComfyUI/input/`.

## Licença

**Só pesquisa e avaliação.** Qualquer uso comercial (inclusive assets de produto grátis publicado) exige licença da Alibaba (model-business@notice.qwencloud.com). Ao redistribuir os pesos, manter o aviso de licença.

## Observações

- O ramo opcional de reescrita de prompt (Qwen3.5 9B, desligado no template) foi removido.
