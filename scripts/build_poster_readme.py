"""Keep the poster README and its native-text alternative in sync.

The first preview remains an immutable content source. The poster was edited
with the built-in image generation tool, not by this script.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'archive' / 'README-2026-10-06-first-preview.md').read_text(encoding='utf-8')
native = re.sub(r'<picture>.*?</picture>\s*', '', source, flags=re.S)
native = native.replace('# Itamar Dahan\n', '# Itamar Dahan\n\n**I build useful systems. Then make them dependable.**\n\nFull-stack development · Automation · AI-assisted engineering\n', 1)
native = re.sub(r'## Contributions\n.*?\n---\n', '---\n', native, flags=re.S)
native = native[:native.index('<details>\n<summary>Profile options</summary>')].rstrip()

intro = '''<a href="assets/portfolio-poster.png">
  <img src="assets/portfolio-poster.png" width="100%" alt="Itamar Dahan — I build useful systems. Then make them dependable. Engineering portfolio featuring DockNest encrypted backup and isolated recovery, Slotline database-enforced booking, Winnow evidence-linked ideas, the six-stage spec workflow, House Rules, GitCheckup and HeWordle. Full project descriptions and links are available below and in the text version." />
</a>

[Open the poster](assets/portfolio-poster.png) · [Read the text version](STATIC.md) · [Start a conversation](mailto:itamardahan1111d@gmail.com)

**Explore:** [Slotline](https://github.com/DahanItamar/Slotline) · [Winnow](https://github.com/DahanItamar/Winnow) · [House Rules](https://github.com/DahanItamar/HouseRules) · [GitCheckup](https://github.com/DahanItamar/GitCheckup) · [HeWordle](https://github.com/DahanItamar/HeWordle)

**Skills:** [spec-architect](https://github.com/DahanItamar/spec-architect) · [readme-architect](https://github.com/DahanItamar/readme-architect) · [uilint](https://github.com/DahanItamar/uilint) · [acsm](https://github.com/DahanItamar/acsm)

<details>
<summary><strong>Read the project details and full portfolio</strong></summary>

'''
contributions = '''
<details>
<summary>Contribution graph</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph-dark.svg" />
  <img alt="Pac-Man eating my contribution graph" src="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph.svg" width="100%" />
</picture>

</details>
'''
readme = intro + native + '\n\n</details>\n' + contributions + '''
<details>
<summary>Previous versions and restoration</summary>

[Original README](archive/README-2026-10-06-before-redesign.md) · [First preview](archive/README-2026-10-06-first-preview.md) · [Restore instructions](RESTORE.md)

</details>
'''
static = '[← View the portfolio poster](README.md)\n\n' + native + '\n\n[Previous README](archive/README-2026-10-06-before-redesign.md) · [Restore instructions](RESTORE.md)\n'
(ROOT / 'README.md').write_text(readme, encoding='utf-8', newline='\n')
(ROOT / 'STATIC.md').write_text(static, encoding='utf-8', newline='\n')

