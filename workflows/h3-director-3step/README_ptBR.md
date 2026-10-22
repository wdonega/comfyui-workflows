# H3 Director · TaoMate 3 steps (timeline)

[comfyui-workflows](../../README_ptBR.md) › **H3 Director · TaoMate 3 steps (timeline)**

Workflow com o **MiniMax H3 Director** (custom node de timeline): um prompt global, até 5 segmentos com prompt próprio, trilhas de áudio e movimento e paisagem sonora. Usa FL2VA e Ref2VA em INT8 com o LoRA TaoMate de 3 steps, 1376x768, 15 s.

| | |
|---|---|
| Status | ✅ testado |
| Família | MiniMax H3 |
| Licença | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Download total | 63.53 GB |
| Teste | timeline de 5 segmentos de 72 frames (362 frames, 1376x768): os 5 segmentos na ordem, com áudio; resultado praticamente idêntico a uma geração anterior na mesma seed (antes do update do ComfyUI). Testado com outra história; o arquivo traz uma história neutra de exemplo |
| Tempo | **10min 10s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15545 MiB |

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

## Custom nodes

| Nó | Versão testada | Página |
|---|---|---|
| ComfyUI-MiniMaxH3-Director | `8486323` | https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director |
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |
| VideoHelperSuite | 1.7.9 | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | modelo FL2VA (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | modelo Ref2VA (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | text encoder Qwen3-VL 32B (NVFP4, Blackwell) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_int8_convrot.safetensors` | VAE de vídeo | 2.81 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | VAE de áudio | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors` | LoRA TaoMate 3 steps | 2.48 GB | [download](https://huggingface.co/drbaph/MiniMax-H3-Turbo-Lora-ComfyUI/resolve/633e6c48cd05f7800e2cb2c007b5c9023b92c576/experimental/minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors) | [página](https://huggingface.co/TaoLiveAIGC/TaoMate-H3-FL2VA) |

<details><summary>SHA-256</summary>

```
e889202c41dafb67b10d67b97f0d8541508036a6090af23425a5c2615d03c47a  models/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
52a2c8c73583c86e4f41cdcce3a6ad0ea562987bc0bf3d60a0cef5f5c8e60c0e  models/vae/minimax_h3_video_vae_int8_convrot.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
6b119983683b265ad65224a9a643eea1714efe5b8bcb93799999635ccc455c73  models/loras/minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors
```

</details>

## Como usar

1. Abra o **Director** (painel de timeline): prompt global, segmentos com o texto de cada trecho, paisagem sonora.
2. Resolução e duração no próprio nó (1376x768, 15 s / 360 frames no exemplo).
3. Em 16 GB, mantenha **MiniMax Chunk FeedForward** e **MiniMax LowVRAM Attention** ligados.

## Licença

Uso pessoal e comercial liberados até US$ 20 mi/ano de receita (acima disso, autorização da MiniMax). **Proibido nos EUA, UE, Reino Unido e Coreia do Sul, inclusive exibir ou distribuir as saídas lá (cláusula V.4)**: não use os vídeos em projetos publicados globalmente. Conteúdo publicado deve ser identificado como gerado por IA; proibido personificar pessoas reais sem consentimento; produto comercial deve exibir "MiniMax H3". LoRAs de terceiros herdam essas regras.

## Observações

- Neste workflow uma textura de tela de arame apareceu em todos os quadros, tanto na geração original quanto no teste (mesma seed); trocar a seed ou pedir "no fence, no mesh overlay" no prompt global resolve.
