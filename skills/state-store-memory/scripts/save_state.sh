#!/usr/bin/env bash
set -euo pipefail

repo="."
phase="implementation"
summary=""
next_step=""
files=""
evidence=""
constraints=""
open_questions=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo) repo="$2"; shift 2 ;;
    --phase) phase="$2"; shift 2 ;;
    --summary) summary="$2"; shift 2 ;;
    --next-step) next_step="$2"; shift 2 ;;
    --files) files="$2"; shift 2 ;;
    --evidence) evidence="$2"; shift 2 ;;
    --constraints) constraints="$2"; shift 2 ;;
    --open-questions) open_questions="$2"; shift 2 ;;
    *) echo "unknown_arg=$1" >&2; exit 2 ;;
  esac
done

if [[ -z "$summary" || -z "$next_step" ]]; then
  echo "missing_required_args=summary,next-step" >&2
  exit 2
fi

repo_abs="$(cd "$repo" && pwd)"
state_dir="$repo_abs/.codex/state"
state_file="$state_dir/session-state.json"
mkdir -p "$state_dir"

to_json_array() {
  local raw="$1"
  if [[ -z "$raw" ]]; then
    jq -cn '[]'
  else
    printf '%s' "$raw" | jq -R 'split(",") | map(gsub("^\\s+|\\s+$"; "")) | map(select(length > 0))'
  fi
}

files_json="$(to_json_array "$files")"
constraints_json="$(to_json_array "$constraints")"
questions_json="$(to_json_array "$open_questions")"

tmp_file="$state_dir/session-state.tmp.$$"
jq -n \
  --arg updated_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
  --arg repo "$repo_abs" \
  --arg phase "$phase" \
  --arg summary "$summary" \
  --arg next_step "$next_step" \
  --arg evidence "$evidence" \
  --argjson files "$files_json" \
  --argjson constraints "$constraints_json" \
  --argjson open_questions "$questions_json" \
  '{updated_at:$updated_at,repo:$repo,phase:$phase,summary:$summary,next_step:$next_step,files:$files,evidence:$evidence,constraints:$constraints,open_questions:$open_questions}' > "$tmp_file"
mv "$tmp_file" "$state_file"

echo "state_file=$state_file"
echo "phase=$phase"
echo "next_step=$next_step"
