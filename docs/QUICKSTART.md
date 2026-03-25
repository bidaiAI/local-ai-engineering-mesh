# Quick Start

This repository supports three adoption paths:

## 1. Single-tool first
Best if you only want to upgrade one tool right now.

### Minimal project setup
```bash
git clone https://github.com/bidaiAI/local-ai-engineering-mesh.git
cd local-ai-engineering-mesh
./scripts/setup-project-runtime.sh /path/to/your-project
```

### What this gives you
- project memory skeleton in `<project>/.codex/memory/`
- project state seed in `<project>/.codex/state/`
- Cursor rule skeleton in `<project>/.cursor/rules/`

### Next step
Copy `templates/AGENTS.example.md` into your shared-law location and adapt it for your tool.

## 2. Dual-tool setup
Best if you want one execution tool and one editor or research tool.

Recommended patterns:
- Codex + Cursor
- Claude + Cursor
- Codex + Claude

Shared principle:
- one law at the top
- separate native strengths underneath

## 3. Full mesh
Best if you already use multiple tools.

Target model:
- Codex for execution and governance
- Claude for workflow benchmark and methodology
- Cursor for IDE-native delivery
- Antigravity for broad capability expansion

## Suggested setup order
1. shared law
2. project memory
3. project state
4. editor rules
5. tool-specific configs
6. evidence and release discipline


## Tool-specific add-ons

### Codex
```bash
cp templates/codex/config.example.toml /path/to/your/codex/config.toml
cp templates/codex/instructions.example.md /path/to/your/codex/instructions.md
```

### Claude
```bash
cp templates/claude/CLAUDE.example.md /path/to/your/project/CLAUDE.md
```

### Cursor
```bash
cp templates/cursor/engineering-mesh.mdc /path/to/your/project/.cursor/rules/00-engineering-mesh.mdc
cp templates/cursor/evidence-release-gate.mdc /path/to/your/project/.cursor/rules/10-evidence-release-gate.mdc
```

### Antigravity
```bash
cp templates/antigravity/local-ai-mesh-workflow.md /path/to/your/antigravity/workflows/
cp templates/antigravity/knowledge-stub.md /path/to/your/antigravity/knowledge/
```
