---
name: visual-evidence
description: Browser-first and desktop-aware visual QA evidence collection. Use when the user asks for screenshots, UI inspection, visual comparison, or proof of frontend behavior, and the workflow should prefer safer narrow capture paths before OS-level screenshots.
---

# Visual Evidence

Use this skill to collect visual proof without turning screenshot capture into a blunt instrument.

## Goals
- prefer the narrowest capture method
- keep evidence relevant to the task
- reduce accidental capture of sensitive information
- unify browser QA and screenshot behavior

## Tool priority

### 1. Browser or app under Playwright control
- prefer `playwright` or `playwright-interactive`
- use browser-native screenshots and traces first

### 2. Tool-specific capture exists
- use that tool-specific path before OS-level capture

### 3. OS-level capture is necessary
- use desktop screenshot only when:
  - the target is a native desktop app
  - the target is an entire window not reachable by browser automation
  - the user explicitly asks for a desktop screenshot

## Required workflow

### Step 1: define the visual claim
- what exactly needs to be shown?
- which state or interaction is being verified?

### Step 2: choose the narrowest capture surface
- single DOM state or browser page
- single browser window
- single app window
- single region
- full screen only as a last resort

### Step 3: choose storage mode
- internal inspection:
  - temp path by default
- user-requested artifact:
  - save where requested

### Step 4: capture and review
- collect the image
- verify it actually proves the intended claim
- if it does not, recapture more narrowly or at the correct state

## Guardrails
- Do not use desktop screenshot when browser-native capture is enough.
- Do not capture all monitors unless the user explicitly asks.
- Avoid capturing terminals, password managers, inboxes, chat apps, or unrelated windows.
- Prefer temporary local storage for internal inspection artifacts.
- State clearly when OS-level permission prompts are required.

## Definition of done
- the capture target is explicit
- the capture method is the narrowest safe choice
- the image supports a concrete QA claim
