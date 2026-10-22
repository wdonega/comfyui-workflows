# VoxCPM2 · TTS, voz por descrição e clonagem

[comfyui-workflows](../../README_ptBR.md) › **VoxCPM2 · TTS, voz por descrição e clonagem**

Exemplo do nó com os dois modos: **VoxCPM2_TTS** cria a voz a partir de uma descrição em texto; **VoxCPM2_Clone** clona uma referência (com a transcrição dela no `prompt_text`). Saída em 48 kHz.

| | |
|---|---|
| Status | ✅ testado |
| Família | VoxCPM2 |
| Licença | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Download total | 0 MB |
| Teste | clone (9,4 s) e voz descrita como "homem calmo, voz grave, português do Brasil" (7,0 s). A frase em PT foi transcrita de volta pelo Qwen3-ASR e saiu correta (só "ComfyUI" vira algo como "Confiuí", normal para um nome em inglês). |
| Tempo | **1min 33s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 6581 MiB |

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
| ComfyUI-VoxCPM2 | `0e52a6c` | https://github.com/Saganaki22/ComfyUI-VoxCPM2 |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|

<details><summary>SHA-256</summary>

```
```

</details>

## Como usar

1. O modelo (~5 GB) baixa sozinho no primeiro uso para `models/tts/VoxCPM/VoxCPM2/` ([openbmb/VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)).
2. Dependências pip: `wetext inflect simplejson sortedcontainers soundfile` (`PIP_USER=true python3.13 -m pip install --no-deps` só do que faltar; veja `requirements.txt` do nó. Não instalar `onnxruntime-openvino` se já houver `onnxruntime`.). **Não** instale o pacote `voxcpm` do PyPI (conflita com `dill`); o nó traz o código em `src/`.
3. `enable_denoiser` e `enable_asr` exigem `modelscope`/`funasr` (não instalados); deixe desligados.

## Licença

Apache-2.0: uso pessoal e comercial livres, sem limite de receita nem de território; basta manter os avisos de licença ao redistribuir os pesos. As saídas são suas.

## Observações

- A voz de referência dos testes é sintética (voz "Serena" do Qwen3-TTS, 12,8 s em PT); nenhuma voz real foi clonada. Clonar a voz de alguém exige o consentimento dessa pessoa (direito de imagem/voz e LGPD).
