#!/usr/bin/env bash
set -euo pipefail

repo="${1:-.}"
cd "$repo"

markers=()

[[ -f wrangler.toml || -f wrangler.json || -f wrangler.jsonc ]] && markers+=("cloudflare")
[[ -f render.yaml ]] && markers+=("render")
[[ -f netlify.toml ]] && markers+=("netlify")
[[ -f vercel.json || -d .vercel ]] && markers+=("vercel")

count="${#markers[@]}"

if [[ "$count" -eq 0 ]]; then
  echo "target=none"
  exit 0
fi

if [[ "$count" -eq 1 ]]; then
  echo "target=${markers[0]}"
  exit 0
fi

echo "target=ambiguous"
printf 'markers=%s\n' "$(IFS=,; echo "${markers[*]}")"
