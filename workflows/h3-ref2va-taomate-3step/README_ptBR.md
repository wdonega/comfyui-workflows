[comfyui-workflows](../../README_ptBR.md) › **H3 Ref2VA · TaoMate 3 steps** · Idioma: [English](README.md) · **Português**

# H3 Ref2VA · TaoMate 3 steps

Workflow base de referência-para-vídeo (Ref2VA) do MiniMax H3 com o LoRA TaoMate de 3 steps: gera vídeo com áudio sincronizado a partir de um prompt estruturado e uma imagem de referência. Base dos itens #59 e da regressão do setup.

| | |
|---|---|
| Item do plano | base |
| Status | ✅ testado |
| Família | MiniMax H3 |
| Licença | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Download total | 42.55 GB |
| Teste | 736x1280, 362 frames (15 s), 3 steps, mesma seed de uma geração anterior: mesma cena e qualidade |
| Tempo | **8min 44s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15559 MiB |

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
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |
| VideoHelperSuite | 1.7.9 | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | modelo Ref2VA (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | text encoder Qwen3-VL 32B (NVFP4, Blackwell) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_int8_convrot.safetensors` | VAE de vídeo | 2.81 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | VAE de áudio | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors` | LoRA TaoMate 3 steps | 2.48 GB | [download](https://huggingface.co/drbaph/MiniMax-H3-Turbo-Lora-ComfyUI/resolve/633e6c48cd05f7800e2cb2c007b5c9023b92c576/experimental/minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors) | [página](https://huggingface.co/TaoLiveAIGC/TaoMate-H3-FL2VA) |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
52a2c8c73583c86e4f41cdcce3a6ad0ea562987bc0bf3d60a0cef5f5c8e60c0e  models/vae/minimax_h3_video_vae_int8_convrot.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
6b119983683b265ad65224a9a643eea1714efe5b8bcb93799999635ccc455c73  models/loras/minimax_h3_taomate_fl2va_3step_ema_comfyui.safetensors
```

</details>

## Como usar

1. Carregue `workflow.json` e escolha a imagem de referência no **LoadImage** (`reference.png`).
2. Escreva o prompt no formato estruturado do H3 (`subject_definitions`, `detailed_description`, `audio`), citando `<Picture 1>`.
3. `length` em frames a 24 fps (362 ≈ 15 s). Sigmas manuais `1.0, 0.961165, 0.853333, 0.0` + `res_multistep` são a receita do TaoMate.
4. Em 16 GB, mantenha **MiniMax Chunk FeedForward** e **MiniMax LowVRAM Attention** (KJNodes) ligados.

## Licença

Uso pessoal e comercial liberados até US$ 20 mi/ano de receita (acima disso, autorização da MiniMax). **Proibido nos EUA, UE, Reino Unido e Coreia do Sul, inclusive exibir ou distribuir as saídas lá (cláusula V.4)**: não use os vídeos em projetos publicados globalmente. Conteúdo publicado deve ser identificado como gerado por IA; proibido personificar pessoas reais sem consentimento; produto comercial deve exibir "MiniMax H3". LoRAs de terceiros herdam essas regras.

## Observações

- O arquivo do TaoMate é a conversão para ComfyUI publicada por drbaph (SHA-256 conferido com o arquivo em uso); o LoRA original é da TaoLiveAIGC.
- Resultados com a mesma seed variam um pouco entre execuções (não-determinismo da GPU).
