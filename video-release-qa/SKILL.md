---
name: video-release-qa
description: "Review AI-video projects for continuity, render artifacts, release readiness, cover/poster quality, platform fit, title/caption packaging, and final delivery completeness. Use when the user wants QA, launch review, release package, poster or cover guidance, title options, continuity checks, artifact checks, or a final production handoff for an AI-generated video."
---

# Video Release QA

Use this skill near the end of a project or after any generated scene. It checks whether the project is coherent, publishable, and ready for iteration or release.

## Workflow

1. Inspect available plan, taste, asset bible, shotboards, render packages, generated videos/stills, poster/cover drafts, captions, and production state.
2. Inspect project conventions and durable outputs: `plans/`, `characters/`, `storyboard/`, `shotboards/`, `render-packages/`, `audio/`, `posters/`, and `.agents/skills/`-style outputs. Check that later files did not fork into a different directory or aspect-ratio convention.
3. If generated video or stills are available, inspect contact sheets and boundary frames when practical: first frame, last frame, scene joins, prop-state changes, face/identity changes, and any generated text.
4. Use `references/release-checklist.md` to run a structured review.
5. Separate blocking issues from polish. Start with continuity, director/edit integrity, aspect-ratio mismatches, stale storyboard images, artifacts, missing files, platform mismatch, text/logo risk, weak concept, unclear story, and audio-policy drift.
   - For Seedance deliverables, verify the prompt/package uses one of the platform menu ratios only: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`.
   - Treat Seedance prompts that specify arbitrary decimal ratios like `2.33:1` as a platform mismatch. The correct Seedance menu selection for `2.33:1` ultra-wide is `21:9`.
6. Route failures to the correct upstream skill:
   - Weak premise, no visual necessity, or no memorable turn -> revise with `video-story-lab`.
   - Unmotivated cuts, bad scene joins, stale storyboard image, unclear geography, or missing viewer attention -> revise with `video-shotboard-director`.
   - Identity/prop/location drift -> revise with `video-asset-bible` and reference images.
   - Overloaded prompts, generated text, provider-generated audio drift, action resets, or bad clip stitching -> revise with `video-render-kit`.
7. If a cover or poster is needed, create 3-5 distinct key-art directions unless the direction is already locked. Inherit taste, character anchors, title language, platform ratio, and approved reference images.
8. When requested, use `image_gen` to generate cover/poster art, or write a prompt/spec if exact typography should be added later with deterministic tools.
9. Update or recommend updates to `production-state.json`.
10. End with a release package checklist: final videos, thumbnails, captions, subtitles, audio, prompt records, source notes, and known risks.

## Output Contract

Use project-local paths:

```text
release/
  qa-report.md
  cover-brief.md
  cover-prompt.md
  cover.png
  title-caption-options.md
  final-checklist.md
```

If the user only asks for review, respond with findings first and write files only when a durable release package is requested.

## Quality Bar

- Lead with actionable findings, not praise.
- Mention exact scene/file references when possible.
- Do not hide uncertainty: mark what could not be inspected.
- Treat generated text, brand marks, faces, hands, and continuity jumps as high-risk surfaces.
- Do not mark a video ready just because the images are individually attractive. The sequence must have motivated cuts, stable visual anchors, a clear story turn, and a final frame that pays off the premise.
- If a scene boundary jumps, identify whether it is a deliberate time/space cut, match cut, insert, reaction, or montage. If it is none of these, treat it as a blocking edit issue.
- For vertical short-video projects, generated character sheets, storyboard images, posters/covers, and provider prompts must all inherit the project ratio unless a file states a deliberate exception. A horizontal image attached to a `9:16` project is a blocking mismatch.
- For Jimeng-style workflows, provider prompts should be silent visual generation unless the user explicitly chose provider-generated sound. Dialogue, voiceover, ambience, music, sound effects, subtitles, and title cards should be unified in post.
- Cover/poster work should not look like a generic template. Composition, typography direction, color, and title treatment must match the story world.

## Resources

- `references/release-checklist.md`: QA dimensions and release package template.
