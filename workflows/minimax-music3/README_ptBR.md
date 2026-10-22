# MiniMax Music 3 · música com letra

[comfyui-workflows](../../README_ptBR.md) › **MiniMax Music 3 · música com letra**

O template oficial `audio_minimax_music_3` com o exemplo original (lo-fi hip-hop, 78 BPM, com letra). Gera a faixa inteira, com voz, a partir de uma descrição de estilo e da letra com marcações de seção.

| | |
|---|---|
| Status | ✅ testado |
| Família | MiniMax Music 3 |
| Licença | [MiniMax-Music3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-Music3/blob/main/LICENSE) |
| Download total | 14.33 GB |
| Teste | exemplo do template: 60 s de MP3 estéreo 44,1 kHz, volume consistente (−16 a −20 dB) |
| Tempo | **2min 26s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 14859 MiB |

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
| `diffusion_models/` | `minimax_music3_dit_fp16.safetensors` | Music 3 DiT (fp16) | 4.91 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/9e364ccd290a401561091fb441ed19cd7de92550/diffusion_models/minimax_music3_dit_fp16.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-Music-3) |
| `text_encoders/` | `minimax_music3_text_encoder_pruned_int8_convrot.safetensors` | text encoder (INT8) | 9.20 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/9e364ccd290a401561091fb441ed19cd7de92550/text_encoders/minimax_music3_text_encoder_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-Music-3) |
| `vae/` | `minimax_music3_dav.safetensors` | VAE de áudio (DAV) | 0.22 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/9e364ccd290a401561091fb441ed19cd7de92550/vae/minimax_music3_dav.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-Music-3) |

<details><summary>SHA-256</summary>

```
45494a2b6b69af115902ff28eaf54118d19067aa54da01000f3e3efce7ba0e34  models/diffusion_models/minimax_music3_dit_fp16.safetensors
010b7416d2336a08c711bc22ee65849c9623069ddb7d89bec011a75699e52014  models/text_encoders/minimax_music3_text_encoder_pruned_int8_convrot.safetensors
2a32155b769be01445fcc2a8663b910fc9e1751e18dc1c3ec528064512d9ef0c  models/vae/minimax_music3_dav.safetensors
```

</details>

## Como usar

No **MiniMaxMusic3TextEncode**: a descrição de estilo (gênero, BPM, tom, clima) e a letra com seções (`[Intro]`, `[Verse]`, `[Chorus]`…). A duração sai do próprio texto; 30 steps, CFG 1,7.

## Licença

Uso pessoal e comercial; **sem restrição de território**. Produto comercial deve exibir "MiniMax-Music3" e há teto de receita para uso sem autorização. A MiniMax não reivindica as músicas geradas (são suas). Serviço que gera músicas para terceiros precisa de salvaguardas contra mau uso.

## Observações

- A licença original é a MiniMax-Music3 Community (o card da Comfy-Org diz Apache-2.0, mas vale o LICENSE do repositório da MiniMax).
