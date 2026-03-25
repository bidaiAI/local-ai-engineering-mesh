# Execution Loop

## Main idea worth borrowing

The most valuable idea is not a specific Claude command.

It is the workflow loop:

`parallel research -> structured persistent plan -> mechanical execution -> evidence-backed completion`

## What to absorb

### 1. Research before broad execution
- do not jump straight from request to implementation
- gather signals from:
  - the codebase
  - prior decisions and memory
  - current external best practices

### 2. Persistent `plan.md` as a checkpoint
- the plan should survive context loss
- it should record:
  - problem summary
  - recommended approach
  - files likely to change
  - patterns to preserve
  - acceptance criteria

### 3. Execution becomes narrower and more mechanical
- once the plan is good, implementation should be less improvisational
- this reduces drift, scope creep, and false starts

### 4. Evidence closes the loop
- the plan is not done when code is written
- the plan is done when evidence satisfies the acceptance criteria

## What not to copy directly

- Claude-specific slash commands
- a specific plugin syntax
- a specific editor or terminal stack
- high-cost parallel-session habits without matching safety controls

## Codex-native interpretation

For Codex, the useful adaptation is:
- role-based orchestration
- research-first routing
- durable plan artifacts
- governed hooks
- evidence gates

That keeps the idea, while remaining native to Codex.
