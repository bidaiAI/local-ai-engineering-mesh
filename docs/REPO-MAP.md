# Repository Map

## Public framing

This repository is organized around three public-safe views:
- overall system layers
- per-tool structure layers
- reusable templates without personal machine paths

## Root

### `README.md`
Main English readme with the full system framework, four-tool evaluation, and sanitized public structure.

### `README.zh-CN.md`
Chinese readme with the full framework explanation and four-tool system assessment.

### `README.ru.md` / `README.ja.md` / `README.fr.md`
Localized overview variants.

## `docs/`

### `ARCHITECTURE.md`
Layered operating-model design.

### `CROSS-PLATFORM.md`
How one shared law coordinates Codex, Claude, Cursor, and Antigravity.

### `COMPARE-WITH-CLAUDE.md`
What this system claims relative to the latest public Claude workflow baseline.

### `EXECUTION-LOOP.md`
The operating loop: research -> plan -> execute -> verify.

### `FRAMEWORK-DIAGRAM.md`
Diagram-oriented mesh view with public-safe structure labels.

### `OPERATING-CHARTER.md`
Default operating laws for how the system should behave.

### `MEMORY-SCHEMA.md`
How memory is layered and promoted across global, project, module, and session scopes.

### `BOOTSTRAP-SPEC.md`
What a repo should discover and establish before deeper implementation begins.

### `STACK.md`
Tooling and stack overview in sanitized form.

### `QUICKSTART.md`
Beginner-friendly adoption guide for single-tool, dual-tool, and full-mesh setup.

### `TOOL-LAYERS.md`
Detailed next-layer breakdown for Codex, Claude, Cursor, and Antigravity.

### `WORKFLOWS-AND-COMBOS.md`
What the system can actually do, original-vs-mesh comparison, and best-performance combinations.

### `scripts/setup-project-runtime.sh`
Project bootstrap helper for creating memory, state, and Cursor rule skeletons.

## `templates/`

### `templates/AGENTS.example.md`
Starter shared-law template for one or more tools.

### `templates/global-memory/`
Global memory seeds.

### `templates/project-memory/`
Project memory templates.

### `templates/codex/`
Codex config and instruction starter templates.

### `templates/claude/`
Claude project-law and command starter templates.

### `templates/cursor/`
Cursor rule templates with public-safe path naming.

### `templates/antigravity/`
Antigravity workflow and knowledge templates.

### `policy.env.example`
Shared policy defaults.


### `LICENSE`
MIT open-source license for public reuse.
