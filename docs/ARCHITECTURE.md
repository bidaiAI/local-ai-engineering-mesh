# Architecture

## Core thesis

The goal is not to create "more prompts."

The goal is to create a Codex-native engineering operating system with durable workflow behavior.

## Layer model

### 1. Bootstrap
- inspect repository shape
- detect commands
- map risk surfaces
- create initial memory and policy defaults

### 2. Constitution
- operating charter
- quality expectations
- release rules
- escalation rules
- definition of done

### 3. Memory
- global memory
- project memory
- path-specific memory
- session context

### 4. Hooks and commands
- preflight
- pre-edit
- pre-publish
- pre-deploy
- post-implementation

### 5. Skills
- core skills
- augmentation skills
- specialized skills

### 6. Orchestration
- task routing
- role assignment
- stop points
- handoff contracts

### 7. Research
- current best practices
- official docs lookup
- X and ecosystem signal gathering
- parallel research paths before broad implementation when uncertainty is high

### 8. Evidence and review
- tests
- logs
- screenshots
- review findings
- explicit verified vs unverified status

### 9. Evolution
- repeated wins become checklists, scripts, or skills
- capability compounds over time

## Role system

The workflow uses explicit roles instead of one monolithic assistant:

- `execution-orchestrator`
- `architecture-gatekeeper`
- `reality-check-qa`
- `release-risk-governor`
- `skillcraft-reuse-loop`

These roles make large work easier to route, verify, and publish safely.

## Durable planning

The architecture also benefits from a durable planning layer:
- structured plan artifacts
- acceptance criteria that survive sessions
- execution that follows a prepared route instead of improvising from scratch each time

## Operating effect

This changes Codex from:
- opportunistic execution

into:
- governed execution
- memory-backed execution
- evidence-backed completion
- safer release behavior
