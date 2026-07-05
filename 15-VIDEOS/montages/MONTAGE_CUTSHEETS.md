# Package 1 — Two-Character Montage Cut Sheets

Rough cuts were auto-assembled with ffmpeg from the approved intros in `15-VIDEOS/intros/`.
Each is a **rough cut**: character windows joined with a 0.6s soft crossfade + a 0.6s fade-out.
No text labels or closing card yet (this ffmpeg build has no `drawtext`/libfreetype) — add those
in a proper editor. Adjust the trim windows below after reviewing the footage, then re-render.

## Common settings
- Output: 1280×720, 24 fps, H.264 + AAC.
- Transition: `xfade` fade, 0.6s. End: 0.6s fade-out.
- Audio: original clip audio, `acrossfade` 0.6s, fade-out at end.

## 1. Noah & Arda — We Build Together → `noah-arda-we-build-together.mp4` (~28.4s)
- Segment 1: `intros/05-noah-intro.mp4` window **3.0s → 17.5s** (14.5s), fade-in 0.5s
- Segment 2: `intros/03-arda-intro.mp4` window **0.5s → 15.0s** (14.5s)
- To add in editor: label "Meet Noah" / "Meet Arda"; closing card "We Build Together"; ties to S01E08.

## 2. Kiko & Mimi — Kind Friends → `kiko-mimi-kind-friends.mp4` (~28.4s)
- Segment 1: `intros/01-kiko-intro.mp4` window **0.5s → 15.0s**, fade-in 0.5s
- Segment 2: `intros/02-mimi-intro.mp4` window **0.5s → 15.0s**
- To add in editor: label "Meet Kiko" / "Meet Mimi"; closing card "Kind Friends"; ties to Mimi's Big Yawn / cozy stories.

## 3. Luca & Opa — Little Wonders → `luca-opa-little-wonders.mp4` (~28.4s)
- Segment 1: `intros/06-luca-intro.mp4` window **0.5s → 15.0s**, fade-in 0.5s
- Segment 2: `intros/04-opa-intro.mp4` window **0.5s → 15.0s** (alt take: `07-opa-intro-2.mp4`)
- To add in editor: label "Meet Luca" / "Meet Opa"; closing card "Little Wonders"; ties to stars/bedtime stories.

## Re-render template (adjust START/DUR per window)
```bash
ffmpeg -y -i intros/<A>.mp4 -i intros/<B>.mp4 -filter_complex \
"[0:v]trim=start=<Astart>:duration=<dur>,setpts=PTS-STARTPTS,scale=1280:720,fps=24,setsar=1,fade=t=in:st=0:d=0.5[va];\
[1:v]trim=start=<Bstart>:duration=<dur>,setpts=PTS-STARTPTS,scale=1280:720,fps=24,setsar=1[vb];\
[va][vb]xfade=transition=fade:duration=0.6:offset=<dur-0.6>,fade=t=out:st=<2*dur-1.2-0.6>:d=0.6[vout];\
[0:a]atrim=start=<Astart>:duration=<dur>,asetpts=PTS-STARTPTS[aa];\
[1:a]atrim=start=<Bstart>:duration=<dur>,asetpts=PTS-STARTPTS[ab];\
[aa][ab]acrossfade=d=0.6,afade=t=out:st=<2*dur-1.2-0.6>:d=0.6[aout]" \
-map "[vout]" -map "[aout]" -c:v libx264 -pix_fmt yuv420p -c:a aac -movflags +faststart montages/<out>.mp4
```

## Still to do (per plan §6, §10)
- Add text labels + closing cards (editor with text support).
- Optional 3-character montages (Friends Who Try / Cozy Friends / Little Questions, Big Wonders) — only after this package is reviewed.
- Full-cast rough cut `intros/all-intros-combined.mp4` still needs pacing/order QA.
