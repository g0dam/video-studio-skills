#!/usr/bin/env python3
"""Create a reusable video taste directory."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SOURCE_TYPES = ["creator", "account", "single-video", "local-video", "mixed", "original"]
CONFIDENCE = ["low", "medium", "high"]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def require_slug(slug: str) -> str:
    if not SLUG_RE.match(slug):
        raise SystemExit(
            f"Invalid slug '{slug}'. Use lowercase letters, digits, and hyphens only."
        )
    return slug


def write_new(path: Path, text: str) -> None:
    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {path}")
    path.write_text(text, encoding="utf-8")


def build_manifest(args: argparse.Namespace) -> dict:
    now = utc_now()
    return {
        "version": 1,
        "slug": args.slug,
        "title": args.title or args.slug.replace("-", " ").title(),
        "source_type": args.source_type,
        "source_refs": [],
        "created_at": now,
        "updated_at": now,
        "aspect_ratios": args.aspect_ratio,
        "duration_range_sec": {"min": args.min_duration, "max": args.max_duration},
        "confidence": args.confidence,
        "style_vectors": {
            "narrative": [],
            "camera": [],
            "editing": [],
            "color_light": [],
            "sound": [],
            "performance": [],
            "platform": [],
        },
        "legal_notes": {
            "public_sources_only": True,
            "no_identity_clone": True,
            "no_shot_for_shot_copy": True,
        },
        "usage_constraints": [],
    }


def taste_template(title: str) -> str:
    return f"""# {title}

## Essence

TODO: Summarize the transferable creative grammar in one paragraph.

## Best For

- TODO

## Narrative Grammar

- Hook:
- Build:
- Turn:
- Payoff:
- Common motifs:

## Visual Grammar

- Composition:
- Lens and shot size:
- Camera movement:
- Blocking:
- Texture and materials:

## Edit Rhythm

- Cut density:
- Transition logic:
- Silence or pause rules:

## Color, Light, and Sound

- Palette:
- Light sources:
- Music:
- Natural sound:
- Voice:

## Performance Direction

- Gesture scale:
- Eye behavior:
- Emotional temperature:

## Platform Behavior

- Aspect ratios:
- First-frame rule:
- Caption/subtitle behavior:
- Loop or ending behavior:

## Prompt Implications

- Use:
- Avoid:
- Render risks:

## Confidence and Gaps

- High confidence:
- Medium confidence:
- Low confidence:
"""


def source_log_template(title: str, source_type: str) -> str:
    return f"""# Source Log: {title}

## Coverage

- Source mode: {source_type}
- Number of sources: 0
- Date analyzed:
- Confidence:

## Sources

| ID | Source | Type | Duration | Notes | Evidence Used |
| --- | --- | --- | ---: | --- | --- |

## Observations

### Repeated Patterns

- TODO

### Exceptions

- TODO

### Uncertain Areas

- TODO
"""


def prompt_vocabulary_template(title: str) -> str:
    return f"""# Prompt Vocabulary: {title}

## Positive Vocabulary

- camera:
- motion:
- color:
- texture:
- sound:
- editing:
- performance:

## Negative Vocabulary

- avoid:
- common AI failures:

## Reusable Prompt Blocks

### Visual Lock

TODO

### Motion Lock

TODO

### Continuity Lock

TODO
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create taste/<slug>/ template files.")
    parser.add_argument("slug", help="Lowercase hyphenated taste slug.")
    parser.add_argument("--root", default=".", help="Video studio skill package root.")
    parser.add_argument("--title", default="", help="Display title for the taste.")
    parser.add_argument(
        "--source-type", choices=SOURCE_TYPES, default="original", help="Taste source mode."
    )
    parser.add_argument(
        "--aspect-ratio", action="append", default=None, help="Aspect ratio; repeatable."
    )
    parser.add_argument("--min-duration", type=int, default=5)
    parser.add_argument("--max-duration", type=int, default=90)
    parser.add_argument("--confidence", choices=CONFIDENCE, default="low")
    args = parser.parse_args()

    args.slug = require_slug(args.slug)
    args.aspect_ratio = args.aspect_ratio or ["9:16"]
    if args.min_duration < 1 or args.max_duration < args.min_duration:
        raise SystemExit("Duration range is invalid.")

    root = Path(args.root).expanduser().resolve()
    taste_dir = root / "taste" / args.slug
    if taste_dir.exists():
        raise SystemExit(f"Taste already exists: {taste_dir}")
    taste_dir.mkdir(parents=True)

    manifest = build_manifest(args)
    title = manifest["title"]
    write_new(taste_dir / "manifest.json", json.dumps(manifest, indent=2) + "\n")
    write_new(taste_dir / "taste.md", taste_template(title))
    write_new(taste_dir / "source-log.md", source_log_template(title, args.source_type))
    write_new(taste_dir / "prompt-vocabulary.md", prompt_vocabulary_template(title))

    print(f"Created taste: {taste_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
