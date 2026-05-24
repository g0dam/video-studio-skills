---
name: video-shotboard-director
description: "Create timed AI-video shotboards, scene boards, frame prompts, camera-direction sheets, and motion-aware per-shot scripts from a story plan, taste profile, and asset bible. Use when the user asks for storyboard panels, shot lists, scene prompts, image-to-video prompts, keyframes, camera movement, timing labels, or shot-by-shot generation packages."
---

# Video Shotboard Director

Use this skill to translate a taste-aware story into timed visual beats. A shotboard is not only a storyboard image: it is a timing, motion, continuity, sound, and render-control document for AI-video generation.

## Workflow

1. Read the story plan, taste profile, and asset bible.
2. Inspect project-local storyboard examples when they exist, especially `storyboard/scene-*.md`, `storyboard/scene-*.png`, `storyboard/scene-*-jimeng-prompt.md`, and provider prompt files. Match their language, panel rhythm, path convention, description density, and sound/edit note style.
3. Choose the scene or sequence to board. If unspecified, start with the hook scene or the user's requested scene.
   - For Scene 02 and later, read the previous scene's final beat. The first beat of the current scene must either match that final frame, explain a deliberate match cut/reverse angle, or add a short bridge beat before the new action.
   - For every scene except the final one, write a last-frame handoff so the next scene knows what to inherit.
4. Pick a timing density from `references/shotboard-system.md`.
5. Assign director cut grammar for every beat transition using `references/shotboard-system.md`: continuous action, cut-on-action, reverse angle, insert, reaction, match cut, time ellipsis, montage, or establishing reset. State the cut motivation, viewer attention, spatial anchor, time relation, and screen direction.
6. Draft per-shot beats with timecode, shot size, subject action, camera motion, foreground/midground/background, continuity anchors, audio cue, director cut note, and render risk.
7. Expand the beats into readable storyboard descriptions, not just a table. Each panel should feel like a tiny director note: what the audience sees, what changes, how the camera behaves, what is heard, why the cut is there, and what must remain consistent.
8. If a story/script revision changes a scene's hook, action, reveal, or final state, update both the text board and the corresponding storyboard image prompt; do not leave an old board image attached to a new script.
9. Write a board image prompt only after the beat list is coherent.
10. When generating board images or keyframes, use available character/location reference images and preserve identity. If an important character, location, or hero prop has no reference image and visual continuity would benefit, directly use the `image_gen` tool to create a board image or keyframe reference.
11. When the user asks for a shotboard/storyboard/scene board, create the corresponding board image with the `image_gen` tool unless they explicitly request text-only output. Reference approved asset images by path in the prompt and restate the identity, location, prop, palette, and negative constraints needed to keep the generated board consistent.
12. If generating a storyboard sheet, choose a grid from scene duration, include per-panel timing labels, and keep every panel in the final video aspect ratio.
   - If the downstream provider is Seedance, the provider ratio must be one of `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`. Map `2.33:1` ultra-wide storyboards to Seedance `21:9` for render handoff.
13. After image generation, check the output dimensions, panel count, grid structure, and visible panel geometry. If the board becomes long horizontal strips, uses too few panels, or ignores the target panel aspect, regenerate before saving the final board.
14. If no image generation is requested and the scene is clear from text, still produce the motion-ready text board.
15. Save board files using the project's convention and hand off to `video-render-kit`.

## Output Contract

Use project-local paths:

```text
shotboards/scene-XX.md
shotboards/scene-XX.png            # optional generated board image
shotboards/scene-XX-keyframes/     # optional generated keyframes
```

If the existing project uses the `.agents/skills/video-storyboard` convention, use `storyboard/scene-XX.md` and `storyboard/scene-XX.png` instead. Do not split one project across `storyboard/` and `shotboards/` unless the user explicitly asks for both.

Use two-digit scene numbers. Do not overwrite existing locked boards; create `scene-XX-v2.*` for alternatives unless the user asked for replacement.

## Quality Bar

- Every shot must advance story, mood, or information.
- Every cut must have a director reason. A shotboard with no cut type, cut motivation, viewer attention, spatial anchor, and time relation is incomplete.
- Not every scene boundary must be seamless, but every discontinuity must be declared and motivated as a time jump, space jump, match cut, insert, reaction, or montage.
- Camera direction must describe motion, not only composition.
- The taste should appear in blocking, lens feel, cut rhythm, color, sound, and text behavior.
- If local storyboard examples exist, match their level of detail. A shotboard is too thin if a later render prompt cannot recover the exact action, camera, geography, sound cue, and story turn from each panel.
- For each panel, write the visible event in concrete cinematic language: framing, actor/object action, emotional or comic beat, camera movement, foreground/midground/background, sound, and transition intention.
- Do not collapse a scene into generic labels like "establishing", "reaction", or "reveal". Name what is being established, what changes in the reaction, and what exact information is revealed or withheld.
- Scene boundaries are continuity-critical. The last panel of Scene N and the first panel of Scene N+1 should share enough visual anchors that separately generated clips can cut together: location geography, camera side, character pose, key prop state, light direction, and revealed/hidden story information.
- When reference images exist, use them for generated boards/keyframes; do not rely on text alone for recurring characters, wardrobe, props, or important locations.
- Storyboard images must be generated through `image_gen`, not by hand-drawn placeholders or text-only tables, whenever the user requests visual boards or when reference images are needed to prevent drift.
- Storyboard images must respect the grid in `references/shotboard-system.md`: for a 3-5 second scene, use a 3x3 sheet and fill the grid with micro-beats whenever possible instead of stretching a few visible panels.
- For vertical short-video projects, both the storyboard sheet and each panel should read as `9:16` vertical composition. Do not generate horizontal character sheets, landscape storyboard strips, or wide poster-like panels unless the project ratio actually calls for them.
- Keep AI renderability in mind: avoid impossible crowd continuity, tiny unreadable text, overly complex hand actions, and uncontrolled logos.
- Use `image_gen` for high-value visual references when a generated image will prevent drift in character identity, location geography, or hero prop shape. Do not generate unnecessary images for simple text-only boards.
- Keep provider-ratio handoff realistic. For Seedance, never hand off arbitrary decimal ratios; write the menu ratio such as `21:9` and optionally note the creative framing as `2.33:1-like ultra-wide`.

## Resources

- `references/shotboard-system.md`: timing grid, shot grammar, and output templates.
