# Source Log: Zombie Scavenger Atomic Wasteland

## Coverage

- Source mode: single-video
- Number of sources: 6 public sources plus direct public-video sampling
- Date analyzed: 2026-05-23
- Confidence: medium
- Direct sampling note: A temporary 360P public Bilibili sample was downloaded to `/tmp/zombie-scavenger-analysis/source-360p.mp4` for analysis only. The source video and extracted frames were not stored in the project directory.

## Sources

| ID | Source | Type | Duration | Notes | Evidence Used |
| --- | --- | --- | ---: | --- | --- |
| S01 | https://www.bilibili.com/video/BV1FFRQB2Eqw/ | public video page/direct sample | 03:33.55 sampled, 03:34 page duration | Bilibili page identifies the work as an AI-generated Mx-Shell video, credits XiaoYunque Seedance2, and exposes metadata: original page dimension 2520x1080; sampled file 640x274, 30fps, AAC audio, no subtitle list. | Metadata, duration, aspect ratio, author/tool credit, 10-second contact sheet, rough scene-change detection. |
| S02 | https://www.douyin.com/video/7637813720252435755 | public video page | 03:34 reported | Douyin public result/snippet frames the reworked short with XiaoYunque, atom-punk, black humor, and AI creation tags. | Platform framing, Chinese viral context, style tags. |
| S03 | https://k.sina.com.cn/article_7879776328_1d5abd84806801lihc.html?from=tech | public summary | 03:34 | Summary describes the LED-faced robot cowboy, ostrich, zombie remains, retro resort/villa ruins, mannequin interaction, sunset dance, and metal-rose-like romantic payoff. The article marks itself AI-generated, so it is secondary evidence. | Plot grammar, character design, romantic payoff, no-dialogue claim. |
| S04 | https://finance.sina.com.cn/jjxw/2026-05-23/doc-inhyvxrq7802651.shtml | news analysis | 03:34 | News article describes the robot on an ostrich in city ruins, zombie action, mannequin dates, loneliness, overseas spread, and the importance of human selection/taste. | Reception, emotional read, platform behavior, director-like taste decisions. |
| S05 | https://k.sina.com.cn/article_1699258907_m6548a21b03301rfjo.html | creator interview/news | 03:34 | Interview-style report says the creator chose atom-punk over generic cyberpunk, placed the story in a seaside city, used a robot lead partly to avoid face-review issues, and made the story by iterating rather than starting with a locked script. | Creator-side style intent, setting choice, robot workaround, iterative production method. |
| S06 | https://www.reddit.com/r/aivideo/comments/1t8rq6m/aigc_short_film_zombie_scavenger_credit_mxshell/ | community reaction | short clip/repost | Reddit reactions compare it to anthology/game language and repeatedly respond to the clear movie-like hook. Comments also surface readable associations like "Wall-E with zombies" and game-like worldbuilding. | Overseas readability, genre associations, audience takeaway. |

## Direct Sampling

- Video properties: 213.546667 seconds, 640x274 sampled frame, 30fps, H.264 video, AAC stereo audio.
- Public page properties: Bilibili API reports 2520x1080 source dimension and one page with `first_frame`; page metadata flags AI-generated content.
- Frame sampling: 10-second contact sheet from the public sample showed the main visual blocks: ocean/pool catastrophe, robot cowboy reveal, red title sequence, seaside resort interiors, LED-face close-ups, ostrich street action, shopping-street ruins, mannequin/romance beats, sunset bench, pod/space tail imagery.
- Edit sampling: FFmpeg scene detection with threshold `gt(scene,0.24)` produced 90 high-contrast scene-change candidates over 213.5 seconds. Treat this as a rough rhythm indicator, not an exact shot count.
- Subtitle/audio limitation: Bilibili metadata returned no subtitle list. Audio track exists, but this pass did not perform detailed listening or music stem analysis.

## Observations

### Repeated Patterns

- The short uses a one-sentence hook with immediate visual proof: a robot cowboy/scavenger clears zombies in a seaside wasteland and then redirects into impossible romance. [S01, S02, S03, S04]
- Worldbuilding is compressed into a small icon set: ocean resort, dead street, robot worker, western hat/coat, ostrich/mount, slow zombie pressure, mannequin companion, red chapter-like typography, final escape/space image. [S01, S03, S04, S05]
- The visual style is atom-punk/weird-western retro-futurism rather than generic neon cyberpunk: sun, rust, resort glass, seaside ruins, old signage, weapon/tool silhouettes, LED facial symbols. [S01, S02, S05]
- Non-human face design is both a taste choice and a production workaround. LED smile/anger/sadness reads clearly at close-up scale and avoids unstable human micro-expression. [S01, S03, S05]
- The edit alternates action bursts with held emotional or comic punctuation. Direct scene detection suggests dense changes in action clusters, but the romance beats are allowed to breathe. [S01]
- The strongest transferable craft is selection: a few memorable images repeat and escalate instead of adding unrelated monsters or plot mechanics. [S01, S04, S05, S06]

### Exceptions

- Some public descriptions call the lead a robot cowboy, while others emphasize cleaner/scavenger. The reusable rule is a clear professional role with readable tools, not a fixed cowboy identity.
- Some reporting uses "cyberpunk" loosely, but the direct visual grammar is closer to sun-bleached atom-punk, weird western, and post-apocalyptic resort imagery.
- The direct sample confirms broad motion and visuals, but not the highest-resolution texture or exact music mix.

### Uncertain Areas

- Exact shot count and average shot length need manual shot logging rather than automated scene detection.
- Exact audio design, music cue timing, and sound-effect layering need a direct listening pass.
- Bilibili and Douyin/reposted versions may differ in blur, compression, subtitles, or censorship treatment.
- This is a single-video taste profile. It is strong for this short's grammar, but not enough to generalize the creator's whole body of work.
