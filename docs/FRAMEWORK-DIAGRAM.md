# Framework Diagram

Use this file as the source for a repository diagram or overview image.

## Diagram title

`Local AI Engineering Mesh`

## Image goal

Show that this repository is not a prompt pack.
It is a networked local AI engineering system with a shared law at the top, specialized tool layers in the middle, concrete public packs under each tool, and project runtime discipline at the bottom.

## Mermaid version

```mermaid
flowchart TD
    A["Shared Law
AGENTS.md"]

    subgraph COD["Codex"]
      B1["config.example.toml
instructions.example.md"]
      B2["state-store-memory
safe-pr-flow
governed-deploy"]
      B3["visual-evidence
project-bootstrap"]
      B4["runtime commands
state + evidence"]
    end

    subgraph CLA["Claude"]
      C1["CLAUDE.example.md"]
      C2["/plan /review /verify /publish"]
      C3["rules-pack
security / testing / git"]
      C4["planning + review
workflow benchmark"]
    end

    subgraph CUR["Cursor"]
      D1["engineering-mesh.mdc
evidence-release-gate.mdc"]
      D2["design-first-gate
tdd-discipline"]
      D3["review / debug / anti-patterns
context / git-safety"]
      D4["project-local delivery"]
    end

    subgraph ANT["Antigravity"]
      E1["local-ai-mesh-workflow
knowledge-stub"]
      E2["browser-research-evidence
cross-tool-handoff"]
      E3["OPERATING-LAW
SESSION-HANDOFF
WORKFLOW-INDEX"]
      E4["browser + artifacts
knowledge + handoff"]
    end

    A --> B1
    A --> C1
    A --> D1
    A --> E1

    B1 --> B2 --> B3 --> B4
    C1 --> C2 --> C3 --> C4
    D1 --> D2 --> D3 --> D4
    E1 --> E2 --> E3 --> E4

    B4 --> F["Project Runtime
<project>/.codex/commands
<project>/.codex/memory
<project>/.codex/state"]
    C4 --> G["Planning + Review"]
    D4 --> H["Editor Delivery"]
    E4 --> I["Research + Artifacts"]

    F --> J["Evidence Gate"]
    F --> K["Release Discipline"]
    F --> L["Reusable Patterns"]
```

## Simple file-tree version

```text
local-ai-engineering-mesh/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── BOOTSTRAP-SPEC.md
│   ├── MEMORY-SCHEMA.md
│   ├── OPERATING-CHARTER.md
│   ├── TOOL-LAYERS.md
│   ├── WORKFLOWS-AND-COMBOS.md
│   ├── QUICKSTART.md
│   ├── COMPARE-WITH-CLAUDE.md
│   ├── CROSS-PLATFORM.md
│   ├── EXECUTION-LOOP.md
│   ├── REPO-MAP.md
│   ├── STACK.md
│   └── FRAMEWORK-DIAGRAM.md
├── scripts/
│   └── setup-project-runtime.sh
├── skills/
│   ├── README.md
│   ├── state-store-memory/
│   ├── safe-pr-flow/
│   ├── governed-deploy/
│   ├── visual-evidence/
│   └── project-bootstrap/
└── templates/
    ├── AGENTS.example.md
    ├── antigravity/
    │   ├── workflows/
    │   └── knowledge/
    ├── claude/
    │   ├── commands/
    │   └── rules-pack/
    ├── codex/
    ├── cursor/
    │   └── rules-pack/
    ├── global-memory/
    ├── project-memory/
    └── policy.env.example
```

## Suggested caption

- top layer: shared operating law
- middle layer: tool-specific structure layers
- concrete layer: public packs that upgrade each tool beyond stock defaults
- bottom layer: project runtime, evidence, and release discipline

That is what turns separate AI tools into a governed engineering mesh.


## Companion labels

For poster-style or social-image text, see [IMAGE-LABELS.md](IMAGE-LABELS.md).
