# Local AI Engineering Mesh

[中文](README.zh-CN.md) | [English](README.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md)

Upgrade your local AI tools from isolated assistants into one governed, memory-backed, evidence-driven engineering system.

This repository is not a prompt pack and not a skill collection. It is a public-safe operating model for turning multiple AI tools into one coordinated local engineering mesh.

## Core idea

Most people do not really have an AI system.
They have several tools they keep switching between.

This repository is built around a different idea:

- one shared law
- multiple specialized endpoints
- one project runtime model
- one quality bar across tools

The goal is not to make one tool worship-worthy.
The goal is to make multiple tools work together without resetting your workflow every time you switch.

## System framework

This mesh is organized in layers.

### 1. Shared law layer
The top layer defines one common engineering law for every endpoint.

Examples:
- shared operating rules
- task discipline
- quality bar
- release discipline
- evidence requirements

Anchor file:
- `AGENTS.md`

### 2. Tool adapter layer
Each AI tool keeps its own native strengths, but plugs into the same law.

Adapters in this repository are framed around:
- Codex
- Claude
- Cursor
- Antigravity

### 3. Capability layer
This layer contains reusable capabilities instead of one-off prompts.

Examples:
- skills
- rules
- workflows
- role packs
- reviewers
- deploy / QA / security helpers

### 4. Project runtime layer
This layer makes the system usable inside a real repo.

Examples:
- project commands
- project memory
- project state
- evidence collection
- execution checkpoints

### 5. Evolution layer
This layer turns repeated wins into reusable system behavior.

Examples:
- memory accumulation
- reusable patterns
- promoted workflows
- specialist review loops

## Four-tool structure and evaluation

These scores are not universal benchmarks. They are architecture-level assessments of one real local setup as of **March 25, 2026**.

### Codex — 92/100
**Position in the mesh:** execution core and governance core.

**Structural layers**
- adapter layer: Codex configuration and endpoint routing
- capability layer: governed skills, reviewers, execution roles
- runtime layer: command wrappers, state, evidence, release gates
- evolution layer: skill promotion and reusable engineering patterns

**What it is best at**
- disciplined local execution
- terminal-first engineering flow
- release and publish governance
- turning plans into deliverable project work

**Current limitation**
- product smoothness and built-in automation feel can still be less polished than Claude in some workflows

### Claude — 90/100
**Position in the mesh:** workflow methodology engine and benchmark layer.

**Structural layers**
- adapter layer: shared-law alignment and workflow compatibility
- capability layer: command culture, modular review habits, collaboration patterns
- runtime layer: strong methodology, less deep execution governance in this setup
- evolution layer: benchmark source for workflow maturity

**What it is best at**
- workflow ergonomics
- modular thinking
- review culture
- polished collaboration feel

**Current limitation**
- in this local system, it is not the deepest execution/governance endpoint

### Cursor — 89/100
**Position in the mesh:** IDE battlefield and editor-native implementation layer.

**Structural layers**
- adapter layer: editor-facing rule alignment
- capability layer: project-local editor rules and implementation guidance
- runtime layer: fast inline coding and low-friction daily development
- evolution layer: project-level coding habits and local delivery patterns

**What it is best at**
- staying close to the coding surface
- reducing day-to-day development friction
- keeping project rules near the editor

**Current limitation**
- weaker operating-system feel and cross-tool governance depth than Codex or Antigravity

### Antigravity — 91/100
**Position in the mesh:** broad capability platform and expansion layer.

**Structural layers**
- adapter layer: platform-facing workflow alignment
- capability layer: broad skills, browser work, knowledge, artifacts
- runtime layer: strong cross-domain execution and workflow expansion
- evolution layer: broad reusable capability growth

**What it is best at**
- expanding beyond narrow coding tasks
- browser-heavy and artifact-heavy work
- acting more like a platform than a single tool

**Current limitation**
- breadth can introduce noise; on the core engineering path it is not always as steady as Codex

## Overall system evaluation — 91/100

This machine is strong not because one tool is unbeatable.
It is strong because the tools have been organized into one system.

That system now has:
- shared operating law
- specialized tool endpoints
- project memory
- execution gates
- evidence discipline
- cross-platform consistency

The most accurate summary is:

**Shared Law + Multi-Tool Specialized AI System**

This is no longer a “pick one tool” setup.
It is a coordinated local AI engineering mesh.

## Public-safe implementation view

To keep this repository safe to publish, local machine details are abstracted into generic layers instead of personal filesystem layout.

Public-safe labels used in this repository:
- `$SHARED_LAW_HOME/AGENTS.md`
- `$CODEX_HOME/config.toml`
- `$CODEX_HOME/instructions.md`
- `$CODEX_HOME/skills/`
- `$CODEX_HOME/memories/`
- `<project>/.codex/commands/`
- `<project>/.codex/memory/`
- `<project>/.codex/state/`
- `<project>/.cursor/rules/`
- `<antigravity-home>/skills|workflows|knowledge`

The purpose is to publish the system design without leaking personal machine structure.

## Live system snapshot (sanitized)

This repository is based on a real working setup. In sanitized form, the live environment behind it includes:
- 30 Codex skills
- 3 global memory files
- 10 project governance commands
- 5 project memory files
- active project state files

That means this is not only a concept. It is already operating at:
- rules layer
- capability layer
- project runtime layer
- state layer
- evidence layer

## Cross-platform design

In this repository’s model:
- one shared law sits at the top
- Codex acts as the strongest execution endpoint
- Claude remains a strong workflow benchmark and compatible peer
- Cursor acts as the IDE-native delivery layer
- Antigravity acts as the capability-expansion platform

So the workflow does not have to restart from zero every time you switch tools.

See [CROSS-PLATFORM.md](docs/CROSS-PLATFORM.md).

## Compared with the latest Claude

As of **March 23, 2026**, Anthropic's latest public Claude coding stack is led by:
- `Claude Opus 4.6` published on **February 5, 2026**
- `Claude Sonnet 4.6` published on **February 17, 2026**

This repository does **not** claim that a local tool automatically beats Claude on raw model capability.

Its claim is narrower and more practical:

Once local tools are upgraded with memory, governance, evidence, and release discipline, they become much more competitive on long-horizon engineering execution.

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
- Cursor rule patterns
- Antigravity workflow and knowledge stubs
- policy defaults

Adoption paths:
- single-tool first
- dual-tool setup
- full mesh: Codex + Claude + Cursor + Antigravity under one shared law

## References

- [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/)
- [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)
- [Introducing Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- [Compound Engineering plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [shinpr/agentic-code](https://github.com/shinpr/agentic-code)
- [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)
