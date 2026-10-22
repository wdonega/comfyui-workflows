# comfyui-workflows

Workflows do ComfyUI **testados** no homelab, cada um com tudo o que precisa para rodar de novo em
outra instalação: o workflow (interface e API), a lista de componentes com pasta de destino, link de
download fixado em commit e página, e um `install.sh` que instala tudo sozinho.

Ambiente dos testes: ComfyUI v0.37.0 (`1568e6c`) em Docker (`yanwk/comfyui-boot` cu130), Python 3.13,
torch 2.13 + CUDA 13.0, **RTX 5060 Ti 16 GB**, 61 GB de RAM.

## O que tem aqui

```
workflows/<pasta>/
├── README.md          componentes, pastas, links, como usar, licença, resultado do teste
├── workflow.json      arrastar na interface do ComfyUI
├── workflow.api.json  formato da API (POST /prompt)
├── install.sh         instala custom nodes e modelos (autocontido)
└── components.json    fonte de dados do README e do install.sh
lib/comfy_install.sh   funções dos install.sh (embutidas em cada um pelo gerador)
tools/                 gerador e conversores (ver tools/README.md)
```

## Workflows

| Workflow | Item | Família | O que faz | Status | Tempo do teste | VRAM | Download | Licença |
|---|---|---|---|---|---|---|---|---|
| [H3 Turbo v4 (larryvrh)](workflows/02-h3-turbo-v4/) | #2 | MiniMax H3 | LoRA turbo de 4–8 steps com sampler próprio (alternativa ao TaoMate) | ✅ testado | 16min 48s · 15 s | 15.2 GB | 40.85 GB | MiniMax H3 Community (⚠️ território) |
| [H3 Character Swap (Relay 2.0)](workflows/14-h3-character-swap/) | #14 | MiniMax H3 | Troca o personagem de um vídeo mantendo performance, cena e áudio | ✅ testado | 14min 28s · 4 s | — | 46.33 GB | MiniMax H3 Community (⚠️ território) |
| [H3 Realism People](workflows/59-h3-realism-people/) | #59 | MiniMax H3 | LoRA de realismo para pessoas (gatilho r34l1sm) | ✅ testado | 2min 14s · 5 s | 15.2 GB | 42.69 GB | MiniMax H3 Community (⚠️ território) |
| [H3 Ref2VA · TaoMate 3 steps](workflows/h3-ref2va-taomate-3step/) | base | MiniMax H3 | Vídeo+áudio a partir de imagem de referência em 3 steps | ✅ testado | 8min 44s · 15 s | 15.2 GB | 42.55 GB | MiniMax H3 Community (⚠️ território) |

Tempos e VRAM medidos na RTX 5060 Ti 16 GB com os parâmetros descritos no README de cada pasta
(o tempo é da execução no ComfyUI, sem fila). "Download" é o total de modelos do workflow, contando
arquivos compartilhados com outros.

## Instalar um workflow

```bash
# na máquina do ComfyUI
bash workflows/<pasta>/install.sh /caminho/do/ComfyUI

# ComfyUI em Docker (container "comfyui"): o script vai pela entrada padrão
docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < workflows/<pasta>/install.sh
```

O script só roda se a pasta for a **raiz do ComfyUI** (`main.py`, `folder_paths.py`, `models/`,
`custom_nodes/`). Se você apontar para uma subpasta (por exemplo `models/`), ele avisa qual é a raiz.
Arquivos existentes com o tamanho certo são pulados; downloads novos têm o SHA-256 conferido.
Repositórios gated precisam da licença aceita no Hugging Face e de `HF_TOKEN` no ambiente.

## Licenças

Cada pasta tem um resumo da licença dos modelos (não é parecer jurídico). Atenção especial:

- **MiniMax H3**: proibido nos EUA, UE, Reino Unido e Coreia do Sul, **inclusive as saídas**.
  Não use os vídeos em projetos publicados globalmente.
- **Qwen-Image 2.1**: só pesquisa e avaliação.

## Manutenção

```bash
python3 tools/gen.py      # regera os README.md e install.sh a partir dos components.json
```

Para adicionar um workflow: crie `workflows/<pasta>/` com `workflow.json`, `workflow.api.json` e
`components.json` (copie um existente como modelo) e rode o gerador.
