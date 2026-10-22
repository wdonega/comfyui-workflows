"""Gera assets/logo.svg: wordmark "COMFYUI WORKFLOWS" em blocos inclinados (glifos próprios).

Uso: python3 tools/make_logo.py
Cada letra é um conjunto de retângulos numa grade de 8 unidades de altura (traço de 2);
o grupo inteiro recebe um skew para o efeito itálico.
"""
from pathlib import Path

GLYPHS = {  # largura, [(x, y, w, h), ...]
    "C": (6, [(0, 0, 6, 2), (0, 0, 2, 8), (0, 6, 6, 2)]),
    "O": (6, [(0, 0, 6, 2), (0, 6, 6, 2), (0, 0, 2, 8), (4, 0, 2, 8)]),
    "M": (8, [(0, 0, 2, 8), (6, 0, 2, 8), (0, 0, 8, 2), (3, 0, 2, 5)]),
    "F": (6, [(0, 0, 2, 8), (0, 0, 6, 2), (0, 3, 5, 2)]),
    "Y": (6, [(0, 0, 2, 5), (4, 0, 2, 5), (0, 3, 6, 2), (2, 3, 2, 5)]),
    "U": (6, [(0, 0, 2, 8), (4, 0, 2, 8), (0, 6, 6, 2)]),
    "I": (2, [(0, 0, 2, 8)]),
    "W": (8, [(0, 0, 2, 8), (6, 0, 2, 8), (0, 6, 8, 2), (3, 3, 2, 5)]),
    "R": (6, [(0, 0, 2, 8), (0, 0, 6, 2), (4, 0, 2, 5), (0, 3, 6, 2), (3, 5, 2, 3)]),
    "K": (6, [(0, 0, 2, 8), (0, 3, 3.5, 2), (4, 0, 2, 2.5), (3, 1.5, 2, 2.5), (3, 4, 2, 2.5), (4, 5.5, 2, 2.5)]),
    "L": (6, [(0, 0, 2, 8), (0, 6, 6, 2)]),
    "S": (6, [(0, 0, 6, 2), (0, 0, 2, 5), (0, 3, 6, 2), (4, 3, 2, 5), (0, 6, 6, 2)]),
}

U = 7            # px por unidade da grade
GAP = 1.5        # espaço entre letras (unidades)
SPACE = 4        # espaço entre palavras (unidades)
SKEW = -14       # graus
PAD_X, PAD_Y = 40, 34
YELLOW, WHITE, BG = "#F2FF59", "#F5F5F0", "#141414"


def word(text, x0, color):
    rects, x = [], x0
    for ch in text:
        w, parts = GLYPHS[ch]
        for (rx, ry, rw, rh) in parts:
            rects.append(f'<rect x="{(x + rx) * U:.1f}" y="{ry * U:.1f}" width="{rw * U:.1f}" height="{rh * U:.1f}" rx="{0.35 * U:.1f}" fill="{color}"/>')
        x += w + GAP
    return rects, x - GAP


def main():
    a, end_a = word("COMFYUI", 0, YELLOW)
    b, end_b = word("WORKFLOWS", end_a + SPACE, WHITE)
    text_w, text_h = end_b * U, 8 * U
    slant = text_h * 0.25  # deslocamento horizontal do skew de -14° (tan 14° ≈ 0.25)
    width, height = int(text_w + slant + 2 * PAD_X), int(text_h + 2 * PAD_Y)
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="ComfyUI Workflows">',
        "<title>ComfyUI Workflows</title>",
        f'<rect width="{width}" height="{height}" rx="18" fill="{BG}"/>',
        f'<g transform="translate({PAD_X + slant:.1f} {PAD_Y}) skewX({SKEW})">',
        *a, *b,
        "</g>",
        "</svg>",
    ]
    out = Path(__file__).resolve().parent.parent / "assets" / "logo.svg"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(svg) + "\n")
    print(f"{out} ({width}x{height})")


if __name__ == "__main__":
    main()
