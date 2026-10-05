"""Keep the accessible still-image view in sync with the authored README."""

from pathlib import Path
import runpy


root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text(encoding="utf-8")
if 'assets/components/' in readme:
    runpy.run_path(str(root / 'scripts' / 'build_component_readme.py'), run_name='__main__')
    raise SystemExit(0)
if 'assets/portfolio-poster.png' in readme:
    runpy.run_path(str(root / 'scripts' / 'build_poster_readme.py'), run_name='__main__')
    raise SystemExit(0)
static = readme.replace('.gif"', '.png"')
static = static.replace("[View without motion](STATIC.md)", "[View with motion](README.md)")
# The legacy contribution graph is an animated SVG; omit it from the still view.
start = static.index("## Contributions\n")
end = static.index("\n---\n", start)
static = static[:start] + static[end:]
static = "[← Back to the profile](README.md)\n\n" + static
(root / "STATIC.md").write_text(static, encoding="utf-8", newline="\n")
