# MOSS-Image (SFT)

[comfyui-workflows](../../README_ptBR.md) › **MOSS-Image (SFT)**

O template oficial `image_moss_image_t2i` com o MOSS-Image SFT em INT8 (25 steps, `er_sde`, CFG 2,5) e o Qwen3.5 9B W4A8 como text encoder e expansor de prompt. Precisa do ComfyUI ≥ 0.42. **Apache-2.0**: a melhor opção da lista para assets de projetos publicados.

| | |
|---|---|
| Status | ✅ testado |
| Família | MOSS-Image |
| Licença | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Download total | 13.01 GB |
| Teste | Prompt do teste (igual nos modelos de imagem da comparação): café-livraria com um gato tricolor e uma placa escrita "OPEN DAILY 8-20", seed 20261022, 1024x1024. |
| Tempo | **35s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 13045 MiB |

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
| `diffusion_models/` | `moss_image_sft_int8_convrot.safetensors` | MOSS-Image SFT (INT8) | 5.41 GB | [download](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/24147db865fcdc207270f844777587223fed8d6e/diffusion_models/moss_image_sft_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MOSS-Image) |
| `text_encoders/` | `qwen3.5_9b_w4a8_gptq.safetensors` | text encoder Qwen3.5 9B (W4A8) | 7.34 GB | [download](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/24147db865fcdc207270f844777587223fed8d6e/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) | [página](https://huggingface.co/Comfy-Org/MOSS-Image) |
| `vae/` | `flux2-vae_small.safetensors` | VAE do Flux 2 (small) | 0.25 GB | [download](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/24147db865fcdc207270f844777587223fed8d6e/vae/flux2-vae_small.safetensors) | [página](https://huggingface.co/Comfy-Org/MOSS-Image) |

<details><summary>SHA-256</summary>

```
b4d1475bc7eeffd7b809e82ea13a1fba1fb85c4e18365af3813722faa5c0fe4f  models/diffusion_models/moss_image_sft_int8_convrot.safetensors
4cc6a1543ad2061806da46f35f90cadb4801dcba246c44782cf42ec0feb6407c  models/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors
d8d52ba036475f5fb07c8b435e176d3d97ebfa82f0d1a1c317f9cc1e25bd013b  models/vae/flux2-vae_small.safetensors
```

</details>

## Como usar

Prompt no **PrimitiveStringMultiline**; o template expande o prompt (pensado para pedidos curtos, inclusive em chinês). Existe uma versão rápida de 8 steps da comunidade (`lodestones/MOSS-Image-SFT-8-steps-dmd`), não testada aqui.

## Licença

Apache-2.0: uso pessoal e comercial livres, sem limite de receita nem de território; basta manter os avisos de licença ao redistribuir os pesos. As saídas são suas.

## Observações

Comparação na mesma seed/prompt (RTX 5060 Ti): Qwen 2.1 24 s · Qwen 2.1 Turbo 10 s · Krea 2 Turbo 23 s · Flux 3 Klein 21 s · MOSS-Image 35 s. Todos acertaram o texto da placa.
