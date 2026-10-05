# Profile components

The profile uses composable GitHub README graphics, with the poster's graphite and lime palette. The generated header, typing and icon SVGs are stored in this repository, so viewing the README does not depend on those generators being online.

| Component | Source | Setup |
|:--|:--|:--|
| Header with a short fade | [kyechan99/capsule-render](https://github.com/kyechan99/capsule-render) | Generated SVG; parameters in `sources.json`. |
| Typing headline | [DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) | Generated SVG; runs once for 4.4 seconds. Static source selected for reduced motion. |
| Technology icons | [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons) | Generated dark/light SVGs for the profile's existing stack. |
| Contribution game | [abozanona/pacman-contribution-graph](https://github.com/abozanona/pacman-contribution-graph) | Existing daily workflow and `output` branch, retained unchanged. |
| Repository cards | Original SVGs | Inspired by the clickable card pattern in [github-readme-stats](https://github.com/anuraghazra/github-readme-stats); no code copied and no statistics invented. |
| Acceptance-criterion path | Original SVGs | Finite 4.4-second animation, with static reduced-motion sources and a mobile layout. |
| DockNest banner | Built-in image generation tool | Derived from the approved poster; illustrative artwork, not a screenshot. |

MIT notices for the three vendored component tools are in [`licenses`](licenses). Geist's [Open Font License](../fonts/OFL.txt) is also retained. The original cards and process diagram use system fonts.

The whole poster is retained as a separate artifact. The README's project links, descriptions, catalogue and text alternative remain native Markdown/HTML. No JavaScript, iframe, private repository token or new deployment is required.

## Rebuild

```sh
python scripts/build_component_readme.py
```

To regenerate the public-service snapshots separately:

```sh
python scripts/refresh_readme_components.py
```

The refresh downloads and validates all four SVGs before replacing any existing snapshot. The contribution graph continues to refresh through its existing workflow. Source links and SVG parameters were checked on 2026-10-06.

## DockNest artwork

The banner's exact generation prompt is recorded in [`docknest-banner-prompt.md`](docknest-banner-prompt.md).
