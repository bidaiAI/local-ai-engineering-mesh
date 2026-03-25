# Local AI Engineering Mesh

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) ![Mesh](https://img.shields.io/badge/System-Local%20AI%20Engineering%20Mesh-6f42c1) ![Tools](https://img.shields.io/badge/Tools-Codex%20%7C%20Claude%20%7C%20Cursor%20%7C%20Antigravity-blue) ![Status](https://img.shields.io/badge/Status-Public--Safe-success)

[中文](README.zh-CN.md) | [English](README.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md)

A public-safe operating model for turning local AI tools into one governed, memory-backed, evidence-driven engineering system.

This repository is not a prompt pack and not a skill collection. It is a structured reference for building a multi-tool local AI workflow with shared rules, explicit roles, project runtime discipline, and reusable system patterns.

## Why this repository exists

Most people do not really have an AI system.
They have several tools they keep switching between.

That usually creates the same failure pattern:
- duplicated instructions
- unstable memory between tools
- inconsistent quality bars
- repeated context reset when switching
- dependence on whichever product feels best that week

This repository proposes a different model:
- one shared law
- multiple specialized endpoints
- one project runtime model
- one quality bar across tools

The point is not to make one tool do everything.
The point is to make multiple tools work together without collapsing the workflow every time you switch.

## At-a-glance architecture

```mermaid
flowchart TD
    A["Shared Law
AGENTS.md"] --> B["Codex
Execution Core
92/100"]
    A --> C["Claude
Workflow Benchmark
90/100"]
    A --> D["Cursor
IDE Delivery Layer
89/100"]
    A --> E["Antigravity
Capability Platform
91/100"]

    B --> F["Project Runtime
commands / memory / state / evidence"]
    C --> G["Methodology
review / command culture / collaboration"]
    D --> H["Editor Surface
project rules / low-friction implementation"]
    E --> I["Expansion Surface
browser / artifacts / knowledge / workflows"]

    F --> J["Release Discipline"]
    F --> K["Evidence Gate"]
    F --> L["Reusable Patterns"]
```

## What this repository includes

- a layered system design
- a four-tool role model for Codex, Claude, Cursor, and Antigravity
- public-safe path conventions
- reusable templates for memory, rules, and workflows
- operating documents for governance, memory, and bootstrap
- diagrams and comparison notes for cross-platform usage

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

## Four-tool role model and reference assessment

These scores are not universal benchmarks. They are a reference assessment of one real local setup as of **March 25, 2026**.

### Codex — 92/100
**Role in the mesh:** execution core and governance core.

**Structural layers**
- adapter layer: Codex configuration and endpoint routing
- capability layer: governed skills, reviewers, execution roles
- runtime layer: command wrappers, state, evidence, release gates
- evolution layer: skill promotion and reusable engineering patterns

**Best fit**
- disciplined local execution
- terminal-first engineering flow
- release and publish governance
- turning plans into deliverable project work

**Current tradeoff**
- product smoothness and built-in automation feel can still be less polished than Claude in some workflows

### Claude — 90/100
**Role in the mesh:** workflow methodology engine and benchmark layer.

**Structural layers**
- adapter layer: shared-law alignment and workflow compatibility
- capability layer: command culture, modular review habits, collaboration patterns
- runtime layer: strong methodology, less deep execution governance in this setup
- evolution layer: benchmark source for workflow maturity

**Best fit**
- workflow ergonomics
- modular thinking
- review culture
- polished collaboration feel

**Current tradeoff**
- in this local system, it is not the deepest execution/governance endpoint

### Cursor — 89/100
**Role in the mesh:** IDE battlefield and editor-native implementation layer.

**Structural layers**
- adapter layer: editor-facing rule alignment
- capability layer: project-local editor rules and implementation guidance
- runtime layer: fast inline coding and low-friction daily development
- evolution layer: project-level coding habits and local delivery patterns

**Best fit**
- staying close to the coding surface
- reducing day-to-day development friction
- keeping project rules near the editor

**Current tradeoff**
- weaker operating-system feel and cross-tool governance depth than Codex or Antigravity

### Antigravity — 91/100
**Role in the mesh:** broad capability platform and expansion layer.

**Structural layers**
- adapter layer: platform-facing workflow alignment
- capability layer: broad skills, browser work, knowledge, artifacts
- runtime layer: strong cross-domain execution and workflow expansion
- evolution layer: broad reusable capability growth

**Best fit**
- expanding beyond narrow coding tasks
- browser-heavy and artifact-heavy work
- acting more like a platform than a single tool

**Current tradeoff**
- breadth can introduce noise; on the core engineering path it is not always as steady as Codex

## Overall system summary — 91/100

The strength of the reference setup does not come from one unbeatable tool.
It comes from organizing multiple tools into one system with:
- shared operating law
- specialized endpoints
- project memory
- execution gates
- evidence discipline
- cross-platform consistency

The most accurate summary is:

**Shared Law + Multi-Tool Specialized AI System**

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

The goal is to publish the system design without leaking personal machine structure.

## Reference setup snapshot (sanitized)

This repository is based on a real working setup. In sanitized form, the reference environment includes:
- 30 Codex skills
- 3 global memory files
- 10 project governance commands
- 5 project memory files
- active project state files

That means this is not only conceptual. It already operates at:
- rules layer
- capability layer
- project runtime layer
- state layer
- evidence layer

## Core operating documents

These are the documents that make the repository feel like a real working system rather than a collection of notes:
- [OPERATING-CHARTER.md](docs/OPERATING-CHARTER.md)
- [MEMORY-SCHEMA.md](docs/MEMORY-SCHEMA.md)
- [BOOTSTRAP-SPEC.md](docs/BOOTSTRAP-SPEC.md)
- [ARCHITECTURE.md](docs/ARCHITECTURE.md)

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
├── LICENSE
├── docs/
│   ├── ARCHITECTURE.md
│   ├── BOOTSTRAP-SPEC.md
│   ├── MEMORY-SCHEMA.md
│   ├── OPERATING-CHARTER.md
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

## License

Released under the [MIT License](LICENSE).
