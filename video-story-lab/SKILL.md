---
name: video-story-lab
description: "Generate original AI-video concepts, scripts, scene plans, narration, dialogue, and platform-native story structures from a taste profile, brief, trend, product, location, or theme. Use when the user wants ideas, short-video scripts, narrative arcs, 15-90 second plans, TikTok/Reels/Shorts concepts, campaign stories, or taste-guided creative directions."
---

# Video Story Lab

Use this skill after a taste exists, or when the user gives a creative brief that should be planned in a taste-aware way. The goal is an original story system that can feed asset design, shotboarding, render prompts, and release QA.

## Workflow

1. Read the chosen `taste/<slug>/taste.md` and `prompt-vocabulary.md` when available.
2. Extract the user's objective: platform/provider, duration, aspect ratio, audience, tone, product/character/location constraints, language, and whether the output is for AI generation or live shooting.
   - If the target provider is Seedance, normalize the deliverable aspect ratio to one of the Seedance menu options: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`.
   - Map ultra-wide `2.33:1`, `2.35:1`, or `2.39:1` creative requests to Seedance `21:9`. Record the creative intent as "2.33:1-like ultra-wide", but use `21:9` as the provider ratio.
   - Do not invent arbitrary Seedance ratios such as `2.33:1` in downstream handoff fields.
3. If duration is missing, offer practical defaults: 30s high-density social cut, 45s compact narrative, 60s standard arc, 90s reflective pacing. If the user wants speed, infer a default and state it.
4. Inspect existing project conventions before planning: `plans/`, `characters/`, `storyboard/`, `shotboards/`, `render-packages/`, `audio/`, and any `.agents/skills/` video outputs. Continue the project's path, ratio, file naming, and language instead of starting a parallel structure.
5. Choose a story form from `references/story-forms.md`; do not default to a vague montage. For Chinese emotional or social shorts, consider `起承转合` or hook-build-turn-payoff before scene writing.
6. Run the concept/aesthetic gate from `references/story-forms.md` before committing to a route. A route must state visual necessity, action mechanism, contrast/irony, first-frame hook, turn/payoff, final image, renderability, and taste fit.
7. When the direction is not locked, produce 3-5 concrete style/concept routes. Each route must include hook, turn, payoff, visual engine, and why it fits the taste. Reject or rewrite routes that are only "setting + cute object", mood boards, or reference-name mimicry.
8. Once a route is selected or obvious, write a scene plan with exact time ranges and scene purposes. Keep scene durations practical for generation or shooting; prefer 4-15 seconds per scene for short-form work, and make the timecodes add up exactly when the final duration is known.
9. Include narration/dialogue only when it improves the piece. Keep lines speakable within the stated duration. For AI-video providers with unreliable sound or subtitles, mark voiceover, dialogue, music, ambience, and subtitles as post-production by default.
10. Flag dependencies for the next skills: required characters, recurring places, props, visual continuity anchors, risky generated text, audio/post-production needs, and render-sensitive motion.

## Output Contract

Save story outputs under the user's project folder, normally:

```text
plans/<project-slug>-concepts.md
plans/<project-slug>-script.md
plans/<project-slug>-scene-plan.md
```

If the project already has a naming convention, follow it. Do not overwrite a locked plan unless the user requests replacement; use a revision suffix.

## Quality Bar

- Every concept must be shootable or generatable, not just a mood.
- Every concept must need video. If the idea works just as a still poster, rewrite it until motion, timing, procedure, or a visible reversal carries the premise.
- A concept is incomplete when it is only a setting plus an appealing character or object. It needs a practical action mechanism, a legible contradiction, and a final image the viewer can remember.
- For social release, identify the comment trigger: the private truth, reversal, awkward recognition, or shared-life detail that makes viewers want to reply. Pretty atmosphere alone is not enough.
- The first 1-4 seconds must have a clear attention mechanism for short-form work.
- If an existing story/script changes materially, call out downstream assets that must be updated: storyboard text, storyboard image, provider prompts, audio plan, captions, and release copy.
- The output language should match the user's language unless they ask otherwise.
- The taste should shape decisions visibly: rhythm, shot grammar, visual motifs, sound, and text behavior.
- The plan must remain original and not recreate the analyzed creator's exact video, persona, catchphrases, or branded identity.
- List the handoff package for `video-asset-bible` and `video-shotboard-director`.
- When provider constraints are known, list both the creative framing intent and provider menu ratio. For Seedance, the provider ratio must be one of `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`.

## Resources

- `references/story-forms.md`: story forms, time structures, and output templates.
