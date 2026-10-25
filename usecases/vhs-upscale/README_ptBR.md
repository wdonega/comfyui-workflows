# Restauração de fitas VHS

[comfyui-workflows](../../README_ptBR.md) › **Restauração de fitas VHS**

Restauração em lote de vídeos caseiros antigos capturados de VHS (e outros formatos antigos): o `restore_vhs.py` limpa
cada arquivo com ffmpeg (bordas, blocos de compressão, ruído, cor, áudio), manda o vídeo limpo para o ComfyUI fazer o
upscale com **SeedVR2** em blocos, junta tudo de volta com o áudio tratado e salva um MP4 moderno. O original nunca é
alterado.

| | |
|---|---|
| Status | ✅ testado |
| Script | [`restore_vhs.py`](restore_vhs.py) (Python 3, sem pacotes extras) |
| Workflows usados | [SeedVR2 · upscale 4x](../../workflows/42-seedvr2-upscale/README_ptBR.md) (modelos); template oficial de vídeo do SeedVR2 do ComfyUI ([`seedvr2_video.api.json`](seedvr2_video.api.json)) |
| Só limpeza | ~1,7× a duração do vídeo na CPU (ffmpeg) |
| Limpeza + upscale 720p (3B) | ~110–130× a duração do vídeo na GPU: **~2 h por minuto de fita** |
| Teste | duas capturas MPEG-2 padrão DVD (720x480 NTSC, 4:3, 9–10 s), RTX 5060 Ti 16 GB, 2026-10-25 |

## Arquivos desta pasta

| Arquivo | O que é |
|---|---|
| `restore_vhs.py` | O script |
| `seedvr2_video.api.json` | Workflow de vídeo do SeedVR2 (formato API) que o script preenche e manda para o ComfyUI |
| `seedvr2_video.json` | O mesmo workflow para arrastar na interface do ComfyUI |
| `usecase.json` | Fonte da linha deste caso de uso no README principal |

## Requisitos

- **ffmpeg** 6 ou mais novo (`ffmpeg`/`ffprobe` no `PATH`) e Python 3.8+.
- Para o upscale: ComfyUI com os modelos do SeedVR2. Instale com o
  [`install.sh` do workflow do SeedVR2](../../workflows/42-seedvr2-upscale/README_ptBR.md#instalação)
  (3B, 3,5 GB). Os modelos 7B são opcionais e estão documentados no final desse README.
- O script copia os arquivos para o ComfyUI com `docker cp`/`docker exec`. Os padrões são para um container chamado
  `comfyui`; mude com `COMFY_URL` (padrão `http://localhost:8188`), `COMFY_CONTAINER` (padrão `comfyui`) e
  `COMFY_OUTPUT` (pasta de saída do ComfyUI no host, padrão `/opt/appdata/comfyui/output`).
- Sem ComfyUI, `--upscale none` ainda faz toda a limpeza com ffmpeg.

## Como usar

```bash
python3 restore_vhs.py niver*.mpg                     # limpeza + upscale 720p com o modelo 3B (padrões)
python3 restore_vhs.py niver*.mpg -t 5                # teste rápido: só os 5 primeiros segundos de cada vídeo
python3 restore_vhs.py -r ~/fitas -o ~/restaurados    # todos os vídeos de uma pasta e das subpastas
python3 restore_vhs.py a.mpg --upscale none           # só a limpeza com ffmpeg (rápido)
python3 restore_vhs.py a.mpg --color mild --upscale 1080 --model 7b
```

Saída: `<pasta de destino>/<nome>_restored.mp4` (H.264 + AAC). Arquivos que já existem são pulados (`--overwrite` refaz).
Se uma entrada for uma pasta e faltar o `-r`, o script avisa e pula. Curingas entre aspas são expandidos pelo script.

| Opção | Valores | Padrão |
|---|---|---|
| `-o`, `--output` | pasta de destino | `./restored` |
| `-r`, `--recursive` | processa pastas, incluindo subpastas | desligado |
| `--color` | `normalize`, `mild`, `strong`, `auto`, `auto45`, `colorcorrect`, `none` | `normalize` |
| `--upscale` | `720`, `1080`, `none` | `720` |
| `--model` | `3b`, `7b` | `3b` |
| `-t`, `--max` | duração máxima de cada vídeo, em segundos | o vídeo inteiro |
| `--start` | começa neste segundo | `0` |
| `--overwrite` | refaz saídas que já existem | desligado |
| `--keep-temp` | mantém os arquivos intermediários (útil quando algo falha) | desligado |

### Opções de cor

| Opção | Filtro do ffmpeg | Quando usar |
|---|---|---|
| `normalize` | `normalize` com 70% de intensidade, suavizado no tempo | **Padrão.** Tira a maior parte da dominante de cor sem matar a luz quente; quase não mexe em vídeo que já está bom |
| `mild` | `colortemperature` 8500 K, 60% | Cenas internas com lâmpada incandescente (amarelo/laranja) |
| `strong` | `colortemperature` 10000 K, 70% | Imagem muito amarelada |
| `auto` | `grayworld` | Raramente: em cena quente deixa pele e parede verdes/azuladas |
| `auto45` | `grayworld` misturado a 45% | Um `auto` mais suave |
| `colorcorrect` | `colorcorrect=analyze=median` | Raramente: deixou uma das cenas de teste azulada |
| `none` | — | Mantém as cores originais |

## O que o script faz

1. **Lê o arquivo** (`ffprobe`): resolução, proporção dos pixels (captura de DVD tem pixel não quadrado), codec, áudio.
   O ffmpeg lê praticamente qualquer formato antigo: `.mpg`, `.vob`, `.avi`, `.dv`, `.wmv`, `.mov`, `.3gp`…
2. **Mede o vídeo**:
   - bordas pretas (`cropdetect`), mais 2 px de cada lado pela borda irregular do VHS e, em captura SD, as 12 linhas do
     rodapé com o **ruído de troca de cabeça**;
   - entrelaçamento (`idet`): só desentrelaça (`bwdif`, para 50/60p) se mais de 25% dos quadros forem entrelaçados.
     As duas capturas de teste estavam marcadas como entrelaçadas no arquivo, mas eram 97% progressivas (o aparelho de
     captura já tinha juntado os campos); desentrelaçar só iria borrar.
3. **Limpa** com ffmpeg: corte, `deblock` (só em fonte MPEG-1/2/4 e WMV), redução de ruído `nlmeans`, cor, escala para
   pixel quadrado; áudio: passa-altas em 60 Hz (zumbido), `afftdn` (chiado da fita), `loudnorm` (um dos vídeos de teste
   estava 10 dB mais baixo).
4. **Faz o upscale** com SeedVR2 pelo ComfyUI (template oficial de vídeo, correção de cor `lab` para manter as cores da
   etapa 3, blocos temporais automáticos para caber na VRAM). O ComfyUI carrega o trecho inteiro na RAM, então vídeos
   longos vão em blocos de 601 quadros (~20 s) em 720p ou 301 (~10 s) em 1080p.
   O SeedVR2 só devolve todos os quadros quando recebe 4n+1, então o último bloco é completado com cópias do último
   quadro, cortado de volta depois, e a contagem de quadros de cada bloco é conferida: a imagem fica em sincronia com o
   áudio.
5. **Junta** os blocos com o áudio da etapa 3 num MP4 H.264 + AAC (`+faststart`, toca em qualquer lugar).

## Testes e decisões

**Cor.** Quatro correções foram comparadas em dois quadros de cada vídeo. O `grayworld` do ffmpeg acertou o vídeo com luz
do dia, mas esverdeou o de lâmpada incandescente; o `colorcorrect` deixou uma cena azulada; o `normalize` ficou mais perto
da correção escolhida no olho, por isso é o padrão. Também pedimos a um LLM com visão (Qwen 3.8 Flash) para ordenar as
versões, embaralhadas e com rótulos neutros, 9 vezes: ele sempre pôs a versão esverdeada em último, mas a primeira escolha
seguia a **posição** da imagem (a posição D em 6 de 9 rodadas), não as cores. Ele não é usado para escolher.

**Upscale.** Os mesmos 3 s (89 quadros), 640x480 → 960x720, todos com os ajustes do SeedVR2 do template oficial:

| Versão | Nitidez (variância do Laplaciano) | Tempo | Pico de VRAM | Rostos |
|---|---|---|---|---|
| entrada (lanczos) | 65 | — | — | — |
| **SeedVR2 3B** | **221** | 329 s | 7,5 GB | fiéis |
| SeedVR2 7B | 119 | 392 s | 10,8 GB | fiéis, mais suaves |
| SeedVR2 7B *sharp* | 109 | 438 s | 10,9 GB | fiéis, mais suaves |
| Wan 2.2 5B, vídeo para vídeo a 0,3 | 75 | 273 s | 14,3 GB | **viram outra pessoa** |
| 3B duas vezes (720p) | — | 329 + 354 s | 7,5 GB | mais nítido, mas contornos duros e sombras inventadas |

Numa fonte tão degradada, os 7B preservam o borrado em vez de reconstruir, e re-gerar com um modelo de geração de vídeo
(Wan 2.2) acrescenta textura mudando as pessoas. **3B, uma passada, 720p** é o padrão; 1080p fica igual (o VHS tem ~250
linhas de detalhe real) e custa ~1,5× mais.

**Script completo:** 3 s de uma captura com limpeza + upscale 720p levaram 391 s de ponta a ponta (380 s no ComfyUI).

## Limitações

- **Tempo.** ~2 h de GPU por minuto de fita em 720p: fitas inteiras levam dias. Use `-t`/`--start` para testar um trecho
  antes e deixe o upscale para os momentos que importam (`--upscale none` no resto).
- Rostos com borrado de movimento podem ganhar textura inventada (olhos estranhos, pele envelhecida) em alguns quadros.
- Cada bloco passa pelo upscale separado; um pequeno salto entre blocos (a cada ~20 s) é possível.
- O que a captura já perdeu (movimento dos campos, erros de tracking, vazamento de cor gravado) não volta.
- O script precisa rodar na máquina do ComfyUI (usa `docker cp` e lê a pasta de saída do ComfyUI).
