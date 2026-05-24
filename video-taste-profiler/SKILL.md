---
name: video-taste-profiler
description: "Analyze a creator, account, public video set, local video file, or uploaded reference into a reusable AI-video taste profile. Use when the user wants to learn a video's style, extract a creator's repeatable visual grammar, build a taste directory, compare video references, or create a non-infringing director-style profile for later scripts, shotboards, render prompts, and release assets."
---

# Video Taste Profiler

Use this skill to turn evidence from existing videos into a portable taste profile. A taste is not a clone of a person or a shot-for-shot recipe. It is a reusable description of narrative habits, cinematic grammar, editing rhythm, sound behavior, performance direction, platform pacing, and constraints that can guide new original videos.

## Workflow

1. Identify the source mode: creator/account, public URL set, local video file, uploaded stills, existing project assets, or user-described references.
2. Gather enough evidence to avoid one-example overfitting. For web sources, cite URLs and summarize observations. For local sources, inspect available files and, when useful, suggest frame extraction without overwriting source media.
3. Analyze the source with `references/director-analysis.md`.
4. Record evidence with `references/source-evidence.md`; do not paste secrets, private account data, transcripts in full, or copyrighted long passages.
5. Create or update `taste/<taste-slug>/` with the schema in `references/taste-schema.md`.
6. Make the taste actionable: include prompt vocabulary, negative constraints, scene planning implications, and render warnings.
7. End with open risks: low confidence areas, missing source types, legal/ethical constraints, and what should be tested in generation.

## Output Contract

Create one directory per taste:

```text
taste/<taste-slug>/
  manifest.json
  taste.md
  source-log.md
  prompt-vocabulary.md
```

Use `../scripts/new_taste.py` from this skill pack to create the directory when starting from scratch, then fill the files by analysis. Use `../scripts/validate_taste.py` before finalizing.

## Taste Rules

- Extract transferable craft, not impersonation. Describe materials, camera behavior, pacing, narrative structure, and constraints.
- Avoid "in the exact style of" language for living creators. Use "informed by the observed taste profile" or "using this reusable taste grammar."
- Separate evidence from inference. Mark uncertain observations as low confidence.
- Preserve source privacy. Do not include private credentials, private URLs, hidden metadata, or full transcripts unless the user explicitly provided them for this purpose.
- Prefer concrete vocabulary: shot distance, lens feel, blocking, cut density, camera path, color contrast, texture, sound bridge, silence, on-screen text behavior.

## Resources

- `references/director-analysis.md`: professional analysis dimensions.
- `references/source-evidence.md`: source sampling, citation, and evidence rules.
- `references/taste-schema.md`: required files and fields for `taste/<slug>/`.
