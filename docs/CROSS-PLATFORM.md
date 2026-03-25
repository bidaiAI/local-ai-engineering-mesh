# Cross-Platform

## What this means

This repository describes the Codex side of a larger cross-platform AI coding system.

In the live setup:
- `~/AGENTS.md` is the shared instruction entrypoint
- `~/.codex/config.toml` loads it through `model_instructions_file`
- `~/.codex/instructions.md` adds Codex-specific guidance
- `~/.cursorrules` and project `.cursor/rules/` carry IDE-facing policy and delivery rules
- Antigravity carries broad skill and workflow execution through its own skills, workflows, and knowledge layers

So the Codex configuration is not isolated.

It is one governed endpoint inside a broader toolchain that also includes:
- Claude Code
- Cursor
- OpenCode
- Antigravity

## Why this matters

This changes the meaning of the repository.

It is not only:
- a Codex customization

It is also:
- the Codex execution layer of a shared agent operating system

## Source influence

The cross-platform philosophy and part of the organizational inspiration come from:
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code)

That project is useful because it treats agent quality as a harness and operating-system problem, not only a prompt problem.

## What is tool-specific here

### Codex

Even inside the shared system, the Codex side still has its own strengths:
- local terminal-first execution
- sandbox-aware action model
- governed skill composition
- release and publish guards
- role-based orchestration

### Cursor

The Cursor side is strongest when the workflow needs:
- IDE-native rule enforcement
- project-local `.cursor/rules/*.mdc`
- fast inline coding iteration
- less friction while staying inside the editor

### Antigravity

The Antigravity side is strongest when the workflow needs:
- very broad skill coverage
- browser and artifact-heavy work
- domain expansion beyond pure coding
- workflow and knowledge layers that feel closer to an AI platform

## Practical takeaway

If you publish this repository, the clean framing is:

- shared cross-platform law at the top
- tool-specific execution layers beneath it
- concrete Codex / Cursor / Antigravity examples in the templates layer
