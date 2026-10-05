# Profile components

The profile opens with centered, static native headings and text, using GitHub's own font, heading sizes and page background. Badges and repository cards use transparent backgrounds, themed text and green accents. Icon SVGs are stored in this repository, so viewing them does not depend on the generator being online.

| Component | Source | Setup |
|:--|:--|:--|
| Name, subtitle and headline | Native HTML headings/text | Static, centered, without an image or custom background. GitHub controls the font and heading sizes. |
| Archived header graphic | [kyechan99/capsule-render](https://github.com/kyechan99/capsule-render) | Retained from the previous preview; not embedded in the current README. Parameters in `sources.json`. |
| Archived typing graphic | [DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) | Retained from the previous preview; not embedded in the current README. |
| Development badges | [simple-icons/simple-icons](https://github.com/simple-icons/simple-icons) and [devicons/devicon](https://github.com/devicons/devicon) | Ten individual static SVG badges. Simple Icons provides nine logos; Devicon provides C#. Original logo paths retained, with themed fills inside transparent badge frames. Sources pinned in `badge-sources.json`. |
| AI and automation badges | [lobehub/lobe-icons](https://github.com/lobehub/lobe-icons) | Four individual static badges for Claude Code, Codex, Gemini and n8n. Monochrome logo paths from commit `82e641b4fece9d1028a127149af9ded00df5ac0c`, recolored lime. Sources pinned in `badge-sources.json`. |
| Archived technology icons | [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons) | Original dark/light icon strips retained for restoration; not embedded in the current README. |
| Contribution game | [abozanona/pacman-contribution-graph](https://github.com/abozanona/pacman-contribution-graph) | Existing daily workflow and `output` branch, retained unchanged. |
| Repository cards | Original SVGs | Four featured projects—DockNest, Slotline, Winnow and House Rules—share the same 420 × 190 layout, transparent background, typography, spacing and themed highlights. Two rows of two cards use equal 48% widths. Each card links to its repository; project descriptions are inside the cards. The GitCheckup graphic is retained outside the current profile. Inspired by the clickable card pattern in [github-readme-stats](https://github.com/anuraghazra/github-readme-stats); no code copied and no statistics invented. |
| Archived acceptance-criterion path | Original SVGs | Finite 4.4-second animation, with static reduced-motion sources and a mobile layout. Retained for restoration; not embedded in the current README. |
| Archived DockNest banner | Built-in image generation tool | Derived from the approved poster; illustrative artwork, not a screenshot. Retained for restoration; the current README uses the matching SVG card instead. |

MIT notices for the vendored component tools, including Lobe Icons and Devicon, and Simple Icons' CC0 license are in [`licenses`](licenses). Geist's [Open Font License](../fonts/OFL.txt) is also retained. The original badges, cards and process diagram use system fonts.

Every badge is a separate SVG with its own icon, name and accessible alternative text. All fourteen share the same 42-pixel height and transparent background, allowing GitHub's page background to show through. Dark variants use lime `#c6f27f` icons and off-white `#f0f2eb` text; light variants use darker green `#456c17` icons and dark `#1f2328` text. Both have subtle borders. Cards use the same transparent background and theme handling. Each image has its own `<picture>` element to select the color scheme, and separate badges allow rows to wrap on narrower screens. The original downloaded logos live in `badges/logos`; the builder creates the styled badge files without modifying those sources.

The AI row reflects the owner's coding workflow and project documentation: Claude Code in ReelScribe and the agent skills, Codex in the coding workflow, Gemini in SmartDataMatcher, and n8n for automation. These identify tools used, not endorsements. Private project documentation is not copied into this repository.

The whole poster is retained as a separate artifact. The profile presents the owner's [website](https://itamardahan.com/) near the top, four selected systems, a short native-text "My signature" section and contribution activity. The signature connects the featured projects through verifiable recovery, database-protected bookings, traceable sources, local-first tools and offline games. The engineering workflow graphic, long project catalogue, skills list, About/principles sections and closing contact link are retained in previous versions rather than displayed in the current README. The text alternative follows the same selection and signature text. No JavaScript, iframe, private repository token or new deployment is required.

## Rebuild

```sh
python scripts/build_component_readme.py
```

To regenerate the public-service snapshots separately:

```sh
python scripts/refresh_readme_components.py
```

The refresh downloads and validates all source SVGs before replacing any existing snapshot. Badge logo URLs are pinned to source commits. Run `build_component_readme.py` after refreshing to rebuild the styled badges. The contribution graph continues to refresh through its existing workflow. Source links and SVG parameters were checked on 2026-10-06.

## Previous versions and maintenance files

These are kept in the repository, outside the public profile layout:

- [Portfolio poster](../portfolio-poster.png)
- [Text version](../../STATIC.md)
- [Original README](../../archive/README-2026-10-06-before-redesign.md)
- [Poster preview](../../archive/README-2026-10-06-poster-preview.md)
- [Restore instructions](../../RESTORE.md)

## DockNest artwork

The banner's exact generation prompt is recorded in [`docknest-banner-prompt.md`](docknest-banner-prompt.md).
