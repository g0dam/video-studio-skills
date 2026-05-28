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
ANALYSIS_DIMENSIONS = [
    "narrative_structure",
    "scene_world",
    "mise_en_scene",
    "character_performance",
    "shot_size",
    "camera_angle_position",
    "camera_movement",
    "composition_visual_design",
    "optics_texture",
    "lighting",
    "color_art_direction",
    "editing_rhythm",
    "transitions_graphic_links",
    "sound_music",
    "platform_ai_production",
]


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
        "analysis_dimensions": {key: [] for key in ANALYSIS_DIMENSIONS},
        "legal_notes": {
            "public_sources_only": True,
            "no_identity_clone": True,
            "no_shot_for_shot_copy": True,
            "no_specific_plot_copy": True,
            "no_protected_design_clone": True,
            "no_voice_or_music_clone": True,
            "source_inventory_in_source_log_only": True,
        },
        "usage_constraints": [],
    }


def taste_template(title: str) -> str:
    return f"""# {title}

## Essence

TODO: Summarize the transferable creative grammar in one paragraph.

## Best For

- TODO

## Director Section Contract

For each director section below, fill the reusable taste rather than source inventory:

- Observed evidence summary:
- Abstract pattern:
- Viewer effect:
- Reusable production rule:
- Copy-risk boundary:
- Evidence confidence:

## Generalization Gate

- Source inventory kept in source-log:
- Transferable craft functions:
- New-work substitution rule:
- Copy-risk boundary:
- Evidence confidence:

## Narrative and Structure

- Hook:
- Build:
- Turn:
- Payoff:
- Common motifs:
- Information reveal order:
- Ending aftertaste:

## Scene and World

- Era and location:
- Social class and cultural signals:
- Space scale and geography:
- Weather and season:
- Realism versus stylization:
- Prop system and set density:
- Movement path and spatial pressure:

## Mise-en-scene

- Staging:
- Foreground/midground/background:
- Prop placement and visual center:
- Occlusion and depth:
- Symmetry/asymmetry:
- Object metaphor:
- Environmental storytelling:

## Character and Performance

- Role identity and status:
- Emotional temperature:
- Face and eye behavior:
- Posture, gait, gesture, breath:
- Dialogue and subtext:
- Distance, power, and intimacy:
- Restraint versus exaggeration:

## Shot Size

- Dominant shot distances:
- Inserts and details:
- Reaction shots:
- Establishing or empty shots:

## Camera Angle and Position

- Angle habits:
- Subjective/objective viewpoint:
- Obstructed, mirror, surveillance, or voyeur positions:
- Power relation created by camera height:

## Camera Movement

- Movement types:
- Movement motivation:
- Handheld/mechanical/breathing feel:
- Focus movement:

## Composition and Visual Design

- Aspect ratio and safe area:
- Subject placement:
- Symmetry, negative space, leading lines:
- Depth layers and foreground:
- Shape language and visual tension:

## Optics and Image Texture

- Focal length feel:
- Depth of field:
- Exposure and shutter feel:
- Grain, sharpness, haze, flare, dirt:
- Film/digital/documentary/commercial feel:

## Lighting

- Motivated sources:
- Key/fill/rim/eye light:
- Hard/soft, high-key/low-key:
- Shadow shape:
- Color temperature and moving light:

## Color and Art Direction

- Main/support/accent colors:
- Warm/cool, saturation, brightness, contrast:
- Skin tone behavior:
- Color symbolism:
- Character/location color rules:
- Color shift across the piece:

## Editing and Rhythm

- Shot length:
- Cut frequency:
- Match logic and continuity:
- Montage, jump cut, cross-cutting, repetition:
- Pause, acceleration, release:

## Transitions and Graphic Links

- Transition types:
- Graphic or action matches:
- Sound lead-in or continuation:
- Time/space/emotion transition logic:

## Sound and Music

- Dialogue:
- Ambience:
- Foley and effects:
- Music role and motif:
- Silence:
- Diegetic/non-diegetic behavior:
- Sound bridge:
- Mix, reverb, spatiality:

## Platform and AI Production Behavior

- First-frame rule:
- Caption/subtitle behavior:
- Cover or thumbnail moment:
- Loop behavior:
- Sound-on/sound-off assumptions:
- Render risks:
- Image-generation opportunities:

## Prompt Implications

- Use:
- Avoid:
- Substitution rules:
- Story planning implications:
- Asset and continuity locks:
- Camera/render prompt locks:
- Sound/edit prompt locks:
- Anti-copy constraints:
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

### Dimension Evidence Matrix

| Dimension | Observed Evidence | Inferred Pattern | Reusable Rule Candidate | Copy-Risk Redline | Confidence |
| --- | --- | --- | --- | --- | --- |

### Repeated Patterns

- TODO

### Source Inventory Kept Out of Taste

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
- lighting:
- composition:
- optics:
- texture:
- sound:
- editing:
- transition:
- performance:

## Negative Vocabulary

- avoid:
- common AI failures:

## Reusable Prompt Blocks

### Story Lock

TODO

### Visual Lock

TODO

### Camera and Edit Lock

TODO

### Motion Lock

TODO

### Continuity Lock

TODO

### Sound and Edit Lock

TODO

### Anti-Copy Lock

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
