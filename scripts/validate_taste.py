#!/usr/bin/env python3
"""Validate video taste directories."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_FILES = ["manifest.json", "taste.md", "source-log.md", "prompt-vocabulary.md"]
REQUIRED_FIELDS = [
    "version",
    "slug",
    "title",
    "source_type",
    "source_refs",
    "created_at",
    "updated_at",
    "aspect_ratios",
    "duration_range_sec",
    "confidence",
    "style_vectors",
    "legal_notes",
    "usage_constraints",
]
SOURCE_TYPES = {"creator", "account", "single-video", "local-video", "mixed", "original"}
CONFIDENCE = {"low", "medium", "high"}
STYLE_KEYS = {
    "narrative",
    "camera",
    "editing",
    "color_light",
    "sound",
    "performance",
    "platform",
}


def load_json(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return None, [f"{path}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return None, [f"{path}: manifest must be a JSON object"]
    return data, []


def validate_one(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_dir():
        return [f"{path}: not a directory"]

    for filename in REQUIRED_FILES:
        if not (path / filename).is_file():
            errors.append(f"{path}: missing {filename}")

    manifest_path = path / "manifest.json"
    if not manifest_path.exists():
        return errors

    manifest, json_errors = load_json(manifest_path)
    errors.extend(json_errors)
    if manifest is None:
        return errors

    for field in REQUIRED_FIELDS:
        if field not in manifest:
            errors.append(f"{manifest_path}: missing field '{field}'")

    slug = manifest.get("slug")
    if not isinstance(slug, str) or not SLUG_RE.match(slug):
        errors.append(f"{manifest_path}: slug must be lowercase hyphen-case")
    elif slug != path.name:
        errors.append(f"{manifest_path}: slug '{slug}' does not match directory '{path.name}'")

    if manifest.get("version") != 1:
        errors.append(f"{manifest_path}: version must be 1")

    if manifest.get("source_type") not in SOURCE_TYPES:
        errors.append(f"{manifest_path}: source_type is invalid")

    if manifest.get("confidence") not in CONFIDENCE:
        errors.append(f"{manifest_path}: confidence must be low, medium, or high")

    if not isinstance(manifest.get("source_refs"), list):
        errors.append(f"{manifest_path}: source_refs must be a list")

    if not isinstance(manifest.get("aspect_ratios"), list) or not manifest.get("aspect_ratios"):
        errors.append(f"{manifest_path}: aspect_ratios must be a non-empty list")

    duration = manifest.get("duration_range_sec")
    if not isinstance(duration, dict) or not {"min", "max"} <= set(duration):
        errors.append(f"{manifest_path}: duration_range_sec must contain min and max")
    else:
        if not isinstance(duration.get("min"), int) or not isinstance(duration.get("max"), int):
            errors.append(f"{manifest_path}: duration min/max must be integers")
        elif duration["min"] < 1 or duration["max"] < duration["min"]:
            errors.append(f"{manifest_path}: duration range is invalid")

    vectors = manifest.get("style_vectors")
    if not isinstance(vectors, dict):
        errors.append(f"{manifest_path}: style_vectors must be an object")
    else:
        missing = STYLE_KEYS - set(vectors)
        if missing:
            errors.append(f"{manifest_path}: style_vectors missing {sorted(missing)}")
        for key in STYLE_KEYS & set(vectors):
            if not isinstance(vectors[key], list):
                errors.append(f"{manifest_path}: style_vectors.{key} must be a list")

    return errors


def discover_targets(path: Path) -> list[Path]:
    if (path / "manifest.json").exists():
        return [path]
    taste_root = path / "taste"
    if taste_root.is_dir():
        return sorted(p for p in taste_root.iterdir() if p.is_dir())
    return sorted(p for p in path.iterdir() if p.is_dir()) if path.is_dir() else [path]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate taste directories.")
    parser.add_argument("path", nargs="?", default=".", help="Taste dir, taste root, or package root.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable result.")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    targets = discover_targets(root)
    all_errors: dict[str, list[str]] = {}
    for target in targets:
        errors = validate_one(target)
        if errors:
            all_errors[str(target)] = errors

    if args.json:
        print(json.dumps({"ok": not all_errors, "errors": all_errors}, indent=2))
    elif all_errors:
        for errors in all_errors.values():
            for error in errors:
                print(error, file=sys.stderr)
    else:
        print(f"OK: validated {len(targets)} taste director{'y' if len(targets) == 1 else 'ies'}")

    return 1 if all_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
