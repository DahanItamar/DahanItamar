"""Render the profile's original diagrams; no screenshots or live data are used."""

from functools import lru_cache
from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "profile"
FONT = ROOT / "assets" / "fonts" / "Geist.ttf"
THEMES = {
    "dark": dict(bg="#101419", text="#f0f2eb", muted="#a9b2a8", line="#3b463d", accent="#c6f27f", soft="#263220", error="#ffaaaa"),
    "light": dict(bg="#f5f4ef", text="#172019", muted="#526052", line="#bfc8b9", accent="#426512", soft="#e3ecd7", error="#a33333"),
}


@lru_cache(maxsize=128)
def font(size, weight=400):
    result = ImageFont.truetype(str(FONT), size)
    result.set_variation_by_axes([weight])
    return result


def label(draw, point, text, size, color, weight=400, anchor="la"):
    draw.text(point, text, font=font(size, weight), fill=color, anchor=anchor)


def line(draw, points, color, width=2):
    draw.line(points, fill=color, width=width, joint="curve")


def marker(draw, start, end, fraction, color, radius=7):
    x = start[0] + (end[0] - start[0]) * fraction
    y = start[1] + (end[1] - start[1]) * fraction
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)


def connector(a, b, start_size, end_size):
    dx, dy = b[0]-a[0], b[1]-a[1]
    length = math.hypot(dx, dy)
    def inset(size):
        return min(size[0]/abs(dx) if dx else float("inf"), size[1]/abs(dy) if dy else float("inf")) + 9/length
    start, end = inset(start_size), inset(end_size)
    return (a[0]+dx*start, a[1]+dy*start), (b[0]-dx*end, b[1]-dy*end)


def progress(t):
    raw = max(0, min(1, (t - .12) / .68))
    return raw * raw * (3 - 2 * raw)


def draw_hero(theme, mobile):
    c = THEMES[theme]
    w, h = (640, 590) if mobile else (1280, 390)
    img = Image.new("RGB", (w, h), c["bg"])
    d = ImageDraw.Draw(img)
    x = 40 if mobile else 52
    label(d, (x, 30), "ITAMAR DAHAN", 22, c["text"], 600)
    if mobile:
        for y, text in [(88, "I build useful systems."), (144, "Then make them"), (200, "dependable.")]:
            label(d, (x, y), text, 46, c["text"], 650)
        label(d, (x, 270), "Full-stack development", 25, c["muted"])
        label(d, (x, 307), "Automation · AI-assisted engineering", 25, c["muted"])
        cx, top, rx, ry, gap = 320, 395, 135, 42, 53
    else:
        label(d, (x, 104), "I build useful systems.", 57, c["text"], 650)
        label(d, (x, 178), "Then make them dependable.", 52, c["text"], 650)
        label(d, (x, 266), "Full-stack development · Automation", 25, c["muted"])
        label(d, (x, 306), "AI-assisted engineering", 25, c["muted"])
        cx, top, rx, ry, gap = 1060, 75, 147, 47, 107
    for i in range(3):
        cy = top + i * gap
        line(d, [(cx-rx, cy), (cx, cy-ry), (cx+rx, cy), (cx, cy+ry), (cx-rx, cy)], c["line"], 2)
        for fraction in [.33, .66]:
            line(d, [(cx-rx+rx*fraction, cy+ry*fraction), (cx+rx*fraction, cy-ry+ry*fraction)], c["line"], 1)
    line(d, [(cx, top), (cx, top+gap*2)], c["accent"], 3)
    for i in range(3):
        cy = top+i*gap
        d.ellipse((cx-5, cy-5, cx+5, cy+5), fill=c["accent"])
    return img


def docknest(theme, mobile, t):
    c = THEMES[theme]
    w, h = (640, 500) if mobile else (1280, 310)
    img = Image.new("RGB", (w, h), c["bg"])
    d = ImageDraw.Draw(img)
    points = [(130, 80), (130, 240), (130, 400)] if mobile else [(180, 116), (640, 116), (1100, 116)]
    p = progress(t)
    connections = [connector(a, b, (65, 43), (65, 43)) for a, b in zip(points, points[1:])]
    for a, b in connections:
        line(d, [a, b], c["line"], 2)
    stages = min(2, int(p*3))
    names = [("SITE", "Docker sites", "Capture"), ("SFTP", "Encrypted archive", "Protect"), ("COPY", "Isolated restore", "Recover privately")]
    for i, ((x, y), (short, name, subtitle)) in enumerate(zip(points, names)):
        active = p == 1 or stages == i
        d.rounded_rectangle((x-65, y-43, x+65, y+43), radius=8, fill=c["soft"] if active else c["bg"], outline=c["accent"] if active else c["line"], width=2)
        label(d, (x, y), short, 29, c["text"], 600, "mm")
        label(d, (405, y-14) if mobile else (x, y+67), name, 30 if mobile else 31, c["text"], 550, "mm")
        label(d, (405, y+28) if mobile else (x, y+108), subtitle, 26 if mobile else 24, c["muted"], anchor="mm")
    if p < 1:
        segment = min(1, int(p*2))
        marker(d, *connections[segment], p*2-segment, c["accent"], 7)
    return img


def slotline(theme, mobile, t):
    c = THEMES[theme]
    w, h = (640, 430) if mobile else (1280, 325)
    img = Image.new("RGB", (w, h), c["bg"])
    d = ImageDraw.Draw(img)
    left, right = (36, 604) if mobile else (50, 880)
    grid_top, grid_bottom = (90, 325) if mobile else (64, 270)
    label(d, (left, 25), "SHARED RESOURCE", 22, c["muted"], 500)
    width = right-left
    for i, hour in enumerate(["09:00", "10:00", "11:00", "12:00"]):
        x = left + i * width / 3
        line(d, [(x, grid_top), (x, grid_bottom)], c["line"], 1)
        label(d, (x, grid_top-25), hour, 24, c["muted"], anchor="lm" if i == 0 else "rm" if i == 3 else "mm")
    line(d, [(left, grid_bottom), (right, grid_bottom)], c["line"], 1)
    existing_y = grid_top+25
    d.rounded_rectangle((left, existing_y, left+width*.49, existing_y+54), radius=5, fill=c["soft"], outline=c["accent"], width=2)
    label(d, (left+16, existing_y+12), "Existing booking", 24, c["text"], 500)
    p = progress(t)
    attempt_x = left+width*(.39-.13*p)
    attempt_y = existing_y+108-18*p
    rejected = p > .6
    color = c["error"] if rejected else c["line"]
    d.rounded_rectangle((attempt_x, attempt_y, attempt_x+width*.49, attempt_y+54), radius=5, fill=c["bg"], outline=color, width=2)
    label(d, (attempt_x+16, attempt_y+12), "Overlap rejected" if rejected else "New request", 24, c["error"] if rejected else c["text"], 500)
    if mobile:
        label(d, (left, 367), "Protected by a database constraint.", 28, c["text"], 500)
    else:
        label(d, (956, 104), "Enforced by", 34, c["text"], 550)
        label(d, (956, 149), "PostgreSQL.", 34, c["text"], 550)
        label(d, (956, 213), "Exclusion constraint", 23, c["muted"])
    return img


def winnow(theme, mobile, t):
    c = THEMES[theme]
    w, h = (640, 490) if mobile else (1280, 300)
    img = Image.new("RGB", (w, h), c["bg"])
    d = ImageDraw.Draw(img)
    sources = [(122, 60), (320, 60), (518, 60)] if mobile else [(160, 58), (160, 149), (160, 240)]
    mid = (320, 244) if mobile else (660, 149)
    end = (320, 420) if mobile else (1090, 149)
    upstream = [connector(a, mid, (89, 27), (98, 44)) for a in sources]
    downstream = connector(mid, end, (98, 44), (98, 44))
    for a, b in upstream:
        line(d, [a, b], c["line"], 2)
    line(d, downstream, c["line"], 2)
    for (x, y), name in zip(sources, ["GitHub", "Hacker News", "Stack Exchange"]):
        d.rounded_rectangle((x-89, y-27, x+89, y+27), radius=5, fill=c["bg"], outline=c["line"], width=2)
        label(d, (x, y), name, 22, c["text"], anchor="mm")
    p = progress(t)
    for pos, text in [(mid, "Evidence"), (end, "Project idea")]:
        x, y = pos
        active = (pos == mid and p > .28) or (pos == end and p > .68)
        d.rounded_rectangle((x-98, y-44, x+98, y+44), radius=5, fill=c["soft"] if active else c["bg"], outline=c["accent"] if active else c["line"], width=2)
        label(d, pos, text, 28, c["text"], 500, "mm")
    if p < .5:
        for a, b in upstream:
            marker(d, a, b, p*2, c["accent"])
    elif p < 1:
        marker(d, *downstream, (p-.5)*2, c["accent"])
    if not mobile:
        label(d, (end[0], 229), "Source-linked insight", 25, c["muted"], anchor="mm")
    return img


def process_scene(theme, mobile, t):
    c = THEMES[theme]
    w, h = (640, 460) if mobile else (1280, 245)
    img = Image.new("RGB", (w, h), c["bg"])
    d = ImageDraw.Draw(img)
    points = [(160, 70), (480, 70), (160, 215), (480, 215), (160, 360), (480, 360)] if mobile else [(100+i*216, 100) for i in range(6)]
    for a, b in zip(points, points[1:]):
        line(d, [a, b], c["line"], 2)
    p = progress(t)
    active = min(5, int(p*6))
    names = ["constitution", "spec", "tasks", "implement", "drift", "refactor"]
    for i, ((x, y), name) in enumerate(zip(points, names)):
        d.ellipse((x-9, y-9, x+9, y+9), fill=c["accent"] if i <= active else c["bg"], outline=c["accent"] if i <= active else c["line"], width=2)
        label(d, (x, y+43), name, 28 if mobile else 26, c["text"], anchor="mm")
    x, y = points[active]
    label(d, (x, y-35), "AC-###", 25, c["accent"], 600, "mm")
    if not mobile:
        label(d, (w/2, 204), "One acceptance criterion. A traceable path through the work.", 24, c["muted"], anchor="mm")
    return img


def save_motion(name, render, theme, mobile):
    stem = f"{name}-{'mobile-' if mobile else ''}{theme}"
    final = render(theme, mobile, 1)
    final.save(OUT / f"{stem}.png", optimize=True)
    # No loop extension: each GIF plays once, then remains on its complete frame.
    # A shared palette prevents temporal colour flicker during quantisation.
    palette = final.quantize(colors=64, method=Image.Quantize.MEDIANCUT)
    frames = [render(theme, mobile, i/47).quantize(palette=palette, dither=Image.Dither.NONE) for i in range(48)]
    frames[0].save(OUT / f"{stem}.gif", save_all=True, append_images=frames[1:], duration=80, disposal=1, optimize=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for theme in THEMES:
        for mobile in [False, True]:
            draw_hero(theme, mobile).save(OUT / f"hero-{'mobile-' if mobile else ''}{theme}.png", optimize=True)
            for name, render in [("docknest", docknest), ("slotline", slotline), ("winnow", winnow), ("process", process_scene)]:
                save_motion(name, render, theme, mobile)
    files = list(OUT.glob("*.png")) + list(OUT.glob("*.gif"))
    print(f"Rendered {len(files)} assets, {sum(p.stat().st_size for p in files)/1024:.0f} KiB total")


if __name__ == "__main__":
    main()
