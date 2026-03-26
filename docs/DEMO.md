# Demo

This repository now includes a minimal `mesh` CLI for showing the operating model as a runnable workflow, not just a documentation set.

## Fastest demo path

```bash
git clone https://github.com/bidaiAI/local-ai-engineering-mesh.git
cd local-ai-engineering-mesh
python3 -m mesh init /tmp/mesh-demo-project
python3 -m mesh inspect /tmp/mesh-demo-project
python3 -m mesh handoff /tmp/mesh-demo-project \
  --task "Add login rate limiting" \
  --summary "Planning complete, ready for editor implementation" \
  --next-endpoint Cursor \
  --evidence "project runtime initialized" \
  --risk "rate limit storage backend not decided yet"
python3 -m mesh verify /tmp/mesh-demo-project
```

## What this demo proves

1. `mesh init`
   - creates a governed project runtime
   - seeds memory, state, cursor rules, handoff, and evidence folders

2. `mesh inspect`
   - shows which parts of the mesh are already attached

3. `mesh handoff`
   - writes a compact cross-tool handoff so work can move between planning, editor work, and execution without resetting context

4. `mesh verify`
   - checks whether the minimum runtime bar is present

## Suggested 60-second recording

1. Run `python3 -m mesh init /tmp/mesh-demo-project`
2. Open the generated folders:
   - `/tmp/mesh-demo-project/.codex/memory/`
   - `/tmp/mesh-demo-project/.codex/state/`
   - `/tmp/mesh-demo-project/.cursor/rules/`
   - `/tmp/mesh-demo-project/.mesh/handoff.md`
3. Run `python3 -m mesh handoff ...`
4. Show the handoff file updating
5. Run `python3 -m mesh verify /tmp/mesh-demo-project`
