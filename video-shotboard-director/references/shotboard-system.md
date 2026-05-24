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

Each finished panel description should answer:

- What exact image is on screen?
- What changed from the previous panel?
- Where are the key character, prop, and location anchors?
- What is the camera doing and how fast?
- What sound, silence, voiceover, title card, or edit note belongs here?
- What continuity or reveal must not be lost?

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

## Scene Boundary

- Entry continuity:
- Exit handoff:

## Beats

| Beat | Timecode | Cut Type | Shot | Action | Camera | Viewer Attention | Continuity | Render Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

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
