<p align="center"><img src="assets/logo.svg" alt="ComfyUI Workflows" width="760"></p>

Language: **English** · [Português](README_ptBR.md)

# comfyui-workflows

**Tested** ComfyUI workflows from my homelab, each with everything needed to run it again on another
install: the workflow (UI and API), the list of components with destination folder, commit-pinned
download link and page, and an `install.sh` that installs everything on its own.

Test environment: ComfyUI v0.37.0 (`1568e6c`) in Docker (`yanwk/comfyui-boot` cu130), Python 3.13,
torch 2.13 + CUDA 13.0, **RTX 5060 Ti 16 GB**, 61 GB of RAM.

## What's here

```
workflows/<folder>/
├── README.md          components, folders, links, usage, license, test result (README_ptBR.md: Portuguese)
├── workflow.json      drag into the ComfyUI interface
├── workflow.api.json  API format (POST /prompt)
├── install.sh         installs custom nodes and models (self-contained)
└── components.json    data source for the READMEs and install.sh
lib/comfy_install.sh   install.sh functions (embedded into each one by the generator)
tools/                 generator and converters (see tools/README.md)
```

## Workflows

| Workflow | Item | Family | What it does | Status | Test time | VRAM | Download | License |
|---|---|---|---|---|---|---|---|---|
| [H3 Turbo v4 (larryvrh)](workflows/02-h3-turbo-v4/README.md) | #2 | MiniMax H3 | 4–8 step turbo LoRA with its own sampler (TaoMate alternative) | ✅ tested | 16min 48s · 15 s | 15.2 GB | 40.85 GB | MiniMax H3 Community (⚠️ territory) |
| [LTX 2.3 · image to video with audio](workflows/04-ltx23-i2v/README.md) | #4 | LTX 2.3 | Image → video with audio and speech in 2 stages (fast) | ✅ tested | 1min 51s · 4.8 s | 15.5 GB | 43.35 GB | LTX-2 Community (free < US$ 10M) |
| [H3 Character Swap (Relay 2.0)](workflows/14-h3-character-swap/README.md) | #14 | MiniMax H3 | Swaps the character in a video while keeping performance, scene and audio | ✅ tested | 14min 28s · 4 s | — | 46.33 GB | MiniMax H3 Community (⚠️ territory) |
| [LTX 2.3 · Face Swap (head swap)](workflows/17-ltx23-face-swap/README.md) | #17 | LTX 2.3 | Swaps a person's head/face in a video keeping body, clothing, motion and audio | ✅ tested | 8min 42s · 4 s | 15.5 GB | 44.71 GB | LTX-2 Community (free < US$ 10M) |
| [H3 HR Endless Sampler (Gemma 4 directs the chunks)](workflows/23-h3-hr-endless-sampler/README.md) | #23 | MiniMax H3 | Long video in chunks; a local Gemma 4 plans the production and writes each chunk's prompt | ✅ tested | 18min 38s · 6.6 s | 15.2 GB | 50.11 GB | MiniMax H3 Community (⚠️ territory) |
| [H3 Long Video (LLM-split prompt)](workflows/24-h3-long-video/README.md) | #24 | MiniMax H3 | Long videos from chained segments, with the prompt split by an LLM | ✅ tested | 11min 27s · 16 s | 15.3 GB | 44.43 GB | MiniMax H3 Community (⚠️ territory) |
| [Herrgott's H3 Infinite Continuation (v1.4)](workflows/25-h3-infinite-continuation/README.md) | #25 | MiniMax H3 | Chains FL2VA clips with safe handover and joins them without visible seams | ✅ tested | 23min 20s · 8.7 s (2 clips) | 15.3 GB | 42.47 GB | MiniMax H3 Community (⚠️ territory) |
| [H3 Realism People](workflows/59-h3-realism-people/README.md) | #59 | MiniMax H3 | Realism LoRA for people (trigger r34l1sm) | ✅ tested | 2min 14s · 5 s | 15.2 GB | 42.69 GB | MiniMax H3 Community (⚠️ territory) |
| [H3 Ref2VA · TaoMate 3 steps](workflows/h3-ref2va-taomate-3step/README.md) | base | MiniMax H3 | Video+audio from a reference image in 3 steps | ✅ tested | 8min 44s · 15 s | 15.2 GB | 42.55 GB | MiniMax H3 Community (⚠️ territory) |

Times and VRAM measured on the RTX 5060 Ti 16 GB with the parameters described in each folder's README
(time is the execution inside ComfyUI, without queue). "Download" is the workflow's total model size,
counting files shared with other workflows.

## Installing a workflow

```bash
# on the ComfyUI machine
bash workflows/<folder>/install.sh /path/to/ComfyUI

# ComfyUI in Docker (container "comfyui"): the script goes through standard input
docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < workflows/<folder>/install.sh
```

The script only runs if the folder is the **ComfyUI root** (`main.py`, `folder_paths.py`, `models/`,
`custom_nodes/`). If you point it at a subfolder (for example `models/`), it tells you where the root is.
Existing files with the right size are skipped; new downloads have their SHA-256 checked.
Gated repositories need the license accepted on Hugging Face and `HF_TOKEN` in the environment.

## Licenses

The content of this repository (scripts, `lib/`, `tools/`, READMEs and the workflows assembled here) is
under **[0BSD](LICENSE)**: use, copy and modify it freely, no credit required.
Redistributed third-party workflows (noted in the folder's README) keep their author's license, and the
**models** downloaded by the `install.sh` scripts have their own licenses, summarized in each folder (not
legal advice). Pay special attention to:

- **MiniMax H3**: prohibited in the US, EU, UK and South Korea, **including the outputs**.
  Do not use the videos in globally published projects.
- **Qwen-Image 2.1**: research and evaluation only.

## Maintenance

```bash
python3 tools/gen.py      # regenerates README.md, README_ptBR.md and install.sh from components.json
```

To add a workflow: create `workflows/<folder>/` with `workflow.json`, `workflow.api.json` and
`components.json` (copy an existing one as a template; translatable texts are `{"pt": ..., "en": ...}`)
and run the generator.

---

Independent project, not affiliated with or endorsed by Comfy Org. The logo uses original lettering; "ComfyUI" is used only to say what these workflows are for.
