# Story Forms for Taste-Guided AI Video

Choose a form before writing scenes. The form should fit both the user's goal and the selected taste.

## Short-Form Patterns

### 1. Object Hook, Human Turn

Best for emotional, folk, travel, and memory pieces.

- 0-3s: object appears before context.
- 3-40%: character follows or resists the object.
- 40-75%: object reveals a human relationship or hidden function.
- ending: object remains changed or newly understood.

### 2. Ordinary Setup, Impossible Detail

Best for surreal, anthology, comedy, or AI-native concepts.

- Start with a familiar situation.
- Introduce one impossible detail.
- Escalate through practical consequences.
- End with a clean reversal or visual punchline.

### 3. Before/After Transformation

Best for products, tools, education, and service demos.

- Problem visible in first seconds.
- Transformation process shown through concrete actions.
- Avoid pure verbal explanation.
- End with proof, not slogan.

### 4. One Walk, Three Discoveries

Best for travel, city, documentary, lifestyle, and creator taste pieces.

- Character moves through a route.
- Each stop reveals a different layer: surface, memory, human detail.
- Ending returns to the initial visual with new meaning.

### 5. Ritual Procedure

Best for craft, food, fashion, beauty, sports, and process videos.

- Step sequence drives story.
- Close-ups and sound carry satisfaction.
- Human stakes appear in pauses, mistakes, or final use.

### 6. 起承转合 / Hook-Build-Turn-Aftertaste

Best for Chinese emotional shorts, city memories, family objects, travel reflections, and social-release stories that need resonance without melodrama.

- 起 / Hook: first 1-4 seconds pose a specific question, line, object, or contradiction.
- 承 / Build: expand routine, place, relationship, or pressure through concrete actions.
- 转 / Turn: reveal a private truth or change the meaning of an earlier image.
- 合 / Aftertaste: end on a quiet visual answer, not a slogan.

Use this form when the project needs comments and shares from recognition. The turn should feel inevitable after the reveal, not like a random twist.

## Concept Aesthetic Gate

Score candidate routes before writing the final scene plan. If any core dimension scores `1-2`, or the total is below `28/40`, rewrite the route instead of polishing it.

| Dimension | What Good Looks Like | 1-2 Failure |
| --- | --- | --- |
| Visual necessity | The idea needs moving images, timing, or a visible transformation. | It could be a poster with no loss. |
| Action mechanism | A repeatable physical, social, procedural, or comic engine drives scenes. | Characters just look around or walk. |
| Contrast / irony | The premise contains a clear mismatch, reversal, or pressure. | It is only an attractive world or mood. |
| First-frame hook | The first 1-4 seconds raise a concrete question. | It opens with generic establishing imagery. |
| Turn / payoff | The middle or ending changes the viewer's understanding. | The ending merely confirms the setup. |
| Comment trigger | The route contains a shared-life detail or private truth viewers can respond to. | Viewers may admire the image but have nothing to say. |
| Taste fit | The reference taste changes shot grammar, rhythm, texture, and sound. | The taste is only named in adjectives. |
| Final-frame memory | The last image is specific enough to describe from memory. | The last image is a generic beauty shot. |
| Renderability | The concept can be split into stable, controllable generated clips. | It depends on fragile text, complex hands, crowds, or many state changes in one shot. |

When a route fails, diagnose the weak dimension and create a new route. Do not rescue a weak premise by adding more style words.

## Output Template

```markdown
# <Project Title>

## Creative Route

- Taste:
- Platform:
- Duration:
- Aspect ratio:
- Provider aspect ratio:
- Audience:
- Story form:
- One-line premise:

## Concept Gate

- Visual necessity:
- Action mechanism:
- Main contrast:
- 3s hook:
- 10s turn:
- Comment trigger:
- Final image:
- Renderability:
- Weakness / rewrite trigger:

## Hook Options

1. <first-frame and first-line idea>
2. <alternative>
3. <alternative>

## Scene Plan

| Scene | Timecode | Purpose | Visual Beat | Action | Sound/Voice | Taste Rule |
| --- | --- | --- | --- | --- | --- | --- |

## Script

Write dialogue, voiceover, or on-screen copy only when useful.

## Audio / Post Plan

- Provider audio policy:
- Voiceover/dialogue timeline:
- Music/ambience continuity:
- Subtitle/text policy:

## Asset Handoff

- Characters:
- Locations:
- Props:
- Continuity anchors:
- Risky render elements:
- Downstream updates needed:
```

## Duration Guidance

- 5-15s: one premise, one visual action, one turn.
- 15-30s: hook, build, turn, final image.
- 30-60s: 4-7 scenes with one clear emotional or informational arc.
- 60-90s: allow a slower setup only if the first frame still creates curiosity.

Keep scenes renderable. If a scene requires many locations, crowd behavior, or precise hands, split it.

## Provider Aspect Ratio Rules

If the project is being planned for Seedance, choose the final provider ratio from the Seedance menu only:

| Creative intent | Seedance ratio |
| --- | --- |
| Ultra-wide `2.33:1`, `2.35:1`, `2.39:1`, or `21:9` | `21:9` |
| Horizontal social / TV frame | `16:9` |
| Classic horizontal | `4:3` |
| Square | `1:1` |
| Portrait classic | `3:4` |
| Vertical short video | `9:16` |

For Seedance plans, write both fields when useful:

- Creative framing: `2.33:1-like ultra-wide`
- Provider aspect ratio: `21:9`

Do not pass arbitrary decimal ratios such as `2.33:1` as the Seedance provider ratio.

## Duration and Scene Rules

- 15-30s: hook, build, turn, final image. Use 3-5 scenes.
- 30-60s: use 4-7 scenes with one clear arc.
- 60-90s: use 6-10 scenes, but keep the first 1-4 seconds hook-readable.
- For scene plans, prefer practical scene durations between 4 and 15 seconds unless creating a micro-beat shotboard.
- Useful duration blocks: 4s, 6s, 9s, 12s, 15s.
- Make timecodes add up exactly when possible; if not, explain the closest practical total.

## Style Consultation

When the user has not locked style, offer 3-5 concrete directions before writing the final plan. Each option should vary the production strategy, not just adjective mood:

- cinematic genre short
- handheld diary or documentary
- editorial montage
- commercial proof or transformation
- object-led emotional story
- surreal AI-native fable

Describe each route through composition, camera behavior, color/light, sound, and why it fits the selected taste.

## Plan Completeness Checklist

- Duration, platform/provider, aspect ratio, provider aspect ratio when constrained, audience, and language are stated.
- Story form or arc is explicit.
- First-frame hook is readable.
- Each scene has purpose, visual beat, action, sound/voice, and taste rule.
- Asset handoff lists characters, locations, props, continuity anchors, risky render elements, and text/logo risks.
