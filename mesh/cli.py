from __future__ import annotations

import argparse

from .commands.handoff_cmd import run_handoff
from .commands.init_cmd import run_init
from .commands.inspect_cmd import run_inspect
from .commands.verify_cmd import run_verify


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mesh", description="Minimal CLI for the Local AI Engineering Mesh.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Bootstrap a project into the mesh runtime.")
    init_parser.add_argument("project", nargs="?", default=".", help="Project path to initialize.")
    init_parser.add_argument("--force", action="store_true", help="Overwrite starter files.")
    init_parser.add_argument("--write-project-agents", action="store_true", help="Write AGENTS.md into the project root.")
    init_parser.set_defaults(func=run_init)

    inspect_parser = subparsers.add_parser("inspect", help="Inspect mesh adoption in a project.")
    inspect_parser.add_argument("project", nargs="?", default=".", help="Project path to inspect.")
    inspect_parser.add_argument("--json", action="store_true", help="Emit JSON.")
    inspect_parser.set_defaults(func=run_inspect)

    handoff_parser = subparsers.add_parser("handoff", help="Write a compact cross-tool handoff file.")
    handoff_parser.add_argument("project", nargs="?", default=".", help="Project path.")
    handoff_parser.add_argument("--task", help="Task summary.")
    handoff_parser.add_argument("--next-endpoint", help="Suggested next tool endpoint.")
    handoff_parser.add_argument("--summary", help="Current status summary.")
    handoff_parser.add_argument("--evidence", action="append", default=[], help="Evidence item. Repeat for multiple entries.")
    handoff_parser.add_argument("--risk", action="append", default=[], help="Risk item. Repeat for multiple entries.")
    handoff_parser.set_defaults(func=run_handoff)

    verify_parser = subparsers.add_parser("verify", help="Check whether the project meets the minimum mesh runtime bar.")
    verify_parser.add_argument("project", nargs="?", default=".", help="Project path.")
    verify_parser.add_argument("--json", action="store_true", help="Emit JSON.")
    verify_parser.set_defaults(func=run_verify)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
