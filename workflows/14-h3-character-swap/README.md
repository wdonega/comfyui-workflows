# H3 Character Swap (Relay 2.0)

Workflow oficial do autor (akatz-ai) com o **H3 Relay 2.0**: o SAM 3.1 mascara a pessoa descrita, e o Ref2VA com o LoRA de Character Swap v1.5 + Turbo FL2V 8 steps troca a identidade pela imagem de referência. Preserva movimento, câmera, cenário e a trilha de áudio original. Vídeos longos são feitos em janelas.

| | |
|---|---|
| Item do plano | #14 |
| Status | ✅ testado |
| Família | MiniMax H3 |
| Licença | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Download total | 46.33 GB |
| Teste | fonte 4 s (96 frames, 736x1280, 24 fps), subject `boy`, receita do autor (8 steps, er_sde, CFG 1, LoRAs 1.0): identidade trocada, pose/cena/tempo preservados; roupa não veio da referência |
| Tempo | **14min 28s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | não medido |

## Arquivos desta pasta

| Arquivo | O que é |
|---|---|
| `workflow.json` | Workflow para arrastar na interface do ComfyUI |
| `workflow.api.json` | Mesmo workflow no formato da API (o que foi testado) |
| `install.sh` | Instala custom nodes e baixa os modelos para as pastas certas |
| `components.json` | Fonte dos dados deste README e do install.sh |

## Instalação

```bash
# na máquina com o ComfyUI (o script confere se a pasta é a raiz do ComfyUI)
bash install.sh /caminho/do/ComfyUI

# ComfyUI em Docker (container "comfyui")
docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh
```

Arquivos que já existem com o tamanho certo são pulados. Downloads novos têm o SHA-256 conferido (`VERIFY_EXISTING=1` confere também os que já existiam).

## Custom nodes

| Nó | Versão testada | Página |
|---|---|---|
| H3 Relay | `e2a7665` | https://github.com/akatz-ai/h3-relay |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | modelo Ref2VA (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | text encoder Qwen3-VL 32B (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_fp16.safetensors` | VAE de vídeo fp16 (receita do autor) | 5.21 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_fp16.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | VAE de áudio | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_fl2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors` | LoRA Turbo FL2V 8 steps (obrigatório) | 1.96 GB | [download](https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/30f485ed874aa44c8183348ad361c5eabad318da/minimax_h3_fl2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors) | [página](https://huggingface.co/lightx2v/Minimax-h3-Turbo) |
| `loras/` | `h3_character_swap_v1.5.safetensors` | LoRA Character Swap v1.5 | 0.16 GB | [download](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/resolve/96ea3407b230b6f7df71c58c70e31df96bd7e533/h3_character_swap_v1.5.safetensors) | [página](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA) |
| `checkpoints/` | `sam3.1_multiplex_fp16.safetensors` | SAM 3.1 (máscara da pessoa) | 1.75 GB | [download](https://huggingface.co/Comfy-Org/sam3.1/resolve/7bb8374780a725b4353ed31f3a9395c9742b5621/checkpoints/sam3.1_multiplex_fp16.safetensors) | [página](https://huggingface.co/Comfy-Org/sam3.1) |
| `loras/` | `h3-v2-challenge-eval-20261013/v2-1000.safetensors` | link → `../h3_character_swap_v1.5.safetensors` (nome que o workflow do autor usa) | — | — | — |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
7c1f131492e7eddacaac9069a61b81bdd39de5cc96561e677c5eab1cdce5e522  models/vae/minimax_h3_video_vae_fp16.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
08cfe946033af7d27719b964b6e0a0e50c32138daabbd6ce4137e23df6bf9980  models/loras/minimax_h3_fl2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors
8f2c3c3eba161df8d0c6099598b4730f641f5ce01e04cd16d2427cff8a35218f  models/loras/h3_character_swap_v1.5.safetensors
9ba99c92703c2e8b4f47de2d34a539bb8e18923049e238b780d70dbe6368eb03  models/checkpoints/sam3.1_multiplex_fp16.safetensors
```

</details>

## Como usar

1. Carregue `workflow.json`. No **LoadVideo**, um plano contínuo (`source.mp4`); no **LoadImage**, a referência do personagem (`reference.png`).
2. Em **Prepare Source**: `duration_seconds` 0 = vídeo inteiro (normaliza para 24 fps e múltiplos de 32 px).
3. No texto do SAM (`subject`), descreva a pessoa a trocar (ex.: `the man on the left`); confira a máscara no preview.
4. Mantenha 8 steps, `er_sde`, scheduler `normal`, CFG 1 e os dois LoRAs em 1.0.
5. Uma pessoa por vez: para trocar duas, rode de novo usando a saída como fonte.

## Licença

Uso pessoal e comercial liberados até US$ 20 mi/ano de receita (acima disso, autorização da MiniMax). **Proibido nos EUA, UE, Reino Unido e Coreia do Sul, inclusive exibir ou distribuir as saídas lá (cláusula V.4)**: não use os vídeos em projetos publicados globalmente. Conteúdo publicado deve ser identificado como gerado por IA; proibido personificar pessoas reais sem consentimento; produto comercial deve exibir "MiniMax H3". LoRAs de terceiros herdam essas regras.

## Observações

- Lento em 16 GB: ~76 s por step (8 steps por janela de até 124 frames) porque a receita foi feita para 24 GB e faz offload. 4 s de vídeo levaram ~14,5 min.
- **Não empilhe com o TaoMate** (receita do autor usa só o Turbo 8 steps).
- Licença: personificar pessoas reais sem consentimento é proibido pela licença do H3.
- **Créditos:** `workflow.json` e `workflow.api.json` são os exemplos oficiais da Akatz Labs ([akatz-ai/MiniMax-H3-Character-Swap-LoRA](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/tree/main/examples)), redistribuídos sem alterações; partes derivadas dos templates do ComfyUI são MIT (Comfy Org). LoRA e H3 Relay pertencem aos seus autores.
