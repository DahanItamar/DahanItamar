# Profile components

The profile opens with centered, static native headings and text, using GitHub's own font, heading sizes and page background. The project graphics retain the poster's graphite and lime palette. Icon SVGs are stored in this repository, so viewing them does not depend on the generator being online.

| Component | Source | Setup |
|:--|:--|:--|
| Name, subtitle and headline | Native HTML headings/text | Static, centered, without an image or custom background. GitHub controls the font and heading sizes. |
| Archived header graphic | [kyechan99/capsule-render](https://github.com/kyechan99/capsule-render) | Retained from the previous preview; not embedded in the current README. Parameters in `sources.json`. |
| Archived typing graphic | [DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) | Retained from the previous preview; not embedded in the current README. |
| Technology icons | [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons) | Generated dark/light SVGs for the profile's existing stack. |
| AI and automation icons | [lobehub/lobe-icons](https://github.com/lobehub/lobe-icons) | Static Claude Code, Codex, Gemini and n8n logos, with native text labels. Vendored unmodified from commit `82e641b4fece9d1028a127149af9ded00df5ac0c`; source URLs in `sources.json`. |
| Contribution game | [abozanona/pacman-contribution-graph](https://github.com/abozanona/pacman-contribution-graph) | Existing daily workflow and `output` branch, retained unchanged. |
| Repository cards | Original SVGs | Inspired by the clickable card pattern in [github-readme-stats](https://github.com/anuraghazra/github-readme-stats); no code copied and no statistics invented. |
| Acceptance-criterion path | Original SVGs | Finite 4.4-second animation, with static reduced-motion sources and a mobile layout. |
| DockNest banner | Built-in image generation tool | Derived from the approved poster; illustrative artwork, not a screenshot. |

MIT notices for the four vendored component tools are in [`licenses`](licenses). Geist's [Open Font License](../fonts/OFL.txt) is also retained. The original cards and process diagram use system fonts.

The AI row reflects the owner's coding workflow and project documentation: Claude Code in ReelScribe and the agent skills, Codex in the coding workflow, Gemini in SmartDataMatcher, and n8n for automation. These identify tools used, not endorsements. Private project documentation is not copied into this repository.

The whole poster is retained as a separate artifact. The README's project links, descriptions, catalogue and text alternative remain native Markdown/HTML. No JavaScript, iframe, private repository token or new deployment is required.

## Rebuild

```sh
python scripts/build_component_readme.py
```

To regenerate the public-service snapshots separately:

```sh
python scripts/refresh_readme_components.py
```

The refresh downloads and validates all eight SVGs before replacing any existing snapshot. The AI logo URLs are pinned to a source commit. The contribution graph continues to refresh through its existing workflow. Source links and SVG parameters were checked on 2026-10-06.

## Previous versions and maintenance files

These are kept in the repository, outside the public profile layout:

- [Portfolio poster](../portfolio-poster.png)
- [Text version](../../STATIC.md)
- [Original README](../../archive/README-2026-10-06-before-redesign.md)
- [Poster preview](../../archive/README-2026-10-06-poster-preview.md)
- [Restore instructions](../../RESTORE.md)

## DockNest artwork

The banner's exact generation prompt is recorded in [`docknest-banner-prompt.md`](docknest-banner-prompt.md).
