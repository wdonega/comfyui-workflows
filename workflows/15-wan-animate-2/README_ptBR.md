# Wan Animate 2 · anima um personagem com o movimento de um vídeo

[comfyui-workflows](../../README_ptBR.md) › **Wan Animate 2 · anima um personagem com o movimento de um vídeo**

O template oficial `video_wan_animate2_distilled` (versão destilada, 10 steps `lcm`, CFG 1) em INT8 convrot com os nós nativos `WanAnimate2ToVideo` e `WanAnimate2Cache`. Recebe uma imagem do personagem e um vídeo-guia; o personagem repete a pose, o movimento do corpo e as expressões do vídeo. Mantém o áudio do vídeo-guia.

| | |
|---|---|
| Status | ✅ testado |
| Família | Wan 2.2 (Animate 2) |
| Licença | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Download total | 24.91 GB |
| Teste | personagem de corpo inteiro + vídeo-guia de uma criança correndo, 480x848, 81 frames, 10 steps: o personagem corre com as mesmas pernas, braços e aproximação da câmera do guia; o fundo é o da imagem do personagem. Com uma referência só de busto, só as expressões e a cabeça foram transferidas |
| Tempo | **7min 02s** (RTX 5060 Ti 16 GB, 2026-10-23) |
| Pico de VRAM | 15345 MiB |

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
| `diffusion_models/` | `wan_animate_2_distill_int8_convrot.safetensors` | Wan Animate 2 destilado (INT8) | 16.65 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/diffusion_models/wan_animate_2_distill_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `text_encoders/` | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | text encoder UMT5-XXL (FP8) | 6.74 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | [página](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `clip_vision/` | `clip_vision_h.safetensors` | CLIP Vision H | 1.26 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/clip_vision/clip_vision_h.safetensors) | [página](https://huggingface.co/Comfy-Org/Wan-Animate-2) |
| `vae/` | `Wan2_1_VAE_bf16.safetensors` | VAE do Wan 2.1 | 0.25 GB | [download](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/e7181fe1896b7f2ce34120d1a3663413548240d7/vae/Wan2_1_VAE_bf16.safetensors) | [página](https://huggingface.co/Comfy-Org/Wan-Animate-2) |

<details><summary>SHA-256</summary>

```
d2e566ecac3f164cb1a6b63dc7d868d6678c9affa49fbceb3abe4f9458f89c8a  models/diffusion_models/wan_animate_2_distill_int8_convrot.safetensors
c3355d30191f1f066b26d93fba017ae9809dce6c627dda5f6a66eaa651204f68  models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
64a7ef761bfccbadbaa3da77366aac4185a6c58fa5de5f589b42a65bcc21f161  models/clip_vision/clip_vision_h.safetensors
1ab9a32cc2c740f6e39d80d367ce5dcc28db8c71b79b28670546b8973e9d75f9  models/vae/Wan2_1_VAE_bf16.safetensors
```

</details>

## Como usar

1. **LoadImage**: o personagem (`character.png`), **de corpo inteiro** se o vídeo-guia tiver movimento de corpo (com um busto, só cabeça e expressões são transferidas).
2. **LoadVideo**: o vídeo-guia (`driving.mp4`).
3. Dois prompts: a ação (ex.: `A man running down a rainy street`) e a aparência do personagem.
4. Resolução nos **ResizeImageMaskNode** do vídeo (480x854 no template) e `length` no **WanAnimate2ToVideo** (81 frames).

## Licença

Apache-2.0: uso pessoal e comercial livres, sem limite de receita nem de território; basta manter os avisos de licença ao redistribuir os pesos. As saídas são suas.

## Observações

- O plano avisava que o loader **GGUF** padrão ignora o vídeo-guia sem avisar; aqui foi usado o INT8 convrot com loader nativo e o movimento do guia apareceu no resultado.
- O template salva também um vídeo de comparação lado a lado (resultado + guia).
- O personagem fica no cenário da própria imagem; para inserir no vídeo-guia, seria o modo de substituição (não testado).
