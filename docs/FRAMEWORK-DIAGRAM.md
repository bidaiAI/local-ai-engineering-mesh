# Framework Diagram

Use this file as the source for the launch image. The easiest workflow is:

1. render the Mermaid chart
2. take a clean screenshot
3. use that screenshot as the X thread image

## Diagram title

`Local AI Engineering Mesh`

## Image goal

Show that this repository is not a prompt pack.  
It is a networked local AI engineering system that can work for one tool first, or for multiple tools together, with:

- shared law
- multi-tool endpoints
- Codex execution layer
- project runtime layer
- memory/state/evidence/release loops

## Mermaid version

```mermaid
flowchart TD
    A["Shared Law<br/>AGENTS.md"] --> B["Codex Adapter Layer<br/>config.toml + instructions.md"]
    A --> C["Cursor Layer<br/><cursor-global-rules> + <project>/.cursor/rules"]
    A --> C2["Antigravity Layer<br/>skills + workflows + knowledge"]
    A --> C3["Claude / OpenCode<br/>peer endpoints"]

    B --> D["Core Skills"]
    D --> D1["execution-orchestrator"]
    D --> D2["architecture-gatekeeper"]
    D --> D3["reality-check-qa"]
    D --> D4["release-risk-governor"]

    B --> E["Upgrade Layers"]
    E --> E1["state-store-memory"]
    E --> E2["codex-skill-manager"]
    E --> E3["build-resolver"]
    E --> E4["TS / Python / Go reviewers"]

    B --> F["Project Runtime"]
    F --> F1["<project>/.codex/commands"]
    F --> F2["<project>/.codex/memory"]
    F --> F3["<project>/.codex/state"]
    F --> F4[".codex/evidence"]

    F1 --> G["preflight"]
    F1 --> H["pre-edit"]
    F1 --> I["pre-publish"]
    F1 --> J["pre-deploy"]
    F1 --> K["post-implementation"]
    F1 --> L["save/show state + qa-score"]

    F --> M["Execution Loop"]
    M --> M1["research-first"]
    M --> M2["structured plan"]
    M --> M3["mechanical execution"]
    M --> M4["evidence-backed completion"]
    M --> M5["release discipline"]
    M --> M6["reusable skill promotion"]
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
│   ├── COMPARE-WITH-CLAUDE.md
│   ├── CROSS-PLATFORM.md
│   ├── EXECUTION-LOOP.md
│   ├── REPO-MAP.md
│   ├── STACK.md
│   └── FRAMEWORK-DIAGRAM.md
└── templates/
    ├── global-memory/
    ├── project-memory/
    └── policy.env.example
```

## Caption for the image

This is the point of the repository:

- top layer: shared operating law
- middle layer: specialized local AI endpoints
- bottom layer: project runtime with commands, memory, state, and evidence

That is what turns separate AI tools into a governed engineering mesh.
