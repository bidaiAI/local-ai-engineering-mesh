from __future__ import annotations

from argparse import Namespace

from ..runtime import bootstrap_project, resolve_project


def run_init(args: Namespace) -> int:
    project = resolve_project(args.project)
    result = bootstrap_project(project, force=args.force, write_agents=args.write_project_agents)
    print("mesh init complete")
    print(f"- project: {result['project']}")
    print("- created / updated:")
    for item in result["copied"]:
        print(f"  - {item}")
    print("- runtime roots:")
    for key, value in result["paths"].items():
        print(f"  - {key}: {value}")
    return 0
