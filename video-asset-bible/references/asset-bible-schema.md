# Asset Bible Schema

Use an asset bible to keep AI-video generations consistent across scenes and providers.

## project-bible.md

```markdown
# <Project Title> Asset Bible

## Source Inputs

- Taste:
- Story plan:
- Aspect ratio:
- Provider aspect ratio:
- Output language:
- Existing project asset conventions:
- Approved image assets to preserve:
- Assets that need regeneration:

## World Rules

- Time and place:
- Reality level:
- Weather and light:
- Color anchors:
- Text/logos policy:

## Core Assets

| Asset | Type | Stable Rules | Allowed Variation | Reference Files |
| --- | --- | --- | --- | --- |

## Generated Reference Images

- Use `image_gen` when a recurring character, location, hero prop, vehicle, or unusual object needs a visual reference to prevent drift.
- Prefer generating reference sheets for core characters and vehicles; prefer single establishing images for important locations.
- Do not generate unnecessary images for one-off background details.
- Store or reference generated images next to the asset spec when possible, such as `characters/<slug>.png`, `locations/<slug>.png`, or `props/<slug>.png`.
- Generated images must obey the same text/logo/privacy constraints as the written asset bible.
- Inherit the project/video ratio for visual reference cards when practical. For a `9:16` short-video project, character, location, prop, and poster-like reference assets should not silently fall back to horizontal layouts.
- If the user wants existing images preserved, keep them as approved references and mark only the mismatched story beats, ratios, or missing assets for regeneration.

## Continuity Risks

- Faces:
- Hands:
- Wardrobe:
- Props:
- Location geography:
- Generated text:
```

## Character Spec

```markdown
# <Character Display Name>

## Role

- Story function:
- Emotional temperature:
- Relationship to other assets:

## Identity Lock

- Age range:
- Face and hair:
- Body and posture:
- Skin/texture:
- Distinguishing details:

## Wardrobe Lock

- Top:
- Bottom:
- Shoes:
- Accessories:
- Materials:
- Color range:
- Construction details:
- Weathering/wear:
- Fit and drape:

## Behavior Lock

- Gesture scale:
- Movement rhythm:
- Eye behavior:
- Performance constraints:

## Reference Image Prompt

Create a clean reference sheet for <character>. Preserve identity across all views...

For 9:16 vertical projects, prefer one vertical reference card: upper full-body front view, middle side/back views, lower detail close-ups for face/head, hands, wardrobe, prop, and material behavior. For horizontal projects, including Seedance `21:9` or `16:9` final renders, prefer a two-row turnaround: row 1 full-body left/front/back/right, row 2 face or detail close-ups. Use plain studio gray unless the asset requires environment context.

If the final provider is Seedance, record the provider ratio from its menu (`21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`). A `2.33:1` creative target maps to Seedance `21:9`; do not record `2.33:1` as the Seedance provider ratio.

## Generated Reference Image

- Path:
- Purpose:
- Reuse notes:
- Ratio:
- Replacement rule:

## Negative Constraints

- No face drift
- No wardrobe change
- No extra logos
- No text labels
- No grid lines unless explicitly requested
- No prop changes between views
- No material changes between views
```

## Location Spec

```markdown
# <Location Name>

## Spatial Layout

- Entrances/exits:
- Foreground:
- Midground:
- Background:
- Light direction:
- Repeating objects:

## Surface and Material Rules

- Walls/floor:
- Practical lights:
- Weather/time:
- Color anchors:

## Continuity Rules

- What must stay fixed:
- What can vary by scene:
- Render risks:

## Reference Image Prompt

Create a clean location reference image for <location>. Preserve spatial layout, fixed landmarks, material palette, and light direction...

## Generated Reference Image

- Path:
- Purpose:
- Reuse notes:
```

## Prop Spec

```markdown
# <Prop Name>

## Form Lock

- Shape:
- Scale:
- Color:
- Material:
- Wear/age:
- Moving parts:

## Use Rules

- Who handles it:
- How it appears:
- Scene dependencies:
- Text/logo policy:

## Reference Image Prompt

Create a clean prop reference image for <prop>. Preserve shape, scale, material, wear pattern, and any moving parts...

## Generated Reference Image

- Path:
- Purpose:
- Reuse notes:
```

## Handoff Notes

For shotboarding, every repeated asset should have a one-line continuity lock:

```text
Continuity lock: same <asset>, same shape/color/material, same relationship to <character/location>, no text/logo changes, allowed changes only in pose/camera/light.
```

Also list:

- Existing image assets that remain valid.
- Existing image assets that must be updated.
- Audio/post-production notes that affect visual continuity, such as visible dialogue moments, silent-video generation, subtitles, or sound-motivated pauses.
