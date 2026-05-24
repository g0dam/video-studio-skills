# Production State

Use `production-state.json` to make long video projects resumable.

## Gates

- `G0_brief`: user goal, platform, duration, aspect ratio.
- `G1_taste`: taste selected or created.
- `G2_story`: concept and scene plan locked.
- `G3_assets`: asset bible and references ready.
- `G4_shotboards`: shotboards or keyframes ready.
- `G5_render`: provider prompts and generated clips tracked.
- `G6_release`: QA, cover, title/caption, final package.

## State Shape

```json
{
  "version": 1,
  "project_slug": "project-slug",
  "title": "Project Title",
  "created_at": "ISO-8601 timestamp",
  "updated_at": "ISO-8601 timestamp",
  "status": "draft",
  "taste": null,
  "gates": {
    "G0_brief": {"status": "pending", "files": [], "notes": ""},
    "G1_taste": {"status": "pending", "files": [], "notes": ""},
    "G2_story": {"status": "pending", "files": [], "notes": ""},
    "G3_assets": {"status": "pending", "files": [], "notes": ""},
    "G4_shotboards": {"status": "pending", "files": [], "notes": ""},
    "G5_render": {"status": "pending", "files": [], "notes": ""},
    "G6_release": {"status": "pending", "files": [], "notes": ""}
  },
  "visual_policy": {
    "creative_aspect_ratio": "",
    "provider_aspect_ratio": "",
    "storyboard_path_convention": "",
    "approved_reference_images": []
  },
  "audio_policy": {
    "mode": "silent-provider-video | provider-audio | unknown",
    "post_audio_plan": "",
    "voiceover_policy": "",
    "subtitle_policy": ""
  },
  "scenes": [],
  "render_attempts": []
}
```

Gate statuses: `pending`, `in_progress`, `ready`, `blocked`, `locked`.

## Usage Rules

- Update state after creating durable files.
- Do not mark a gate `locked` unless the user approved it or the project convention says it is final.
- Keep render attempts factual: provider, scene, input files, result path, issue, next action.
- Record whether the provider prompt should generate silent visuals only. For Jimeng-style scene generation, use `silent-provider-video` unless the user explicitly requests provider-generated audio.
- Track the project's storyboard path convention, such as `storyboard/scene-XX.*` or `shotboards/scene-XX.*`, so later skills do not split outputs across directories.
- Do not store API keys, tokens, private cookies, or billing data.
