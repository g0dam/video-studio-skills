# Source Evidence Rules

Use this guide when building `source-log.md` and deciding how much source material is enough.

## Sampling Strategy

For a creator or account:

- Prefer 5-12 representative videos across different dates and formats.
- Include at least one high-performing piece, one typical piece, and one recent piece when available.
- If only 1-2 examples are available, state that the taste is provisional.

For a single video:

- Record title or local filename, duration, aspect ratio, apparent platform, and source path or URL.
- Analyze the first frame, hook seconds, midpoint, ending, and any repeated visual motifs.
- If possible, inspect stills at regular intervals instead of relying on memory.

For local video:

- Do not modify the source file.
- Suggest extracting stills into a separate working folder when needed:

```bash
mkdir -p analysis-frames/<video-slug>
ffmpeg -i input.mp4 -vf fps=1 analysis-frames/<video-slug>/frame-%04d.jpg
```

For uploaded images or screenshots:

- Treat them as visual evidence, not full motion evidence.
- Mark editing, sound, pacing, and motion as low confidence unless the user provides more context.

## Evidence Log Format

Use `source-log.md`:

```markdown
# Source Log: <taste title>

## Coverage

- Source mode:
- Number of sources:
- Date analyzed:
- Confidence:

## Sources

| ID | Source | Type | Duration | Notes | Evidence Used |
| --- | --- | --- | ---: | --- | --- |
| S01 | <URL or local path> | video | 00:32 | hook uses object reveal | frames 1s/8s/24s, audio notes |

## Observations

### Repeated Patterns

- <pattern> [S01, S03, S05]

### Exceptions

- <exception> [S02]

### Uncertain Areas

- <unknown or low-confidence inference>
```

## Citation and Copyright Hygiene

- Link to public URLs instead of copying long text.
- Quote at most short phrases when necessary.
- Summarize dialogue, captions, and scene content rather than reproducing full scripts.
- Never include account cookies, private URLs, watermarked source files, or credentials.
- For brand/product references, record what is visible and avoid inventing official usage rights.
