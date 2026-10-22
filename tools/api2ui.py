"""Converte um prompt no formato da API do ComfyUI para um workflow da interface (nodes/links).

Uso: python3 api2ui.py prompt.api.json saida.json [http://localhost:8188]
Layout simples: colunas por profundidade no grafo. Os valores de widget seguem a ordem
de /object_info, incluindo os subcampos dos combos dinâmicos (V3) e o
"control_after_generate" das seeds (gravado como "fixed").
"""
import json
import sys
import urllib.request

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from ui2api import has_control, section_widgets  # noqa: E402


def widget_values(inputs, widgets):
    vals = []
    for name, spec in widgets:
        if name not in inputs or isinstance(inputs[name], list):
            default = spec[1].get("default") if len(spec) > 1 and isinstance(spec[1], dict) else None
            v = default if default is not None else 0
        else:
            v = inputs[name]
        vals.append(v)
        if has_control(name.rsplit(".", 1)[-1], spec):
            vals.append("fixed")
        if spec[0] == "COMFY_DYNAMICCOMBO_V3":
            for opt in spec[1].get("options", []):
                if opt.get("key") == v:
                    vals += widget_values(inputs, section_widgets(opt.get("inputs", {}), prefix=name + "."))
                    break
    return vals


def convert(api, oi):
    ids = {k: i + 1 for i, k in enumerate(api)}
    # profundidade = maior distância de um nó sem entradas
    depth = {}

    def d(k, seen=()):
        if k in depth:
            return depth[k]
        parents = [v[0] for v in api[k]["inputs"].values() if isinstance(v, list) and v and v[0] in api and v[0] not in seen]
        depth[k] = 0 if not parents else 1 + max(d(p, seen + (k,)) for p in parents)
        return depth[k]

    for k in api:
        d(k)
    rows = {}
    nodes, links = [], []
    out_links = {}
    for k, v in api.items():
        info = oi[v["class_type"]]
        widgets = section_widgets(info["input"], info.get("input_order"))
        widget_names = {n for n, _ in widgets}
        col = depth[k]
        row = rows.get(col, 0)
        rows[col] = row + 1
        node = {
            "id": ids[k], "type": v["class_type"], "pos": [col * 420, row * 260], "size": [380, 220],
            "flags": {}, "order": 0, "mode": 0, "inputs": [], "outputs": [],
            "properties": {"Node name for S&R": v["class_type"]},
            # nós VHS criam widgets dinâmicos no JS e salvam como dicionário
            "widgets_values": ({n: x for n, x in v["inputs"].items() if not isinstance(x, list)}
                               if v["class_type"].startswith("VHS_") else widget_values(v["inputs"], widgets)),
        }
        if v.get("_meta", {}).get("title") not in (None, v["class_type"]):
            node["title"] = v["_meta"]["title"]
        for name, val in v["inputs"].items():
            if not (isinstance(val, list) and len(val) == 2 and val[0] in api):
                continue
            lid = len(links) + 1
            src_type = oi[api[val[0]]["class_type"]]["output"][val[1]]
            links.append([lid, ids[val[0]], val[1], ids[k], len(node["inputs"]), src_type])
            entry = {"name": name, "type": src_type, "link": lid}
            if name in widget_names:
                entry["widget"] = {"name": name}
            node["inputs"].append(entry)
            out_links.setdefault((val[0], val[1]), []).append(lid)
        for slot, (otype, oname) in enumerate(zip(info["output"], info.get("output_name", info["output"]))):
            node["outputs"].append({"name": oname, "type": otype, "slot_index": slot, "links": []})
        nodes.append((k, node))
    for k, node in nodes:
        for o in node["outputs"]:
            o["links"] = out_links.get((k, o["slot_index"]), [])
    for i, (_, node) in enumerate(sorted(nodes, key=lambda kn: depth[kn[0]])):
        node["order"] = i
    return {
        "last_node_id": len(nodes), "last_link_id": len(links),
        "nodes": [n for _, n in nodes], "links": links, "groups": [], "config": {}, "extra": {}, "version": 0.4,
    }


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    server = sys.argv[3] if len(sys.argv) > 3 else "http://localhost:8188"
    with urllib.request.urlopen(server + "/object_info") as r:
        oi = json.load(r)
    wf = convert(json.load(open(src)), oi)
    json.dump(wf, open(dst, "w"), indent=1, ensure_ascii=False)
    print(f"{len(wf['nodes'])} nós -> {dst}")
