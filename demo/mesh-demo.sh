#!/usr/bin/env bash
set -euo pipefail

DEMO_DIR="${1:-/tmp/mesh-demo-project}"

echo "[1/4] init"
python3 -m mesh init "$DEMO_DIR"
echo

echo "[2/4] inspect"
python3 -m mesh inspect "$DEMO_DIR"
echo

echo "[3/4] handoff"
python3 -m mesh handoff "$DEMO_DIR" \
  --task "Add login rate limiting" \
  --summary "Planning complete, ready for editor implementation" \
  --next-endpoint Cursor \
  --evidence "project runtime initialized" \
  --risk "rate limit storage backend not decided yet"
echo

echo "[4/4] verify"
python3 -m mesh verify "$DEMO_DIR"
