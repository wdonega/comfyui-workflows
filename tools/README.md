# tools

| Arquivo | Para quê |
|---|---|
| `gen.py` | Regera `workflows/*/README.md`, `workflows/*/install.sh` e o `README.md` geral a partir dos `components.json` |
| `hfmeta.py` | Resolve `repo:caminho[@revisão]` do Hugging Face para URL fixada em commit + SHA-256 + tamanho (precisa de `huggingface_hub`) |
| `.hf_cache.json` | Cache do `hfmeta.py` (o que fixa as versões; versionado de propósito) |
| `ui2api.py` | Converte workflow da interface (nodes/links) para o formato da API, usando o `/object_info` de um ComfyUI rodando |
| `api2ui.py` | O inverso: API → interface (layout simples em colunas) |
| `cmp_api.py` | Compara dois prompts de API (usado para validar as conversões) |
| `README.head.md`, `README.tail.md` | Texto fixo do README geral (o gerador insere a tabela entre eles) |

Conversores validados com ida e volta (0 diferenças) no workflow do Character Swap (45 nós,
combos dinâmicos V3, loops) e no Ref2VA (19 nós, widgets dinâmicos do VHS). Tratam notas, Reroute,
Set/Get (KJNodes), PrimitiveNode, nós em bypass/mutados, subgraphs e widgets ligados por link.

```bash
python3 tools/ui2api.py workflow.json workflow.api.json http://localhost:8188
python3 tools/api2ui.py workflow.api.json workflow.json http://localhost:8188
python3 tools/gen.py
```
