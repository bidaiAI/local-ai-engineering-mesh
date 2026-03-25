---
name: safe-pr-flow
description: Safe GitHub branch, commit, push, and PR workflow with explicit staging and verification gates. Use when the user wants to publish work for review without the risks of one-shot stage-all automation.
---

# Safe PR Flow

Use this skill instead of any one-command publish flow.

## Goals
- prevent unrelated files from being published
- keep git and GitHub actions explicit
- separate verification from publication
- make PR creation review-safe

## Default policy
- No `git add -A` by default.
- No push until the staged diff is understood.
- No PR until verification has run or its absence is explicitly acknowledged.
- Draft PR is safer than ready-for-review by default.

## Required workflow

### Step 1: inspect repository state
- run the bundled pre-publish checker first:

```bash
bash <path-to-skill>/scripts/pre_publish_check.sh [repo]
```

- inspect branch
- inspect changed files
- inspect whether unrelated changes are present
- if unexpected changes appear, stop and realign before publishing

### Step 2: select files intentionally
- stage only the intended files or hunks
- confirm the staged diff matches the task

### Step 3: verify
- run the smallest meaningful checks
- if checks are missing, state that clearly before publishing

### Step 4: commit
- use a focused commit message that matches the staged diff

### Step 5: push
- push only after the staged diff and verification story are clear
- do not auto-pull and retry blindly on push failure

### Step 6: create PR
- use a draft PR by default
- summarize:
  - what changed
  - why it changed
  - what was verified
  - what remains risky or unverified

## Guardrails
- Do not use `git add -A` unless the user explicitly wants all changes included.
- Do not publish when the worktree contains unexplained unrelated changes.
- Do not auto-resolve push failures with hidden merge or pull behavior.
- Do not create a misleading PR description that overstates verification.

## Works with
- `gh-fix-ci`
- `gh-address-comments`

## Definition of done
- intended files are staged intentionally
- verification status is explicit
- pushed branch and draft PR reflect only the intended work
