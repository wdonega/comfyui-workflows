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

### Modelos 7B (opcionais)

O repositório [Comfy-Org/SeedVR2](https://huggingface.co/Comfy-Org/SeedVR2) (Apache-2.0) também tem o SeedVR2 **7B**, normal e *sharp*. Funcionam neste mesmo workflow trocando o `unet_name` do **UNETLoader**; não estão no `install.sh`. Para baixar, em `models/diffusion_models/`:

| Arquivo | Tamanho | SHA-256 |
|---|---|---|
| [`seedvr2_7b_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/SeedVR2/resolve/df48879708206a403d2a61acd55578c2e80fd233/diffusion_models/seedvr2_7b_int8_convrot.safetensors) | 8.33 GB | `5aa0d25fc9d35e449b659d0c9a5dcb22e2a4fa04032101b95a39da42b32c1be6` |
| [`seedvr2_7b_sharp_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/SeedVR2/resolve/df48879708206a403d2a61acd55578c2e80fd233/diffusion_models/seedvr2_7b_sharp_int8_convrot.safetensors) | 8.33 GB | `db48be2f1cc7e36b01a2aa529810f5d9c6a971edd29be225cf1b0eb18d51c366` |

Teste (2026-10-25, template de vídeo oficial `utility_seedvr2_3b_int8_upscale_video`, 3 s de uma captura de VHS 640x480 → 960x720, correção de cor `lab`, blocos temporais automáticos):

| Modelo | Tempo | Pico de VRAM | Nitidez (variância do Laplaciano) |
|---|---|---|---|
| entrada (lanczos) | — | — | 65 |
| 3B INT8 | 329 s | 7,5 GB | **221** |
| 7B INT8 | 392 s | 10,8 GB | 119 |
| 7B *sharp* INT8 | 438 s | 10,9 GB | 109 |

Com fonte muito degradada (VHS), os 7B saíram mais conservadores que o 3B: preservam o borrado em vez de reconstruir. O 3B foi o melhor nesse caso, além de mais rápido. Os 7B podem render mais em fontes menos degradadas (não testado).

Segunda passada (o resultado do 3B passado de novo pelo 3B): 354 s mantendo 960x720 e 384 s subindo para 1440x1080. Fica mais nítido, mas o rosto piora: contornos duros, olhos escurecidos e sombras inventadas. Uma passada só é o limite.
