<div align="center">

# Itamar Dahan

<samp>FULL-STACK&nbsp;&nbsp;&amp;&nbsp;&nbsp;AUTOMATION&nbsp;&nbsp;DEVELOPER</samp>

<samp>clean architecture&nbsp;&nbsp;·&nbsp;&nbsp;AI-driven engineering&nbsp;&nbsp;·&nbsp;&nbsp;intelligent automation</samp>

<samp>[itamardahan1111d@gmail.com](mailto:itamardahan1111d@gmail.com)</samp>

</div>

---

## About

I build web applications end to end — server, data and interface — with a focus on code that stays readable, secure and maintainable long after it ships. My work spans games, scheduling systems, education platforms and business websites.

**AI is at the center of how I work — twice over.** *As an engineering method*, I develop with Claude Code and LLM-assisted workflows across the whole cycle: architecture, implementation, review and testing. *As a product capability*, I design intelligent automations with n8n and LLM APIs — connecting services, orchestrating agents, turning manual processes into systems that run themselves.

- **Architecture first** — small classes, clear layers, code that explains itself
- **Zero-dependency mindset** — fewer moving parts, fewer things that break
- **Security by default** — encryption at rest, proper password hashing, secrets never in git
- **Accessible** — built to WCAG 2.1 AA, keyboard and screen-reader friendly

<samp>**Core**&nbsp;&nbsp;&nbsp;JavaScript&nbsp;&nbsp;·&nbsp;&nbsp;TypeScript&nbsp;&nbsp;·&nbsp;&nbsp;Node.js&nbsp;&nbsp;·&nbsp;&nbsp;C#&nbsp;&nbsp;·&nbsp;&nbsp;.NET&nbsp;&nbsp;·&nbsp;&nbsp;PostgreSQL&nbsp;&nbsp;·&nbsp;&nbsp;SQLite&nbsp;&nbsp;·&nbsp;&nbsp;Docker</samp>

<samp>**AI**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Claude Code&nbsp;&nbsp;·&nbsp;&nbsp;n8n&nbsp;&nbsp;·&nbsp;&nbsp;LLM APIs&nbsp;&nbsp;·&nbsp;&nbsp;agent workflows</samp>

## Selected Work

| Project | About | Stack |
|:--|:--|:--|
| [**GitCheckup**](https://github.com/DahanItamar/GitCheckup)<br><samp>↗ [gitcheckup.com](https://gitcheckup.com)</samp> | Scores any public GitHub repository out of 100 — docs, community, activity, popularity and hygiene — and returns a ranked list of what to fix rather than just a number. | <samp>TypeScript · Next.js</samp> |
| [**Slotline**](https://github.com/DahanItamar/Slotline) | Multi-tenant booking system for rooms, equipment and consultants. Double-booking is made impossible by a Postgres exclusion constraint rather than by application code; tenant isolation by row-level security; live calendars over SSE. | <samp>TypeScript · Fastify · Postgres</samp> |
| [**HeWordle**](https://github.com/DahanItamar/HeWordle)<br><samp>↗ [wordlehebrew.com](https://wordlehebrew.com)</samp> | Daily Hebrew Wordle, playable now and self-hostable — accounts, streaks, leaderboard. Zero npm dependencies, answers encrypted at rest, WCAG 2.1 AA. | <samp>Node.js · SQLite</samp> |
| [**Airport Simulator**](https://github.com/DahanItamar/AirportSimulator) | Real-time airport simulation — arrivals and departures competing for a shared runway and gates, watched live from a zero-dependency control-tower UI. | <samp>C# · ASP.NET Core · JS</samp> |
| [**ShortLinks**](https://github.com/DahanItamar/ShortLinks-Project) | URL shortener with per-user click analytics — Google sign-in, ownership-guarded click logs, short codes from `RandomNumberGenerator` rather than a seeded `Random`. | <samp>C# · ASP.NET Core · EF Core</samp> |
| [**Dealership Platform**](https://github.com/DahanItamar/dealership-platform) | White-label bilingual (RTL) car-dealership platform — showroom, financing, leads and a full admin back office, with a zero-setup in-memory demo mode. | <samp>TypeScript · TanStack · Supabase</samp> |
| [**Warehouse Serial Scanner**](https://github.com/DahanItamar/warehouse-serial-scanner) | Touchscreen warehouse intake station — barcode scanning, on-screen keypad checkout, pluggable SQL Server/MySQL/Postgres with a zero-setup mock mode. | <samp>Node.js · Express</samp> |

<details>
<summary><samp>Also built&nbsp;&nbsp;(6 more projects)</samp></summary>

<br>

| Project | About | Stack |
|:--|:--|:--|
| **Smart Data Matcher** | AI-powered spreadsheet normalizer — LLM column mapping, value cleanup and rule-based filtering, from messy export to standard schema. | <samp>TypeScript · Gemini · Supabase</samp> |
| **Market News Engine** | Autonomous market and stock-news content pipeline — AI-generated posts, stories, tweets and short-form video, published across X, Threads, Instagram and Facebook. | <samp>n8n · LLM APIs · Social APIs</samp> |
| **TeachersPlatform** | Marketplace connecting music teachers and students — granular service listings, faceted search, escrow-protected payments. Hebrew-first, full RTL. | <samp>TypeScript · Next.js · Prisma</samp> |
| **Shift Harmony** | Shift-scheduling platform — planning and managing team work schedules through a refined, component-driven interface. | <samp>React · TypeScript · Cloudflare</samp> |
| **SmartRadar** | Personal event radar — curates and ranks concerts and events by taste, distance and price. Installable web app, Hebrew RTL. | <samp>JavaScript · PWA</samp> |
| [**Calculator**](https://github.com/DahanItamar/Calculator) | Web calculator with a real expression engine — operator precedence, no `eval`, keyboard support. | <samp>HTML · CSS · JS</samp> |

</details>

## Skills for AI coding agents

Reusable skills that shape *how* the work gets done — the engineering discipline above, packaged so it applies on every project instead of being remembered on each one.

| Skill | What it does | Use it when |
|:--|:--|:--|
| [**spec-architect**](https://github.com/DahanItamar/flowsystem/tree/main/plugins/flowsystem/skills/spec-architect) | Turns a rough idea into an engineering-grade technical spec — architecture, data models, interfaces, edge cases and risks — before any code is written. Asks only the questions where two answers produce two different systems, then decides the rest and writes the assumptions down where they can be rejected. | Starting a project or a major feature from a loose description |
| [**spec-drift**](https://github.com/DahanItamar/flowsystem/tree/main/plugins/flowsystem/skills/spec-drift) | Checks whether the code still matches the spec and realigns whichever side is wrong. Reports gaps as regressions or staleness — never silently rewrites either one. | Returning to a project, finishing a milestone, or onboarding anyone onto a codebase that has a spec |
| [**readme-architect**](https://github.com/DahanItamar/readme-architect/blob/main/SKILL.md) | Writes a README from evidence rather than adjectives — runs the project first, then fills a tight skeleton with real output, observed numbers and the exact setup path. Refuses badge walls, empty sections, and any number it did not measure. | Making a repo public, or fixing a README that describes the project instead of showing it |
| [**uilint**](https://github.com/DahanItamar/uilint/blob/main/SKILL.md) | Catches the interface states that get skipped because whoever built it only clicked the path that works — loading, empty, error, success and partial. Blocks only on the ones that cause silent user harm, and reports each as the consequence a user would feel rather than as a rule number. | Building or reviewing any UI that fetches, submits or navigates |

All of them live in one catalogue, [**ai-skills**](https://github.com/DahanItamar/ai-skills). Add it once, install whichever you want:

```
/plugin marketplace add DahanItamar/ai-skills
/plugin install uilint@dahanitamar
```

In the VS Code extension the command is `/plugins`, plural, and opens a dialog instead. Each skill is ultimately a single `SKILL.md` — Markdown, no code, nothing to install — so dropping the file in works just as well in Cursor, Codex, or any agent that reads Markdown.

## Contributions

<div align="center">

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph.svg" />
  <img alt="Pac-Man eating my contribution graph" src="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph.svg" width="100%" />
</picture>

</div>
