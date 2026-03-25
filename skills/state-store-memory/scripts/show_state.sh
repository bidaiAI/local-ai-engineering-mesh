#!/usr/bin/env bash
set -euo pipefail

repo="."
json_mode="no"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo) repo="$2"; shift 2 ;;
    --json) json_mode="yes"; shift ;;
    *) echo "unknown_arg=$1" >&2; exit 2 ;;
  esac
done

repo_abs="$(cd "$repo" && pwd)"
state_file="$repo_abs/.codex/state/session-state.json"

if [[ ! -f "$state_file" ]]; then
  echo "missing_state_file=$state_file" >&2
  exit 1
fi

if [[ "$json_mode" == "yes" ]]; then
  cat "$state_file"
  exit 0
fi

jq -r '
  "updated_at=" + .updated_at,
  "phase=" + .phase,
  "summary=" + .summary,
  "next_step=" + .next_step,
  "files=" + (.files | join(",")),
  "evidence=" + .evidence,
  "constraints=" + (.constraints | join(",")),
  "open_questions=" + (.open_questions | join(","))
' "$state_file"
