---
name: video-shotboard-director
description: "Create timed AI-video shotboards, scene boards, frame prompts, camera-direction sheets, and motion-aware per-shot scripts from a story plan, taste profile, and asset bible. Use when the user asks for storyboard panels, shot lists, scene prompts, image-to-video prompts, keyframes, camera movement, timing labels, or shot-by-shot generation packages. Enforces master visual locks, panel state handoffs, and audio/music continuity so generated boards do not become disconnected images."
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
5. Build a master visual lock before writing beats: canonical character identity, hero prop state, location geography, camera axis/lens feel, light direction, color/material rendering, and audio identity. If a recurring character, location, or hero prop lacks a visual reference and continuity matters, create or request a keyframe/asset reference before generating a multi-panel board unless the user explicitly asks for text-only speed.
6. Draft a panel state table from `references/shotboard-system.md`: each row must inherit the previous row's end state, describe only the delta action, and name camera/focus and audio/music state.
7. For an emotion-driven close-up, trial testimony, confession, reveal, grief beat, intimidation beat, or any scene where the performance is the action, draft a precision performance arc from `references/shotboard-system.md` before writing the beat table. Track the change in voluntary control, breathing, gaze, facial/hand tension, tears or moisture, and light.
8. Assign director cut grammar for every beat transition using `references/shotboard-system.md`: continuous action, cut-on-action, reverse angle, insert, reaction, match cut, time ellipsis, montage, or establishing reset. State the cut motivation, viewer attention, spatial anchor, time relation, and screen direction.
9. Define an audio/music continuity track: one music cue or silence strategy, ambience bed, foley palette, sound bridge points, and visible actions that trigger sound. Do not let each panel invent unrelated music.
10. Draft per-shot beats with timecode, shot size, subject action, camera motion, foreground/midground/background, continuity anchors, audio cue, director cut note, and render risk.
11. Expand the beats into readable storyboard descriptions, not just a table. Each panel should feel like a tiny director note: what the audience sees, what changes from the previous panel, how the camera behaves, what is heard, why the cut is there, and what must remain consistent.
12. If a story/script revision changes a scene's hook, action, reveal, or final state, update both the text board and the corresponding storyboard image prompt; do not leave an old board image attached to a new script.
13. Write a board image prompt only after the beat list, master visual lock, panel state table, and audio track are coherent.
14. When generating board images or keyframes, use available character/location reference images and preserve identity. If an important character, location, or hero prop has no reference image and visual continuity would benefit, directly use the `image_gen` tool to create a board image or keyframe reference.
15. When the user asks for a shotboard/storyboard/scene board, create the corresponding board image with the `image_gen` tool unless they explicitly request text-only output. Reference approved asset images by path in the prompt and restate the identity, location, prop, palette, audio identity, and negative constraints needed to keep the generated board consistent.
16. If generating a storyboard sheet, choose a grid from scene duration, include per-panel timing labels, and keep every panel in the final video aspect ratio.
   - If the downstream provider is Seedance, the provider ratio must be one of `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`. Map `2.33:1` ultra-wide storyboards to Seedance `21:9` for render handoff.
17. After image generation, check the output dimensions, panel count, grid structure, visible panel geometry, character identity, prop state chain, location continuity, light direction, and whether panels look like a causal sequence rather than independent posters. If continuity breaks, regenerate before saving the final board.
18. If no image generation is requested and the scene is clear from text, still produce the motion-ready text board.
19. Save board files using the project's convention and hand off to `video-render-kit`.

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
- A shotboard must include a master visual lock, panel state table, and audio/music continuity track for any multi-panel scene.
- Each beat should describe the delta from the previous beat. Re-describing the whole frame with new words in every beat causes identity, prop, lighting, and style drift.
- Every cut must have a director reason. A shotboard with no cut type, cut motivation, viewer attention, spatial anchor, and time relation is incomplete.
- Not every scene boundary must be seamless, but every discontinuity must be declared and motivated as a time jump, space jump, match cut, insert, reaction, or montage.
- Camera direction must describe motion, not only composition.
- The taste should appear in blocking, lens feel, cut rhythm, color, sound, and text behavior.
- If local storyboard examples exist, match their level of detail. A shotboard is too thin if a later render prompt cannot recover the exact action, camera, geography, sound cue, and story turn from each panel.
- For each panel, write the visible event in concrete cinematic language: framing, actor/object action, emotional or comic beat, camera movement, foreground/midground/background, sound, and transition intention.
- For each panel, state what remains unchanged: character identity, hero prop state, location anchors, light direction, camera axis/lens feel, material style, and music/ambience state.
- For emotion-heavy close-ups, never stop at labels like "breaks down", "looks devastated", "becomes determined", or "cries". Convert the emotion into observable physiology: brow/eyelid tension, gaze lock or drift, jaw/lip/neck behavior, breathing rhythm, hand pressure, shoulder posture, tears, skin flush, and blink state.
- Use quantitative micro-detail when it clarifies timing or motion: millimeters of movement, seconds of delay, degrees of chin tilt or camera drift, tremor frequency, breath cycle length, or percentage-like intensity. Do not overload every shot with anatomy; use it where the performance itself carries the scene.
- Tie camera, focus, lens, and light to the performance arc. Push-ins, rack focus, handheld shake, Dutch angle, rim light, or overhead light should mark a visible control-state change, not decorate the shot.
- Preserve the control transition. If a character moves from suppression to spasm, dissociation, concealment, and deliberate resolve, each state needs a visible body cue and a timed handoff to the next state.
- Do not collapse a scene into generic labels like "establishing", "reaction", or "reveal". Name what is being established, what changes in the reaction, and what exact information is revealed or withheld.
- Scene boundaries are continuity-critical. The last panel of Scene N and the first panel of Scene N+1 should share enough visual anchors that separately generated clips can cut together: location geography, camera side, character pose, key prop state, light direction, and revealed/hidden story information.
- Audio boundaries are continuity-critical. The last audio state of Scene N and first audio state of Scene N+1 should either continue the same cue/ambience bed or declare a motivated stop, hit, silence, or new cue.
- When reference images exist, use them for generated boards/keyframes; do not rely on text alone for recurring characters, wardrobe, props, or important locations.
- Storyboard images must be generated through `image_gen`, not by hand-drawn placeholders or text-only tables, whenever the user requests visual boards or when reference images are needed to prevent drift.
- Storyboard images must respect the grid in `references/shotboard-system.md`: for a 3-5 second scene, use a 3x3 sheet and fill the grid with micro-beats whenever possible instead of stretching a few visible panels.
- For vertical short-video projects, both the storyboard sheet and each panel should read as `9:16` vertical composition. Do not generate horizontal character sheets, landscape storyboard strips, or wide poster-like panels unless the project ratio actually calls for them.
- Keep AI renderability in mind: avoid impossible crowd continuity, tiny unreadable text, overly complex hand actions, and uncontrolled logos.
- Use `image_gen` for high-value visual references when a generated image will prevent drift in character identity, location geography, or hero prop shape. Do not generate unnecessary images for simple text-only boards.
- Keep provider-ratio handoff realistic. For Seedance, never hand off arbitrary decimal ratios; write the menu ratio such as `21:9` and optionally note the creative framing as `2.33:1-like ultra-wide`.

## Resources

- `references/shotboard-system.md`: timing grid, shot grammar, and output templates.
