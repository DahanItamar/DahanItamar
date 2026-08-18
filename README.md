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
| [**HeWordle**](https://github.com/DahanItamar/HeWordle)<br><samp>↗ [wordlehebrew.com](https://wordlehebrew.com)</samp> | Daily Hebrew Wordle, playable now and self-hostable — accounts, streaks, leaderboard. Zero npm dependencies, answers encrypted at rest, WCAG 2.1 AA. | <samp>Node.js · SQLite</samp> |
| [**Slotline**](https://github.com/DahanItamar/Slotline) | Multi-tenant booking system for rooms, equipment and consultants. Double-booking is made impossible by a Postgres exclusion constraint rather than by application code; tenant isolation by row-level security; live calendars over SSE. | <samp>TypeScript · Fastify · Postgres</samp> |
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

Reusable skills that shape *how* the work gets done — the engineering discipline above, packaged so it applies on every project instead of being remembered on each one. Four standalone plugins for Claude Code.

| Plugin | About | |
|:--|:--|:--|
| [**spec-architect**](https://github.com/DahanItamar/spec-architect) | The six-stage spec chain — `constitution → spec → tasks → implement → drift → refactor`. Every requirement is one EARS sentence with a stable `AC-###`; each stage cites, verifies or reports against that same number, so *done* is checked rather than felt. The last stage restructures only what blocks scheduled work, and may not reword a single criterion doing it. | <samp>7&nbsp;skills</samp> |
| [**readme-architect**](https://github.com/DahanItamar/readme-architect) | Writes a README after running the project, not after reading its folder names — real output, observed numbers, a diagram of the mechanism, and badges that each state a fact you can check. Writes no number it did not measure. | <samp>7&nbsp;files</samp> |
| [**uilint**](https://github.com/DahanItamar/uilint) | Catches the interface states that get skipped because whoever built it only clicked the path that works — loading, empty, error, success, partial. Blocks on the 16 that cause silent user harm; the other 23 only report. | <samp>39&nbsp;rules</samp> |
| [**acsm**](https://github.com/DahanItamar/acsm) | Works out which laws actually bind a project and loads only those modules — a local desktop tool in Israel reads three of eight and never sees the CCPA. Every obligation carries its citation, and the build fails if one loses it. | <samp>83&nbsp;checks</samp> |

## Contributions

<div align="center">

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph.svg" />
  <img alt="Pac-Man eating my contribution graph" src="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph.svg" width="100%" />
</picture>

</div>
