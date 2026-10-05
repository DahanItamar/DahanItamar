# Profile visuals

These diagrams belong to the first preview, retained for restoration. The current profile uses the [finished portfolio poster](../portfolio-poster.md). Run `python scripts/build_poster_readme.py` from the repository root to rebuild its README and native-text alternative.

Original diagrams for Itamar Dahan's profile, generated from geometry and text by [`scripts/build_profile_assets.py`](../../scripts/build_profile_assets.py). They illustrate product behavior; they are not screenshots, benchmarks, or evidence of a live deployment.

- Hero: useful systems and dependable engineering.
- DockNest: capture, encrypted SFTP storage, and isolated recovery.
- Slotline: an overlapping reservation rejected by a PostgreSQL constraint.
- Winnow: public sources connected to evidence and a project idea.
- Process: one acceptance criterion carried through six development stages.

Every graphic has light/dark and desktop/mobile variants. Each motion asset also has a static PNG. GIFs play once for approximately four seconds and stop on the completed diagram; they have no infinite-loop extension. README `<picture>` sources select a static image for reduced motion.

The diagrams contain no private hostnames, credentials, customer information, or production metrics. DockNest is identified as a private project in the profile; no inaccessible repository link is presented as a public demo.

## Rebuild

Use Python 3.10 or newer:

```sh
python -m pip install -r scripts/requirements.txt
python scripts/build_profile_assets.py
python scripts/build_static_readme.py
```

The bundled Geist font is distributed under the [SIL Open Font License](../fonts/OFL.txt). Pillow renders the assets directly from source; no API keys or image generation services are required.

The contribution graph continues to use the existing `output` branch and workflow. It is kept in its own expandable section.
