#!/usr/bin/env bash
set -euo pipefail

repo="."
limit="10"
json_mode="no"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo) repo="$2"; shift 2 ;;
    --limit) limit="$2"; shift 2 ;;
    --json) json_mode="yes"; shift ;;
    *) echo "unknown_arg=$1" >&2; exit 2 ;;
  esac
done

repo_abs="$(cd "$repo" && pwd)"
log_file="$repo_abs/.codex/state/delivery-log.ndjson"

if [[ ! -f "$log_file" ]]; then
  echo "missing_log_file=$log_file" >&2
  exit 1
fi

if [[ "$json_mode" == "yes" ]]; then
  tail -n "$limit" "$log_file"
  exit 0
fi

tail -n "$limit" "$log_file" | jq -r '"timestamp=" + .timestamp + " event=" + .event + " status=" + .status + " summary=" + .summary'
