# Qwen3-TTS · built-in voices and cloning

[comfyui-workflows](../../README.md) › **Qwen3-TTS · built-in voices and cloning**

Two workflows for the **ComfyUI-Qwen-TTS** node: `01-custom-voice` speaks the text with one of the 9 built-in voices (Serena, Ryan, Eric…); `02-voice-clone` clones a reference from its audio and transcript. The node also has **VoiceDesign** (voice from a description) and multi-speaker dialogue.

| | |
|---|---|
| Status | ✅ tested |
| Family | Qwen3-TTS |
| License | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Total download | 0 MB |
| Test | "Serena" voice in PT (12.8 s), transcribed word for word; cloning that voice with the PT sentence (7.5 s, 81 s including the base model download). The PT sentence was transcribed back by Qwen3-ASR and came out right (only "ComfyUI" turns into something like "Confiuí", normal for an English name). |
| Time | **1min 29s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Peak VRAM | 8439 MiB |

## Files in this folder

| File | What it is |
|---|---|
| `01-custom-voice.json` | Built-in voice: drag into the UI |
| `01-custom-voice.api.json` | Built-in voice (API) |
| `02-voice-clone.json` | Cloning: drag into the UI |
| `02-voice-clone.api.json` | Cloning (API) |
| `install.sh` | Installs custom nodes and downloads the models into the right folders |
| `components.json` | Source of this README and of install.sh |

## Installation

```bash
# on the ComfyUI machine (the script checks that the folder is the ComfyUI root)
bash install.sh /path/to/ComfyUI

# ComfyUI in Docker (container "comfyui")
docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh
```

Files that already exist with the right size are skipped. New downloads have their SHA-256 checked (`VERIFY_EXISTING=1` also checks the existing ones).

## Custom nodes

| Node | Tested version | Page |
|---|---|---|
| ComfyUI-Qwen-TTS | `a1328c8` | https://github.com/flybirdxx/ComfyUI-Qwen-TTS |

## Models

| Folder (`models/…`) | File | Role | Size | Download | Page |
|---|---|---|---|---|---|

<details><summary>SHA-256</summary>

```
```

</details>

## How to use

1. The models download themselves on first use to `models/qwen-tts/` (`Qwen3-TTS-12Hz-1.7B-CustomVoice`, `-Base` and the tokenizer, ~4.5 GB each). To download ahead of time: `python3 download_models.py` in the node folder.
2. Pip dependencies from `requirements.txt` **without** `onnxruntime-openvino` (`PIP_USER=true python3.13 -m pip install --no-deps` só do que faltar; veja `requirements.txt` do nó. Não instalar `onnxruntime-openvino` se já houver `onnxruntime`.).
3. `attention` = `sdpa` if SageAttention is not installed; `language` = `Portuguese`.

## License

Apache-2.0: free personal and commercial use, with no revenue or territory limits; just keep the license notices when redistributing the weights. The outputs are yours.

## Notes

- The node's original example clones a real person's voice (`雷军.mp3`); here it was replaced with the synthetic voice.
- The node repository declares no license.
- Cloning someone's voice requires that person's consent.
