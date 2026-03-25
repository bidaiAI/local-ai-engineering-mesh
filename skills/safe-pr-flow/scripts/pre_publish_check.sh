#!/usr/bin/env bash
set -euo pipefail

repo="${1:-.}"
cd "$repo"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "FAIL: not inside a git worktree"
  exit 2
fi

branch="$(git branch --show-current 2>/dev/null || true)"
staged="$(git diff --cached --name-only)"
unstaged="$(git diff --name-only)"
untracked="$(git ls-files --others --exclude-standard)"

echo "branch=${branch:-detached}"
echo
echo "== git status =="
git status -sb

echo
echo "== staged files =="
if [[ -n "$staged" ]]; then
  printf '%s\n' "$staged"
else
  echo "(none)"
fi

echo
echo "== unstaged files =="
if [[ -n "$unstaged" ]]; then
  printf '%s\n' "$unstaged"
else
  echo "(none)"
fi

echo
echo "== untracked files =="
if [[ -n "$untracked" ]]; then
  printf '%s\n' "$untracked"
else
  echo "(none)"
fi

if [[ -z "$staged" ]]; then
  echo
  echo "FAIL: no staged changes"
  exit 1
fi

if [[ "$branch" == "main" || "$branch" == "master" ]]; then
  echo
  echo "WARN: publishing directly from $branch"
fi

if [[ -n "$unstaged" || -n "$untracked" ]]; then
  echo
  echo "WARN: worktree contains extra changes outside the staged set"
  exit 2
fi

echo
echo "PASS: staged set is isolated enough for review"
