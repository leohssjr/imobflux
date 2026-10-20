#!/usr/bin/env python3
"""Kit ImobFlux (conceito B, Casa F): símbolo, versão pequena, versão invertida, lockups.
O wordmark usa a Poppins Bold (OFL) convertida em curvas; nenhum <text> nos arquivos finais."""
import os
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

OUT = sys.argv[1] if len(sys.argv) > 1 else 'kit/svg'
os.makedirs(OUT, exist_ok=True)

TEAL = '#0E7C7B'
NAVY = '#0F1B2D'
MINT = '#7FD6D3'
WHITE = '#FFFFFF'

FONT = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
font = TTFont(FONT)
gs = font.getGlyphSet()
cmap = font.getBestCmap()
upm = font['head'].unitsPerEm
hmtx = font['hmtx']


def fmt(v):
    v = round(v, 2)
    return ('%.2f' % v).rstrip('0').rstrip('.')


# ---------------------------------------------------------------- símbolo
# Pontos no canvas 256; bbox da forma: x 56..200, y 32..224 (centrada).
MAIN = [(128, 32), (200, 104), (200, 120), (92, 120), (92, 206), (120, 206), (120, 182),
        (158, 182), (158, 160), (120, 160), (120, 142), (200, 142), (200, 224), (56, 224), (56, 104)]
# Versão invertida (branco sobre escuro): F ~2 unidades mais grosso para compensar a irradiação
REV = [(128, 32), (200, 104), (200, 118), (90, 118), (90, 208), (122, 208), (122, 184),
       (160, 184), (160, 158), (122, 158), (122, 144), (200, 144), (200, 224), (56, 224), (56, 104)]
# Versão pequena (16-32 px): F maior e mais grosso, vãos amplos (>= 24 unidades)
SMALL = [(128, 28), (200, 100), (200, 116), (84, 116), (84, 212), (122, 212), (122, 196),
         (166, 196), (166, 168), (122, 168), (122, 144), (200, 144), (200, 228), (56, 228), (56, 100)]


def poly(pts, dx=0, dy=0):
    return 'M' + 'L'.join(f'{fmt(x+dx)} {fmt(y+dy)}' for x, y in pts) + 'Z'


def symbol_svg(pts, color, name):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="ImobFlux">\n'
           f'<title>ImobFlux</title>\n<path d="{poly(pts)}" fill="{color}"/>\n</svg>\n')
    open(f'{OUT}/{name}', 'w').write(svg)


# ---------------------------------------------------------------- wordmark
WORD = 'imobflux'
FS = 112
TRACK = -1.5


def letters(text, size, x0, base_y, tracking):
    s = size / upm
    x = x0
    out = []
    for ch in text:
        name = cmap[ord(ch)]
        pen = SVGPathPen(gs, ntos=fmt)
        gs[name].draw(TransformPen(pen, (s, 0, 0, -s, x, base_y)))
        out.append(pen.getCommands())
        x += hmtx[name][0] * s + tracking
    return out, x - tracking


def gb(ch):
    bp = BoundsPen(gs)
    gs[cmap[ord(ch)]].draw(bp)
    return bp.bounds


def xheight(size):
    return gb('x')[3] * size / upm


def asc(size):
    return gb('l')[3] * size / upm


def word_paths(x0, base_y, c_imob, c_flux):
    ds, xend = letters(WORD, FS, x0, base_y, TRACK)
    a = ' '.join(ds[:4])
    b = ' '.join(ds[4:])
    return (f'<path d="{a}" fill="{c_imob}"/>\n<path d="{b}" fill="{c_flux}"/>', xend)


def wordmark_extent():
    """Largura do wordmark em px (para centrar) e limites verticais relativos à linha de base."""
    ds, xend = letters(WORD, FS, 0, 0, TRACK)
    xs = gb('i')[0] * FS / upm
    return xend, xs


# ---------------------------------------------------------------- lockups
def horizontal(pts, c_sym, c_imob, c_flux, name):
    # símbolo na origem: bbox 144 x 192 (desloca -56, -32)
    sym = poly(pts, -56, -32)
    H = 192
    xh = xheight(FS)
    base_y = H / 2 + xh / 2
    gap = 44
    words, xend = word_paths(144 + gap, base_y, c_imob, c_flux)
    # recorte justo: do lado esquerdo do símbolo ao fim do x; altura do símbolo
    width = round(xend)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {H}" role="img" aria-label="ImobFlux">\n'
           f'<title>ImobFlux</title>\n<path d="{sym}" fill="{c_sym}"/>\n{words}\n</svg>\n')
    open(f'{OUT}/{name}', 'w').write(svg)
    return width, H


def stacked(pts, c_sym, c_imob, c_flux, name):
    wm_w, xs = wordmark_extent()
    W = round(wm_w)
    H_sym = 192
    gap = 40
    base_y = H_sym + gap + asc(FS)          # ascendentes encostam abaixo do respiro
    sym = poly(pts, (W - 144) / 2 - 56, -32)
    words, _ = word_paths(0, base_y, c_imob, c_flux)
    H = round(base_y + 24)                   # espaço para descendentes (nenhum em 'imobflux'); margem mínima
    H = round(base_y)                        # sem descendentes: termina na linha de base
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="ImobFlux">\n'
           f'<title>ImobFlux</title>\n<path d="{sym}" fill="{c_sym}"/>\n{words}\n</svg>\n')
    open(f'{OUT}/{name}', 'w').write(svg)
    return W, H


def wordmark(c_imob, c_flux, name):
    wm_w, xs = wordmark_extent()
    a, d = asc(FS), 0
    base_y = a
    words, xend = word_paths(0, base_y, c_imob, c_flux)
    W, H = round(xend), round(a)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="ImobFlux">\n'
           f'<title>ImobFlux</title>\n{words}\n</svg>\n')
    open(f'{OUT}/{name}', 'w').write(svg)
    return W, H


def lum(h):
    h = h.lstrip('#')
    r, g, b = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def cmyk(h):
    h = h.lstrip('#')
    r, g, b = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    k = 1 - max(r, g, b)
    if k >= 1:
        return 0, 0, 0, 100
    return tuple(round(v * 100) for v in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))


if __name__ == '__main__':
    symbol_svg(MAIN, TEAL, 'imobflux-symbol.svg')
    symbol_svg(SMALL, TEAL, 'imobflux-symbol-small.svg')
    symbol_svg(REV, MINT, 'imobflux-symbol-reversed.svg')
    print('horizontal', horizontal(MAIN, TEAL, NAVY, TEAL, 'imobflux-horizontal.svg'))
    print('horizontal-rev', horizontal(REV, MINT, WHITE, MINT, 'imobflux-horizontal-reversed.svg'))
    print('stacked', stacked(MAIN, TEAL, NAVY, TEAL, 'imobflux-stacked.svg'))
    print('stacked-rev', stacked(REV, MINT, WHITE, MINT, 'imobflux-stacked-reversed.svg'))
    print('wordmark', wordmark(NAVY, TEAL, 'imobflux-wordmark.svg'))
    print('wordmark-rev', wordmark(WHITE, MINT, 'imobflux-wordmark-reversed.svg'))
    for n, c in (('teal', TEAL), ('navy', NAVY), ('mint', MINT)):
        print(n, c, 'CMYK', cmyk(c), 'vs branco %.2f' % ratio(c, WHITE), 'vs navy %.2f' % ratio(c, NAVY))
    print('branco vs navy %.2f' % ratio(WHITE, NAVY))
