from __future__ import annotations

from argparse import Namespace

from ..runtime import render_handoff, resolve_project


def run_handoff(args: Namespace) -> int:
    project = resolve_project(args.project)
    handoff_path = render_handoff(project=project, task=args.task, next_endpoint=args.next_endpoint, summary=args.summary, evidence=args.evidence, risks=args.risk)
    print("mesh handoff written")
    print(f"- file: {handoff_path}")
    return 0
