---
name: state-store-memory
description: Persist and reload repo working state across long tasks and sessions. Use when work spans multiple phases, pauses, reviews, or handoffs and the next session should recover task state from files instead of memory alone.
---

# State Store Memory

Use this skill to turn transient session knowledge into durable repo state.

## Goals
- persist the current phase, summary, and next step
- keep a machine-readable event log for governance hooks and deliveries
- reload recent context without re-reading the whole thread

## Load these only when needed
- Read `references/state-schema.md` when changing the persisted shape.
- Use `scripts/save_state.sh` to write the latest working snapshot.
- Use `scripts/show_state.sh` to inspect the latest snapshot.
- Use `scripts/log_event.sh` to append a structured delivery or governance event.
- Use `scripts/recent_events.sh` to review the latest state transitions.

## Required workflow

### Step 1: capture the active state
- current phase
- current summary
- next concrete step
- affected files or modules
- evidence gathered so far
- open questions or constraints

### Step 2: keep the event log honest
- log hook outcomes
- log release or publish decisions
- log meaningful verification moments
- log resumable summaries instead of chatty narrative

### Step 3: reload before resuming large work
- inspect the latest snapshot
- inspect recent events
- prefer repo state over stale recollection

## Outputs
- `<project>/.codex/state/session-state.json`
- `<project>/.codex/state/delivery-log.ndjson`

## Guardrails
- Do not duplicate the same snapshot when nothing material changed.
- Do not claim the state is current unless it was refreshed after the last real change.
- Keep entries factual, compact, and machine-parseable.
