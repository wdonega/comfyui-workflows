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
