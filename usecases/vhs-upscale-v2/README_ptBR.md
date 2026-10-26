# Restauração de fitas VHS v2

[comfyui-workflows](../../README_ptBR.md) › **Restauração de fitas VHS v2**

O mesmo script da [v1](../vhs-upscale/README_ptBR.md) (mesma limpeza com ffmpeg, opções e saída), com outro upscale: em vez
do SeedVR2 nativo do ComfyUI (INT8), a v2 usa o custom node
[ComfyUI-SeedVR2_VideoUpscaler](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler) do numz com o mesmo modelo
SeedVR2 3B em **GGUF Q8_0**. No mesmo trecho foi **~3x mais rápida** e, a olho, tão boa ou melhor que a v1. A v1
continua como está, para instalações do ComfyUI sem custom nodes.

| | |
|---|---|
| Status | ✅ testado |
| Script | [`restore_vhs.py`](restore_vhs.py) (Python 3, sem pacotes extras) |
| Workflow usado | [SeedVR2 v2 · upscale de vídeo (GGUF)](../../workflows/42-seedvr2-upscale-v2/README_ptBR.md) ([`seedvr2_v2.api.json`](seedvr2_v2.api.json)) |
| Só limpeza | ~1,7× a duração do vídeo na CPU (ffmpeg), igual à v1 |
| Limpeza + upscale 720p (3B) | ~45–65× a duração do vídeo na GPU: **~50 min por minuto de fita** (v1: ~2 h) |
| Teste | capturas MPEG-2 padrão DVD (720x480 NTSC, 4:3), RTX 5060 Ti 16 GB, 2026-10-26 |

## Resultado

O mesmo quadro e a mesma entrada limpa (`--start 0.3 -t 3`, cor `normalize`, 720p):

1. **Captura VHS**: a captura original em DVD, só cortada como as outras e redimensionada para o mesmo tamanho;
2. **Limpeza com ffmpeg** (`--upscale none`);
3. **v1**: SeedVR2 3B INT8 nativo do ComfyUI (~410 s);
4. **v2**: custom node do numz, SeedVR2 3B GGUF Q8_0 (134 s).

![Captura VHS, limpeza com ffmpeg, v1 e v2](assets/compare.jpg)

![Detalhe do rosto nas quatro etapas](assets/compare_face.jpg)

## Arquivos desta pasta

| Arquivo | O que é |
|---|---|
| `restore_vhs.py` | O script |
| `seedvr2_v2.api.json` | Workflow SeedVR2 v2 (formato API) que o script preenche e manda para o ComfyUI |
| `seedvr2_v2.json` | O mesmo workflow para arrastar na interface do ComfyUI |
| `usecase.json` | Fonte da linha deste caso de uso no README principal |
| `assets/` | Imagens de comparação acima |

## Requisitos

- **ffmpeg** 6 ou mais novo (`ffmpeg`/`ffprobe` no `PATH`) e Python 3.8+.
- Para o upscale: ComfyUI com o custom node do numz e o modelo GGUF. Instale com o
  [`install.sh` do workflow SeedVR2 v2](../../workflows/42-seedvr2-upscale-v2/README_ptBR.md#instalação) (3B Q8_0 +
  VAE, 4,2 GB), depois `pip install rotary-embedding-torch==0.9.1` no Python do ComfyUI e reinicie o ComfyUI.
  O `--model 7b` precisa do `seedvr2_ema_7b-Q8_0.gguf` (8,8 GB, link nesse README).
- A conversa com o ComfyUI é igual à da v1: só a API HTTP, `COMFY_URL` (padrão `http://localhost:8188`) e o
  `COMFY_CONTAINER` opcional para apagar os blocos usados.
- Sem ComfyUI, `--upscale none` ainda faz toda a limpeza com ffmpeg.

## Como usar

Mesmos comandos e opções da [v1](../vhs-upscale/README_ptBR.md#como-usar):

```bash
python3 restore_vhs.py aniversario*.mpg               # limpeza + upscale 720p com o modelo 3B (padrões)
python3 restore_vhs.py aniversario*.mpg -t 5          # teste rápido: só os primeiros 5 s de cada vídeo
python3 restore_vhs.py -r ~/fitas -o ~/restaurados    # todos os vídeos de uma pasta e subpastas
python3 restore_vhs.py a.mpg --upscale none           # só a limpeza com ffmpeg (rápido)
python3 restore_vhs.py a.mpg --color mild --upscale 1080 --model 7b
```

## O que muda em relação à v1

Só a etapa 4 (upscale). O workflow enviado ao ComfyUI é `LoadVideo` → `SeedVR2LoadDiTModel` (GGUF) +
`SeedVR2LoadVAEModel` → `SeedVR2VideoUpscaler` → `SaveVideo`, com:

- `resolution` = 720 ou 1080 (o lado menor; o nó mantém a proporção);
- `batch_size` 21 (frames processados juntos; 4n+1);
- correção de cor `lab` (mantém as cores da limpeza com ffmpeg);
- VAE em blocos de 512 px.

O resto é igual à v1: blocos de 601 frames (~20 s) em 720p ou 181 (~6 s) em 1080p completados até 4n+1 e conferidos frame a frame, juntados com o áudio tratado.

## Testes

**v1 x v2, só o upscale** (mesmos 3 s da captura crua, 720p, `lab`):

| Versão | Tempo | Pico de VRAM |
|---|---|---|
| v1 nativo 3B INT8 | 411 s | 7,0 GB |
| v2 3B Q8_0 | 150 s | 8,1 GB |
| v2 3B Q4_K_M | 148 s | 8,0 GB |
| v2 3B Q8_0, `batch_size` 93 | sem VRAM | — |
| v2 3B Q8_0, `batch_size` 93, `blocks_to_swap` 16 | 142 s | 15,6 GB |

A olho, Q4 e Q8 ficaram iguais; o Q8 é o padrão por ser o mais próximo dos pesos originais. Lotes maiores não trouxeram
ganho visível, e nenhuma versão teve salto entre lotes.

**Limpar antes ou depois do upscale?** Mesmos 3 s, v2 3B Q8_0, nitidez como variância do Laplaciano (quadro todo / rosto):

| Ordem | Quadro todo | Rosto |
|---|---|---|
| captura crua, sem limpeza | 106 | 70 |
| **limpeza completa com ffmpeg antes (o que o script faz)** | **174** | **106** |
| só corte antes | 136 | 73 |
| corte + cor antes | 141 | 73 |
| limpeza completa depois do upscale | 104 | 69 |
| só cor depois do upscale | 108 | 74 |

Limpar antes entrega ao modelo um sinal mais limpo e ele reconstrói mais detalhe; limpar depois só tira. Também foi a
versão escolhida a olho.

**Script completo:**

| Teste | Resultado | Tempo de GPU | Pico de VRAM | RAM livre mínima |
|---|---|---|---|---|
| captura inteira (10 s, 313 frames), 3B 720p | 313 frames + áudio | 696 s | 14,5 GB | não medida |
| 22 s (660 frames, 2 blocos), 3B 720p | 660 frames + áudio | 983 s | 15,6 GB | 2,2 GB |
| captura inteira, 3B 1080p, blocos de 301 frames | 313 frames + áudio | 1059 s | 15,6 GB | **0,3 GB** |
| 7 s (210 frames, blocos de 181 + 29), 3B 1080p | 210 frames + áudio, sem salto na emenda | 705 s | 11,7 GB | 5,6 GB |
| 3 s, 7B 720p | 90 frames + áudio | 160 s | 12,1 GB | 3,9 GB |
| 3 s, 7B 1080p | 90 frames + áudio | 347 s | 15,4 GB | 4,1 GB |

Com blocos de 301 frames em 1080p o host quase ficou sem RAM, então o 1080p agora usa blocos de 181 frames (~6 s). O 7B
saiu mais suave que o 3B (nitidez 108 contra 174 no mesmo trecho), como na v1, então **3B, 720p** continua o padrão.

## Limitações

- **Tempo.** ~50 min de GPU por minuto de fita em 720p e ~1h40 em 1080p: fitas inteiras ainda demoram. Use `-t`/`--start` para testar um trecho antes.
- **Memória.** Cada bloco fica na RAM do ComfyUI. Os testes rodaram com ~9 GB de RAM livre no host; com menos, diminua o bloco com `RESTORE_VHS_CHUNK_FRAMES` (sempre 4n+1, por exemplo 301 ou 181).
- Rostos com borrão de movimento podem ganhar textura inventada em alguns quadros (como na v1).
- Cada bloco passa pelo upscale separado; um pequeno salto entre blocos é possível.
- Depende de um custom node de terceiros: uma atualização do ComfyUI pode quebrá-lo (a v1 não tem esse risco).
- O que a captura já perdeu (movimento dos campos, erros de tracking, vazamento de cor gravado) não volta.
