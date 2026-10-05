"""Refresh generated public-service SVGs, validating all before overwriting."""

import json
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree

root = Path(__file__).resolve().parents[1] / 'assets' / 'components'
sources = json.loads((root / 'sources.json').read_text(encoding='utf-8'))
sources.update(json.loads((root / 'badge-sources.json').read_text(encoding='utf-8-sig')))
downloaded = {}
for name, url in sources.items():
    with urlopen(Request(url, headers={'User-Agent': 'portfolio-components'}), timeout=45) as response:
        data = response.read()
    parsed = ElementTree.fromstring(data)
    if parsed.tag != '{http://www.w3.org/2000/svg}svg':
        raise ValueError(f'{name}: expected SVG')
    downloaded[name] = data
for name, data in downloaded.items():
    (root / name).parent.mkdir(parents=True, exist_ok=True)
    (root / name).write_bytes(data)
print(f'Refreshed {len(downloaded)} SVG components.')
