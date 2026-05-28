# Shotboard System

A shotboard is a timed instruction set for visual continuity and motion. It can include a board image, but the text plan is the source of truth.

## Timing Density

Choose panel count by scene duration and complexity:

| Duration | Default Beats | Use When |
| ---: | ---: | --- |
| 3-5s | 3-6 | one action or hook |
| 6-9s | 6-9 | short scene with simple motion |
| 10-12s | 8-12 | reveal, process, or emotional pause |
| 13-20s | 10-16 | complex scene; consider splitting |

For provider render prompts, prefer fewer coherent beats over a crowded board.

## Director Cut Grammar

Choose a cut type before describing the next shot. The cut type is the reason the viewer accepts a visual change.

| Cut Type | Use When | Required Anchor | Common Failure |
| --- | --- | --- | --- |
| Continuous action | One action continues across adjacent beats. | Same subject, prop state, screen direction, and time flow. | Subject or prop resets between shots. |
| Cut-on-action | The cut hides a movement change by cutting during the action. | Matching motion vector and matching prop/body state. | The action restarts or finishes twice. |
| Reverse angle | The camera crosses to the opposite view for reaction or spatial information. | Same axis logic, same positions, same light direction. | It looks like a new location. |
| Insert | A detail shot reveals evidence, a prop, or a tactile action. | Clear relation to the previous wide/medium shot. | The object appears from nowhere or changes design. |
| Reaction cut | A face/body/object reaction completes the meaning of the previous action. | The viewer understands what the subject is reacting to. | Reaction has no cause or wrong emotional temperature. |
| Match cut | Shape, color, motion, or composition connects two different images. | The matching element must be visually obvious in both shots. | The cut feels accidental because the match is weak. |
| Time ellipsis | Skip unimportant time while preserving the action result. | Start/end states make the skipped time legible. | The viewer reads it as continuity error. |
| Montage | Compress repeated actions, process, or escalation. | Repeated framing rule, object motif, rhythm, or sound motif. | Random pretty images with no cumulative change. |
| Establishing reset | Intentionally change time or space. | New geography is clear in the first frame. | A new establishing shot interrupts a continuous scene. |

Every beat transition should specify:

- Cut type
- Cut motivation
- Viewer attention: where the viewer's eye should land at the cut
- Spatial anchor: what proves where we are
- Time relation: continuous, compressed, skipped, simultaneous, or new time
- Screen direction: subject/camera movement direction that should remain stable or intentionally change

Hard discontinuity is allowed only when the story intentionally changes time or space. The first frame after that cut must re-establish geography and state before continuing the action.

## Storyboard Sheet Grid

Use this only when generating a board image, not for every text shotboard:

| Scene Duration | Grid | Panel Count |
| ---: | --- | ---: |
| `<= 9s` | `3 rows x 3 columns` | 9 |
| `> 9s` and `<= 12s` | `4 rows x 3 columns` | 12 |
| `> 12s` | `4 rows x 4 columns` | 16 |

- If the project already has storyboard examples, match their page structure, label style, and panel rhythm unless the user asks for a different format.
- Every panel should be composed for the final video aspect ratio; for `9:16` projects, panels are vertical, and for horizontal projects, panels are horizontal.
- For a `9:16` project, the full storyboard sheet should also read as a vertical board. Do not create a wide horizontal canvas filled with vertical thumbnails unless the local examples already require that layout.
- A visual storyboard sheet may use a practical page/cell ratio for readability. Enforce exact output aspect ratio in the render prompt, keyframe crop, or per-shot frame instead of stretching storyboard cells into unusable strips.
- If the final provider is Seedance, use only Seedance's menu ratios for provider handoff: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`. Ultra-wide `2.33:1` story intent maps to `21:9`.
- A storyboard sheet is a grid of panels, not a stack of stretched horizontal strips. Do not turn five beats into five full-width bands.
- A storyboard sheet is not final video. Downstream provider prompts must say the sheet is only action order and timing reference, not a grid to reproduce.
- For short scenes, subdivide motion into the grid's panel count when possible. A 3-5 second hook can still use 9 micro-panels to show movement, reaction, and reveal timing.
- Use no gaps between panels. Thin borders are acceptable for readability.
- Each visible panel should include a small top-left panel number and top-right duration or timecode label.
- Empty final panels are a fallback only when the user explicitly wants sparse beats or the action cannot be subdivided cleanly. Default to filling the grid with meaningful panels.
- After generating a board image, verify pixel dimensions, grid count, and visible panel geometry. If the image does not follow the required grid, uses the wrong panel orientation, or collapses into strips, regenerate before finalizing.

## Beat Fields

Each beat should include:

- Timecode
- Shot size and angle
- Subject action
- Camera motion
- Foreground / midground / background
- Continuity lock
- Cut type and cut motivation
- Viewer attention
- Spatial anchor
- Time relation
- Screen direction
- Sound or silence cue
- Render risk
- Boundary role: entry match, bridge beat, normal beat, or exit handoff

Beat fields are a floor, not the finished description. When the local project uses paragraph-style storyboard panels, write each panel as a short cinematic paragraph after or instead of the table so the downstream render prompt can inherit concrete detail.

## Master Visual Lock and State Table

For any multi-panel board, write these sections before the beat descriptions.

### Master Visual Lock

Lock the things that should not drift:

- Character identity: silhouette, face, age/body proportions, wardrobe, material, unique marks, approved reference images.
- Hero props: exact shape, color, scale, location, state, and whether they can deform or move.
- Location geography: fixed left/right map, foreground/midground/background, doors/windows/surfaces/landmarks, entrance and exit paths.
- Camera and optics: axis, height, focal-length feel, depth of field, stabilization/handheld feel, framing range.
- Light/color/material: light source direction, time of day, contrast, palette, texture rendering, surface behavior.
- Audio identity: music cue or silence rule, ambience bed, foley palette, sound bridge strategy.

### Panel State Table

Use this table to prevent unrelated panels:

| Panel | Start State | Delta Action Only | End State / Handoff | Camera / Focus State | Audio / Music State |
| ---: | --- | --- | --- | --- | --- |

Rules:

- `Start State` inherits the previous panel's `End State / Handoff` unless a cut type declares a time jump, space jump, match cut, insert, reverse angle, or establishing reset.
- `Delta Action Only` names only the visible change in this panel. Do not rewrite the character, room, prop, or mood from scratch with new wording.
- `End State / Handoff` is the first-frame requirement for the next panel.
- `Camera / Focus State` says unchanged, push/pull, pan/tilt, insert, reverse angle, focus pull, or return from cut.
- `Audio / Music State` inherits the same cue/ambience/foley bed unless a visible action changes it.

If a storyboard sheet looks like independent pretty images instead of this state chain, it should be regenerated.

## Audio and Music Continuity Track

Sound is part of continuity, not a separate afterthought.

- Define one scene-level music or silence strategy before per-panel cues.
- Keep tempo, instrumentation, mood, volume trend, and reverb/space consistent unless a story event changes them.
- Assign foley to visible actions: cloth contact, footstep, door, breath, object pickup, impact, or environmental movement.
- Use sound bridges intentionally to connect cuts.
- For providers where audio is unreliable, keep generated video silent and put all music, ambience, foley, dialogue, and captions in post. Still write the post audio plan once so every rendered segment is edited against the same cue.
- Do not write a different music style, instrument family, or emotional cue for every panel unless the scene is explicitly a montage with motivated music changes.

Each finished panel description should answer:

- What exact image is on screen?
- What changed from the previous panel?
- Where are the key character, prop, and location anchors?
- What is the camera doing and how fast?
- What sound, silence, voiceover, title card, or edit note belongs here?
- What continuity or reveal must not be lost?
- What start state did this panel inherit, and what exact end state must the next panel inherit?
- What audio/music state continues through the panel?

## Precision Performance Arc

Use this section for close-ups, emotional reversals, interrogations, confessions, court scenes, grief scenes, vengeance turns, or any beat where the face/body performance is the main action. The goal is to make an AI-video prompt preserve controllable visible detail instead of collapsing the scene into "sad", "angry", or "crying".

Build the arc as timed slices. Each slice should include:

- Time range: exact start/end seconds.
- Camera and optics: shot size, lens feel, angle, push/pull speed, focus behavior, handheld or stabilization state.
- Light and environment: key/rim/backlight direction, color temperature shift, bokeh, dust, reflections, or other small environmental motion.
- Control state: suppressed, involuntary tremor, spasm, dissociation, concealment, voluntary control returning, or resolved stillness.
- Face and gaze: brow, eyelids, eye opening, blink state, gaze target, pupil focus/dilation when relevant, jaw, lips, cheek, chin, nostrils.
- Breath and posture: inhale/exhale length, clavicle/shoulder/rib movement, neck tension, chin angle, torso curl or square-up.
- Hands and props: finger curl, grip pressure, tremor, knuckle color, hand-to-face motion, prop contact, timing delay between hands.
- Tears and surface detail: moisture pooling, tear release, track path, wet/dry layering, skin flush, light catching the tear line.
- Quantifiers: use numbers for control where helpful, such as `2mm`, `0.4s delay`, `3Hz tremor`, `5 degree chin drop`, or `1.5s exhale`. Keep them tied to visible outcomes.
- Segment handoff: what exact visible state starts the next slice.

Example structure:

```markdown
## Precision Performance Arc

| Time | Control State | Camera / Light | Visible Performance | Handoff |
| --- | --- | --- | --- | --- |
| 00:00-00:01.3 | Suppressed shock | Close-up, slow push in, cold overhead key | Chin tucked, eyes shut, jaw locked, shoulders frozen mid-exhale | Chin begins rising |
| 00:01.3-00:02.8 | Forced ascent | Same close-up, slight crane up, background dissolves | Eyelids open in small increments, brow furrows, first moisture appears | Eyes reach full open |
| 00:02.8-00:04.2 | Swallowing sob | Tight close-up, headroom narrows | Tear forms but holds, nostrils flare, fingers curl on armrest, throat dips once | Tear releases |
```

Use anatomical labels only when they improve control, and pair them with the visible result. `corrugator supercilii engages, carving a vertical brow furrow` is useful; a list of muscle names without screen-visible change is not.

## Scene Boundary Continuity

For sequential scenes, add an explicit boundary handoff:

- **Entry continuity**: For Scene 02 and later, describe how the first frame inherits the previous scene's final frame. This can be a direct match, a short hold, a reverse angle with the same spatial anchors, or a cut-on-action.
- **Exit handoff**: For every scene except the final one, describe the final frame state the next scene must inherit.
- **Bridge beat**: If the previous final frame and current first action are too different, add a 0.3-0.7 second bridge at the start of the current scene or the end of the previous scene.
- **Reference still**: When rendering clips separately, recommend exporting Scene N's final frame and using it as Scene N+1's first-frame reference if the video tool supports it.

Do not create a new establishing shot at the start of each scene unless the story intentionally jumps time or space.

## Scene Board Template

```markdown
# Scene XX Shotboard

## Source

- Taste:
- Story plan:
- Asset bible:
- Duration:
- Aspect ratio:
- Provider aspect ratio:
- Provider target:

## Scene Purpose

<What must change for the viewer by the end of this scene.>

## Continuity Locks

- Character:
- Wardrobe:
- Props:
- Location:
- Light:
- Camera / optics:
- Color / material:
- Audio / music:

## Scene Boundary

- Entry continuity:
- Exit handoff:

## Master Visual Lock

- Character identity:
- Hero props:
- Location geography:
- Camera and optics:
- Light/color/material:
- Audio identity:

## Panel State Table

| Panel | Start State | Delta Action Only | End State / Handoff | Camera / Focus State | Audio / Music State |
| ---: | --- | --- | --- | --- | --- |

## Beats

| Beat | Timecode | Cut Type | Shot | Action | Camera | Viewer Attention | Continuity | Render Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Audio and Music Continuity Track

- Music/silence strategy:
- Ambience bed:
- Foley palette:
- Sound bridges:
- Entry/exit cue points:

## Director Notes

- Cut motivation:
- Spatial anchor:
- Time relation:
- Screen direction:

## Board Image Prompt

Create a single shotboard sheet...

If the project uses `storyboard/scene-XX.png`, write the prompt in the same style as the local storyboard files and include:

- Final video ratio and full-sheet ratio.
- Grid size and panel timing.
- Character/location/prop reference image paths.
- "Do not generate horizontal panels for a vertical project."
- "Do not add subtitles, speech bubbles, random logos, or readable text unless explicitly required."

## Generated Images

- Board image:
- Keyframes:
- Reference images used:
- Existing image superseded:
- Existing image kept:

## Video Prompt Script

- If a board image is generated, also write a matching motion script with the same panel order, panel timing, continuity paragraph, sound design, edit notes, and negative prompts.
- The script language should match the user's language unless requested otherwise.
- The timing in the script must add up exactly to the scene duration.
- The script must be detailed enough to become a provider prompt without guessing. Avoid generic shot labels; include scene geography, character identity, exact action chain, camera rhythm, sound design, and negative constraints.
- The script must include the master visual lock, panel state table, and audio/music continuity track. Per-panel descriptions should inherit prior state and describe only the next visible change.
- If a precision performance arc exists, carry its time slices into the script. Preserve the visible physiology, timing measurements, camera/focus behavior, light changes, and control-state handoffs.

## Motion Notes

- Subject motion:
- Camera motion:
- Environmental motion:
- Transition out:
```

## Renderability Rules

- Avoid tiny readable text unless exact typography will be added later.
- Keep hands visible only when the action is simple and important.
- For crowds, describe silhouettes, flow, or background movement rather than individual continuity.
- If character identity matters, use approved reference images and restate the identity lock.
- If location geography matters, name fixed landmarks and camera direction.
- Use `image_gen` for board sheets or keyframes when an image will materially reduce ambiguity in character identity, location geography, hero prop shape, or first-frame readability.
- Do not generate images by default for every text-only board; generate selectively for scenes that need visual locking.

## Taste Integration

Do not paste a taste into every beat. Convert it into shot choices:

- Taste says "restrained observation" -> fewer cuts, more static holds, micro-actions.
- Taste says "tabletop comedy" -> locked camera, object timing, reaction cut.
- Taste says "hand-drawn depth" -> foreground occlusion, layered parallax, atmospheric perspective.
- Taste says "commercial proof" -> visible before/after evidence, clean product handling, controlled background.
