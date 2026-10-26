# SeedVR2 v2 · upscale de vídeo (GGUF)

[comfyui-workflows](../../README_ptBR.md) › **SeedVR2 v2 · upscale de vídeo (GGUF)**

Segunda versão do [SeedVR2](../42-seedvr2-upscale/README_ptBR.md): em vez do suporte nativo do ComfyUI (INT8), usa o custom node [ComfyUI-SeedVR2_VideoUpscaler](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler) v2.5 do numz com o modelo 3B em GGUF Q8_0. Mesmo modelo e mesma qualidade a olho; no mesmo trecho de VHS levou 134 s contra ~410 s do nativo. Processa o vídeo em lotes de 21 frames (`batch_size`, sempre 4n+1) e define a altura final em `resolution` (lado menor).

| | |
|---|---|
| Status | ✅ testado |
| Família | SeedVR2 |
| Licença | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Download total | 4.16 GB |
| Teste | 3 s de VHS limpo com ffmpeg (632x468, 90 frames) → 972x720: 90 frames e áudio preservados, sem saltos entre lotes |
| Tempo | **2min 14s** (RTX 5060 Ti 16 GB, 2026-10-26) |
| Pico de VRAM | 7887 MiB |

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
| ComfyUI-SeedVR2_VideoUpscaler (v2.5.23) | `5a4bf42` | https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `SEEDVR2/` | `seedvr2_ema_3b-Q8_0.gguf` | SeedVR2 3B (GGUF Q8_0) | 3.66 GB | [download](https://huggingface.co/cmeka/SeedVR2-GGUF/resolve/de058a1261f2fc4bb41f39e9ddf313877e4ebf0d/seedvr2_ema_3b-Q8_0.gguf) | [página](https://huggingface.co/cmeka/SeedVR2-GGUF) |
| `SEEDVR2/` | `ema_vae_fp16.safetensors` | VAE do SeedVR2 | 0.50 GB | [download](https://huggingface.co/numz/SeedVR2_comfyUI/resolve/09ced71023636e9bc8cdf9cdecfb2625d1e691e8/ema_vae_fp16.safetensors) | [página](https://huggingface.co/numz/SeedVR2_comfyUI) |

<details><summary>SHA-256</summary>

```
be0d60083a2051a265eb4b77f28edf494e6db67ffc250216f32b72292e5cbd96  models/SEEDVR2/seedvr2_ema_3b-Q8_0.gguf
20678548f420d98d26f11442d3528f8b8c94e57ee046ef93dbb7633da8612ca1  models/SEEDVR2/ema_vae_fp16.safetensors
```

</details>

## Como usar

1. Depois do `install.sh`, instale a dependência do custom node no Python do ComfyUI: `pip install rotary-embedding-torch==0.9.1` (as outras do `requirements.txt` já vêm com o ComfyUI) e reinicie o ComfyUI.
2. Vídeo no **LoadVideo** (`input.mp4`).
3. Altura final em `resolution` do **SeedVR2VideoUpscaler** (720; é o lado menor). `batch_size` 21: lotes maiores pedem mais VRAM (93 frames estouraram 16 GB sem `blocks_to_swap`).
4. Para vídeos longos, divida em trechos (o [caso de uso de VHS v2](../../usecases/vhs-upscale-v2/README_ptBR.md) faz isso sozinho): todos os frames do vídeo ficam na RAM.

## Licença

Apache-2.0 (modelos GGUF, VAE e custom node): uso pessoal e comercial livres, sem limite de receita nem de território; basta manter os avisos de licença ao redistribuir. As saídas são suas.

## Observações

### Comparação (2026-10-26, mesmos 3 s de VHS, 720p, correção de cor `lab`)

| Versão | Tempo | Pico de VRAM |
|---|---|---|
| [v1](../42-seedvr2-upscale/README_ptBR.md) nativo 3B INT8 | 411 s | 7,0 GB |
| v2 3B Q8_0, `batch_size` 21 | 150 s | 8,1 GB |
| v2 3B Q4_K_M, `batch_size` 21 | 148 s | 8,0 GB |
| v2 3B Q8_0, `batch_size` 93 | sem VRAM (OOM) | — |
| v2 3B Q8_0, `batch_size` 93, `blocks_to_swap` 16 | 142 s | 15,6 GB |

Fonte crua (sem limpeza), para medir só o upscale. A olho, as versões ficaram iguais (o Q4 também); lotes maiores não trouxeram ganho visível e nenhuma versão teve salto entre lotes. O `torch.compile` (nó **SeedVR2TorchCompileSettings**) não foi usado nem testado.

### Modelo 7B (opcional)

[`seedvr2_ema_7b-Q8_0.gguf`](https://huggingface.co/cmeka/SeedVR2-GGUF/resolve/de058a1261f2fc4bb41f39e9ddf313877e4ebf0d/seedvr2_ema_7b-Q8_0.gguf) (8,84 GB, Apache-2.0), em `models/SEEDVR2/`. Não está no `install.sh`; troque o `model` do **SeedVR2LoadDiTModel**. Teste (mesmos 3 s de VHS limpo, 720p): 160 s e 12,1 GB de pico de VRAM (3B: 134 s, 7,9 GB), mas nitidez 108 contra 174 do 3B: com fonte tão degradada, o 7B preserva o borrado em vez de reconstruir, como na [v1](../42-seedvr2-upscale/README_ptBR.md). Em 1080p: 347 s, 15,4 GB.
