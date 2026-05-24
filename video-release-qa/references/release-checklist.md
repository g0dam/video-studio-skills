# Release QA Checklist

Use this checklist for final review and packaging.

## Blocking Review

1. **Story clarity**
   - The first frame creates a reason to keep watching.
   - The viewer can understand the core turn or payoff.
   - The ending image matches the promised emotion or idea.
   - The premise has visual necessity: motion, timing, procedure, or reversal makes it worth being a video.
   - The final image is specific, not a generic beauty shot.

2. **Taste fit**
   - The piece uses the selected taste through shot grammar, pacing, color, sound, and performance.
   - It does not merely name the taste in text.
   - It remains original and avoids creator impersonation.

3. **Continuity**
   - Same face, wardrobe, props, location geography, light direction, and object scale where required.
   - No unexplained costume or hairstyle jumps.
   - Repeated objects keep shape and color.

4. **Director / edit integrity**
   - Every cut has a visible motivation: continuous action, cut-on-action, reverse angle, insert, reaction, match cut, time ellipsis, montage, or establishing reset.
   - Scene boundaries do not accidentally reset subject position, prop state, scale, light, or story information.
   - If time or space jumps, the first frame after the cut re-establishes geography and state.
   - Inserts and reaction cuts have a clear cause/effect relationship.
   - Montage shots accumulate change instead of becoming unrelated pretty images.
   - The story turn is visible on screen, not only implied by the written prompt.

5. **AI artifacts**
   - Hands, teeth, eyes, reflections, text, logos, and crowd edges are acceptable.
   - Motion does not melt, stutter, or break object permanence.
   - The model did not render a storyboard grid as the final video.

6. **Platform fit**
   - Correct aspect ratio and duration.
   - Generated stills, character sheets, storyboard pages, posters/covers, and provider prompts inherit the project ratio unless a deliberate exception is documented.
   - A `9:16` short-video project does not contain accidental horizontal storyboard images, wide character reference cards, or `3:4` cover art unless explicitly approved.
   - If the provider is Seedance, the aspect ratio is one of the menu options: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`.
   - For Seedance, `2.33:1` / `2.35:1` / `2.39:1` ultra-wide intent should be delivered as `21:9`, not as a decimal ratio.
   - Cover frame is legible on mobile.
   - Captions/subtitles are optional or readable.
   - Audio strategy matches sound-on or sound-off use.

7. **Storyboard and prompt sync**
   - If the script changed, matching storyboard text, storyboard image prompt, generated storyboard image, and provider prompt were updated.
   - Storyboard sheets are clearly marked as reference only and provider prompts say not to generate a grid.
   - Existing approved images are either preserved intentionally or listed as needing regeneration.

8. **Audio continuity**
   - For silent-provider workflows such as Jimeng scene generation, prompts explicitly say not to generate dialogue, voiceover, music, ambience, sound effects, subtitles, or title cards.
   - Multi-scene projects have one unified audio/post-production plan rather than separate per-scene voice or ambience inventions.
   - Voiceover and dialogue timelines fit the total duration and do not duplicate the ending beat.

## QA Report Template

```markdown
# QA Report: <Project Title>

## Verdict

- Status: ready / revise / blocked
- Biggest risk:

## Blocking Issues

| Priority | File/Scene | Issue | Failure Route | Fix |
| --- | --- | --- | --- | --- |

## Polish Notes

- <note>

## Release Package

- Final video:
- Cover/poster:
- Captions:
- Subtitles:
- Audio:
- Prompt records:
- Source/taste notes:

## Known Risks

- <risk>
```

## Failure Routes

- Weak concept, no visual necessity, no memorable turn -> `video-story-lab`
- Missing cut motivation, unclear geography, bad scene boundary -> `video-shotboard-director`
- Identity, wardrobe, hero prop, or location drift -> `video-asset-bible`
- Wrong aspect ratio, stale storyboard image, or missing generated board -> `video-shotboard-director`
- Overloaded prompt, generated text failure, provider-generated audio drift, bad micro-clip stitching -> `video-render-kit`
- Poster/cover mismatch or weak title packaging -> `video-poster-design` or cover workflow

## Cover Brief Template

```markdown
# Cover Brief

## Source

- Taste:
- Final video:
- Title language:
- Platform:

## Composition

- Main subject:
- Background:
- Negative space:
- Color anchors:
- Text placement:

## Text

- Title:
- Subtitle:
- Avoid:

## Creative Directions

1. <concept name>: <main image, typography, color, emotion, fit>
2. <concept name>: <main image, typography, color, emotion, fit>
3. <concept name>: <main image, typography, color, emotion, fit>

## Image Generation Prompt

- Aspect ratio:
- Reference assets:
- Composition:
- Main subject:
- Typography direction:
- Color and lighting:
- Negative constraints:
```

## Key Art Rules

- Inherit aspect ratio from the final video or platform; for vertical short-video projects use 9:16 unless the user asks otherwise.
- For Seedance cover/key-art specs, choose from the same ratio menu: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`.
- Use available `characters/*.png`, `shotboards/*.png`, stills, or approved asset references when identity or location continuity matters.
- If exact title typography matters, generate art with intentional empty space and add text deterministically later.
- Avoid fake credits, random extra text, official logos, unreadable generated letters, and generic poster templates.
- Vary creative directions: character-led, environment-led, object-led, action/motion, minimal teaser, or graphic reflection.
