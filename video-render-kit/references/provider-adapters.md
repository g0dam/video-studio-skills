# Provider Adapter Guide

Use provider adapters to translate one shotboard into tool-specific prompt packages. Keep the creative intent stable while adapting duration, reference images, and motion detail.

## Universal Package

Every provider package should include:

- Scene ID and duration
- Aspect ratio
- Reference images and how to use them
- Usage notes for the selected provider
- Renderability strategy: single clip or segmented micro-clips
- Cut/montage plan: cut type, transition method, and stitching note for each segment
- Audio/post policy: provider-generated audio or silent visual generation with unified post audio
- First-frame continuity from the previous scene
- A full clip prompt that can be pasted directly into the video tool
- Per-shot or per-segment prompts when the storyboard has multiple beats
- Last-frame handoff for the next scene
- First-frame or keyframe visual lock when the provider benefits from it
- Motion prompt, written as concrete timed action rather than abstract labels
- Continuity lock
- Negative prompt
- Audio/post-production notes
- Retry plan

When local examples exist, treat them as the formatting authority. In this repo, `storyboard/*-jimeng-prompt.md` is the target quality level for Jimeng-style prompt packages: detailed Chinese usage notes, a complete full-video prompt, one prompt per storyboard panel, a concrete negative prompt, and post audio or voiceover notes.

## Generic Prompt Structure

```markdown
# Scene XX Generic Render Prompt

## 使用建议 / Usage Notes

- Duration:
- Aspect ratio:
- References:
- Provider mode:
- Audio policy:
- Storyboard image warning: use as action order only, not as a rendered grid.

## 入场连续性 / First-Frame Continuity

<If this is not Scene 01, describe the previous scene's last frame. The first 0.3-0.7 seconds should match that state before the new action begins. If possible, use the previous scene's final still as the first-frame image reference.>

## 整段视频 Prompt / Full Clip Prompt

<One directly pasteable prompt. Include final output format, scene geography, characters, props, action sequence, camera rhythm, light, style, and post-only elements.>

## 逐镜头 Prompt / Per-Shot Prompts

### 01 | 00:00-00:01

<Generation-ready prompt for this shot: framing, subject action, camera, environment, continuity risk.>

### 02 | 00:01-00:02

<Continue until the scene is fully covered.>

## Continuity Lock

<Identity, wardrobe, props, location geography, light direction.>

## 出场交接 / Last-Frame Handoff

<Describe the exact final frame state the next scene must inherit: character pose, props, crowd/location position, light, camera distance, and what information must remain hidden or revealed.>

## Negative Prompt

<No text, no logos, no face drift, no wardrobe change, no grid, no artifacts...>

## Post Notes

<Voiceover, sound, subtitles, edit notes to add outside the video model.>
```

## Prompt Depth Standard

- Full clip prompt: usually several substantial paragraphs, not a short synopsis. It should make the scene reproducible without reading the shotboard.
- Per-shot prompt: describe the exact frame and motion for that time slice. Do not write only "wide shot", "close-up", or "camera pushes in".
- Negative prompt: include provider risks and story-specific risks, such as no grid, no readable accidental text, no identity drift, no prop drift, no wrong aspect ratio, and no unwanted reveal.
- Post notes: separate subtitles, voiceover, sound design, title cards, and graphic overlays from the generated image whenever text reliability matters.
- For multi-scene AI-video projects, keep voiceover, dialogue, music, ambience, sound effects, and subtitles in a unified post plan unless the provider and project intentionally support reliable synchronized audio. Do not let each scene prompt invent separate sound.
- Boundary continuity: do not let scene starts become new establishing shots unless intended. The first shot of Scene N should visibly inherit Scene N-1's last frame, then transition by a hold, match cut, push-in, reverse angle, or cut-on-action.

## Renderability Strategy

Plan generation in renderable units before writing provider prompts.

- Use one continuous clip only when the scene has one clear action, stable geography, simple camera motion, and no exact generated text.
- Split into 2-4 second micro-clips when the scene contains multiple actions, fragile hands/tools, crowd behavior, prop transformation, exact text, scene-boundary continuity, or a visible story reversal.
- Each segment must name start state, one main action, camera motion, end state, cut type, and next-segment handoff.
- Use accepted output stills as the next first-frame reference whenever the provider supports image-to-video or image references.
- Treat generated text as a post-production element by default. Ask the model for blank signs, screens, tickets, book covers, or labels, then add exact typography later.
- If a montage is needed, define the repeated framing rule or sound/object motif. Do not write random visual variety as a substitute for escalation.

## Provider Notes

### Sora

- Use when the user wants cinematic text-to-video or reference-guided generation.
- Keep instructions direct and scene-level.
- Separate edit/extend requests from new generation requests.
- Include exact duration and aspect ratio when known.

### Runway

- Strong for image-to-video and controlled camera moves.
- Pair a first frame with concise motion language.
- Avoid overloading the prompt with too many sequential events in one clip.

### Kling

- Strong for image-to-video with visible subject motion.
- Be explicit about face/wardrobe consistency and camera path.
- Use short clips for complex human motion.

### Seedance

- Useful for short-form cinematic motion.
- Keep prompt vivid but complete. Seedance prompts may be shorter than Jimeng, but they still need scene geography, subject identity, exact action order, camera behavior, lighting, continuity anchors, and negative constraints.
- Use a clear motion hierarchy inside the prose: subject first, camera second, environment third. Do not output only the hierarchy labels.
- For scenes longer than 5-6 seconds or with many action reversals, provide segmented prompts with exact time ranges and a stitching note.
- Do not ask Seedance to perform multiple unrelated actions in one prompt. Split complex action chains into micro-clips and carry the accepted last frame forward as the next first-frame reference when possible.
- Aspect ratio must come from the Seedance menu only: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`.
- Map ultra-wide creative ratios to the nearest Seedance menu option:

| Source / creative ratio | Seedance menu ratio | Note |
| --- | --- | --- |
| `2.33:1` | `21:9` | Exact practical match because `21 / 9 = 2.333...` |
| `2.35:1` or `2.39:1` | `21:9` | Closest available ultra-wide option |
| `1.78:1` or horizontal social | `16:9` | Standard horizontal |
| `1.33:1` | `4:3` | Classic horizontal |
| `1:1` | `1:1` | Square |
| `0.75:1` | `3:4` | Portrait classic |
| `0.5625:1` or vertical short video | `9:16` | Vertical short video |

- In Seedance files, write the actual provider selection, for example `输出：4 秒，Seedance 比例选择 21:9（最接近 2.33:1）横版`. Do not write `输出：4 秒，2.33:1` as the platform setting.
- Seedance continuity tip: if rendering scenes separately, export the previous scene's final frame and use it as the next scene's first-frame image reference when the interface allows it. If not, the first sentence of the prompt must restate the previous final frame before introducing new camera movement.

### Wan

- Use a structured prompt when available: subject, scene, action, camera, lighting, style, negatives.
- Keep style vocabulary concrete and avoid vague artist labels.

### Jimeng

- When using storyboard images, explicitly say the final output must be one full-screen video, not a grid.
- Provide per-shot prompts when the scene is safer as separate generated segments.
- Default to silent visual generation. Add voiceover, dialogue, subtitles, ambience, music, and sound effects in post rather than asking the model to render them.
- If the project has `audio/audio-continuity-guide.md`, reference it in the post notes and keep every Jimeng scene prompt consistent with it.
- Match the local `storyboard/*-jimeng-prompt.md` structure when present. Use Chinese headings and detailed prose:

````markdown
# Scene XX 即梦视频生成 Prompt

## 使用建议

- 视频比例：
- 时长：
- 推荐模式：图生视频 / 参考图生视频
- 渲染策略：单段连续生成 / 分段微镜头生成；说明每段的剪辑方式和交接帧。
- 参考图：可以使用 `<storyboard image>` 理解分镜顺序，但要明确告诉模型“不要生成九宫格画面，最终输出单一全屏视频”。
- 更稳的方式：把分镜面板分别裁成单张图，按短镜头逐段生成，再后期剪辑。
- 即梦只生成无声画面；不要生成对白、旁白、音乐、环境声、音效或字幕。声音、旁白、字幕、标题卡统一后期加。

## 入场连续性

写清楚上一场最后一帧：同一地点、同一镜头轴或可解释的反打关系、同一角色姿势、同一道具状态、同一光线方向。第一帧先接住上一场，不要直接跳到新空间或新状态。

## 整段视频 Prompt

```text
参考上传的分镜图和素材图，但不要生成九宫格画面。分镜图只作为动作顺序和镜头节奏参考，最终输出一段单一全屏的指定画幅视频，时长指定秒数。

只生成无声画面：不要生成或模拟对白、旁白、音乐、环境声、音效或字幕。所有声音统一在后期制作。

场景：写清楚空间、时间、天气、光线、地理锚点、画面质感。

人物：写清楚每个主要角色的年龄感、体型、脸部/发型、服装、材质、道具，并声明全片保持一致。

关键道具：写清楚本场必须准确出现或必须暂时隐藏的道具，以及不能提前揭示的信息。

剧情动作：按时间顺序写完整动作链，包含反转、误导、喜剧点或情绪转折。

镜头节奏：写清楚前中后节奏、镜头类型、推拉摇移、景别变化、停顿点。

后期声音参考，不要交给即梦生成：写清楚后期添加的旁白、拟音、环境声、音乐或标题卡。
```

## 逐镜头分镜 Prompt

### 01 | 00:00-00:01

```text
指定画幅、风格和镜头。写清楚构图、主体动作、相机运动、环境光、连续性锚点和本镜头不能出错的细节。
```

## 负向 Prompt

```text
不要字幕，不要屏幕文字，不要 logo，不要水印，不要九宫格画面，不要错误画幅，不要人物换脸，不要服装变化，不要道具变化，不要提前揭示，不要畸形手指，不要不符合本片风格的内容。
```

## 后期声音 / 旁白

```text
按时间码列出后期声音、旁白、标题卡或剪辑提示。
```

## 出场交接

写清楚最后一帧留给下一场继承的状态，包括角色位置、表情/LED、道具、队伍/背景、阴影和需要隐藏或已经揭示的信息。
````
- The Jimeng full prompt must read like a finished director brief, not a table converted into prose. It should include enough detail that a user can paste it without also opening the shotboard.

## Retry Strategy

Record each retry:

```markdown
| Attempt | Problem | Keep Fixed | Change | Result |
| --- | --- | --- | --- | --- |
```

Common fixes:

- Face drift -> stronger reference image, shorter clip, fewer face turns.
- Wardrobe drift -> restate clothing layers and colors in the visual lock.
- Location jumps -> simplify camera motion and name fixed landmarks.
- Grid rendered as video -> remove board image or state "reference only, do not reproduce layout" at the top.
- Bad text -> remove generated text; add text in editing.
