"""Render the profile README badges and open-source PR cards.

Outputs, all SVG with transparent backgrounds:
  .github/assets/stats/*.svg      stat badges (merged PRs, projects, website, email)
  .github/assets/tools/*.svg      language and tool badges
  .github/assets/oss/*.svg        dark and light cards for the latest merged PRs
and rewrites the README block between the OSS-PRS markers.

Badges use shields.io's for-the-badge geometry (Verdana 10px, uppercase,
1.25px letter spacing). The width table below was measured from Verdana and
Verdana Bold at 10px, so text fits exactly without needing the font installed.

Only public data is read. GITHUB_TOKEN, when set, is sent as a header to raise
the API rate limit and is never written anywhere.
"""

import html
import json
import math
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

USER = "DahanItamar"
WEBSITE = "itamardahan.com"
ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / ".github" / "assets"
LOGOS = ROOT / "assets" / "components" / "badges" / "logos"
README = ROOT / "README.md"
PR_CARD_COUNT = 4

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

# Stat badge colours: the profile's green, dark enough for white text.
LABEL_BG = "#3b5d14"
VALUE_BG = "#4b7519"

# 14x14 white glyphs, drawn at (9, 7). {bg} is the label colour.
ICONS = {
    "merge": (
        '<g fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round">'
        '<circle cx="3.5" cy="2.8" r="1.8"/><circle cx="3.5" cy="11.2" r="1.8"/><circle cx="10.5" cy="11.2" r="1.8"/>'
        '<path d="M3.5 4.6v4.8M3.5 5.2c0 2.6 2.2 3.9 5.2 4.6"/></g>'
    ),
    "repo": (
        '<g fill="none" stroke="#fff" stroke-width="1.6" stroke-linejoin="round">'
        '<path d="M2.5 1.5h7.5a1.5 1.5 0 0 1 1.5 1.5v9.5H4a1.5 1.5 0 0 1-1.5-1.5z"/><path d="M2.5 11a1.5 1.5 0 0 1 1.5-1.5h7.5"/></g>'
    ),
    "globe": (
        '<g fill="none" stroke="#fff" stroke-width="1.4"><circle cx="7" cy="7" r="6"/>'
        '<ellipse cx="7" cy="7" rx="2.6" ry="6"/><path d="M1 7h12M2 3.8h10M2 10.2h10"/></g>'
    ),
    "mail": (
        '<g fill="none" stroke="#fff" stroke-width="1.6" stroke-linejoin="round">'
        '<rect x="1" y="2.5" width="12" height="9" rx="1.5"/><path d="M1.6 3.3 7 7.8l5.4-4.5"/></g>'
    ),
}

# (file, label, logo file, background, foreground)
TOOLS = [
    ("typescript", "TypeScript", "typescript.svg", "#3178C6", "#fff"),
    ("javascript", "JavaScript", "javascript.svg", "#F7DF1E", "#000"),
    ("react", "React", "react.svg", "#20232A", "#61DAFB"),
    ("nodedotjs", "Node.js", "nodedotjs.svg", "#3C873A", "#fff"),
    ("csharp", "C#", "csharp.svg", "#68217A", "#fff"),
    ("dotnet", ".NET", "dotnet.svg", "#512BD4", "#fff"),
    ("postgresql", "PostgreSQL", "postgresql.svg", "#336791", "#fff"),
    ("sqlite", "SQLite", "sqlite.svg", "#003B57", "#fff"),
    ("docker", "Docker", "docker.svg", "#1D63ED", "#fff"),
    ("git", "Git", "git.svg", "#F05032", "#fff"),
    ("claudecode", "Claude Code", "claudecode.svg", "#C15F3C", "#fff"),
    ("codex", "Codex", "codex.svg", "#000000", "#fff"),
    ("gemini", "Gemini", "gemini.svg", "#6F57A8", "#fff"),
    ("n8n", "n8n", "n8n.svg", "#EA4B71", "#fff"),
]

CARD_THEMES = {
    "dark": {"border": "#39464d", "muted": "#a5b0b9", "title": "#f0f2eb", "accent": "#c6f27f", "rule": "#2b363e"},
    "light": {"border": "#d1d9e0", "muted": "#59636e", "title": "#1f2328", "accent": "#456c17", "rule": "#d1d9e0"},
}

BEGIN, END = "<!-- BEGIN OSS-PRS -->", "<!-- END OSS-PRS -->"


def text_length(s, bold):
    table = VERDANA_BOLD if bold else VERDANA
    width = sum(table[ord(c) - 32] if 32 <= ord(c) <= 126 else 10.0 for c in s)
    return math.floor(width) + 1.25 * len(s)


def esc(s):
    return html.escape(s, quote=True)


def svg_text(x, text, bold=False):
    """A centred badge label at x (in badge pixels), drawn at 10x scale like shields."""
    length = text_length(text, bold)
    weight = ' font-weight="bold"' if bold else ""
    return (f'<text transform="scale(.1)" x="{(x + length / 2) * 10:g}" y="175" '
            f'textLength="{length * 10:g}"{weight}>{esc(text)}</text>')


def stat_badge(label, value, icon):
    label, value = label.upper(), value.upper()
    lt, vt = text_length(label, False), text_length(value, True)
    lx = 9 + 14 + 9
    lw = lx + lt + 12
    w = lw + 12 + vt + 12
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}" height="28" role="img" aria-label="{esc(label)}: {esc(value)}">'
        f'<title>{esc(label)}: {esc(value)}</title>'
        f'<g shape-rendering="crispEdges"><rect width="{lw:g}" height="28" fill="{LABEL_BG}"/>'
        f'<rect x="{lw:g}" width="{w - lw:g}" height="28" fill="{VALUE_BG}"/></g>'
        f'<g transform="translate(9 7)">{ICONS[icon]}</g>'
        '<g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" '
        'text-rendering="geometricPrecision" font-size="100">'
        f'{svg_text(lx, label)}{svg_text(lw + 12, value, True)}</g></svg>\n'
    )


def button_badge(text, icon):
    """A single-colour call-to-action badge with an icon."""
    text = text.upper()
    lt = text_length(text, True)
    lx = 9 + 14 + 9
    w = lx + lt + 12
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}" height="28" role="img" aria-label="{esc(text)}">'
        f'<title>{esc(text)}</title><rect width="{w:g}" height="28" fill="{LABEL_BG}" shape-rendering="crispEdges"/>'
        f'<g transform="translate(9 7)">{ICONS[icon]}</g>'
        '<g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" '
        f'text-rendering="geometricPrecision" font-size="100">{svg_text(lx, text, True)}</g></svg>\n'
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


def tool_badge(label, logo_file, bg, fg):
    text = label.upper()
    lt = text_length(text, False)
    lx = 9 + 14 + 9
    w = lx + lt + 12
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}" height="28" role="img" aria-label="{esc(label)}">'
        f'<title>{esc(label)}</title><rect width="{w:g}" height="28" fill="{bg}" shape-rendering="crispEdges"/>'
        f'{logo(LOGOS / logo_file, fg)}'
        f'<g fill="{fg}" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" '
        f'text-rendering="geometricPrecision" font-size="100">{svg_text(lx, text)}</g></svg>\n'
    )


def wrap(text, limit, lines):
    """Split text into at most `lines` lines of about `limit` characters, adding an ellipsis if cut."""
    words, out, current = text.split(), [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) <= limit:
            current = candidate
            continue
        out.append(current)
        current = word
        if len(out) == lines:
            break
    else:
        out.append(current)
        return [line for line in out if line]
    out[-1] = out[-1].rstrip(" .,:;") + "…"
    return out


def pr_card(pr, theme):
    t = CARD_THEMES[theme]
    title_lines = wrap(pr["title"], 46, 2)
    merged = datetime.fromisoformat(pr["merged_at"].replace("Z", "+00:00"))
    footer = f"Merged {merged:%b} {merged.day}, {merged:%Y}  ·  +{pr['additions']} −{pr['deletions']}"
    titles = "".join(
        f'<text x="22" y="{58 + i * 21}" fill="{t["title"]}" font-size="16" font-weight="600">{esc(line)}</text>'
        for i, line in enumerate(title_lines)
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="420" height="124" viewBox="0 0 420 124" role="img" '
        f'aria-label="{esc(pr["repo"])}: {esc(pr["title"])}"><title>{esc(pr["repo"])}: {esc(pr["title"])}</title>'
        '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">'
        f'<rect x=".5" y=".5" width="419" height="123" rx="8" fill="none" stroke="{t["border"]}"/>'
        f'<g transform="translate(22 13)" fill="none" stroke="{t["accent"]}" stroke-width="1.4" stroke-linecap="round">'
        '<circle cx="3" cy="2.5" r="1.7"/><circle cx="3" cy="10.5" r="1.7"/><circle cx="10" cy="10.5" r="1.7"/>'
        '<path d="M3 4.2v4.6M3 4.8c0 2.5 2.1 3.7 5.1 4.4"/></g>'
        f'<text x="40" y="23" fill="{t["accent"]}" font-size="10" letter-spacing="2">{esc(pr["repo"].upper())}</text>'
        f'{titles}<path d="M22 92H398" stroke="{t["rule"]}"/>'
        f'<text x="22" y="111" fill="{t["muted"]}" font-size="12">{esc(footer)}</text></g></svg>\n'
    )


def get_json(url):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": f"{USER}-profile-badges"}
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as resp:
        return json.load(resp)


def merged_external_prs():
    """Merged PRs authored by USER in repositories USER doesn't own, newest first."""
    query = urllib.parse.quote(f"is:pr author:{USER} is:merged -user:{USER}")
    items, page = [], 1
    while True:
        data = get_json(f"https://api.github.com/search/issues?q={query}&sort=updated&order=desc&per_page=100&page={page}")
        items += data["items"]
        if len(items) >= data["total_count"] or not data["items"]:
            break
        page += 1
    prs = []
    for item in items:
        repo = item["repository_url"].split("/repos/", 1)[1]
        prs.append({"repo": repo, "number": item["number"], "title": item["title"], "url": item["html_url"],
                    "merged_at": item["pull_request"]["merged_at"]})
    prs.sort(key=lambda p: p["merged_at"], reverse=True)
    return prs


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def readme_block(prs):
    cells = []
    for pr in prs:
        name = f'{pr["repo"].replace("/", "-")}-{pr["number"]}'
        alt = esc(f'{pr["repo"]} #{pr["number"]}: {pr["title"]}')
        cells.append(
            f'<a href="{pr["url"]}"><picture>'
            f'<source media="(prefers-color-scheme: dark)" srcset=".github/assets/oss/{name}-dark.svg" />'
            f'<img src=".github/assets/oss/{name}-light.svg" width="48%" alt="{alt}" /></picture></a>'
        )
    rows = ["<p>\n  " + "\n  ".join(cells[i:i + 2]) + "\n</p>" for i in range(0, len(cells), 2)]
    return f"{BEGIN}\n" + "\n".join(rows) + f"\n{END}"


def main():
    prs = merged_external_prs()
    projects = len({p["repo"] for p in prs})

    write(ASSETS / "stats" / "merged-prs.svg", stat_badge("Merged PRs", str(len(prs)), "merge"))
    write(ASSETS / "stats" / "projects.svg", stat_badge("OSS projects", str(projects), "repo"))
    write(ASSETS / "stats" / "website.svg", stat_badge("Website", WEBSITE, "globe"))
    write(ASSETS / "stats" / "email.svg", stat_badge("Email", "Say hello", "mail"))
    write(ASSETS / "stats" / "see-all.svg", button_badge("See all contributions", "merge"))

    for name, label, logo_file, bg, fg in TOOLS:
        write(ASSETS / "tools" / f"{name}.svg", tool_badge(label, logo_file, bg, fg))

    latest = prs[:PR_CARD_COUNT]
    oss = ASSETS / "oss"
    for old in oss.glob("*.svg") if oss.exists() else []:
        old.unlink()
    for pr in latest:
        detail = get_json(f'https://api.github.com/repos/{pr["repo"]}/pulls/{pr["number"]}')
        pr["additions"], pr["deletions"] = detail["additions"], detail["deletions"]
        name = f'{pr["repo"].replace("/", "-")}-{pr["number"]}'
        for theme in CARD_THEMES:
            write(oss / f"{name}-{theme}.svg", pr_card(pr, theme))

    text = README.read_text(encoding="utf-8")
    if BEGIN in text and END in text:
        before, rest = text.split(BEGIN, 1)
        after = rest.split(END, 1)[1]
        README.write_text(before + readme_block(latest) + after, encoding="utf-8", newline="\n")

    print(f"{len(prs)} merged PRs across {projects} projects; {len(latest)} cards; {len(TOOLS)} tool badges")


if __name__ == "__main__":
    main()
