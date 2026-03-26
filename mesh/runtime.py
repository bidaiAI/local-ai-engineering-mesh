from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import shutil
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass
class MeshPaths:
    project: Path
    codex_memory: Path
    codex_state: Path
    cursor_rules: Path
    mesh_dir: Path
    mesh_evidence: Path
    mesh_handoff: Path
    mesh_runtime: Path


def resolve_project(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()


def get_paths(project: Path) -> MeshPaths:
    return MeshPaths(
        project=project,
        codex_memory=project / ".codex" / "memory",
        codex_state=project / ".codex" / "state",
        cursor_rules=project / ".cursor" / "rules",
        mesh_dir=project / ".mesh",
        mesh_evidence=project / ".mesh" / "evidence",
        mesh_handoff=project / ".mesh" / "handoff.md",
        mesh_runtime=project / ".mesh" / "runtime.json",
    )


def ensure_dirs(paths: MeshPaths) -> None:
    for p in (paths.codex_memory, paths.codex_state, paths.cursor_rules, paths.mesh_dir, paths.mesh_evidence):
        p.mkdir(parents=True, exist_ok=True)


def copy_if_missing(src: Path, dest: Path, force: bool = False) -> bool:
    if dest.exists() and not force:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return True


def write_text_if_missing(dest: Path, content: str, force: bool = False) -> bool:
    if dest.exists() and not force:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content)
    return True


def bootstrap_project(project: Path, force: bool = False, write_agents: bool = False) -> dict:
    paths = get_paths(project)
    ensure_dirs(paths)
    copied: list[str] = []

    for name in [
        "PROJECT-active-context.md",
        "PROJECT-command-map.md",
        "PROJECT-decisions.md",
        "PROJECT-patterns.md",
        "PROJECT-troubleshooting.md",
    ]:
        src = TEMPLATES_DIR / "project-memory" / name
        dest = paths.codex_memory / name
        if copy_if_missing(src, dest, force=force):
            copied.append(str(dest.relative_to(project)))

    policy_src = TEMPLATES_DIR / "policy.env.example"
    policy_dest = paths.codex_state / "policy.env.example"
    if copy_if_missing(policy_src, policy_dest, force=force):
        copied.append(str(policy_dest.relative_to(project)))

    for src_name, dest_name in [
        ("engineering-mesh.mdc", "00-engineering-mesh.mdc"),
        ("evidence-release-gate.mdc", "10-evidence-release-gate.mdc"),
    ]:
        src = TEMPLATES_DIR / "cursor" / src_name
        dest = paths.cursor_rules / dest_name
        if copy_if_missing(src, dest, force=force):
            copied.append(str(dest.relative_to(project)))

    handoff_template = """# Mesh Handoff

## Task
- 

## Current Status
- 

## Evidence Collected
- 

## Open Risks
- 

## Recommended Next Endpoint
- Codex / Claude / Cursor / Antigravity

## Next Concrete Action
- 
"""
    if write_text_if_missing(paths.mesh_handoff, handoff_template, force=force):
        copied.append(str(paths.mesh_handoff.relative_to(project)))

    evidence_readme = """# Evidence

Store lightweight verification artifacts here:
- screenshots
- logs
- test notes
- runtime proofs
"""
    evidence_readme_path = paths.mesh_evidence / "README.md"
    if write_text_if_missing(evidence_readme_path, evidence_readme, force=force):
        copied.append(str(evidence_readme_path.relative_to(project)))

    runtime_payload = {
        "version": "0.1.0",
        "initialized_at": utc_now_iso(),
        "project_root": ".",
        "features": {
            "project_memory": True,
            "project_state": True,
            "cursor_rules": True,
            "mesh_handoff": True,
            "mesh_evidence": True,
        },
    }
    paths.mesh_runtime.write_text(json.dumps(runtime_payload, indent=2) + "\n")
    copied.append(str(paths.mesh_runtime.relative_to(project)))

    if write_agents:
        agents_src = TEMPLATES_DIR / "AGENTS.example.md"
        agents_dest = project / "AGENTS.md"
        if copy_if_missing(agents_src, agents_dest, force=force):
            copied.append(str(agents_dest.relative_to(project)))

    return {
        "project": str(project),
        "copied": copied,
        "paths": {
            "codex_memory": str(paths.codex_memory),
            "codex_state": str(paths.codex_state),
            "cursor_rules": str(paths.cursor_rules),
            "mesh_dir": str(paths.mesh_dir),
        },
    }


def count_files(paths: Iterable[Path]) -> int:
    total = 0
    for path in paths:
        if path.exists():
            total += sum(1 for item in path.rglob("*") if item.is_file())
    return total


def inspect_project(project: Path) -> dict:
    paths = get_paths(project)
    claude_root = project / "CLAUDE.md"
    ag_workflows = project / "_agents" / "workflows"
    ag_knowledge = project / "_agents" / "knowledge"
    return {
        "project": str(project),
        "shared_law": {"project_agents": (project / "AGENTS.md").exists()},
        "codex": {"present": (project / ".codex").exists(), "memory_files": count_files([paths.codex_memory]), "state_files": count_files([paths.codex_state])},
        "claude": {"present": claude_root.exists()},
        "cursor": {"present": (project / ".cursor").exists(), "rule_files": count_files([paths.cursor_rules])},
        "antigravity": {"present": ag_workflows.exists() or ag_knowledge.exists(), "workflow_files": count_files([ag_workflows]), "knowledge_files": count_files([ag_knowledge])},
        "mesh": {"handoff_present": paths.mesh_handoff.exists(), "evidence_files": count_files([paths.mesh_evidence]), "runtime_present": paths.mesh_runtime.exists()},
    }


def render_handoff(project: Path, task: str | None, next_endpoint: str | None, summary: str | None, evidence: list[str], risks: list[str], force: bool = True) -> Path:
    paths = get_paths(project)
    ensure_dirs(paths)
    body = "\n".join([
        "# Mesh Handoff",
        "",
        f"_Updated: {utc_now_iso()}_",
        "",
        "## Task",
        f"- {task}" if task else "- ",
        "",
        "## Current Status",
        f"- {summary}" if summary else "- ",
        "",
        "## Evidence Collected",
        *([f"- {i}" for i in evidence] or ["- "]),
        "",
        "## Open Risks",
        *([f"- {i}" for i in risks] or ["- "]),
        "",
        "## Recommended Next Endpoint",
        f"- {next_endpoint}" if next_endpoint else "- Codex / Claude / Cursor / Antigravity",
        "",
        "## Next Concrete Action",
        "- ",
        "",
    ])
    write_text_if_missing(paths.mesh_handoff, body, force=force)
    return paths.mesh_handoff


def verify_project(project: Path) -> tuple[dict, int]:
    paths = get_paths(project)
    checks = {
        "project_memory": paths.codex_memory.exists() and any(paths.codex_memory.iterdir()) if paths.codex_memory.exists() else False,
        "project_state": paths.codex_state.exists() and any(paths.codex_state.iterdir()) if paths.codex_state.exists() else False,
        "cursor_rules": paths.cursor_rules.exists() and any(paths.cursor_rules.iterdir()) if paths.cursor_rules.exists() else False,
        "mesh_handoff": paths.mesh_handoff.exists(),
        "mesh_evidence": paths.mesh_evidence.exists(),
        "runtime_metadata": paths.mesh_runtime.exists(),
    }
    passed = sum(1 for v in checks.values() if v)
    core_ok = checks["project_memory"] and checks["project_state"] and checks["cursor_rules"]
    return {"project": str(project), "checks": checks, "passed": passed, "total": len(checks), "status": "ready" if core_ok else "incomplete"}, 0 if core_ok else 1
