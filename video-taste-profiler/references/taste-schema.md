# Taste Schema

Every taste lives in:

```text
taste/<taste-slug>/
  manifest.json
  taste.md
  source-log.md
  prompt-vocabulary.md
```

Use lowercase hyphenated slugs. Do not use a creator's legal name as the slug unless the user explicitly wants that and it is appropriate. Prefer craft-based names such as `warm-rainy-urban-memory`, `deadpan-tabletop-comedy`, or `handdrawn-depth-folk-fantasy`.

## manifest.json

Required fields:

```json
{
  "version": 1,
  "slug": "taste-slug",
  "title": "Taste Display Name",
  "source_type": "creator|account|single-video|local-video|mixed|original",
  "source_refs": [],
  "created_at": "ISO-8601 timestamp",
  "updated_at": "ISO-8601 timestamp",
  "aspect_ratios": ["9:16"],
  "duration_range_sec": {"min": 5, "max": 90},
  "confidence": "low|medium|high",
  "style_vectors": {
    "narrative": [],
    "camera": [],
    "editing": [],
    "color_light": [],
    "sound": [],
    "performance": [],
    "platform": []
  },
  "legal_notes": {
    "public_sources_only": true,
    "no_identity_clone": true,
    "no_shot_for_shot_copy": true
  },
  "usage_constraints": []
}
```

## taste.md

Recommended structure:

```markdown
# <Taste Title>

## Essence

One paragraph describing the portable creative grammar.

## Best For

- <format or use case>

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
```

## prompt-vocabulary.md

Use this file to make the taste reusable by other skills:

```markdown
# Prompt Vocabulary: <Taste Title>

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

<static look, material, light, composition>

### Motion Lock

<camera path, subject action, environmental motion>

### Continuity Lock

<identity, wardrobe, props, location geography>
```
