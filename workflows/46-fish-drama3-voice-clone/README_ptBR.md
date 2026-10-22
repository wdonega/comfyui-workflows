# Fish Audio Drama 3 · clonagem de voz

[comfyui-workflows](../../README_ptBR.md) › **Fish Audio Drama 3 · clonagem de voz**

O exemplo `drama3_voice_clone` do nó: o Qwen3-ASR transcreve a voz de referência, o Drama 3 codifica a voz e fala o texto (aceita deixas como `[laughs]`, `[whispers]`). Variante **int8experts**: ~6 GB do modelo na GPU e os experts na **RAM** (~48 GB de RAM livre).

| | |
|---|---|
| Status | ✅ testado |
| Família | Fish Audio Drama 3 |
| Licença | [Fish Audio Community License](https://huggingface.co/fishaudio/drama-3) |
| Download total | 44.34 GB |
| Teste | clonagem da voz sintética com a frase em PT (8,6 s, 44,1 kHz). A frase em PT foi transcrita de volta pelo Qwen3-ASR e saiu correta (só "ComfyUI" vira algo como "Confiuí", normal para um nome em inglês). |
| Tempo | **1min 04s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 14215 MiB |

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
| ComfyUI-Drama3 | `67a733a` | https://github.com/PedroMarinhoDev/ComfyUI-Drama3 |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `drama3_int8experts_bf16.safetensors` | Drama 3 (experts INT8; o mais rápido em < 24 GB) | 38.70 GB | [download](https://huggingface.co/PedroMarinhoDev/Drama-3-ComfyUI/resolve/681e2fae64af1f12e64b9c19c82930a5f3bba1a4/drama3_int8experts_bf16.safetensors) | [página](https://huggingface.co/PedroMarinhoDev/Drama-3-ComfyUI) |
| `vae/` | `drama3_codec.safetensors` | codec de áudio | 1.57 GB | [download](https://huggingface.co/PedroMarinhoDev/Drama-3-ComfyUI/resolve/681e2fae64af1f12e64b9c19c82930a5f3bba1a4/drama3_codec.safetensors) | [página](https://huggingface.co/PedroMarinhoDev/Drama-3-ComfyUI) |
| `asr/` | `qwen3_asr_1.7b_bf16.safetensors` | Qwen3-ASR 1.7B (transcreve a referência) | 4.08 GB | [download](https://huggingface.co/PedroMarinhoDev/Qwen3-ASR-ComfyUI/resolve/6ad8c9be026925839479a8d97749068a4202fbe9/qwen3_asr_1.7b_bf16.safetensors) | [página](https://huggingface.co/PedroMarinhoDev/Qwen3-ASR-ComfyUI) |

<details><summary>SHA-256</summary>

```
f407996b17583ba857ace14e0330a13788cf89f4d47cfdcd4766ad5106576899  models/diffusion_models/drama3_int8experts_bf16.safetensors
4fecf102907a48414230da9a74d72d07c3a92368eab53fab655797837bddf5ae  models/vae/drama3_codec.safetensors
958ac49a7015ad546206e87fbcf390ac567b81d1cc7d613a1255a41033b8345f  models/asr/qwen3_asr_1.7b_bf16.safetensors
```

</details>

## Como usar

1. **LoadAudio**: 5 a 15 s da voz a clonar (`reference_voice.flac`).
2. **Drama3Generate**: o texto; deixas entre colchetes (`[sighs]`, `[laughs]`). `speakers` = `one take per line` para uma voz.
3. **Drama3Decode**: `shorten_long_pauses` ligado corta pausas longas.

## Licença

Pesquisa e uso não comercial grátis; uso comercial grátis para quem fatura menos de US$ 500 mil/ano. **Serviço hospedado (gerar voz para terceiros) exige licença separada.** Proibido imitar a voz de uma pessoa identificável sem consentimento prévio, e usar as saídas para treinar outros modelos de voz. As saídas são suas.

## Observações

- **RAM:** precisa de ~48 GB de RAM livre (~32 GB na variante W4A8, que falha mais com vozes reais). No teste foi preciso pausar outro serviço que usava 48 GB.
- O nó é mais novo que o exemplo dele: `speakers` e `shorten_long_pauses` foram adicionados.
- Sem dependências pip extras.
- A voz de referência dos testes é sintética (voz "Serena" do Qwen3-TTS, 12,8 s em PT); nenhuma voz real foi clonada. Clonar a voz de alguém exige o consentimento dessa pessoa (direito de imagem/voz e LGPD).
