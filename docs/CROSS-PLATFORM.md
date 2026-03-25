# Cross-Platform

## What this means

This repository describes the Codex side of a larger cross-platform AI coding system.

In the live setup:
- `~/AGENTS.md` is the shared instruction entrypoint
- `~/.codex/config.toml` loads it through `model_instructions_file`
- `~/.codex/instructions.md` adds Codex-specific guidance

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

## What is Codex-specific here

Even inside the shared system, the Codex side still has its own strengths:
- local terminal-first execution
- sandbox-aware action model
- governed skill composition
- release and publish guards
- role-based orchestration

## Practical takeaway

If you publish this repository, the clean framing is:

- shared cross-platform law at the top
- Codex-specific engineering operating layer here

