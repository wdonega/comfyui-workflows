# Herrgott's H3 Infinite Continuation (v1.4)

[comfyui-workflows](../../README_ptBR.md) › **Herrgott's H3 Infinite Continuation (v1.4)**

Gera vídeos de qualquer duração clipe a clipe: o **Start** cria o clipe 1 (T2VA/I2VA/FL2VA) e salva o latente com metadados de *handover*; cada **Continue** carrega o anterior, protege os últimos 39 frames seguros como contexto (Masked AV nativo) e gera o próximo; o **Stitch** decodifica a cadeia salva e junta nos pontos seguros, com crossfade curto de vídeo e áudio.

| | |
|---|---|
| Status | ✅ testado |
| Família | MiniMax H3 |
| Licença | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Download total | 42.47 GB |
| Teste | 736x1280, 15 steps: Start 5 s (553 s) + Continue 5 s (732 s) + Stitch (115 s) = 8,7 s finais. O Auto Handover detectou o final forçado e passou o ponto seguro: emenda sem salto. Referência usada como primeiro/último frame, por isso o retrato no fim |
| Tempo | **23min 20s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15651 MiB |

## Arquivos desta pasta

| Arquivo | O que é |
|---|---|
| `01-start.json` | Clipe 1: arrastar na interface |
| `01-start.api.json` | Clipe 1 (API) |
| `02-continue.json` | Clipes 2, 3, …: aumente `clip_index` no Load/Save a cada clipe |
| `02-continue.api.json` | Continue (API) |
| `03-stitch.json` | Junta a cadeia salva em um vídeo final |
| `03-stitch.api.json` | Stitch (API) |
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
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |
| VideoHelperSuite | 1.7.9 | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |
| Herrgotts-H3-Infinite-Continuation-Suite | `4b1edd6` | https://github.com/HerrgottMargott/Herrgotts-H3-Infinite-Continuation-Suite |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | modelo FL2VA (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | text encoder Qwen3-VL 32B (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_fp16.safetensors` | VAE de vídeo fp16 | 5.21 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_fp16.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | VAE de áudio | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |

<details><summary>SHA-256</summary>

```
e889202c41dafb67b10d67b97f0d8541508036a6090af23425a5c2615d03c47a  models/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
7c1f131492e7eddacaac9069a61b81bdd39de5cc96561e677c5eab1cdce5e522  models/vae/minimax_h3_video_vae_fp16.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
```

</details>

## Como usar

1. **01-start**: primeiro e último frame são opcionais (o autor recomenda repetir o mesmo frame nas pontas como "reset" de qualidade); a referência Qwen vira `<Picture 2>`. Rode e ele salva `output/h3_continuous/clip_00001`.
2. **02-continue**: `clip_index` do Load = anterior, do Save = atual. `duration_mode` `Net New Content` faz a duração pedida ser só conteúdo novo.
3. Repita o Continue quantas vezes quiser.
4. **03-stitch**: `first_clip`/`last_clip` (0 = até o último) e gera o vídeo final.

## Licença

Uso pessoal e comercial liberados até US$ 20 mi/ano de receita (acima disso, autorização da MiniMax). **Proibido nos EUA, UE, Reino Unido e Coreia do Sul, inclusive exibir ou distribuir as saídas lá (cláusula V.4)**: não use os vídeos em projetos publicados globalmente. Conteúdo publicado deve ser identificado como gerado por IA; proibido personificar pessoas reais sem consentimento; produto comercial deve exibir "MiniMax H3". LoRAs de terceiros herdam essas regras.

## Observações

- Os exemplos do autor usam **SageAttention** (`PathchSageAttentionKJ`), que não estava instalado; aqui foi trocado pela atenção do comfy-kitchen + MiniMax LowVRAM Attention + Chunk FeedForward (KJNodes), e funcionou em 16 GB.
- Não use o mesmo retrato de estúdio como último frame se quiser que a cena termine no cenário: o clipe é obrigado a chegar nele (foi o que aconteceu no teste).
- O tempo da tabela soma os três passos (553 + 732 + 115 s).
