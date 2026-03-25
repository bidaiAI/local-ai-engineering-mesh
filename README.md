# Local AI Engineering Mesh

Upgrade your AI tools from isolated assistants into a governed, memory-backed, evidence-driven engineering system.

This repository is not a chat prompt pack. It is a repository-shaped operating model for upgrading local AI tools from "can answer" to "can run a disciplined engineering workflow."

It reflects a bigger idea: Codex is not running alone. In this setup, Codex, Cursor, Antigravity, Claude Code, and OpenCode can be treated as specialized endpoints inside one cross-platform AI coding system, coordinated through a unified `AGENTS.md`.

## Why this exists

The real gap between agent tools is rarely just the model name.

The bigger gap is workflow closure:
- memory
- bootstrap
- commands
- hooks
- orchestration
- research-first planning
- evidence
- release discipline

This repository packages that layer as a reusable local AI engineering mesh.

## What this upgrades

- `memory`: persistent working law, routing rules, and skill layering
- `bootstrap`: project initialization for commands, memory, and risk posture
- `orchestration`: explicit roles for planning, design, verification, and release
- `planning`: parallel research and structured `plan.md` before broad implementation
- `evidence`: completion requires proof instead of narrative
- `release safety`: preview-first and publish gates
- `evolution`: repeated wins can become native reusable skills

## What you get

- A local-AI workflow model organized like a real repository
- A cross-platform instruction model with multiple governed execution endpoints
- Concrete starting templates for Codex, Cursor, and Antigravity layers
- Publish-ready documentation instead of a process diary
- Templates for global memory and project memory
- A clean comparison frame against the latest Claude workflow model
- X-style social copy for public posting

## Cross-platform setup

In the live environment behind this repository:
- `~/.codex/config.toml` loads `~/AGENTS.md` through `model_instructions_file`
- `~/.codex/instructions.md` adds Codex-specific routing, profiles, and skill guidance
- the same top-level operating law is shared across multiple coding tools

This means the system here is both:
- tool-native in execution
- cross-platform in policy

See [CROSS-PLATFORM.md](docs/CROSS-PLATFORM.md).

## Compared with the latest Claude

As of **March 23, 2026**, Anthropic's latest public Claude coding stack is led by:
- `Claude Opus 4.6` published on **February 5, 2026**
- `Claude Sonnet 4.6` published on **February 17, 2026**

This repository does **not** claim that a local tool automatically beats Claude on raw model capability.

It makes a narrower and more useful claim:

If you give local AI tools a stronger operating system layer, they become much more competitive on long-horizon engineering execution because the workflow stops depending on one perfect prompt.

See [COMPARE-WITH-CLAUDE.md](docs/COMPARE-WITH-CLAUDE.md).

## Repository map

```text
local-ai-engineering-mesh/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── COMPARE-WITH-CLAUDE.md
│   ├── CROSS-PLATFORM.md
│   ├── EXECUTION-LOOP.md
│   ├── REPO-MAP.md
│   ├── STACK.md
│   └── FRAMEWORK-DIAGRAM.md
├── social/
│   ├── X-POSTS-CN.md
│   └── X-LONG-POST-CN.md
└── templates/
    ├── antigravity/
    ├── cursor/
    ├── global-memory/
    ├── project-memory/
    └── policy.env.example
```

See [REPO-MAP.md](docs/REPO-MAP.md).

## Architecture

The operating model is built in layers:

1. Bootstrap
2. Constitution
3. Memory
4. Hooks and commands
5. Skills
6. Orchestration
7. Research
8. Evidence and review
9. Evolution

See [ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Execution loop

One of the strongest ideas absorbed into this setup is:

`parallel research -> structured plan -> mechanical execution -> evidence-backed completion`

The key is not copying someone else's slash commands.
The key is making planning durable and session-resistant through explicit plan artifacts and governed execution.

See [EXECUTION-LOOP.md](docs/EXECUTION-LOOP.md).

## Tool stack

Core stack:
- Codex desktop
- Cursor
- Antigravity
- shared `AGENTS.md`
- local terminal execution
- governed skill layers

Key workflow tools:
- `playwright`
- `gh-fix-ci`
- `security-*`
- `frontend-skill`
- `sentry`
- governed deploy and PR flows

See [STACK.md](docs/STACK.md).

## Templates included

This repository includes reusable templates for:
- global memory
- project memory
- Cursor project rules
- Antigravity workflow and knowledge stubs
- policy defaults

The goal is to help you start with a governed local-AI layout instead of inventing one from scratch.

## Social copy

If you want to post the project publicly, use:
- [X-POSTS-CN.md](social/X-POSTS-CN.md)
- [X-LONG-POST-CN.md](social/X-LONG-POST-CN.md)
- [FRAMEWORK-DIAGRAM.md](docs/FRAMEWORK-DIAGRAM.md)

## References

- [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/)
- [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)
- [Introducing Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- [Compound Engineering plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [shinpr/agentic-code](https://github.com/shinpr/agentic-code)
- [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)
