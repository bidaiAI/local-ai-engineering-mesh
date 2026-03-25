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
