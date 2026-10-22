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
