# Qwen3-TTS · vozes prontas e clonagem

[comfyui-workflows](../../README_ptBR.md) › **Qwen3-TTS · vozes prontas e clonagem**

Dois workflows do nó **ComfyUI-Qwen-TTS**: `01-custom-voice` fala o texto com uma das 9 vozes prontas (Serena, Ryan, Eric…); `02-voice-clone` clona uma referência a partir do áudio e da transcrição dela. O nó também tem **VoiceDesign** (voz por descrição) e diálogo com vários falantes.

| | |
|---|---|
| Status | ✅ testado |
| Família | Qwen3-TTS |
| Licença | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Download total | 9.75 GB |
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
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/` | `model.safetensors` | Qwen3-TTS 1.7B CustomVoice (vozes prontas) | 3.83 GB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/model.safetensors) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/speech_tokenizer/` | `model.safetensors` | Tokenizador de fala (cópia do modelo) | 0.68 GB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/speech_tokenizer/model.safetensors) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/` | `vocab.json` | configuração / tokenizador | 3 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/vocab.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/` | `merges.txt` | configuração / tokenizador | 2 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/merges.txt) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/` | `config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/` | `generation_config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/generation_config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/` | `preprocessor_config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/preprocessor_config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/` | `tokenizer_config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/tokenizer_config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/speech_tokenizer/` | `config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/speech_tokenizer/config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/speech_tokenizer/` | `configuration.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/speech_tokenizer/configuration.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/speech_tokenizer/` | `preprocessor_config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/resolve/0c0e3051f131929182e2c023b9537f8b1c68adfe/speech_tokenizer/preprocessor_config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/` | `model.safetensors` | Qwen3-TTS 1.7B Base (clonagem) | 3.86 GB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/model.safetensors) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/speech_tokenizer/` | `model.safetensors` | Tokenizador de fala (cópia do modelo) | 0.68 GB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/speech_tokenizer/model.safetensors) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/` | `vocab.json` | configuração / tokenizador | 3 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/vocab.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/` | `merges.txt` | configuração / tokenizador | 2 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/merges.txt) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/` | `config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/` | `generation_config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/generation_config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/` | `preprocessor_config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/preprocessor_config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/` | `tokenizer_config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/tokenizer_config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/speech_tokenizer/` | `config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/speech_tokenizer/config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/speech_tokenizer/` | `configuration.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/speech_tokenizer/configuration.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/speech_tokenizer/` | `preprocessor_config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base/resolve/fd4b254389122332181a7c3db7f27e918eec64e3/speech_tokenizer/preprocessor_config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| `qwen-tts/Qwen3-TTS-Tokenizer-12Hz/` | `model.safetensors` | Tokenizador de fala 12 Hz | 0.68 GB | [download](https://huggingface.co/Qwen/Qwen3-TTS-Tokenizer-12Hz/resolve/7dd38ad4e9bad454aae9cd937d0cd577604fe229/model.safetensors) | [página](https://huggingface.co/Qwen/Qwen3-TTS-Tokenizer-12Hz) |
| `qwen-tts/Qwen3-TTS-Tokenizer-12Hz/` | `config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-Tokenizer-12Hz/resolve/7dd38ad4e9bad454aae9cd937d0cd577604fe229/config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-Tokenizer-12Hz) |
| `qwen-tts/Qwen3-TTS-Tokenizer-12Hz/` | `configuration.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-Tokenizer-12Hz/resolve/7dd38ad4e9bad454aae9cd937d0cd577604fe229/configuration.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-Tokenizer-12Hz) |
| `qwen-tts/Qwen3-TTS-Tokenizer-12Hz/` | `preprocessor_config.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/Qwen/Qwen3-TTS-Tokenizer-12Hz/resolve/7dd38ad4e9bad454aae9cd937d0cd577604fe229/preprocessor_config.json) | [página](https://huggingface.co/Qwen/Qwen3-TTS-Tokenizer-12Hz) |

<details><summary>SHA-256</summary>

```
38b1d5971bdbd982b561cccec982669a53b0537c3cf5e9bd4778ed07bb2f5137  models/qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/model.safetensors
836b7b357f5ea43e889936a3709af68dfe3751881acefe4ecf0dbd30ba571258  models/qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice/speech_tokenizer/model.safetensors
38fc7fc51c5e776e840414b6fd443962e9411b9654888fd7913e4da643cb857c  models/qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/model.safetensors
836b7b357f5ea43e889936a3709af68dfe3751881acefe4ecf0dbd30ba571258  models/qwen-tts/Qwen3-TTS-12Hz-1.7B-Base/speech_tokenizer/model.safetensors
836b7b357f5ea43e889936a3709af68dfe3751881acefe4ecf0dbd30ba571258  models/qwen-tts/Qwen3-TTS-Tokenizer-12Hz/model.safetensors
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
