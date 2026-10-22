# SeedVR2 · upscale 4x

[comfyui-workflows](../../README_ptBR.md) › **SeedVR2 · upscale 4x**

O template oficial `utility_seedvr2_3b_int8_upscale_image`, com suporte nativo no ComfyUI (o custom node do plano não foi necessário). Restaura e amplia 4x em um único passo de difusão, com VAE em blocos.

| | |
|---|---|
| Status | ✅ testado |
| Família | SeedVR2 |
| Licença | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Download total | 3.96 GB |
| Teste | imagem 1024x1024 do MOSS-Image → 4096x4096: pelos e bigodes nítidos, sem artefatos |
| Tempo | **23s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 7831 MiB |

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
| `diffusion_models/` | `seedvr2_3b_int8_convrot.safetensors` | SeedVR2 3B (INT8) | 3.46 GB | [download](https://huggingface.co/Comfy-Org/SeedVR2/resolve/df48879708206a403d2a61acd55578c2e80fd233/diffusion_models/seedvr2_3b_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/SeedVR2) |
| `vae/` | `seedvr2_ema_vae_fp16.safetensors` | VAE do SeedVR2 | 0.50 GB | [download](https://huggingface.co/Comfy-Org/SeedVR2/resolve/df48879708206a403d2a61acd55578c2e80fd233/vae/seedvr2_ema_vae_fp16.safetensors) | [página](https://huggingface.co/Comfy-Org/SeedVR2) |

<details><summary>SHA-256</summary>

```
c3dec8bcc5916843a8a858572970597462e1f2dc598d6dfd818f6cd40f53a157  models/diffusion_models/seedvr2_3b_int8_convrot.safetensors
20678548f420d98d26f11442d3528f8b8c94e57ee046ef93dbb7633da8612ca1  models/vae/seedvr2_ema_vae_fp16.safetensors
```

</details>

## Como usar

1. Imagem no **LoadImage** (`input.png`).
2. Fator no **ResizeImageMaskNode** (`multiplier` 4). Para vídeo, use o template `utility_seedvr2_3b_int8_upscale_video`.

## Licença

Apache-2.0: uso pessoal e comercial livres, sem limite de receita nem de território; basta manter os avisos de licença ao redistribuir os pesos. As saídas são suas.

## Observações

- O nó `ImageCompare` do template (comparador visual da interface) foi removido da versão API.
- Só 7,8 GB de pico de VRAM: cabe com folga em 16 GB.
