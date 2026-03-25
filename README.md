# Local AI Engineering Mesh

[中文](README.zh-CN.md) | [English](README.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md)

Upgrade your AI tools from isolated assistants into a governed, memory-backed, evidence-driven engineering system.

This repository is not a chat prompt pack. It is a repository-shaped operating model for upgrading local AI tools from “can answer” to “can run a disciplined engineering workflow.”

It reflects a bigger idea: Codex is not running alone. In this setup, Codex, Cursor, Antigravity, Claude Code, and OpenCode can be treated as specialized endpoints inside one cross-platform AI coding system, coordinated through a unified `AGENTS.md`.

## Why this exists

Most people do not really have an AI system.
They have several tools they keep switching between:
- one for coding
- one for research
- one for browser-heavy work
- one fallback tool when the first one feels weak

That creates a familiar failure pattern:
- repeated tool switching
- duplicated instructions
- unstable memory across tools
- drifting output style and quality bar
- dependence on whichever one product currently feels best

This repository exists to solve that problem.

The goal is not to worship one tool.
The goal is to make multiple local AI tools behave like one coordinated engineering system.

## What this upgrades

- `shared law`: one top-level operating model through `AGENTS.md`
- `memory`: persistent working law, routing rules, and project state
- `bootstrap`: project initialization for commands, memory, and risk posture
- `orchestration`: explicit roles for planning, design, verification, and release
- `planning`: parallel research and structured execution plans
- `evidence`: completion requires proof instead of narrative
- `release safety`: preview-first and publish gates
- `evolution`: repeated wins can become native reusable skills

## Live system snapshot

This repository is based on a real working local setup. At the time of writing, the live environment behind it includes:
- `30` Codex skills in `~/.codex/skills`
- `3` global memory files in `~/.codex/memories`
- `10` project governance commands in `.codex/commands`
- `5` project memory files in `.codex/memory`
- active project state files in `.codex/state`

That means this is not just a theory post. It is already operating at:
- rules layer
- skill layer
- project runtime layer
- state layer
- evidence layer

## Four-tool assessment on this machine

These are not universal benchmark scores. They are architecture-level assessments of one real local setup as of **March 25, 2026**.

### Codex — 92/100
**Role:** primary engineering execution and governance hub.

**Strengths**
- strongest local execution center in this setup
- governed skills, commands, release discipline, and evidence workflow
- best fit for turning plans into disciplined project delivery

**Limitations**
- default product smoothness and automation feel can still be less natural than Claude in some workflows

### Claude — 90/100
**Role:** workflow methodology engine and reference stack.

**Strengths**
- strongest command-and-workflow feel
- strong modular thinking, review habits, and collaboration ergonomics
- still the most mature benchmark for coding workflow design

**Limitations**
- in this specific local system, it is not as deeply integrated into execution governance as Codex

### Cursor — 89/100
**Role:** IDE battlefield and editor-native implementation layer.

**Strengths**
- closest to the coding surface
- strong project rule density inside the editor
- ideal for reducing day-to-day development friction

**Limitations**
- weaker system-governance and operating-system feel than Codex or Antigravity

### Antigravity — 91/100
**Role:** broad capability expansion platform.

**Strengths**
- wide coverage across browsing, artifacts, knowledge, and extended skills
- feels more like a platform than a single tool
- excellent for capability expansion and cross-domain work

**Limitations**
- breadth can introduce noise
- for the core engineering path, it is not always as steady as Codex

### Overall local system — 91/100
This machine is strongest not because one single AI is unbeatable, but because the tools have been organized into one system:
- shared operating law
- multiple specialized endpoints
- project memory
- execution gates
- cross-platform consistency

The most accurate summary is:

**Shared Law + Multi-Tool Specialized AI System**

This is no longer a “pick one tool” setup.
It is a coordinated local AI engineering mesh.

## Cross-platform setup

In the live environment behind this repository:
- `~/.codex/config.toml` loads `~/AGENTS.md` through `model_instructions_file`
- `~/.codex/instructions.md` adds Codex-specific routing, profiles, and skill guidance
- the same top-level operating law is shared across multiple coding tools

This means the system here is both:
- tool-native in execution
- cross-platform in policy

It also means your workflow does not need to reset every time you switch tools.

See [CROSS-PLATFORM.md](docs/CROSS-PLATFORM.md).

## Compared with the latest Claude

As of **March 23, 2026**, Anthropic's latest public Claude coding stack is led by:
- `Claude Opus 4.6` published on **February 5, 2026**
- `Claude Sonnet 4.6` published on **February 17, 2026**

This repository does **not** claim that a local tool automatically beats Claude on raw model capability.

It makes a narrower and more useful claim:

If you give local AI tools a stronger operating system layer, they become much more competitive on long-horizon engineering execution because the workflow stops depending on one perfect prompt or one permanently available product.

See [COMPARE-WITH-CLAUDE.md](docs/COMPARE-WITH-CLAUDE.md).

## Repository map

```text
local-ai-engineering-mesh/
├── README.md
├── README.zh-CN.md
├── README.ru.md
├── README.ja.md
├── README.fr.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── COMPARE-WITH-CLAUDE.md
│   ├── CROSS-PLATFORM.md
│   ├── EXECUTION-LOOP.md
│   ├── REPO-MAP.md
│   ├── STACK.md
│   └── FRAMEWORK-DIAGRAM.md
└── templates/
    ├── antigravity/
    ├── cursor/
    ├── global-memory/
    ├── project-memory/
    └── policy.env.example
```

See [REPO-MAP.md](docs/REPO-MAP.md).

## Included templates

This repository includes reusable templates for:
- global memory
- project memory
- Cursor project rules
- Antigravity workflow and knowledge stubs
- policy defaults

Adoption paths:
- single-tool first
- dual-tool setup
- full mesh: Codex + Cursor + Antigravity + Claude under one shared law

## References

- [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/)
- [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)
- [Introducing Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- [Compound Engineering plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [shinpr/agentic-code](https://github.com/shinpr/agentic-code)
- [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)
