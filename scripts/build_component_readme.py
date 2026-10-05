"""Compose a GitHub-native profile from vendored tools and original SVG cards."""

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'components'
OUT.mkdir(parents=True, exist_ok=True)
FONT = '-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif'


def svg(width, height, body, title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title, quote=True)}"><title>{escape(title)}</title><g font-family="{FONT}">{body}</g></svg>\n'


cards = [
    ('Slotline', 'BOOKING SYSTEM', 'One resource. One booking.', ['Database-enforced reservations.', 'Tenant isolation. Live calendars.'], 'TypeScript · Fastify · PostgreSQL'),
    ('Winnow', 'LOCAL-FIRST DESKTOP', 'Ideas with evidence.', ['Developer complaints become ideas,', 'with links back to their sources.'], 'Electron · React · SQLite'),
    ('HouseRules', 'OFFLINE GAME', 'An offline casino adventure.', ['Nine casino cabinets. Four rooms.', 'An offline adventure built with Godot.'], 'Godot 4 · GDScript'),
    ('GitCheckup', 'DEVELOPER TOOLING', 'Healthier repositories.', ['Repository health scores and', 'a ranked list of practical fixes.'], 'TypeScript · Next.js'),
]
for name, category, headline, description, stack in cards:
    title = 'House Rules' if name == 'HouseRules' else name
    body = '<rect x=".5" y=".5" width="419" height="189" rx="8" fill="#101419" stroke="#39464d"/>'
    body += f'<text x="22" y="23" fill="#a5b0b9" font-size="10" letter-spacing="2">{category}</text>'
    body += f'<text x="398" y="23" text-anchor="end" fill="#c6f27f" font-size="10">PUBLIC</text>'
    body += f'<text x="22" y="59" fill="#f0f2eb" font-size="29" font-weight="650">{title}</text>'
    if name == 'Slotline':
        body += '<path d="M329 40H397M329 53H397M329 66H397M344 35V74M370 35V74" stroke="#39464d" fill="none"/><rect x="335" y="42" width="36" height="14" rx="2" fill="#263220" stroke="#c6f27f"/><rect x="355" y="56" width="36" height="14" rx="2" fill="#291d1b" stroke="#ffaaaa"/>'
    elif name == 'Winnow':
        for y in [39, 54, 69]:
            body += f'<rect x="330" y="{y}" width="16" height="11" rx="1" stroke="#a5b0b9" fill="none"/><path d="M347 {y+5}Q366 {y+5} 378 58" stroke="#a5b0b9" fill="none"/>'
        body += '<circle cx="380" cy="58" r="4" fill="#c6f27f"/><rect x="389" y="45" width="10" height="26" rx="2" fill="none" stroke="#c6f27f"/>'
    body += f'<text x="22" y="91" fill="#c6f27f" font-size="18" font-weight="550">{escape(headline)}</text>'
    for i, line in enumerate(description):
        body += f'<text x="22" y="{119+i*22}" fill="#bac3cb" font-size="15">{escape(line)}</text>'
    body += '<path d="M22 154H398" stroke="#2b363e"/>'
    body += f'<text x="22" y="176" fill="#a5b0b9" font-size="12">{escape(stack)}</text>'
    (OUT / f'{name.lower()}-card.svg').write_text(svg(420, 190, body, f'{title}: {headline}'), encoding='utf-8')

still = '<rect width="900" height="66" rx="5" fill="#101419"/><text x="450" y="40" text-anchor="middle" fill="#c6f27f" font-size="27" font-weight="550">I build useful systems. Then make them dependable.</text>'
(OUT / 'typing-still.svg').write_text(svg(900, 66, still, 'I build useful systems. Then make them dependable.'), encoding='utf-8')

for mobile in [False, True]:
    width, height = (640, 370) if mobile else (900, 174)
    points = [(105, 90), (320, 90), (535, 90), (105, 250), (320, 250), (535, 250)] if mobile else [(82+i*147, 72) for i in range(6)]
    end_x,end_y = points[-1]
    body = f'<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="8" fill="#101419" stroke="#39464d"/>'
    path = 'M105 90H535H589V170H51V250H535' if mobile else 'M82 72H817'
    body += f'<path d="{path}" stroke="#66747b" fill="none"/>'
    for (x,y), name in zip(points, ['constitution', 'spec', 'tasks', 'implement', 'drift', 'refactor']):
        body += f'<circle cx="{x}" cy="{y}" r="7" fill="#101419" stroke="#f0f2eb"/><text x="{x}" y="{y+38}" text-anchor="middle" fill="#f0f2eb" font-size="{23 if mobile else 18}">{name}</text>'
    values = ';'.join(f'{x} {y}' for x,y in points)
    animation = f'<animateTransform attributeName="transform" type="translate" values="{values}" keyTimes="0;.2;.4;.6;.8;1" dur="4.4s" repeatCount="1" fill="freeze"/>'
    body += f'<g transform="translate({end_x},{end_y})">{animation}<circle r="8" fill="#c6f27f"/><rect x="-43" y="-52" width="86" height="28" rx="5" fill="#101419" stroke="#c6f27f"/><text y="-32" text-anchor="middle" fill="#c6f27f" font-size="18">AC-###</text></g>'
    body += f'<text x="{width/2}" y="{height-25}" text-anchor="middle" fill="#a5b0b9" font-size="{20 if mobile else 17}">One requirement. A traceable path through the work.</text>'
    suffix = '-mobile' if mobile else ''
    (OUT / f'process{suffix}.svg').write_text(svg(width, height, body, 'One acceptance criterion through constitution, spec, tasks, implement, drift and refactor.'), encoding='utf-8')
    (OUT / f'process{suffix}-still.svg').write_text(svg(width, height, body.replace(animation, ''), 'One acceptance criterion through constitution, spec, tasks, implement, drift and refactor.'), encoding='utf-8')

source = (ROOT / 'archive' / 'README-2026-10-06-first-preview.md').read_text(encoding='utf-8')
catalogue = source[source.index('<details>\n<summary><strong>Also built'):source.index('## Skills for AI coding agents')].strip()
about = source[source.index('## About\n') + len('## About\n'):source.index('## Selected Work')].strip()
principles = source[source.index('<details>\n<summary><strong>Engineering principles'):source.index('## Contributions')].strip()

readme = '''<h1 align="center">ITAMAR DAHAN</h1>

<p align="center"><strong>Full-stack development · Automation · AI-assisted engineering</strong></p>

<h2 align="center">I build useful systems.<br />Then make them dependable.</h2>

<p align="center">
  <a href="#selected-systems">Selected systems</a> · <a href="#how-i-build">How I build</a> · <a href="mailto:itamardahan1111d@gmail.com">Start a conversation</a>
</p>

<p align="center"><strong>Readable architecture. Secure defaults. Accessible interfaces.</strong></p>

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/components/stack-dark.svg" />
  <img src="assets/components/stack-light.svg" width="520" alt="TypeScript, JavaScript, React, Node.js, C#, .NET, PostgreSQL, SQLite, Docker and Git" />
</picture>
</p>

## Selected systems

<img src="assets/components/docknest-banner.png" width="100%" alt="DockNest — private project in controlled beta. Backups are only useful if recovery works. Docker sites become encrypted SFTP archives and isolated recovery environments." />

**DockNest** is my self-hosted backup and recovery system. It packages encrypted backups on SFTP and restores isolated private copies, with recovery evidence and an independently encrypted manager recovery kit. **Private · controlled beta.**

<p>
  <a href="https://github.com/DahanItamar/Slotline"><img src="assets/components/slotline-card.svg" width="410" alt="Slotline — database-enforced reservations, tenant isolation and live calendars. TypeScript, Fastify, PostgreSQL." /></a>
  <a href="https://github.com/DahanItamar/Winnow"><img src="assets/components/winnow-card.svg" width="410" alt="Winnow — local-first project ideas grounded in developer complaints and original sources. Electron, React, SQLite." /></a>
</p>

<p>
  <a href="https://github.com/DahanItamar/HouseRules"><img src="assets/components/houserules-card.svg" width="410" alt="House Rules — offline casino adventure with nine cabinets and four rooms, built with Godot." /></a>
  <a href="https://github.com/DahanItamar/GitCheckup"><img src="assets/components/gitcheckup-card.svg" width="410" alt="GitCheckup — repository health scores and ranked fixes. TypeScript, Next.js." /></a>
</p>

[Play House Rules](https://houserules.itamardahan.com/) · [Try GitCheckup](https://gitcheckup.com) · [Play HeWordle](https://wordlehebrew.com)

## How I build

<picture>
  <source media="(max-width: 640px) and (prefers-reduced-motion: reduce)" srcset="assets/components/process-mobile-still.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/components/process-still.svg" />
  <source media="(max-width: 640px)" srcset="assets/components/process-mobile.svg" />
  <img src="assets/components/process.svg" width="100%" alt="The same acceptance criterion stays traceable through constitution, spec, tasks, implementation, drift checking and refactoring." />
</picture>

I turn engineering workflows into reusable skills for AI coding agents:

- [**spec-architect**](https://github.com/DahanItamar/spec-architect) — six stages with stable, verified acceptance criteria.
- [**readme-architect**](https://github.com/DahanItamar/readme-architect) — documentation grounded in running the project.
- [**uilint**](https://github.com/DahanItamar/uilint) — checks loading, empty, error, success and partial interface states.
- [**acsm**](https://github.com/DahanItamar/acsm) — routes projects to applicable security and compliance obligations, with citations.

## Contribution activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph-dark.svg" />
  <img src="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph.svg" width="100%" alt="Pac-Man eating my GitHub contribution graph, generated from my contribution activity." />
</picture>

'''
readme += catalogue + '\n\n<details>\n<summary><strong>About and engineering principles</strong></summary>\n\n' + about + '\n\n' + principles + '\n\n</details>\n\n'
readme += '''---

**Explore the work. Start a conversation.**

[itamardahan1111d@gmail.com](mailto:itamardahan1111d@gmail.com)

<details>
<summary>Poster, text version, components and previous versions</summary>

[Portfolio poster](assets/portfolio-poster.png) · [Text version](STATIC.md) · [README components and credits](assets/components/README.md) · [Original README](archive/README-2026-10-06-before-redesign.md) · [Poster preview](archive/README-2026-10-06-poster-preview.md) · [Restore instructions](RESTORE.md)

</details>
'''
(ROOT / 'README.md').write_text(readme, encoding='utf-8', newline='\n')

native = re.sub(r'<picture>.*?</picture>\s*', '', source, flags=re.S)
native = re.sub(r'## Contributions\n.*?\n---\n', '---\n', native, flags=re.S)
native = native[:native.index('<details>\n<summary>Profile options</summary>')].rstrip()
native = native.replace('# Itamar Dahan\n', '# Itamar Dahan\n\n**I build useful systems. Then make them dependable.**\n', 1)
(ROOT / 'STATIC.md').write_text('[← View the profile](README.md)\n\n'+native+'\n', encoding='utf-8', newline='\n')
