# tools

[comfyui-workflows](../README.md) › **tools**

| File | Purpose |
|---|---|
| `gen.py` | Regenerates `workflows/*/README.md`, `README_ptBR.md`, `install.sh` and the root READMEs from `components.json` |
| `hfmeta.py` | Resolves Hugging Face `repo:path[@revision]` into a commit-pinned URL + SHA-256 + size (needs `huggingface_hub`) |
| `.hf_cache.json` | `hfmeta.py` cache (it is what pins the versions; versioned on purpose) |
| `ui2api.py` | Converts a UI workflow (nodes/links) to API format, using the `/object_info` of a running ComfyUI |
| `api2ui.py` | The reverse: API → UI (simple column layout) |
| `cmp_api.py` | Compares two API prompts (used to validate the conversions) |
| `make_logo.py` | Generates `assets/logo.svg` (original block lettering, magenta/white with a thin black outline, transparent background) |
| `README.head.*.md`, `README.tail.*.md` | Fixed text of the root READMEs per language (the generator inserts the table between them) |

The converters are validated round-trip (0 differences) on the Character Swap workflow (45 nodes,
V3 dynamic combos, loops), on Ref2VA (19 nodes, VHS dynamic widgets) and on the LTX 2.3 template
(subgraph with promoted widgets) and Bernini-R (nested subgraphs, `proxyWidgets` format). They handle notes, Reroute, Set/Get (KJNodes), PrimitiveNode,
bypassed/muted nodes, subgraphs and link-driven widgets.

```bash
python3 tools/ui2api.py workflow.json workflow.api.json http://localhost:8188
python3 tools/api2ui.py workflow.api.json workflow.json http://localhost:8188
python3 tools/gen.py
```
