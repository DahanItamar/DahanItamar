"""Render the profile README badges into .github/assets.

Badges use shields.io's for-the-badge geometry (Verdana 10px, uppercase,
1.25px letter spacing). The width table below was measured from Verdana and
Verdana Bold at 10px, so text fits exactly without needing the font installed.
Logos come from assets/components/badges/logos (sources in badge-sources.json).

Run after changing a badge: python3 .github/scripts/profile_badges.py
"""

import html
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / ".github" / "assets"
LOGOS = ROOT / "assets" / "components" / "badges" / "logos"

# Advance widths at 10px for ASCII 32..126.
VERDANA = [float(w) for w in (
    "3.52 3.94 4.59 8.18 6.36 10.76 7.27 2.69 4.54 4.54 6.36 8.18 3.64 4.54 3.64 4.54 6.36 6.36 6.36 6.36 "
    "6.36 6.36 6.36 6.36 6.36 6.36 4.54 4.54 8.18 8.18 8.18 5.45 10 6.84 6.86 6.98 7.71 6.32 5.75 7.75 7.51 "
    "4.21 4.55 6.93 5.57 8.43 7.48 7.87 6.03 7.87 6.95 6.84 6.16 7.32 6.84 9.89 6.85 6.15 6.85 4.54 4.54 4.54 "
    "8.18 6.36 6.36 6.01 6.23 5.21 6.23 5.96 3.52 6.23 6.33 2.74 3.44 5.92 2.74 9.73 6.33 6.07 6.23 6.23 4.27 "
    "5.21 3.94 6.33 5.92 8.18 5.92 5.92 5.25 6.35 4.54 6.35 8.18"
).split()]
VERDANA_BOLD = [float(w) for w in (
    "3.42 4.02 5.87 8.67 7.11 12.72 8.62 3.32 5.43 5.43 7.11 8.67 3.61 4.8 3.61 6.89 7.11 7.11 7.11 7.11 7.11 "
    "7.11 7.11 7.11 7.11 7.11 4.02 4.02 8.67 8.67 8.67 6.17 9.64 7.76 7.62 7.24 8.3 6.83 6.5 8.11 8.37 5.46 "
    "5.55 7.71 6.37 9.48 8.47 8.5 7.33 8.5 7.82 7.1 6.82 8.12 7.64 11.28 7.64 7.37 6.92 5.43 6.89 5.43 8.67 "
    "7.11 7.11 6.68 6.99 5.88 6.99 6.64 4.22 6.99 7.12 3.42 4.03 6.71 3.42 10.58 7.12 6.87 6.99 6.99 4.97 "
    "5.93 4.56 7.12 6.5 9.79 6.69 6.51 5.97 7.11 5.43 7.11 8.67"
).split()]

# (file, label, logo file, background, foreground)
TOOLS = [
    ("typescript", "TypeScript", "typescript.svg", "#3178C6", "#fff"),
    ("react", "React", "react.svg", "#20232A", "#61DAFB"),
    ("nodedotjs", "Node.js", "nodedotjs.svg", "#3C873A", "#fff"),
    ("csharp-dotnet", "C# / .NET", "dotnet.svg", "#512BD4", "#fff"),
    ("postgresql", "PostgreSQL", "postgresql.svg", "#336791", "#fff"),
    ("docker", "Docker", "docker.svg", "#1D63ED", "#fff"),
    ("claudecode", "Claude Code", "claudecode.svg", "#C15F3C", "#fff"),
    ("codex", "Codex", "codex.svg", "#000000", "#fff"),
    ("gemini", "Gemini", "gemini.svg", "#6F57A8", "#fff"),
    ("n8n", "n8n", "n8n.svg", "#EA4B71", "#fff"),
]

# Contact button: the profile's green, dark enough for white text.
CONTACT_BG = "#3b5d14"
MAIL_ICON = (
    '<g fill="none" stroke="#fff" stroke-width="1.6" stroke-linejoin="round">'
    '<rect x="1" y="2.5" width="12" height="9" rx="1.5"/><path d="M1.6 3.3 7 7.8l5.4-4.5"/></g>'
)


def text_length(s, bold):
    table = VERDANA_BOLD if bold else VERDANA
    width = sum(table[ord(c) - 32] if 32 <= ord(c) <= 126 else 10.0 for c in s)
    return math.floor(width) + 1.25 * len(s)


def esc(s):
    return html.escape(s, quote=True)


def badge(label, icon, bg, fg, bold=False):
    """A single-section badge: 14px icon at (9, 7), then the uppercase label."""
    text = label.upper()
    length = text_length(text, bold)
    x = 9 + 14 + 9
    w = x + length + 12
    weight = ' font-weight="bold"' if bold else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}" height="28" role="img" aria-label="{esc(label)}">'
        f'<title>{esc(label)}</title><rect width="{w:g}" height="28" fill="{bg}" shape-rendering="crispEdges"/>'
        f'{icon}<g fill="{fg}" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" '
        'text-rendering="geometricPrecision" font-size="100">'
        f'<text transform="scale(.1)" x="{(x + length / 2) * 10:g}" y="175" textLength="{length * 10:g}"{weight}>'
        f'{esc(text)}</text></g></svg>\n'
    )


def logo(path, color):
    """The logo's paths in a 14x14 box at (9, 7), recoloured."""
    src = path.read_text(encoding="utf-8")
    view_box = re.search(r'viewBox="([^"]+)"', src).group(1)
    inner = re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", src, flags=re.S)
    inner = re.sub(r"<title>.*?</title>", "", inner, flags=re.S)
    # Drop hard-coded colours so the badge foreground applies (fill="none" stays).
    inner = re.sub(r'\sfill="#[0-9A-Fa-f]{3,8}"', "", inner)
    return (f'<svg x="9" y="7" width="14" height="14" viewBox="{view_box}" fill="{color}" '
            f'color="{color}">{inner}</svg>')


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def main():
    for name, label, logo_file, bg, fg in TOOLS:
        write(ASSETS / "tools" / f"{name}.svg", badge(label, logo(LOGOS / logo_file, fg), bg, fg))
    write(ASSETS / "contact.svg",
          badge("Start a conversation", f'<g transform="translate(9 7)">{MAIL_ICON}</g>', CONTACT_BG, "#fff", True))
    print(f"{len(TOOLS)} tool badges and the contact badge")


if __name__ == "__main__":
    main()
