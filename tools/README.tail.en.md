Times measured on the RTX 5060 Ti 16 GB with the parameters described in each folder's README
(execution inside ComfyUI, without queue; peak VRAM is in each folder's README). "Download" is the workflow's total model size,
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
`components.json` (copy an existing one as a template; translatable texts are `{"pt": ..., "en": ...}`; `kind` is `image`, `video` or `audio`)
and run the generator.

---

Independent project, not affiliated with or endorsed by Comfy Org. The logo uses original lettering; "ComfyUI" is used only to say what these workflows are for.
