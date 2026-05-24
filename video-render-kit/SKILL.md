---
name: video-render-kit
description: "Convert shotboards and asset bibles into provider-ready AI-video prompt packages for Sora, Runway, Kling, Seedance, Wan, Jimeng, and other image-to-video or text-to-video tools. Use when the user wants render prompts, provider adapters, retry plans, production state tracking, first-frame prompts, motion prompts, negative prompts, or a staged generation package."
---

# Video Render Kit

Use this skill after a shotboard exists. It turns creative direction into provider-specific prompt packages while staying API-neutral by default. It does not require secrets, paid APIs, telemetry, or network calls.

## Workflow

1. Read the chosen shotboard, taste, asset bible, and current production state if present.
2. Before writing, inspect project-local examples when they exist, especially `storyboard/*-jimeng-prompt.md`, `storyboard/scene-*.md`, `audio/audio-continuity-guide.md`, and existing render packages. Match their language, section order, prompt density, audio policy, and per-shot specificity.
   - Also read the previous and next scene shotboards/render packages when they exist. Extract the previous scene's final frame and the next scene's first frame before writing the current prompt.
3. Choose provider mode from `references/provider-adapters.md`; if unknown, create a generic adapter plus the most likely platform requested by the user.
   - Normalize provider aspect ratios before writing prompts. For Seedance, choose only from `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`.
   - If the source plan says `2.33:1`, `2.35:1`, or `2.39:1`, use Seedance `21:9` and note it as the closest provider menu ratio.
4. Create a renderability strategy before writing final prompts. Decide whether the scene is one continuous clip or several micro-clips; keep one main action per generation; move unreliable text/graphics to post; and state the cut type or stitching method for each segment.
   - For Jimeng-style workflows in this project, default to silent video generation: do not ask the provider to generate dialogue, voiceover, music, ambience, sound effects, subtitles, or title text. Put those in post-production notes or `audio/audio-continuity-guide.md`.
5. Separate static visual lock from motion instruction, but do not stop at short labels. Expand each provider package into a directly pasteable full-scene prompt, per-shot or per-segment prompts, negative prompt, and post-production notes.
6. Add scene-boundary continuity. Each scene package should include:
   - `入场连续性 / First-frame continuity`: what must match the previous scene's last frame, including geography, camera axis, character pose, prop state, LED/expression, crowd position, and light.
   - `出场交接 / Last-frame handoff`: the exact final frame state that the next scene should inherit.
   - If the provider supports image-to-video or first-frame upload, instruct the user to use the previous scene's final still as the next scene's first-frame reference whenever possible.
7. For storyboard sheets, explicitly tell the video model not to render the grid as the final video. Treat the board as action order only.
8. Create or update production state using `references/production-state.md`.
9. Add retry strategy: what to keep fixed, what to vary, and what failure each retry addresses.
10. Save provider packages and update state.

## Output Contract

Use project-local paths:

```text
render-packages/
  scene-XX/
    generic.md
    sora.md
    runway.md
    kling.md
    seedance.md
    wan.md
    jimeng.md
    retry-log.md
production-state.json
```

If the existing project uses `storyboard/scene-XX-jimeng-prompt.md`, keep writing Jimeng packages there instead of creating a parallel location.

Only create provider files that are relevant to the task. Never include API keys or private account data.

## Quality Bar

- Prompt packages must be directly usable by a human in the selected video tool.
- Preserve identity, wardrobe, props, location geography, lighting direction, and aspect ratio.
- Include duration, aspect ratio, reference image usage, motion, sound/post notes, and negative constraints.
- Warn when the requested scene is too long or too complex for a single generation and recommend segmentation.
- Default to one main visible action per generation. If a beat has multiple actions, fragile hands/tools, crowd behavior, prop transformation, text, or a scene boundary, split it into 2-4 second micro-clips with explicit start and end states.
- Do not ask the video model to generate exact readable text, title cards, tickets, labels, logos, subtitles, or UI copy by default. Use clean blank surfaces in the render and add exact text in post unless exact text is intentionally non-critical.
- Do not let provider prompts fragment audio continuity. If a project has multiple generated scenes, write one unified audio/post plan and keep scene prompts visual-only unless the user explicitly wants provider-generated sound.
- Each per-shot or per-segment prompt must include cut type, transition method, first-frame state, last-frame handoff, and whether the next segment should use the accepted output still as a reference.
- Use the project's working language. If the brief and examples are Chinese, write the provider package in Chinese unless the user asks otherwise.
- A prompt package is not acceptable if it is only a compact summary, a motion-hierarchy checklist, or a few generic labels. It must spell out scene geography, character identity, exact actions, camera rhythm, emotional beat, prop continuity, and what should be added in post.
- Per-shot prompts must be generation-ready. Each shot or segment needs framing, subject action, camera behavior, environment/light, continuity anchors, and the specific thing that must not drift.
- Do not rely on "use the references" as a substitute for description. Restate the visible identity, costume/materials, location landmarks, and hero props from the asset bible.
- Provider-specific packages should follow the strongest local precedent. For Jimeng in this repo, that means the `使用建议` / `整段视频 Prompt` / `逐镜头分镜 Prompt` / `负向 Prompt` / `后期声音或旁白` structure.
- If a previous generated package feels thinner than the local examples, rewrite it to the local example standard instead of preserving the old structure.
- Seedance prompt packages must not ask for arbitrary decimal ratios. Use the platform menu ratio and, if needed, describe the visual intent separately, for example: `Seedance ratio: 21:9; creative framing: 2.33:1-like ultra-wide`.
- Scene cuts must not jump unless the story explicitly calls for a hard discontinuity. For continuous shorts, every render package needs a boundary handoff: the next scene's first shot should either reuse the previous scene's final still or restate the same frame state before moving into the new action.

## Resources

- `references/provider-adapters.md`: provider-specific prompt structure.
- `references/production-state.md`: state gates and retry tracking.
