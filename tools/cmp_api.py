# compara dois prompts de API casando nós por class_type (ordem de aparição); ignora ids
import json, sys
a, b = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
def group(p):
    out = {}
    for v in p.values(): out.setdefault(v['class_type'], []).append(v['inputs'])
    return out
ga, gb = group(a), group(b)
print('só no gabarito:', set(ga) - set(gb), '| só no convertido:', set(gb) - set(ga))
bad = 0
for t in ga:
    for ia, ib in zip(ga[t], gb.get(t, [])):
        wa = {x: y for x, y in ia.items() if not isinstance(y, list)}
        wb = {x: y for x, y in ib.items() if not isinstance(y, list) and x in wa}
        if wa != wb: bad += 1; print('DIF', t, '\n  gab ', wa, '\n  conv', wb)
        la = sorted(x for x, y in ia.items() if isinstance(y, list)); lb = sorted(x for x, y in ib.items() if isinstance(y, list))
        if la != lb: bad += 1; print('LINKS DIF', t, la, lb)
print(f'diferenças: {bad} de {len(a)} nós')
