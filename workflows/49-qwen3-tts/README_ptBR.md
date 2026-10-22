# Qwen3-TTS · vozes prontas e clonagem

[comfyui-workflows](../../README_ptBR.md) › **Qwen3-TTS · vozes prontas e clonagem**

Dois workflows do nó **ComfyUI-Qwen-TTS**: `01-custom-voice` fala o texto com uma das 9 vozes prontas (Serena, Ryan, Eric…); `02-voice-clone` clona uma referência a partir do áudio e da transcrição dela. O nó também tem **VoiceDesign** (voz por descrição) e diálogo com vários falantes.

| | |
|---|---|
| Status | ✅ testado |
| Família | Qwen3-TTS |
| Licença | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Download total | 0 MB |
| Teste | voz "Serena" em PT (12,8 s), transcrita palavra por palavra; clonagem dessa voz com a frase em PT (7,5 s, 81 s com o download do modelo base). A frase em PT foi transcrita de volta pelo Qwen3-ASR e saiu correta (só "ComfyUI" vira algo como "Confiuí", normal para um nome em inglês). |
| Tempo | **1min 29s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 8439 MiB |

## Arquivos desta pasta

| Arquivo | O que é |
|---|---|
| `01-custom-voice.json` | Voz pronta: arrastar na interface |
| `01-custom-voice.api.json` | Voz pronta (API) |
| `02-voice-clone.json` | Clonagem: arrastar na interface |
| `02-voice-clone.api.json` | Clonagem (API) |
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
| ComfyUI-Qwen-TTS | `a1328c8` | https://github.com/flybirdxx/ComfyUI-Qwen-TTS |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|

<details><summary>SHA-256</summary>

```
```

</details>

## Como usar

1. Os modelos baixam sozinhos no primeiro uso para `models/qwen-tts/` (`Qwen3-TTS-12Hz-1.7B-CustomVoice`, `-Base` e o tokenizer, ~4,5 GB cada). Para baixar antes: `python3 download_models.py` na pasta do nó.
2. Dependências pip do `requirements.txt` **sem** `onnxruntime-openvino` (`PIP_USER=true python3.13 -m pip install --no-deps` só do que faltar; veja `requirements.txt` do nó. Não instalar `onnxruntime-openvino` se já houver `onnxruntime`.).
3. `attention` = `sdpa` se o SageAttention não estiver instalado; `language` = `Portuguese`.

## Licença

Apache-2.0: uso pessoal e comercial livres, sem limite de receita nem de território; basta manter os avisos de licença ao redistribuir os pesos. As saídas são suas.

## Observações

- O exemplo original do nó clona a voz de uma pessoa real (`雷军.mp3`); aqui foi trocado pela voz sintética.
- O repositório do nó não declara licença.
- Clonar a voz de alguém exige o consentimento dessa pessoa (direito de imagem/voz e LGPD).
