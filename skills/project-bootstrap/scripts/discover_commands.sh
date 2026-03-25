#!/usr/bin/env bash
set -euo pipefail

repo="${1:-.}"
cd "$repo"

found=0

echo "== Repository =="
pwd

if [[ -f package.json ]]; then
  echo
  echo "== package.json scripts =="
  if command -v jq >/dev/null 2>&1; then
    jq -r '
      .scripts // {}
      | to_entries[]
      | select(.key == "dev" or .key == "test" or .key == "lint" or .key == "build" or .key == "typecheck" or .key == "start")
      | "\(.key): \(.value)"' package.json
  else
    echo "jq not found; cannot inspect package.json scripts safely"
  fi
  found=1
fi

if [[ -f Makefile ]]; then
  echo
  echo "== Makefile targets =="
  awk -F: '
    /^[a-zA-Z0-9_.-]+:/ {
      target=$1
      if (target == "install" || target == "dev" || target == "test" || target == "lint" || target == "build" || target == "typecheck") {
        print target
      }
    }' Makefile | sort -u
  found=1
fi

if [[ -f pyproject.toml ]]; then
  echo
  echo "== Python project markers =="
  rg -n '^\[tool\.(poetry|uv|pytest|ruff|mypy)' pyproject.toml || true
  found=1
fi

if [[ -f Cargo.toml ]]; then
  echo
  echo "== Rust project markers =="
  echo "cargo build"
  echo "cargo test"
  found=1
fi

if [[ "$found" -eq 0 ]]; then
  echo "No explicit command map discovered from common project files."
fi
