"""Converte um workflow do ComfyUI no formato da interface (nodes/links) para o formato da API.

Uso: python3 ui2api.py workflow.json saida.api.json [http://localhost:8188]
Usa /object_info do servidor para mapear widgets_values -> nomes de inputs.
Suporta: notas (ignoradas), Reroute, PrimitiveNode, SetNode/GetNode (KJNodes),
nós bypassados (mode 4) e mutados (mode 2), subgraphs (definitions.subgraphs).
"""
import json
import sys
import urllib.request

SKIP = {"Note", "MarkdownNote", "PrimitiveNode", "Reroute", "SetNode", "GetNode"}
LINK_TYPES_WIDGET = {"INT", "FLOAT", "STRING", "BOOLEAN", "COMBO"}
CONTROL_VALUES = ("fixed", "increment", "decrement", "randomize")


def load_object_info(server):
    with urllib.request.urlopen(server + "/object_info") as r:
        return json.load(r)


def is_widget(spec):
    t = spec[0]
    opts = spec[1] if len(spec) > 1 and isinstance(spec[1], dict) else {}
    if isinstance(t, list) or opts.get("widgetType"):
        return True
    # tipos compostos como "FLOAT,INT" viram widget se todas as partes forem tipos de widget
    return isinstance(t, str) and (all(p in LINK_TYPES_WIDGET for p in t.split(",")) or (t.startswith("COMFY_") and "COMBO" in t))


def section_widgets(input_spec, order=None, prefix=""):
    """Lista ordenada de (nome_completo, spec) dos widgets de um bloco required/optional."""
    out = []
    for section in ("required", "optional"):
        specs = input_spec.get(section, {})
        names = (order or {}).get(section) or list(specs)
        for name in names:
            spec = specs.get(name)
            if spec is not None and is_widget(spec):
                out.append((prefix + name, spec))
    return out


def fits(v, spec):
    """O valor salvo combina com o tipo do widget? (nós com JS próprio às vezes omitem widgets)"""
    t = spec[0]
    if isinstance(t, str) and "," in t:
        return any(fits(v, [p] + list(spec[1:])) for p in t.split(","))
    if t == "BOOLEAN":
        return isinstance(v, bool)
    if t == "INT":
        return isinstance(v, int) and not isinstance(v, bool)
    if t == "FLOAT":
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    if t == "STRING":
        return isinstance(v, str)
    options = t if isinstance(t, list) else (spec[1].get("options") if len(spec) > 1 and isinstance(spec[1], dict) else None)
    if t == "COMBO" or isinstance(t, list):
        return not options or v in options or isinstance(v, str)
    return True


def consume_widgets(widgets, vals, inputs, pos=0, linked=()):
    """Atribui vals[pos:] aos widgets; combos dinâmicos (V3) expandem os subcampos da opção escolhida.
    Widgets conectados por link ocupam a posição mesmo com valor de tipo errado."""
    for name, spec in widgets:
        if pos >= len(vals):
            break
        v = vals[pos]
        if name not in linked and not fits(v, spec):
            default = spec[1].get("default") if len(spec) > 1 and isinstance(spec[1], dict) else None
            if default is not None:
                inputs[name] = default
            continue
        inputs[name] = v
        pos += 1
        if has_control(name.rsplit(".", 1)[-1], spec) and pos < len(vals) and vals[pos] in CONTROL_VALUES:
            pos += 1
        if spec[0] == "COMFY_DYNAMICCOMBO_V3":
            for opt in spec[1].get("options", []):
                if opt.get("key") == v:
                    pos = consume_widgets(section_widgets(opt.get("inputs", {}), prefix=name + "."), vals, inputs, pos, linked)
                    break
    return pos


def has_control(name, spec):
    opts = spec[1] if len(spec) > 1 and isinstance(spec[1], dict) else {}
    if opts.get("control_after_generate"):
        return True
    return spec[0] == "INT" and name in ("seed", "noise_seed") and "control_after_generate" not in opts


def flatten(wf):
    """Expande subgraphs em nós/links planos. Retorna (nodes, links) com ids string."""
    subgraphs = {s["id"]: s for s in (wf.get("definitions") or {}).get("subgraphs") or []}
    nodes, links = {}, {}

    def add_graph(g, prefix, link_prefix):
        for n in g["nodes"]:
            nid = prefix + str(n["id"])
            n = dict(n, id=nid)
            nodes[nid] = n
        for l in g.get("links", []):
            if isinstance(l, dict):
                lid, o, os_, t, ts, typ = l["id"], l["origin_id"], l["origin_slot"], l["target_id"], l["target_slot"], l.get("type")
            else:
                lid, o, os_, t, ts, typ = l[:6]
            links[link_prefix + str(lid)] = [prefix + str(o), os_, prefix + str(t), ts, typ]
        # links dos nós deste nível também usam o prefixo
        for n in g["nodes"]:
            nn = nodes[prefix + str(n["id"])]
            nn["inputs"] = [dict(i, link=None if i.get("link") is None else link_prefix + str(i["link"])) for i in n.get("inputs", [])]
            nn["outputs"] = [dict(o, links=[link_prefix + str(x) for x in (o.get("links") or [])]) for o in n.get("outputs", [])]

    add_graph(wf, "", "")
    # expande subgraphs (um nível ou aninhado)
    changed = True
    while changed:
        changed = False
        for nid, n in list(nodes.items()):
            sg = subgraphs.get(n["type"])
            if not sg:
                continue
            changed = True
            prefix = nid + ":"
            add_graph(sg, prefix, prefix)
            # nós de entrada/saída do subgraph: -10 = input, -20 = output.
            # A entrada é casada pelo NOME (a lista inputs do nó externo pode estar desatualizada);
            # sem link, o valor vem de widgets_values na ordem das entradas do subgraph que são widgets.
            sg_inputs = sg.get("inputs", [])
            outer_by_name = {i["name"]: i for i in n.get("inputs", [])}
            wv = n.get("widgets_values") or []
            widget_pos, k = {}, 0
            for idx, si in enumerate(sg_inputs):
                if any(t in LINK_TYPES_WIDGET or t == "COMBO" for t in str(si.get("type", "")).split(",")):
                    widget_pos[idx] = k
                    k += 1
            for lid, (o, os_, t, ts, typ) in list(links.items()):
                if o == prefix + "-10":  # vem de uma entrada do subgraph
                    name = sg_inputs[os_]["name"] if os_ < len(sg_inputs) else None
                    ext = (outer_by_name.get(name) or {}).get("link")
                    if ext is not None and ext in links:
                        links[lid] = [links[ext][0], links[ext][1], t, ts, typ]
                    else:
                        wi = widget_pos.get(os_)
                        links[lid] = ["__const__", wv[wi] if wi is not None and wi < len(wv) else None, t, ts, typ]
            for lid, (o, os_, t, ts, typ) in list(links.items()):
                if t == nid:  # links de fora que entram no nó-subgraph: já tratados acima
                    continue
                if o == nid:  # saída do nó-subgraph -> achar quem alimenta a saída interna
                    inner = [l for l in links.values() if l[2] == prefix + "-20" and l[3] == os_]
                    if inner:
                        links[lid] = [inner[0][0], inner[0][1], t, ts, typ]
            del nodes[nid]
    return nodes, links


def convert(wf, oi):
    nodes, links = flatten(wf)
    setters = {}
    for nid, n in nodes.items():
        if n["type"] == "SetNode":
            name = (n.get("widgets_values") or [""])[0]
            lk = n["inputs"][0].get("link") if n.get("inputs") else None
            setters[name] = lk

    def resolve(link_id, depth=0):
        """Retorna [node_id, slot] da origem real, ou ('const', valor)."""
        o, os_, *_ = links[link_id]
        if o == "__const__":
            return ("const", os_)
        src = nodes.get(o)
        if src is None:
            return None
        t = src["type"]
        if t == "Reroute":
            return resolve(src["inputs"][0]["link"], depth + 1)
        if t == "GetNode":
            name = (src.get("widgets_values") or [""])[0]
            return resolve(setters[name], depth + 1)
        if t == "PrimitiveNode":
            return ("const", (src.get("widgets_values") or [None])[0])
        if src.get("mode") == 4:  # bypass: repassa a primeira entrada de mesmo tipo
            out_type = src["outputs"][os_]["type"]
            for i in src.get("inputs", []):
                if i.get("type") == out_type and i.get("link") is not None:
                    return resolve(i["link"], depth + 1)
            return None
        return [o, os_]

    api = {}
    for nid, n in nodes.items():
        t = n["type"]
        if t in SKIP or n.get("mode") in (2, 4) or nid.endswith(":-10") or nid.endswith(":-20"):
            continue
        info = oi.get(t)
        if info is None:
            raise SystemExit(f"nó desconhecido no servidor: {t} (id {nid})")
        inputs = {}
        wv = n.get("widgets_values")
        if isinstance(wv, dict):
            inputs.update({k: v for k, v in wv.items() if k != "videopreview"})
        elif wv:
            linked = {i["name"] for i in n.get("inputs", []) if i.get("link") is not None}
            consume_widgets(section_widgets(info["input"], info.get("input_order")), list(wv), inputs, linked=linked)
        for inp in n.get("inputs", []):
            lk = inp.get("link")
            if lk is None or lk not in links:
                continue
            r = resolve(lk)
            if r is None:
                continue
            if isinstance(r, tuple):
                inputs[inp["name"]] = r[1]
            else:
                inputs[inp["name"]] = r
        api[nid] = {"class_type": t, "inputs": inputs, "_meta": {"title": n.get("title", t)}}
    return api


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    server = sys.argv[3] if len(sys.argv) > 3 else "http://localhost:8188"
    wf = json.load(open(src))
    api = convert(wf, load_object_info(server))
    json.dump(api, open(dst, "w"), indent=1, ensure_ascii=False)
    print(f"{len(api)} nós -> {dst}")
