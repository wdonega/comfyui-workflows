<p align="center"><img src="assets/logo.svg" alt="ComfyUI Workflows" width="100%"></p>

Idioma: [English](README.md) · **Português**

# comfyui-workflows

Workflows do ComfyUI **testados** no homelab, cada um com tudo o que precisa para rodar de novo em
outra instalação: o workflow (interface e API), a lista de componentes com pasta de destino, link de
download fixado em commit e página, e um `install.sh` que instala tudo sozinho.

Ambiente dos testes: ComfyUI v0.42.4 (`3f438ca6`) em Docker (`yanwk/comfyui-boot` cu130), Python 3.13,
torch 2.13 + CUDA 13.0, **RTX 5060 Ti 16 GB**, 61 GB de RAM. A GPU ficou dedicada ao ComfyUI durante os testes:
nada mais rodava nela. Os primeiros workflows foram montados na v0.37.0 e todos rodaram de novo na v0.42.4
(teste de regressão); os tempos mostrados são da execução mais recente.

## O que tem aqui

```
workflows/<pasta>/
├── README_ptBR.md     componentes, pastas, links, como usar, licença, resultado do teste (README.md: inglês)
├── workflow.json      arrastar na interface do ComfyUI
├── workflow.api.json  formato da API (POST /prompt)
├── install.sh         instala custom nodes e modelos (autocontido)
└── components.json    fonte de dados do README e do install.sh
lib/comfy_install.sh   funções dos install.sh (embutidas em cada um pelo gerador)
tools/                 gerador e conversores (ver tools/README_ptBR.md)
```

## Workflows

Todos os workflows abaixo foram testados no setup descrito acima; os tempos são dessas execuções.

### Imagem

| Workflow | Família | O que faz | Tempo do teste | Download | Licença |
|---|---|---|---|---|---|
| [Qwen-Image 2.1 Turbo](workflows/37-qwen-image-21-turbo/README_ptBR.md) | Qwen-Image 2.1 | A versão turbo do Qwen-Image 2.1: mesma qualidade, 2,4x mais rápida | 10s · 1024² | 17.28 GB | Qwen Research (só pesquisa) |
| [Krea 2 Turbo](workflows/38-krea2-turbo/README_ptBR.md) | Krea 2 | Texto para imagem com visual cinematográfico, 8 steps | 23s · 1024² | 18.61 GB | Krea 2 Community (grátis < US$ 1 mi) |
| [Flux 3 Klein (destilado)](workflows/39-flux3-klein/README_ptBR.md) | Flux 3 | Texto para imagem rico em detalhes, com upsampler de prompt | 21s · 1024² | 17.75 GB | FLUX Kommunity (grátis < US$ 5 mi) |
| [MOSS-Image (SFT)](workflows/40-moss-image/README_ptBR.md) | MOSS-Image | Texto para imagem de licença livre (Apache-2.0) | 35s · 1024² | 13.01 GB | Apache-2.0 (livre) |
| [SeedVR2 · upscale 4x](workflows/42-seedvr2-upscale/README_ptBR.md) | SeedVR2 | Upscale de imagem 4x em 1 step (também há versão para vídeo) | 23s · 1024² → 4096² | 3.96 GB | Apache-2.0 (livre) |
| [Qwen-Image 2.1 · edição por instrução](workflows/qwen-image-21-edit/README_ptBR.md) | Qwen-Image 2.1 | Edita uma foto por texto, com até 10 imagens de referência | 1min 17s · 896x1152 | 17.28 GB | Qwen Research (só pesquisa) |
| [Qwen-Image 2.1 · texto para imagem](workflows/qwen-image-21-t2i/README_ptBR.md) | Qwen-Image 2.1 | O template oficial do Qwen-Image 2.1 (25 steps) | 26s · 1024² | 17.28 GB | Qwen Research (só pesquisa) |
| [Qwen-Image 2.1 · Viggle 4 steps (edição)](workflows/qwen-image-21-viggle-edit/README_ptBR.md) | Qwen-Image 2.1 | Edição por instrução em 4 steps, até 3 referências, saída de até 4 MP | 1min 23s · 2752x1536 | 17.62 GB | Qwen Research (só pesquisa) |
| [Qwen-Image 2.1 · Viggle 4 steps (texto para imagem)](workflows/qwen-image-21-viggle-t2i/README_ptBR.md) | Qwen-Image 2.1 | Qwen-Image 2.1 em 4 steps com o LoRA turbo da Viggle, até 2 MP | 11s · 1920x1088 | 17.62 GB | Qwen Research (só pesquisa) |

### Vídeo

| Workflow | Família | O que faz | Tempo do teste | Download | Licença |
|---|---|---|---|---|---|
| [H3 Turbo v4 (larryvrh)](workflows/02-h3-turbo-v4/README_ptBR.md) | MiniMax H3 | LoRA turbo de 4–8 steps com sampler próprio (alternativa ao TaoMate) | 16min 34s · 15 s | 40.85 GB | MiniMax H3 Community (⚠️ território) |
| [LTX 2.3 · imagem para vídeo com áudio](workflows/04-ltx23-i2v/README_ptBR.md) | LTX 2.3 | Imagem → vídeo com áudio e fala em 2 estágios (rápido) | 1min 35s · 4,8 s | 43.35 GB | LTX-2 Community (grátis < US$ 10 mi) |
| [Wan 2.2 5B · texto/imagem para vídeo](workflows/06-wan22-5b-ti2v/README_ptBR.md) | Wan 2.2 | Vídeo 720p de 5 s a partir de texto (ou imagem), cabe nativo em 16 GB | 9min 10s · 5 s | 18.14 GB | Apache-2.0 (livre) |
| [H3 Character Swap (Relay 2.0)](workflows/14-h3-character-swap/README_ptBR.md) | MiniMax H3 | Troca o personagem de um vídeo mantendo performance, cena e áudio | 12min 56s · 4 s | 46.33 GB | MiniMax H3 Community (⚠️ território) |
| [Wan Animate 2 · anima um personagem com o movimento de um vídeo](workflows/15-wan-animate-2/README_ptBR.md) | Wan 2.2 (Animate 2) | Transfere pose, corpo e expressões de um vídeo-guia para a imagem de um personagem | 7min 02s · 3.4 s | 24.91 GB | Apache-2.0 (livre) |
| [Bernini-R · transferência de estilo (anime / real)](workflows/16-bernini-r-style-transfer/README_ptBR.md) | Wan 2.2 (Bernini-R) | Edita vídeo com o Bernini-R; LoRAs de estilo anime e real-life | 18min 33s · 4,9 s | 39.15 GB | Apache-2.0 (livre) |
| [LTX 2.3 · Face Swap (head swap)](workflows/17-ltx23-face-swap/README_ptBR.md) | LTX 2.3 | Troca a cabeça/rosto de uma pessoa num vídeo mantendo corpo, roupa, movimento e áudio | 6min 45s · 4 s | 44.71 GB | LTX-2 Community (grátis < US$ 10 mi) |
| [H3 HR Endless Sampler (Gemma 4 dirige os chunks)](workflows/23-h3-hr-endless-sampler/README_ptBR.md) | MiniMax H3 | Vídeo longo em chunks; Gemma 4 local planeja a produção e escreve o prompt de cada chunk | 16min 36s · 6,6 s | 50.11 GB | MiniMax H3 Community (⚠️ território) |
| [H3 Long Video (prompt dividido por LLM)](workflows/24-h3-long-video/README_ptBR.md) | MiniMax H3 | Vídeos longos em segmentos encadeados, com o prompt dividido por um LLM | 11min 26s · 16 s | 44.43 GB | MiniMax H3 Community (⚠️ território) |
| [Herrgott's H3 Infinite Continuation (v1.4)](workflows/25-h3-infinite-continuation/README_ptBR.md) | MiniMax H3 | Encadeia clipes FL2VA com handover seguro e junta tudo sem emenda visível | 22min 31s · 8,7 s (2 clipes) | 42.47 GB | MiniMax H3 Community (⚠️ território) |
| [LTX 2.3 · Foley (som para vídeo mudo)](workflows/33-ltx23-foley-v2a/README_ptBR.md) | LTX 2.3 | Gera efeitos sonoros sincronizados para um vídeo sem áudio | 32min 09s · 7 s | 39.07 GB | LTX-2 Community (grátis < US$ 10 mi) |
| [H3 Realism People](workflows/59-h3-realism-people/README_ptBR.md) | MiniMax H3 | LoRA de realismo para pessoas (gatilho r34l1sm) | 1min 55s · 5 s | 42.69 GB | MiniMax H3 Community (⚠️ território) |
| [LTX 2.3 · Clean Plate (remove pessoas do vídeo)](workflows/60-ltx23-clean-plate/README_ptBR.md) | LTX 2.3 | Apaga pessoas e objetos em movimento e devolve o fundo vazio | 3min 39s · 4 s | 42.68 GB | LTX-2 Community (grátis < US$ 10 mi) |
| [H3 Director · TaoMate 3 steps (timeline)](workflows/h3-director-3step/README_ptBR.md) | MiniMax H3 | Vídeo de 15 s com áudio, montado numa timeline de segmentos | 10min 10s · 15 s | 63.53 GB | MiniMax H3 Community (⚠️ território) |
| [H3 Ref2VA · TaoMate 3 steps](workflows/h3-ref2va-taomate-3step/README_ptBR.md) | MiniMax H3 | Vídeo+áudio a partir de imagem de referência em 3 steps | 8min 39s · 15 s | 42.55 GB | MiniMax H3 Community (⚠️ território) |

### Áudio

| Workflow | Família | O que faz | Tempo do teste | Download | Licença |
|---|---|---|---|---|---|
| [ACE-Step 1.5 Turbo · música](workflows/32-ace-step-15-turbo/README_ptBR.md) | ACE-Step 1.5 | Música com letra em 8 steps; 30 s em 16 s | 16s · 30 s | 10.03 GB | MIT (livre) |
| [Fish Audio Drama 3 · clonagem de voz](workflows/46-fish-drama3-voice-clone/README_ptBR.md) | Fish Audio Drama 3 | TTS expressivo de 35B com clonagem, deixas como [laughs] e vários falantes | 1min 04s · 8.6 s | 44.34 GB | Fish Audio Community (comercial < US$ 500 mil) |
| [VoxCPM2 · TTS, voz por descrição e clonagem](workflows/47-voxcpm2/README_ptBR.md) | VoxCPM2 | TTS de 2B em 30 idiomas, 48 kHz: voz criada por texto ou clonada | 1min 33s · 2 × ~8 s | 4.96 GB | Apache-2.0 (livre) |
| [Chatterbox Multilingual · TTS com clonagem (23 idiomas)](workflows/48-chatterbox-multilingual/README_ptBR.md) | Chatterbox | TTS leve e rápido com clonagem, inclui português | 11s · 8.6 s | 3.21 GB | MIT (livre) |
| [Qwen3-TTS · vozes prontas e clonagem](workflows/49-qwen3-tts/README_ptBR.md) | Qwen3-TTS | TTS de 1.7B em 10 idiomas (inclui PT): 9 vozes prontas, clonagem e voz por descrição | 1min 29s · 12.8 s + 7.5 s | 9.75 GB | Apache-2.0 (livre) |
| [MiniMax Music 3 · música com letra](workflows/minimax-music3/README_ptBR.md) | MiniMax Music 3 | Gera uma música de até alguns minutos a partir de estilo + letra | 2min 26s · 60 s | 14.33 GB | MiniMax-Music3 Community |

Tempos medidos na RTX 5060 Ti 16 GB com os parâmetros descritos no README de cada pasta
(execução no ComfyUI, sem fila; o pico de VRAM está no README de cada pasta). "Download" é o total de modelos do workflow, contando
arquivos compartilhados com outros.

## Instalar um workflow

```bash
# na máquina do ComfyUI
bash workflows/<pasta>/install.sh /caminho/do/ComfyUI

# ComfyUI em Docker (container "comfyui"): o script vai pela entrada padrão
docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < workflows/<pasta>/install.sh
```

O script só roda se a pasta for a **raiz do ComfyUI** (`main.py`, `folder_paths.py`, `models/`,
`custom_nodes/`). Se você apontar para uma subpasta (por exemplo `models/`), ele avisa qual é a raiz.
Arquivos existentes com o tamanho certo são pulados; downloads novos têm o SHA-256 conferido.
Repositórios gated precisam da licença aceita no Hugging Face e de `HF_TOKEN` no ambiente.

## Licenças

O conteúdo deste repositório (scripts, `lib/`, `tools/`, READMEs e os workflows montados aqui) está sob
**[0BSD](LICENSE)**: use, copie e modifique à vontade, sem precisar dar crédito.
Workflows de terceiros redistribuídos (indicados no README da pasta) mantêm a licença do autor, e os
**modelos** baixados pelos `install.sh` têm licenças próprias, resumidas em cada pasta (não é parecer
jurídico). Atenção especial:

- **MiniMax H3**: proibido nos EUA, UE, Reino Unido e Coreia do Sul, **inclusive as saídas**.
  Não use os vídeos em projetos publicados globalmente.
- **Qwen-Image 2.1**: só pesquisa e avaliação.

## Manutenção

```bash
python3 tools/gen.py      # regera README.md, README_ptBR.md e install.sh a partir dos components.json
```

Para adicionar um workflow: crie `workflows/<pasta>/` com `workflow.json`, `workflow.api.json` e
`components.json` (copie um existente como modelo; textos traduzíveis são `{"pt": ..., "en": ...}`; `kind` é `image`, `video` ou `audio`) e rode o gerador.

---

Projeto independente, sem afiliação nem endosso da Comfy Org. O logo usa letras próprias; "ComfyUI" aparece só para dizer para que servem estes workflows.
