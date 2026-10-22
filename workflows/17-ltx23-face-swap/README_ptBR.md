# LTX 2.3 · Face Swap (head swap)

[comfyui-workflows](../../README_ptBR.md) › **LTX 2.3 · Face Swap (head swap)**

Workflow de head swap com o LTX 2.3 destilado e o LoRA **BFS head swap v3** do @Alissonerdx. O `ReservedRegionFrameComposer` (BFSNodes) monta cada frame com o rosto de referência numa faixa reservada ao lado do vídeo; o LTX gera o vídeo com a cabeça trocada e o áudio original é mantido. Também salva um vídeo de comparação lado a lado.

| | |
|---|---|
| Status | ✅ testado |
| Família | LTX 2.3 |
| Licença | [LTX-2 Community License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE) |
| Download total | 44.71 GB |
| Teste | fonte 4 s (97 frames, 736x1280, 24 fps) + 1 imagem de rosto, 8 steps (euler_ancestral_cfg_pp + bong_tangent): cabeça trocada, pose/câmera/cenário/roupa preservados; elementos do fundo que não estavam no prompt (monstro, fumaça) sumiram |
| Tempo | **8min 42s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15821 MiB |

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
| ComfyUI-BFSNodes | `64be9ce` | https://github.com/alisson-anjos/ComfyUI-BFSNodes |
| RES4LYF | `56e4475` | https://github.com/ClownsharkBatwing/RES4LYF |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors` | LTX 2.3 22B destilado, só transformer (FP8 com escala de ativação) | 25.02 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_video_vae_bf16.safetensors` | VAE de vídeo | 1.45 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_video_vae_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `vae/` | `LTX23_audio_vae_bf16.safetensors` | VAE de áudio | 0.36 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/vae/LTX23_audio_vae_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `text_encoders/` | `gemma_3_12B_it_fp8_scaled.safetensors` | text encoder Gemma 3 12B (FP8) | 13.21 GB | [download](https://huggingface.co/Comfy-Org/ltx-2/resolve/ccde4ba417d7900669fd56dd292a883cee11ff37/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) | [página](https://huggingface.co/Comfy-Org/ltx-2) |
| `text_encoders/` | `ltx-2.3_text_projection_bf16.safetensors` | projeção de texto do LTX 2.3 | 2.31 GB | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/6d980fde0d330f2fed6ff8dfdfddb06d88a004e5/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | [página](https://huggingface.co/Kijai/LTX2.3_comfy) |
| `latent_upscale_models/` | `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | upscaler espacial x2 (2º estágio) | 1.00 GB | [download](https://huggingface.co/Lightricks/LTX-2.3/resolve/c1521179de480464f366a98a9d9b2acc4cc097b9/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) | [página](https://huggingface.co/Lightricks/LTX-2.3) |
| `loras/` | `ltx23-head_swap_v3_rank_adaptive_fro_098.safetensors` | LoRA BFS head swap v3 (renomeado como o workflow espera) | 1.36 GB | [download](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap-Video/resolve/d0adb5394c6a1b05f2245ec33cb91051a8000853/ltx-2.3/head_swap_v3_rank_adaptive_fro_098.safetensors) | [página](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap-Video) |

<details><summary>SHA-256</summary>

```
7327111e298066af8032f573d8db187986229ed2d4c926818ebf02041cfac8cf  models/diffusion_models/ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3.safetensors
01ea62d09bc139f95c5dee7b5c062ad6a3e6cd8be910a1983ac02e7eb5b8ee3b  models/vae/LTX23_video_vae_bf16.safetensors
5bc10fa4adecf99dda132d916e23048cbd56797702c5fa50eb5d2079048a38c3  models/vae/LTX23_audio_vae_bf16.safetensors
60216ce97c01c3a8753c2dfd0a89fc76e16fbe446d1a32ef8f1b528ac8bae466  models/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors
911d59bb4cb7708179c9a0045ea0fe41212ecfb77aed3a02702b7c0a8274911f  models/text_encoders/ltx-2.3_text_projection_bf16.safetensors
5f416311fa8172b65af67530758964708d29a317b830d689a51143b7f91913ed  models/latent_upscale_models/ltx-2.3-spatial-upscaler-x2-1.1.safetensors
78083ede0004c500ac0ae7b8fee43d28a1c3b503bac4a21edfeba7c60da8460d  models/loras/ltx23-head_swap_v3_rank_adaptive_fro_098.safetensors
```

</details>

## Como usar

1. **VHS LoadVideo**: o vídeo-fonte (`source.mp4`); a duração em segundos fica no **PrimitiveFloat** (5 no original) e o fps no outro (24).
2. **LoadImage**: o rosto/cabeça a colocar (`face.png`), de frente e bem iluminado.
3. **Prompt**: descreva a pessoa que deve aparecer **e o resto da cena** (fundo, objetos, luz). O que não estiver no prompt pode sumir.
4. Mantenha 8 steps, sampler `euler_ancestral_cfg_pp` e scheduler `bong_tangent` (RES4LYF); LoRA de head swap em 1.0.

## Licença

Uso pessoal e comercial grátis para pessoas e empresas com receita anual abaixo de US$ 10 mi; acima disso, licença comercial paga da Lightricks. **Sem restrição de território.** A Lightricks não reivindica as saídas (são suas). Não pode usar saídas para treinar modelos concorrentes. O text encoder Gemma 3 segue os Gemma Terms of Use do Google (política de uso proibido; saídas livres).

## Observações

- **Créditos:** workflow original de Rob no [comfy.org](https://comfy.org/workflows/download/bed989744195.json?filename=bed989744195), LoRA de [@Alissonerdx](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap-Video). Esta pasta tem a versão testada, convertida para API e reorganizada automaticamente (o layout original está no link).
- **BFSNodes e RES4LYF:** o RES4LYF precisa de `PyWavelets` (`pip install --no-deps PyWavelets` no Python do ComfyUI). As versões recentes do BFSNodes aparecem como *Flagged* no registro do ComfyUI; o código do commit testado foi revisado (`subprocess` só para ffmpeg, downloads só de OpenCV Zoo e Comfy-Org, patch do Wan inativo quando o core já suporta Bernini).
- O mesmo autor publica um LoRA de head swap para o **MiniMax H3** (`h3/minimax_h3_head_swap_v1.0_r32.safetensors`).
- Mais rápido que o Character Swap do H3 (#14: 868 s para 4 s) e mantém a roupa original; o #14 troca o personagem inteiro.
- Licença: trocar o rosto de pessoas reais sem consentimento pode violar direito de imagem; use com pessoas que autorizaram ou rostos fictícios.
