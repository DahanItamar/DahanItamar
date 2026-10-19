"""Replace the illustrations on the project cards, keeping every other element byte-for-byte.

The art sits in the right column (x 304-398, y 30-146), clear of the text, which ends near x 290.
Dark colours are written here; light cards get the same art through the light palette below,
which matches light_theme() in build_component_readme.py.

Run: python3 scripts/build_card_art.py
"""

import re
from pathlib import Path

CARDS = Path(__file__).resolve().parents[1] / "assets" / "components"

MUTED, GRID, ACCENT, SOFT, ERROR, ERROR_SOFT, TEXT = "#a5b0b9", "#39464d", "#c6f27f", "#263220", "#ffaaaa", "#291d1b", "#f0f2eb"
LIGHT = {"#c6f27f": "#456c17", "#f0f2eb": "#1f2328", "#a5b0b9": "#59636e", "#39464d": "#d1d9e0",
         "#263220": "#f0f6e5", "#291d1b": "#fff1f1", "#ffaaaa": "#c54b4b"}


def docknest():
    """Servers are captured into an encrypted, verified package, then restored into an isolated copy."""
    art = ""
    for y in (36, 52, 68):  # three source containers
        art += (f'<rect x="306" y="{y}" width="36" height="12" rx="2" fill="none" stroke="{MUTED}"/>'
                f'<circle cx="312" cy="{y + 6}" r="1.4" fill="{MUTED}"/><path d="M318 {y + 6}H336" stroke="{MUTED}"/>')
    # capture: containers -> package
    art += f'<path d="M346 58H360" stroke="{MUTED}" stroke-dasharray="2 3"/><path d="M357 54.5L361 58L357 61.5" fill="none" stroke="{MUTED}"/>'
    # encrypted package: shield with a check
    art += (f'<path d="M379 38L395 44V60C395 71 388 78 379 82C370 78 363 71 363 60V44Z" fill="{SOFT}" stroke="{ACCENT}"/>'
            f'<path d="M372 60L377 65L386 54" fill="none" stroke="{ACCENT}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
    # restore: package -> isolated private copy
    art += (f'<path d="M379 86V104H350" fill="none" stroke="{MUTED}" stroke-dasharray="2 3"/>'
            f'<path d="M353.5 100.5L350 104L353.5 107.5" fill="none" stroke="{MUTED}"/>'
            f'<rect x="306" y="92" width="40" height="26" rx="3" fill="none" stroke="{ACCENT}" stroke-dasharray="3 2"/>'
            f'<rect x="313" y="99" width="26" height="12" rx="2" fill="none" stroke="{ACCENT}"/>'
            f'<circle cx="319" cy="105" r="1.4" fill="{ACCENT}"/><path d="M325 105H334" stroke="{ACCENT}"/>')
    return art


def slotline():
    """A calendar where one booking holds a slot and an overlapping one is refused."""
    x0, y0, w, h = 306, 40, 90, 82
    art = f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="4" fill="none" stroke="{MUTED}"/>'
    art += f'<path d="M{x0} {y0 + 14}H{x0 + w}" stroke="{MUTED}"/>'
    for i in range(1, 4):  # day columns
        x = x0 + i * w / 4
        art += f'<path d="M{x:g} {y0 + 14}V{y0 + h}" stroke="{GRID}"/>'
    for j in range(1, 4):  # hour rows
        y = y0 + 14 + j * (h - 14) / 4
        art += f'<path d="M{x0} {y:g}H{x0 + w}" stroke="{GRID}"/>'
    for x in (322, 380):  # binding rings
        art += f'<path d="M{x} {y0 - 4}V{y0 + 5}" stroke="{MUTED}" stroke-linecap="round"/>'
    art += f'<rect x="{x0 + 3}" y="{y0 + 17}" width="{w / 4 - 6:g}" height="11" rx="2" fill="none" stroke="{MUTED}"/>'
    art += f'<rect x="{x0 + w * 3 / 4 + 3:g}" y="{y0 + 51}" width="{w / 4 - 6:g}" height="11" rx="2" fill="none" stroke="{MUTED}"/>'
    # the held booking
    art += f'<rect x="{x0 + w / 4 + 3:g}" y="{y0 + 34}" width="{w / 2 - 6:g}" height="11" rx="2" fill="{SOFT}" stroke="{ACCENT}"/>'
    # the refused overlap
    rx, ry, rw = x0 + w / 2 + 3, y0 + 40, w / 4 + 8
    art += (f'<rect x="{rx:g}" y="{ry}" width="{rw:g}" height="11" rx="2" fill="{ERROR_SOFT}" stroke="{ERROR}" stroke-dasharray="3 2"/>'
            f'<circle cx="{rx + rw:g}" cy="{ry}" r="5" fill="{ERROR_SOFT}" stroke="{ERROR}"/>'
            f'<path d="M{rx + rw - 2:g} {ry - 2}L{rx + rw + 2:g} {ry + 2}M{rx + rw + 2:g} {ry - 2}L{rx + rw - 2:g} {ry + 2}" '
            f'stroke="{ERROR}" stroke-linecap="round"/>')
    return art


def winnow():
    """Many complaints pass through a sieve; one idea comes out, linked to its sources."""
    art = ""
    for x, y, w in ((306, 40, 28), (338, 36, 26), (368, 42, 28)):  # complaint bubbles
        art += (f'<path d="M{x + 3} {y}H{x + w - 3}Q{x + w} {y} {x + w} {y + 3}V{y + 10}Q{x + w} {y + 13} {x + w - 3} {y + 13}'
                f'H{x + 9}L{x + 5} {y + 17}V{y + 13}H{x + 3}Q{x} {y + 13} {x} {y + 10}V{y + 3}Q{x} {y} {x + 3} {y}Z" fill="none" stroke="{MUTED}"/>'
                f'<path d="M{x + 6} {y + 6.5}H{x + w - 6}" stroke="{MUTED}"/>')
    # sieve
    art += f'<path d="M308 66H396L362 94H342Z" fill="none" stroke="{MUTED}"/><path d="M316 73H388" stroke="{GRID}" stroke-dasharray="3 3"/><path d="M325 81H379" stroke="{GRID}" stroke-dasharray="3 3"/>'
    for cx, cy in ((330, 61), (352, 62), (374, 61)):  # falling fragments
        art += f'<circle cx="{cx}" cy="{cy}" r="1.6" fill="{MUTED}"/>'
    art += f'<path d="M352 94V100" stroke="{ACCENT}"/>'
    # the idea, with links back to sources
    art += (f'<rect x="318" y="100" width="68" height="22" rx="4" fill="{SOFT}" stroke="{ACCENT}"/>'
            f'<circle cx="331" cy="111" r="4" fill="{ACCENT}"/><path d="M340 107H376M340 115H364" stroke="{ACCENT}"/>')
    return art


def houserules():
    """A playing card, a casino chip and a die."""
    art = (f'<g transform="rotate(-8 330 76)"><rect x="310" y="44" width="42" height="60" rx="4" fill="{SOFT}" stroke="{ACCENT}"/>'
           f'<text x="316" y="58" fill="{ACCENT}" font-size="11" font-weight="650">A</text>'
           f'<path d="M331 64C331 64 322 71 322 77C322 81 326 83 329 81L327 87H335L333 81C336 83 340 81 340 77C340 71 331 64 331 64Z" fill="{ACCENT}"/></g>')
    # chip
    art += (f'<circle cx="378" cy="54" r="17" fill="none" stroke="{MUTED}"/><circle cx="378" cy="54" r="11" fill="none" stroke="{MUTED}" stroke-dasharray="3 3"/>'
            f'<circle cx="378" cy="54" r="4" fill="{MUTED}"/>')
    # die
    art += f'<g transform="rotate(10 377 106)"><rect x="362" y="91" width="30" height="30" rx="5" fill="none" stroke="{MUTED}"/>'
    for px, py in ((370, 99), (377, 106), (384, 113), (384, 99), (370, 113)):
        art += f'<circle cx="{px}" cy="{py}" r="2" fill="{MUTED}"/>'
    art += "</g>"
    return art


ART = {"docknest": docknest, "slotline": slotline, "winnow": winnow, "houserules": houserules}


def light(markup):
    for dark, value in LIGHT.items():
        markup = markup.replace(dark, value)
    return markup


def replace_art(path, art):
    """Swap everything between the title <text> and the tagline <text> for the new art."""
    src = path.read_text(encoding="utf-8")
    title = re.search(r'<text x="22" y="59"[^>]*>[^<]*</text>', src)
    tagline = re.search(r'<text x="22" y="91"', src)
    out = src[:title.end()] + f'<g aria-hidden="true">{art}</g>' + src[tagline.start():]
    path.write_text(out, encoding="utf-8", newline="\n")


for name, draw in ART.items():
    art = draw()
    replace_art(CARDS / f"{name}-card.svg", art)
    replace_art(CARDS / f"{name}-card-light.svg", light(art))
print("updated", len(ART) * 2, "cards")
