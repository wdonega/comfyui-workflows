# Flux 3 Klein (destilado)

[comfyui-workflows](../../README_ptBR.md) › **Flux 3 Klein (destilado)**

O template oficial `image_flux3_klein_distilled_t2i` em INT8, com o upsampler de prompt (Qwen3.5 9B W4A8) ligado como no original. Precisa do ComfyUI ≥ 0.42 (suporte ao Flux 3 Image). O editor de layout opcional do template foi removido da versão API.

| | |
|---|---|
| Status | ✅ testado |
| Família | Flux 3 |
| Licença | [FLUX Kommunity License](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |
| Download total | 17.75 GB |
| Teste | Prompt do teste (igual nos modelos de imagem da comparação): café-livraria com um gato tricolor e uma placa escrita "OPEN DAILY 8-20", seed 20261022, 1024x1024. |
| Tempo | **21s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15421 MiB |

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
| `diffusion_models/` | `flux3-image-klein-int8-convrot.safetensors` | Flux 3 Image Klein (INT8) | 5.83 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/diffusion_models/flux3-image-klein-int8-convrot.safetensors) | [página](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |
| `text_encoders/` | `qwen3vl_4b_int8_convrot.safetensors` | text encoder Qwen3-VL 4B (INT8) | 4.86 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/text_encoders/qwen3vl_4b_int8_convrot.safetensors) | [página](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |
| `text_encoders/` | `qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors` | upsampler de prompt Qwen3.5 9B (W4A8) | 6.72 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors) | [página](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |
| `vae/` | `flux2-vae.safetensors` | VAE do Flux 2 | 0.34 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/vae/flux2-vae.safetensors) | [página](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) |

<details><summary>SHA-256</summary>

```
847d8933548afd93df4af2cac2498e70891bf28d9dae06d695f536992e168fe2  models/diffusion_models/flux3-image-klein-int8-convrot.safetensors
32de113cbf8282b02cbff0794b637b9d6676da09314a1db5a30bcea9bf4ee01c  models/text_encoders/qwen3vl_4b_int8_convrot.safetensors
e5d85a7421d197bf5a12474511936ecabce19a833252f16e9310a983194a4458  models/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors
868fe7b343cc8f3a19dbcfcafbc3d5f888802be3f89bd81b65b3621a066ce8f3  models/vae/flux2-vae.safetensors
```

</details>

## Como usar

1. Prompt curto no **PrimitiveStringMultiline**; o upsampler transforma em uma descrição detalhada.
2. 16 steps, CFG 1, `euler`. Para desligar o upsampler, troque a chave do template (economiza tempo e VRAM).

## Licença

Uso não comercial grátis; uso comercial grátis para "Qualifying Users" (receita anual < US$ 5 mi) que mantenham filtros de conteúdo. A BFL não reivindica as saídas. Proibido usar saídas para treinar modelo concorrente. Repositório gated: aceite os termos no Hugging Face e use HF_TOKEN.

## Observações

Comparação na mesma seed/prompt (RTX 5060 Ti): Qwen 2.1 24 s · Qwen 2.1 Turbo 10 s · Krea 2 Turbo 23 s · Flux 3 Klein 21 s · MOSS-Image 35 s. Todos acertaram o texto da placa.
