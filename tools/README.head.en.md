# comfyui-workflows

**Tested** ComfyUI workflows from my homelab, each with everything needed to run it again on another
install: the workflow (UI and API), the list of components with destination folder, commit-pinned
download link and page, and an `install.sh` that installs everything on its own.

Test environment: ComfyUI v0.37.0 (`1568e6c`) in Docker (`yanwk/comfyui-boot` cu130), Python 3.13,
torch 2.13 + CUDA 13.0, **RTX 5060 Ti 16 GB**, 61 GB of RAM. The GPU was dedicated to ComfyUI during the tests:
nothing else was running on it.

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
