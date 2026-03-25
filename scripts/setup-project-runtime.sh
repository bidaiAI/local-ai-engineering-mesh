#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 /path/to/project"
  exit 1
fi

PROJECT_DIR="$1"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

mkdir -p "$PROJECT_DIR/.codex/memory"
mkdir -p "$PROJECT_DIR/.codex/state"
mkdir -p "$PROJECT_DIR/.cursor/rules"

cp "$REPO_ROOT/templates/project-memory/PROJECT-active-context.md" "$PROJECT_DIR/.codex/memory/PROJECT-active-context.md"
cp "$REPO_ROOT/templates/project-memory/PROJECT-command-map.md" "$PROJECT_DIR/.codex/memory/PROJECT-command-map.md"
cp "$REPO_ROOT/templates/project-memory/PROJECT-decisions.md" "$PROJECT_DIR/.codex/memory/PROJECT-decisions.md"
cp "$REPO_ROOT/templates/project-memory/PROJECT-patterns.md" "$PROJECT_DIR/.codex/memory/PROJECT-patterns.md"
cp "$REPO_ROOT/templates/project-memory/PROJECT-troubleshooting.md" "$PROJECT_DIR/.codex/memory/PROJECT-troubleshooting.md"
cp "$REPO_ROOT/templates/policy.env.example" "$PROJECT_DIR/.codex/state/policy.env.example"
cp "$REPO_ROOT/templates/cursor/engineering-mesh.mdc" "$PROJECT_DIR/.cursor/rules/00-engineering-mesh.mdc"
cp "$REPO_ROOT/templates/cursor/evidence-release-gate.mdc" "$PROJECT_DIR/.cursor/rules/10-evidence-release-gate.mdc"

cat <<EOF
Done.

Created:
- $PROJECT_DIR/.codex/memory/
- $PROJECT_DIR/.codex/state/
- $PROJECT_DIR/.cursor/rules/

Next steps:
1. Copy templates/AGENTS.example.md into your shared-law location.
2. Edit the project memory files for your repo.
3. Add your tool-specific configs separately.
EOF
