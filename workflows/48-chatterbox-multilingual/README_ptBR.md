# Chatterbox Multilingual · TTS com clonagem (23 idiomas)

[comfyui-workflows](../../README_ptBR.md) › **Chatterbox Multilingual · TTS com clonagem (23 idiomas)**

O nó **FL Chatterbox Multilingual TTS** (ResembleAI) clonando uma voz de referência em português (`Portuguese (pt)`). Usa ~3,7 GB de VRAM.

| | |
|---|---|
| Status | ✅ testado |
| Família | Chatterbox |
| Licença | [MIT](https://opensource.org/license/mit) |
| Download total | 3.21 GB |
| Teste | temperatura 0,6: 8,6 s só com a frase. Com a temperatura padrão (0,8) o modelo continuou ~30 s com balbucio depois da frase. A frase em PT foi transcrita de volta pelo Qwen3-ASR e saiu correta (só "ComfyUI" vira algo como "Confiuí", normal para um nome em inglês). |
| Tempo | **11s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 3729 MiB |

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
| ComfyUI_Fill-ChatterBox | `f7d7a16` | https://github.com/filliptm/ComfyUI_Fill-ChatterBox |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `chatterbox/chatterbox_multilingual/` | `t3_mtl23ls_v2.safetensors` | T3 multilíngue v2 (texto → tokens de fala) | 2.14 GB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/t3_mtl23ls_v2.safetensors) | [página](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `s3gen.pt` | S3Gen (tokens → áudio) | 1.06 GB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/s3gen.pt) | [página](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `ve.pt` | Codificador de voz | 6 MB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/ve.pt) | [página](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `conds.pt` | Voz padrão | 0 MB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/conds.pt) | [página](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `Cangjie5_TC.json` | configuração / tokenizador | 2 MB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/Cangjie5_TC.json) | [página](https://huggingface.co/ResembleAI/chatterbox) |
| `chatterbox/chatterbox_multilingual/` | `grapheme_mtl_merged_expanded_v1.json` | configuração / tokenizador | 0 MB | [download](https://huggingface.co/ResembleAI/chatterbox/resolve/5bb1f6ee58e50c3b8d408bc82a6d3740c2db6e18/grapheme_mtl_merged_expanded_v1.json) | [página](https://huggingface.co/ResembleAI/chatterbox) |

<details><summary>SHA-256</summary>

```
b1237586127ce98e7800a68e49938eb5092846862aabcb6e17b2fda7889a6c75  models/chatterbox/chatterbox_multilingual/t3_mtl23ls_v2.safetensors
9b9ff07e60b20c136e2b1b3d7563a24604e8d2c4c267888d1ee929dd0151d2a3  models/chatterbox/chatterbox_multilingual/s3gen.pt
4b16d836bc598509860f6fa068165a8bb5e9ac84f05582dfcf278a5a372879f1  models/chatterbox/chatterbox_multilingual/ve.pt
6552d70568833628ba019c6b03459e77fe71ca197d5c560cef9411bee9d87f4e  models/chatterbox/chatterbox_multilingual/conds.pt
```

</details>

## Como usar

1. Os modelos baixam sozinhos no primeiro uso para `models/chatterbox/chatterbox_multilingual/` ([ResembleAI/chatterbox](https://huggingface.co/ResembleAI/chatterbox)).
2. Dependências pip do `requirements.txt` do nó (`PIP_USER=true python3.13 -m pip install --no-deps` só do que faltar; veja `requirements.txt` do nó. Não instalar `onnxruntime-openvino` se já houver `onnxruntime`.).
3. Use **temperatura 0,6**; em 0,8 ele alucinou depois do fim da frase.

## Licença

MIT: uso pessoal e comercial livres, sem limite; basta manter o aviso de copyright ao redistribuir os pesos.

## Observações

- O repositório do nó não declara licença.
- A voz de referência dos testes é sintética (voz "Serena" do Qwen3-TTS, 12,8 s em PT); nenhuma voz real foi clonada. Clonar a voz de alguém exige o consentimento dessa pessoa (direito de imagem/voz e LGPD).
