#!/usr/bin/env python3
"""Create a production-state.json file for a video project."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
GATES = [
    "G0_brief",
    "G1_taste",
    "G2_story",
    "G3_assets",
    "G4_shotboards",
    "G5_render",
    "G6_release",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise SystemExit("Project slug cannot be empty.")
    if not SLUG_RE.match(slug):
        raise SystemExit(f"Invalid project slug: {value}")
    return slug


def build_state(args: argparse.Namespace) -> dict:
    now = utc_now()
    return {
        "version": 1,
        "project_slug": args.project_slug,
        "title": args.title or args.project_slug.replace("-", " ").title(),
        "created_at": now,
        "updated_at": now,
        "status": "draft",
        "taste": args.taste,
        "gates": {
            gate: {"status": "pending", "files": [], "notes": ""} for gate in GATES
        },
        "scenes": [],
        "render_attempts": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create production-state.json.")
    parser.add_argument("project_slug", help="Project slug or title.")
    parser.add_argument("--path", default="production-state.json", help="Output JSON path.")
    parser.add_argument("--title", default="", help="Project title.")
    parser.add_argument("--taste", default=None, help="Taste slug to attach.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing file.")
    args = parser.parse_args()

    args.project_slug = normalize_slug(args.project_slug)
    output = Path(args.path).expanduser().resolve()
    if output.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(build_state(args), indent=2) + "\n", encoding="utf-8")
    print(f"Created production state: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
