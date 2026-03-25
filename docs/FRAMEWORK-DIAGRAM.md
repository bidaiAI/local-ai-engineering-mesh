# Framework Diagram

Use this file as the source for a repository diagram or overview image.

## Diagram title

`Local AI Engineering Mesh`

## Image goal

Show that this repository is not a prompt pack.
It is a networked local AI engineering system with a shared law at the top, specialized tool layers in the middle, concrete public packs under each tool, one converged project runtime, and evidence/release discipline at the bottom.

## Mermaid version

```mermaid
flowchart TB
    A["Shared Law
AGENTS.md"]
    A2["Shared Principles
plan / memory / evidence / release / reuse"]

    A --> A2

    subgraph COD["Codex — Execution + Governance"]
      B1["Adapter
config.example.toml
instructions.example.md"]
      B2["Native Skills
state-store-memory
safe-pr-flow
governed-deploy"]
      B3["Execution Helpers
visual-evidence
project-bootstrap"]
      B4["Runtime Discipline
commands
state
evidence"]
    end

    subgraph CLA["Claude — Planning + Review"]
      C1["Adapter
CLAUDE.example.md"]
      C2["Commands
/plan
/review
/verify
/publish"]
      C3["Rules Pack
agents
security
testing
git
performance"]
      C4["Method Layer
planning
review
workflow benchmark"]
    end

    subgraph CUR["Cursor — IDE Delivery"]
      D1["Starter Rules
engineering-mesh.mdc
evidence-release-gate.mdc"]
      D2["Build Discipline
design-first-gate
tdd-discipline"]
      D3["Delivery Rules
review
debug
anti-patterns
context
git-safety"]
      D4["Editor Layer
project-local delivery
low-friction edits"]
    end

    subgraph ANT["Antigravity — Capability Expansion"]
      E1["Starter Files
local-ai-mesh-workflow
knowledge-stub"]
      E2["Workflow Pack
browser-research-evidence
cross-tool-handoff"]
      E3["Knowledge Pack
OPERATING-LAW
SESSION-HANDOFF
WORKFLOW-INDEX"]
      E4["Expansion Layer
browser
artifacts
knowledge
handoff"]
    end

    A2 --> B1
    A2 --> C1
    A2 --> D1
    A2 --> E1

    B1 --> B2 --> B3 --> B4
    C1 --> C2 --> C3 --> C4
    D1 --> D2 --> D3 --> D4
    E1 --> E2 --> E3 --> E4

    C4 --> X1["Design + Review Output"]
    D4 --> X2["Editor Implementation Output"]
    E4 --> X3["Research + Artifact Output"]

    B4 --> F["Project Runtime
<project>/.codex/commands
<project>/.codex/memory
<project>/.codex/state"]
    X1 --> F
    X2 --> F
    X3 --> F

    F --> J["Evidence Gate
tests / logs / screenshots / runtime proof"]
    F --> K["Release Discipline
publish / PR / deploy safety"]
    F --> L["Reusable Patterns
promote wins into templates / rules / skills"]

    J --> M["Verified Delivery"]
    K --> M
    L --> M
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
- tool layer: four specialized endpoints
- concrete layer: public packs that upgrade each tool beyond stock defaults
- integration layer: plan, editor, and research outputs converge into one project runtime
- bottom layer: evidence, release discipline, and reusable patterns

That is what turns separate AI tools into a governed engineering mesh.
