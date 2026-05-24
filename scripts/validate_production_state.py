#!/usr/bin/env python3
"""Validate a production-state.json file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


GATES = [
    "G0_brief",
    "G1_taste",
    "G2_story",
    "G3_assets",
    "G4_shotboards",
    "G5_render",
    "G6_release",
]
STATUSES = {"pending", "in_progress", "ready", "blocked", "locked"}


def load_state(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return None, [f"{path}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return None, [f"{path}: state must be a JSON object"]
    return data, []


def validate_state(path: Path, check_files: bool) -> list[str]:
    errors: list[str] = []
    state, load_errors = load_state(path)
    errors.extend(load_errors)
    if state is None:
        return errors

    for field in ["version", "project_slug", "title", "created_at", "updated_at", "status", "gates"]:
        if field not in state:
            errors.append(f"{path}: missing field '{field}'")

    if state.get("version") != 1:
        errors.append(f"{path}: version must be 1")

    gates = state.get("gates")
    if not isinstance(gates, dict):
        errors.append(f"{path}: gates must be an object")
        return errors

    for gate in GATES:
        item = gates.get(gate)
        if not isinstance(item, dict):
            errors.append(f"{path}: missing gate {gate}")
            continue
        status = item.get("status")
        if status not in STATUSES:
            errors.append(f"{path}: {gate}.status is invalid")
        files = item.get("files")
        if not isinstance(files, list):
            errors.append(f"{path}: {gate}.files must be a list")
            continue
        if check_files:
            for rel in files:
                if not isinstance(rel, str):
                    errors.append(f"{path}: {gate}.files entries must be strings")
                    continue
                if not (path.parent / rel).exists():
                    errors.append(f"{path}: referenced file does not exist: {rel}")

    if not isinstance(state.get("scenes", []), list):
        errors.append(f"{path}: scenes must be a list")
    if not isinstance(state.get("render_attempts", []), list):
        errors.append(f"{path}: render_attempts must be a list")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate production-state.json.")
    parser.add_argument("path", nargs="?", default="production-state.json")
    parser.add_argument("--check-files", action="store_true", help="Verify referenced files exist.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable result.")
    args = parser.parse_args()

    path = Path(args.path).expanduser().resolve()
    errors = validate_state(path, args.check_files)
    if args.json:
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2))
    elif errors:
        for error in errors:
            print(error, file=sys.stderr)
    else:
        print(f"OK: {path}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
