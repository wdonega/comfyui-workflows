# Krea 2 Turbo

[comfyui-workflows](../../README_ptBR.md) › **Krea 2 Turbo**

O template oficial `image_krea2_turbo_t2i_int8` (8 steps, CFG 1). O próprio text encoder (Qwen3-VL 4B) expande o prompt antes de gerar. Usa o Qwen3-VL 4B em INT8 (o mesmo arquivo do Flux 3 Klein) no lugar do FP8 do template.

| | |
|---|---|
| Status | ✅ testado |
| Família | Krea 2 |
| Licença | [Krea 2 Community License](https://huggingface.co/krea/Krea-2-Turbo) |
| Download total | 18.61 GB |
| Teste | Prompt do teste (igual nos modelos de imagem da comparação): café-livraria com um gato tricolor e uma placa escrita "OPEN DAILY 8-20", seed 20261022, 1024x1024. |
| Tempo | **23s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15477 MiB |

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
| `diffusion_models/` | `krea2_turbo_int8_convrot.safetensors` | Krea 2 Turbo (INT8) | 13.49 GB | [download](https://huggingface.co/Comfy-Org/Krea-2/resolve/1171f4dc7e325bf3734586942e737872506c73e1/diffusion_models/krea2_turbo_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/Krea-2) |
| `text_encoders/` | `qwen3vl_4b_int8_convrot.safetensors` | text encoder Qwen3-VL 4B (INT8; repositório gated da BFL, mesmo arquivo do Krea-2) | 4.86 GB | [download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/feef60b0aaf63a4773ace96636ebbcf43b881312/text_encoders/qwen3vl_4b_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/Krea-2) |
| `vae/` | `qwen_image_vae.safetensors` | VAE do Qwen-Image | 0.25 GB | [download](https://huggingface.co/Comfy-Org/Krea-2/resolve/1171f4dc7e325bf3734586942e737872506c73e1/vae/qwen_image_vae.safetensors) | [página](https://huggingface.co/Comfy-Org/Krea-2) |

<details><summary>SHA-256</summary>

```
8e4eeda70dd5037ab1ba2bef6b417f9f901e26093117cf397f741fc1fdaaf3f1  models/diffusion_models/krea2_turbo_int8_convrot.safetensors
32de113cbf8282b02cbff0794b637b9d6676da09314a1db5a30bcea9bf4ee01c  models/text_encoders/qwen3vl_4b_int8_convrot.safetensors
a70580f0213e67967ee9c95f05bb400e8fb08307e017a924bf3441223e023d1f  models/vae/qwen_image_vae.safetensors
```

</details>

## Como usar

1. Prompt no **PrimitiveStringMultiline** do usuário; a chave de expansão de prompt vem ligada.
2. Os 9 LoRAs de estilo oficiais (`Comfy-Org/Krea-2/loras`: aquarela, anime retrô, desenho infantil, tarô…) entram num **LoraLoaderModelOnly** depois do modelo; o template tinha um, desligado, que foi removido.

## Licença

Uso pessoal e comercial grátis para quem fatura menos de US$ 1 mi/ano (empresa e afiliadas); acima disso, Enterprise License. Deploy acessível a terceiros exige filtro de conteúdo e aviso de que a imagem é gerada por IA. As saídas são suas.

## Observações

Comparação na mesma seed/prompt (RTX 5060 Ti): Qwen 2.1 24 s · Qwen 2.1 Turbo 10 s · Krea 2 Turbo 23 s · Flux 3 Klein 21 s · MOSS-Image 35 s. Todos acertaram o texto da placa.
