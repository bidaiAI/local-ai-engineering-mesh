# Framework Diagram

Use this file as the source for a repository diagram or overview image.

## Diagram title

`Local AI Engineering Mesh`

## Image goal

Show that this repository is not a prompt pack.
It is a networked local AI engineering system with a shared law at the top, specialized tool layers in the middle, and project runtime discipline at the bottom.

## Mermaid version

```mermaid
flowchart TD
    A["Shared Law
AGENTS.md"]

    subgraph COD["Codex"]
      B1["config + instructions"]
      B2["governed skills"]
      B3["reviewers + routing"]
      B4["runtime commands + evidence"]
    end

    subgraph CLA["Claude"]
      C1["project law"]
      C2["command culture"]
      C3["review + planning"]
      C4["workflow benchmark"]
    end

    subgraph CUR["Cursor"]
      D1["editor rules"]
      D2["inline implementation"]
      D3["project-local delivery"]
    end

    subgraph ANT["Antigravity"]
      E1["skills"]
      E2["workflows"]
      E3["knowledge"]
      E4["browser + artifacts"]
    end

    A --> B1
    A --> C1
    A --> D1
    A --> E1

    B1 --> B2 --> B3 --> B4
    C1 --> C2 --> C3 --> C4
    D1 --> D2 --> D3
    E1 --> E2 --> E3 --> E4

    B4 --> F["Project Runtime
<project>/.codex/commands
<project>/.codex/memory
<project>/.codex/state"]
    C3 --> G["Planning + Review"]
    D3 --> H["Editor Delivery"]
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
└── templates/
    ├── AGENTS.example.md
    ├── antigravity/
    ├── claude/
    ├── codex/
    ├── cursor/
    ├── global-memory/
    ├── project-memory/
    └── policy.env.example
```

## Suggested caption

- top layer: shared operating law
- middle layer: tool-specific structure layers
- bottom layer: project runtime, evidence, and release discipline

That is what turns separate AI tools into a governed engineering mesh.
