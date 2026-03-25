#!/usr/bin/env bash
set -euo pipefail

repo="."
event=""
status=""
summary=""
details=""
files=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo) repo="$2"; shift 2 ;;
    --event) event="$2"; shift 2 ;;
    --status) status="$2"; shift 2 ;;
    --summary) summary="$2"; shift 2 ;;
    --details) details="$2"; shift 2 ;;
    --files) files="$2"; shift 2 ;;
    *) echo "unknown_arg=$1" >&2; exit 2 ;;
  esac
done

if [[ -z "$event" || -z "$status" || -z "$summary" ]]; then
  echo "missing_required_args=event,status,summary" >&2
  exit 2
fi

repo_abs="$(cd "$repo" && pwd)"
state_dir="$repo_abs/.codex/state"
log_file="$state_dir/delivery-log.ndjson"
mkdir -p "$state_dir"

files_json="$(if [[ -n "$files" ]]; then printf '%s' "$files" | jq -R 'split(",") | map(gsub("^\\s+|\\s+$"; "")) | map(select(length > 0))'; else jq -cn '[]'; fi)"

jq -cn \
  --arg timestamp "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
  --arg repo "$repo_abs" \
  --arg event "$event" \
  --arg status "$status" \
  --arg summary "$summary" \
  --arg details "$details" \
  --argjson files "$files_json" \
  '{timestamp:$timestamp,repo:$repo,event:$event,status:$status,summary:$summary,details:$details,files:$files}' >> "$log_file"

echo "logged=$log_file"
echo "event=$event"
echo "status=$status"
