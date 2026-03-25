# Memory Schema

## Purpose
- Define how Codex memory should be structured so context compounds instead of turning noisy.

## Memory Layers

### Layer 1: Global memory
- Stable operating laws
- default routing rules
- personal collaboration preferences
- publication and deployment posture

### Layer 2: Project memory
- project conventions
- core commands
- build and test paths
- architecture decisions
- deployment targets
- recurring pitfalls

### Layer 3: Path or module memory
- rules for specific subsystems
- sensitive files or fragile surfaces
- module-local commands
- ownership or review notes when relevant

### Layer 4: Session memory
- temporary discoveries
- task-local assumptions
- pending decisions
- unresolved blockers

## Promotion Rules

### Promote to global when
- the rule applies to most work, not just one repo

### Promote to project when
- the same repo fact must be repeated across sessions

### Promote to path or module when
- the rule only applies to a subsystem or directory

### Keep session-local when
- the insight is still provisional or task-specific

## Memory Quality Rules
- concise over verbose
- durable over transient
- scoped over generic
- actionable over narrative

## Suggested Global Memory Files
- `global-operating-charter.md`
- `global-routing-rules.md`
- `global-publish-and-deploy.md`

## Suggested Project Memory Fields
- project name
- primary stack
- main commands
- verification commands
- dangerous paths
- deploy platform
- open architectural constraints
