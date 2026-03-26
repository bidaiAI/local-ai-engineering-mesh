from __future__ import annotations

from argparse import Namespace
import json

from ..runtime import inspect_project, resolve_project


def run_inspect(args: Namespace) -> int:
    project = resolve_project(args.project)
    result = inspect_project(project)
    if args.json:
        print(json.dumps(result, indent=2))
        return 0
    print("mesh inspect")
    print(f"- project: {result['project']}")
    print(f"- shared law in project: {'yes' if result['shared_law']['project_agents'] else 'no'}")
    print(f"- codex: {'yes' if result['codex']['present'] else 'no'} | memory={result['codex']['memory_files']} | state={result['codex']['state_files']}")
    print(f"- claude: {'yes' if result['claude']['present'] else 'no'}")
    print(f"- cursor: {'yes' if result['cursor']['present'] else 'no'} | rules={result['cursor']['rule_files']}")
    print(f"- antigravity: {'yes' if result['antigravity']['present'] else 'no'} | workflows={result['antigravity']['workflow_files']} | knowledge={result['antigravity']['knowledge_files']}")
    print(f"- mesh runtime: handoff={'yes' if result['mesh']['handoff_present'] else 'no'} | evidence_files={result['mesh']['evidence_files']} | runtime_metadata={'yes' if result['mesh']['runtime_present'] else 'no'}")
    return 0
