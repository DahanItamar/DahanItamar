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

Reusable skills that shape *how* the work gets done — the engineering discipline above, packaged so it applies on every project instead of being remembered on each one.

Three plugins, each standalone. Every repository is its own marketplace, so there is no catalogue to add first.

### [spec-architect](https://github.com/DahanItamar/spec-architect) — the five-stage spec chain

`constitution → spec → tasks → implement → drift`, and a front door that tells you which stage you are at. What travels between them is an identifier: every requirement is one EARS sentence with a stable `AC-###`, and each stage cites, verifies, or reports against the same number. That traceability is the whole reason it is more than five prompts that happen to run in order.

| Stage | Skill | What it does |
|:-:|:--|:--|
| — | [**spec-start**](https://github.com/DahanItamar/spec-architect/blob/main/skills/spec-start/SKILL.md) | Reads the repo, prints the chain, and names the one command to run next |
| 1 | [**spec-constitution**](https://github.com/DahanItamar/spec-architect/blob/main/skills/spec-constitution/SKILL.md) | The repo's rules and its verify command. A rule earns its place only if you can name what breaks without it |
| 2 | [**spec-architect**](https://github.com/DahanItamar/spec-architect/blob/main/skills/spec-architect/SKILL.md) | Turns a rough idea into a spec precise enough to build from. Asks only the questions where two answers produce two different systems, then decides the rest and writes the assumptions down where they can be rejected |
| 3 | [**spec-tasks**](https://github.com/DahanItamar/spec-architect/blob/main/skills/spec-tasks/SKILL.md) | An ordered list where every task names the criteria it closes. A task closing nothing is either unnecessary or a requirement nobody wrote |
| 4 | [**spec-implement**](https://github.com/DahanItamar/spec-architect/blob/main/skills/spec-implement/SKILL.md) | One task, verified, then the next — stopping at the first unmet criterion instead of building nine tasks on top of a broken one |
| 5 | [**spec-drift**](https://github.com/DahanItamar/spec-architect/blob/main/skills/spec-drift/SKILL.md) | Whether the code still matches the spec, and *which side is wrong* — regression or staleness, never a silent rewrite of either |

```
/plugin marketplace add DahanItamar/spec-architect
/plugin install spec-architect@spec-architect
```

### [readme-architect](https://github.com/DahanItamar/readme-architect) — READMEs from evidence

Writes a README after running the project, not after reading its folder names. Real output, observed numbers, a mermaid diagram of the mechanism, and an identity block where every badge states a fact you can check — a status, a version, a count, or a licence. It writes no number it did not measure, references no image it did not produce, and tells you plainly what it could not verify.

```
/plugin marketplace add DahanItamar/readme-architect
/plugin install readme-architect@readme-architect
```

### [uilint](https://github.com/DahanItamar/uilint) — the states everyone forgets

Catches the interface states that get skipped because whoever built it only clicked the path that works — loading, empty, error, success and partial. 39 rules, of which 16 block completion and 23 only report: a gate trusted enough to leave switched on is worth more than a stricter one disabled in week two. Findings read as the consequence a user would feel, not as a rule number.

```
/plugin marketplace add DahanItamar/uilint
/plugin install uilint@uilint
```

In the VS Code extension the command is `/plugins`, plural, and opens a dialog instead — the `/plugin` lines above are terminal-CLI syntax and do nothing there. Each skill is ultimately a `SKILL.md` — Markdown, no code, nothing to install — so dropping the file into `~/.claude/skills/` works too, as does pasting it into Cursor, Codex, or any agent that reads Markdown.

## Contributions

<div align="center">

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph.svg" />
  <img alt="Pac-Man eating my contribution graph" src="https://raw.githubusercontent.com/DahanItamar/DahanItamar/output/pacman-contribution-graph.svg" width="100%" />
</picture>

</div>
