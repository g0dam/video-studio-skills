---
name: video-taste-profiler
description: "Analyze a creator, account, public video set, local video file, or uploaded reference into a reusable AI-video taste profile. Use when the user wants to learn a video's style, extract a creator's repeatable visual grammar, build a taste directory, compare video references, or create a non-infringing director-style profile for later scripts, shotboards, render prompts, and release assets."
---

# Video Taste Profiler

Use this skill to turn evidence from existing videos into a portable taste profile. A taste is not a clone of a person, a shot-for-shot recipe, or a recap of what happened in one source video. It is a reusable director-level grammar: narrative structure, world logic, mise-en-scene, performance, camera, optics, light, color, edit, transition, sound, and production constraints that can guide new original videos.

## Director Abstraction Requirement

The main output must abstract the source's repeatable taste, not list the source's literal contents. Treat source details as evidence in `source-log.md`; translate them into craft rules in `taste.md` and `prompt-vocabulary.md`.

- Do not write the taste as "this video has a cat, a gift box, a pool, and a final card." That is source inventory.
- Do write the taste as "ordinary domestic space is interrupted by an object-triggered fantasy reveal; the emotional beat lands through animal reaction, soft light contrast, and a short release hold." That is transferable taste.
- If the user names a known film, studio, creator, or IP as the taste source, use it only as analysis context. Extract broad craft grammar and explicitly avoid requests to copy protected characters, exact shots, logos, costumes, dialogue, music, or scene order.
- Keep concrete frame facts, metadata, transcripts, and one-off props in `source-log.md` unless they reveal a repeatable grammar.
- Every major claim in `taste.md` should answer: what is the abstract pattern, why does it work, and how should a later story/shotboard/render preserve it?

## Generalization Gate

Before finalizing a taste, run every important observation through this gate:

1. **Source fact**: what was directly observed, with source IDs, kept in `source-log.md`.
2. **Craft function**: what job the fact performs, such as reveal, intimacy, pressure, comic delay, power shift, or emotional release.
3. **Reusable rule**: how a new original work can recreate that function with different characters, objects, locations, dialogue, and shot order.
4. **Copy-risk boundary**: what must not transfer, including protected characters, exact scene sequence, signature props, readable text, logos, costumes, music, voice, dialogue, layout, or distinctive set design.

Only step 3 belongs in `taste.md` and `prompt-vocabulary.md`. Steps 1 and 4 should be visible in `source-log.md`, `usage_constraints`, and negative vocabulary so downstream story, asset, storyboard, and render steps do not drift into copying.

## Workflow

1. Identify the source mode: creator/account, public URL set, local video file, uploaded stills, existing project assets, or user-described references.
2. Gather enough evidence to avoid one-example overfitting. For web sources, cite URLs and summarize observations. For local sources, inspect available files and, when useful, suggest frame extraction without overwriting source media.
3. Analyze the source with `references/director-analysis.md`. Cover the full director craft map unless source evidence is missing: narrative/structure, scene/world, mise-en-scene, character/performance, shot size, camera angle/position, camera movement, composition/visual design, optics/texture, lighting, color/art direction, editing/rhythm, transitions/graphic links, and sound/music. For each dimension, record evidence, inferred pattern, reusable rule, confidence, and copy-risk redline. Add platform and AI-production behavior only after the director analysis is complete.
4. Record evidence with `references/source-evidence.md`; do not paste secrets, private account data, transcripts in full, or copyrighted long passages.
5. Translate literal details with the Generalization Gate. If an observation cannot be expressed without keeping source-specific nouns, names, dialogue, or shot order, leave it as evidence rather than turning it into a taste rule.
6. Create or update `taste/<taste-slug>/` with the schema in `references/taste-schema.md`.
7. Make the taste actionable: include abstract prompt vocabulary, negative constraints, scene planning implications, render warnings, and production locks for story logic, blocking, camera, light, color, edit, and sound. Production locks should preserve the grammar, not recreate the source's specific props or shot order.
8. End with open risks: low confidence areas, missing source types, legal/ethical constraints, copy-risk boundaries, and what should be tested in generation.

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
- Separate evidence from abstraction. `source-log.md` can name concrete source facts; `taste.md` should mainly contain reusable director rules.
- Preserve source privacy. Do not include private credentials, private URLs, hidden metadata, or full transcripts unless the user explicitly provided them for this purpose.
- Prefer concrete vocabulary: shot distance, lens feel, camera angle, blocking, cut density, camera path, composition, optical texture, light motivation, color contrast, transition logic, sound bridge, silence, on-screen text behavior.
- Do not flatten a taste into a mood board. Record how image, performance, time, sound, and platform behavior work together.
- Do not overfit a single reference. If only one video is available, mark coverage as provisional and phrase the taste as "observed grammar in this sample" rather than a complete account-level style.
- Do not let downstream prompts say "same as this video." They should say which abstract rule to use, what new story material replaces the source material, and what source-specific elements are forbidden.

## Resources

- `references/director-analysis.md`: professional analysis dimensions.
- `references/source-evidence.md`: source sampling, citation, and evidence rules.
- `references/taste-schema.md`: required files and fields for `taste/<slug>/`.
