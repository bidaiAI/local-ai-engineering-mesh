# Tool Layers

## Purpose
This document expands the next layer under each tool in the mesh so readers can see what each endpoint is actually responsible for, and which concrete public packs in this repository map to that role.

## Codex

### Top role
- execution core
- governance core

### Next layer
- config and instructions
- governed skills
- reviewers
- project runtime commands
- state and evidence
- release gates

### Concrete public packs in this repository
- `templates/codex/config.example.toml`
- `templates/codex/instructions.example.md`
- `skills/state-store-memory/`
- `skills/safe-pr-flow/`
- `skills/governed-deploy/`
- `skills/visual-evidence/`
- `skills/project-bootstrap/`

### What this means in practice
- repo execution with state carryover
- safer branch / PR / deploy flow
- evidence-backed completion instead of narrative-only completion
- project bootstrap into a governed runtime

## Claude

### Top role
- workflow benchmark
- methodology engine

### Next layer
- project law file
- command culture
- review prompts and checklists
- design and review framing
- collaboration patterns

### Concrete public packs in this repository
- `templates/claude/CLAUDE.example.md`
- `templates/claude/commands/plan.md`
- `templates/claude/commands/review.md`
- `templates/claude/commands/verify.md`
- `templates/claude/commands/publish.md`
- `templates/claude/rules-pack/agents.md`
- `templates/claude/rules-pack/coding-style.md`
- `templates/claude/rules-pack/testing.md`
- `templates/claude/rules-pack/git-workflow.md`
- `templates/claude/rules-pack/security.md`
- `templates/claude/rules-pack/performance.md`

### What this means in practice
- better planning before broad implementation
- stronger review / verify / publish separation
- reusable methodology instead of ad hoc prompting
- easier alignment with the same operating law as other tools

## Cursor

### Top role
- IDE delivery layer
- editor-native implementation surface

### Next layer
- project-local rules
- inline coding flow
- local editor memory
- implementation guardrails near the code surface

### Concrete public packs in this repository
- `templates/cursor/engineering-mesh.mdc`
- `templates/cursor/evidence-release-gate.mdc`
- `templates/cursor/rules-pack/design-first-gate.mdc`
- `templates/cursor/rules-pack/tdd-discipline.mdc`
- `templates/cursor/rules-pack/risk-first-code-review.mdc`
- `templates/cursor/rules-pack/systematic-debug-discipline.mdc`
- `templates/cursor/rules-pack/anti-patterns.mdc`
- `templates/cursor/rules-pack/context-discipline.mdc`
- `templates/cursor/rules-pack/git-safety.mdc`

### What this means in practice
- stronger implementation discipline directly inside the editor
- better review and debugging habits at the coding surface
- less day-to-day drift in quality and delivery standards
- a clearer path from default Cursor behavior to governed delivery behavior

## Antigravity

### Top role
- capability expansion platform
- broad workflow endpoint

### Next layer
- skills
- workflows
- knowledge / brain notes
- browser and artifact-heavy flows
- cross-domain execution patterns

### Concrete public packs in this repository
- `templates/antigravity/local-ai-mesh-workflow.md`
- `templates/antigravity/knowledge-stub.md`
- `templates/antigravity/workflows/browser-research-evidence.md`
- `templates/antigravity/workflows/cross-tool-handoff.md`
- `templates/antigravity/knowledge/OPERATING-LAW.md`
- `templates/antigravity/knowledge/SESSION-HANDOFF.md`
- `templates/antigravity/knowledge/WORKFLOW-INDEX.md`

### What this means in practice
- stronger browser-heavy and artifact-heavy execution
- cleaner handoff from broad exploration back into governed delivery
- persistent operating-law alignment through knowledge files
- a more structured role for Antigravity inside a multi-tool system
