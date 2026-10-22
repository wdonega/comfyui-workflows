# H3 Realism People

O Ref2VA + TaoMate base com o LoRA **Realism People** da fal encadeado depois do TaoMate. Deixa pessoas com aparência mais natural e cinematográfica (menos brilho de IA). Gatilho no prompt: `r34l1sm`.

| | |
|---|---|
| Item do plano | #59 |
| Status | ✅ testado |
| Família | MiniMax H3 |
| Licença | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Download total | 42.69 GB |
| Teste | 736x1280, 122 frames (5 s), 3 steps; LoRA aplicado sem chaves ignoradas (208/208) |
| Tempo | **2min 14s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15577 MiB |

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
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |
| VideoHelperSuite | 1.7.9 | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | modelo Ref2VA (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | text encoder Qwen3-VL 32B (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_int8_convrot.safetensors` | VAE de vídeo | 2.81 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | VAE de áudio | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors` | LoRA TaoMate 3 steps | 2.48 GB | [download](https://huggingface.co/drbaph/MiniMax-H3-Turbo-Lora-ComfyUI/resolve/633e6c48cd05f7800e2cb2c007b5c9023b92c576/experimental/minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors) | [página](https://huggingface.co/TaoLiveAIGC/TaoMate-H3-FL2VA) |
| `loras/` | `h3-realism-people-t2v-i2v-r2v.safetensors` | LoRA Realism People (força 1.0) | 0.13 GB | [download](https://huggingface.co/fal/MiniMax-H3-Realism-People-LoRA/resolve/039cc8579d7aa357a882d7f4111b25da4f72dccc/h3-realism-people-t2v-i2v-r2v.safetensors) | [página](https://huggingface.co/fal/MiniMax-H3-Realism-People-LoRA) |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
52a2c8c73583c86e4f41cdcce3a6ad0ea562987bc0bf3d60a0cef5f5c8e60c0e  models/vae/minimax_h3_video_vae_int8_convrot.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
6b119983683b265ad65224a9a643eea1714efe5b8bcb93799999635ccc455c73  models/loras/minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors
acc529601d2da117fb81179e76c56e488a3beab1171659d305f04fa3655b787e  models/loras/h3-realism-people-t2v-i2v-r2v.safetensors
```

</details>

## Como usar

Igual ao workflow base, com o nó **Realism People LoRA (#59)** depois do TaoMate. Comece o prompt com `r34l1sm,`. Funciona em T2V, I2V e R2V segundo o autor.

## Licença

Uso pessoal e comercial liberados até US$ 20 mi/ano de receita (acima disso, autorização da MiniMax). **Proibido nos EUA, UE, Reino Unido e Coreia do Sul, inclusive exibir ou distribuir as saídas lá (cláusula V.4)**: não use os vídeos em projetos publicados globalmente. Conteúdo publicado deve ser identificado como gerado por IA; proibido personificar pessoas reais sem consentimento; produto comercial deve exibir "MiniMax H3". LoRAs de terceiros herdam essas regras.

## Observações

- No teste curto (5 s) o resultado ficou mais natural e menos saturado que o base, sem artefatos.
