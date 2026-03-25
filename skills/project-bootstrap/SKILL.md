---
name: project-bootstrap
description: Bootstrap new or inherited codebases into the governed project operating model. Use when starting work on a repo for the first time, onboarding a project, or when commands, memory, verification, and risk surfaces need to be established before deeper work.
---

# Project Bootstrap

Use this skill to initialize a repository into the governed project operating model.

## Goals
- discover the repo shape
- establish command knowledge
- establish verification paths
- seed project memory
- identify risk surfaces

## Required workflow

### Step 1: profile the repository
- identify languages, frameworks, package managers, and deployment markers
- identify whether the repo is app, library, infra, monorepo, or mixed

### Step 2: discover command paths
- identify install, dev, test, lint, build, and typecheck commands
- prefer the bundled script for first-pass command discovery:

```bash
bash <path-to-skill>/scripts/discover_commands.sh [repo]
```

- if commands are unclear, state that clearly instead of guessing

### Step 3: map risk surfaces
- publish and PR surfaces
- deploy surfaces
- external integration surfaces
- sensitive files and directories

### Step 4: define evidence path
- backend: tests, logs, API checks
- frontend: screenshots, traces, browser checks
- infra: plan output, config diff, deployment target confirmation

### Step 5: seed memory
- capture project conventions
- capture command map
- capture architecture constraints
- capture known fragile areas

## Project bootstrap outputs
- `<project>/.codex/memory/*` project memory seeds
- `<project>/.codex/state/policy.env` default routing and risk settings

## Guardrails
- Do not pretend the repo is understood after only reading one file.
- Do not invent commands that were not found.
- Do not skip deployment or auth surfaces.
- If bootstrap reveals major ambiguity, surface it before implementation starts.

## Definition of done
- project type is explicit
- command map is explicit
- risk surfaces are explicit
- evidence path is explicit
- initial memory seed exists
