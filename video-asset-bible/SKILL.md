---
name: video-asset-bible
description: "Create a reusable visual asset bible for AI-video projects: characters, casting notes, wardrobe, locations, props, product forms, world rules, continuity anchors, and reference-image prompts. Use when the user needs consistent characters or places across scenes, a project bible before shotboarding, a continuity sheet, character/location/prop specs, or image-generation prompts for reusable video assets."
---

# Video Asset Bible

Use this skill to convert a story plan and optional taste into production assets that can survive multiple AI generations. It extends character design into a full continuity bible: people, spaces, objects, wardrobe, materials, and rules for what must not drift.

## Workflow

1. Read the selected taste and story plan.
2. Inspect existing project asset conventions before creating anything: `characters/`, `locations/`, `props/`, `assets-bible/`, `storyboard/`, `.agents/skills/video-character-design`, and any approved `.png` references. Reuse existing paths and approved images when they match the project.
3. Identify all repeated assets: characters, locations, props, wardrobe pieces, vehicles, UI/screens, product packaging, symbols, and text-bearing objects.
4. Build the bible with `references/asset-bible-schema.md`.
   - Preserve both creative framing and provider ratio when the plan includes a provider constraint.
   - For Seedance, record the provider ratio using the platform menu only: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`. Ultra-wide `2.33:1` maps to `21:9`.
5. For each core asset, write an image-generation prompt for a reference sheet when useful. Inherit the project/video aspect ratio for reusable visual assets unless the asset has a stronger reference-sheet reason to use another layout.
6. For identity-critical characters or expensive-to-iterate designs, create the `.md` spec first and only generate the `.png` after the user approves or explicitly says to proceed. For simple locations/props or explicit image requests, proceed directly.
7. When a core character, location, hero prop, or vehicle would materially improve continuity, directly use the `image_gen` tool to generate a reference image or sheet. Prefer generating images for assets that recur across scenes, have unusual geometry, or are hard to keep stable from text alone.
8. Define continuity anchors and allowed variation. Distinguish stable identity from per-scene lighting, pose, expression, weather, and camera changes.
9. Create handoff notes for shotboarding and render prompts.

## Output Contract

Use project-local paths:

```text
assets-bible/
  project-bible.md
  characters/<slug>.md
  characters/<slug>.png          # optional generated reference image
  locations/<slug>.md
  locations/<slug>.png           # optional generated reference image
  props/<slug>.md
  props/<slug>.png               # optional generated reference image
  continuity-rules.md
```

If the user already has `characters/`, `locations/`, or `props/`, use those directories and avoid duplication. Do not overwrite approved assets without explicit replacement instructions.

## Quality Bar

- Make continuity operational: exact clothing layers, material behavior, object shape, color range, scale, and placement rules.
- For character assets, specify sheet layout, body proportions, wardrobe construction, material behavior, accessories, and prop consistency. Treat fabric seams, folds, weathering, and mechanical details as continuity anchors. For vertical short-video projects, prefer `9:16` character reference cards or sheets unless the project has already approved another ratio.
- Do not regenerate or replace approved image assets just because the story changed. Mark which existing images can remain, and only regenerate visuals whose story beat, ratio, identity, or prop state is now wrong.
- Do not invent official brand assets, logos, or readable typography unless the user provides them.
- Use reference images when available; text-only continuity is weaker.
- If no reference image exists for a recurring visual asset, consider generating one with `image_gen` instead of leaving the asset purely textual.
- Include negative constraints for common AI-video failures: face drift, wardrobe changes, prop morphing, extra fingers, fake text, location geography jumps.
- Keep asset reference-sheet ratios separate from final provider ratio. A reference sheet may use a practical horizontal/vertical layout, but the final Seedance render ratio must still be one of the Seedance menu options.

## Resources

- `references/asset-bible-schema.md`: bible sections, file templates, and continuity rules.
