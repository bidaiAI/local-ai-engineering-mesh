from __future__ import annotations

from argparse import Namespace
import json

from ..runtime import resolve_project, verify_project


def run_verify(args: Namespace) -> int:
    project = resolve_project(args.project)
    result, code = verify_project(project)
    if args.json:
        print(json.dumps(result, indent=2))
        return code
    print("mesh verify")
    print(f"- project: {result['project']}")
    print(f"- status: {result['status']} ({result['passed']}/{result['total']})")
    for key, value in result['checks'].items():
        print(f"  - {key}: {'pass' if value else 'missing'}")
    return code
