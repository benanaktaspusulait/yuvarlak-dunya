# E07 — Shot 06 — Together

---

## Scene Context

| Alan | Değer |
| --- | --- |
| Episode | S01E07 — The Round Stone |
| Shot | 06 / 06 |
| Duration | 15 seconds |
| Location | Stone Hill — Rounded Stone Discovery Area |
| Characters | Luca, Kiko |
| Time of Day | Morning |

---

## Continuity

This shot continues directly from Shot 05.

Same Stone Hill discovery area. Both Luca and Kiko are already present.
The round stone now rests safely on the mossy patch among the rounded stones.

---

## Stone Hill Visual Identity

Same rounded stone discovery area: smooth round toy-like stones, soft pebble path,
warm moss patches, gentle slope, child-safe rounded rock clusters, warm morning daylight.
Never sharp rocks, cliffs, quarry or generic rocky field.

---

## Start Frame

Start from the approved continuity frame exported from Shot 05 as closely as possible.
Preserve the established composition, lighting, background objects and character
proportions while allowing natural character motion. Match the Episode Colour Master.

Maintain:
- Character appearance
- Stone Hill environment
- Warm morning daylight
- Camera composition
- Character proportions

Do not redesign the environment. Both characters are already present, and the stone is
already resting on the ground.

---

## Background Object Lock

The first frame defines the physical Stone Hill set. All visible stone clusters, the
pebble path, moss patches and slope remain stable throughout the shot.

Do not remove stone clusters, replace stones with bushes, turn stones into trees, move
the pebble path, add cliffs/houses/modern objects, repaint the environment or change the
Stone Hill layout.

Allowed: Luca moves, Kiko moves, grass or moss moves gently, camera performs a gentle
planned pull-back.

## Visual Prompt

```text
Luca and Kiko stepping back and looking together at the smooth round stone resting safely on the mossy patch among the rounded stones on Stone Hill, both smiling warmly, peaceful shared moment, warm moss and rounded stones around them, warm morning daylight, no other characters, {style} {camera} {lighting}

Use @image1 as the starting continuity frame from Shot 05.
Preserve Luca, Kiko, the placed round stone resting safely on the mossy patch, the same Stone Hill layout, camera position, lighting and Episode Colour Master from @image1.

Match the lighting and colour grading exactly from the Episode Colour Master.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
The Stone Hill background is locked from the first frame; keep all visible rounded stones, pebble path, moss and slope stable throughout the shot.
```

Start from the Shot 05 exported continuity frame as closely as possible. Preserve the
established composition, lighting, background objects and character proportions while
allowing natural character motion. Do not reset or reposition the camera into a new
composition, redesign the set, change the lighting, or morph the background. Continue the
action naturally into the gentle ending pull-back.

---

## Reference Usage

OpenArt Reference Setup:

@image1 = approved exported final continuity frame from Shot 05.

Use @image1 as the required starting continuity reference. Preserve Luca, Kiko, the placed round stone, the Stone Hill layout, lighting, camera position and Episode Colour Master. Continue naturally from @image1 into the gentle ending pull-back; do not reset the camera or redesign the environment.

The reference image is supplied by the production workflow and should not be hardcoded
into this document.

---

## Camera Direction

Begin from the Shot 05 continuity frame with no camera reset. Maintain the identical
camera position from the previous shot; do not recompose into a new setup. Preserve the
established framing and composition while allowing natural character motion; keep the
camera in the same setup rather than recomposing into a new shot.

Allow a gentle pull-back to reveal Luca, Kiko, the placed stone and the Stone Hill
discovery area together. Do not introduce new characters, new landmarks, new paths,
buildings, caves, waterfalls or a different Stone Hill area. The placed round stone
must remain safely and flat on the mossy patch throughout the shot. Keep movement slow
and cinematic. The last 2 seconds (13-15s) are clearly silent and peaceful, with no
spoken lines. Hold the final frame quietly.

The final frame should be clean, peaceful and YouTube end-screen friendly, with some
uncluttered background/sky space if naturally available. Do not add any text inside the
video. No extra dialogue after the final line. No logo, no title card, no captions, no subtitles, no subscribe graphics and no end-card graphics inside the generated video.

Warm morning daylight throughout.

The first 1 second of Shot 06 should preserve the Shot 05 final frame, with the stone
already resting safely on the mossy patch, before the gentle pull-back begins.

---

## Transition Continuity Rule

@image1 must be the approved final continuity frame of Shot 05.

The first frame of this shot should match @image1 as closely as possible in: camera
angle, camera height, lens feel, framing, character positions, character scale,
background object positions, pebble path position, stone cluster positions, lighting,
colour grading, exposure and contrast.

This shot may continue the action naturally, but it must not begin with a noticeable
camera reset, jump cut, environment shift, character scale change, or background layout
change.

If the transition from Shot 05 feels slightly jumpy, regenerate this shot using the
Shot 05 final frame as a stricter first-frame continuity reference (see
`00_EPISODE_OVERVIEW/01-overview.md` § Transition QA for the repair workflow).

---

## Dialogue

Match the lighting, colour grading, exposure and colour temperature of the Episode
Colour Master. Do not change exposure, brightness, light intensity, colour temperature
or colour grading.

```
Luca: Now everyone can see it.
Kiko: Together.
Luca: Together.
```

---

## Shot Breakdown

| Time | Action | Camera |
|---|---|---|
| 0-5 sn | Luca and Kiko step back and look at the placed stone | Medium |
| 5-9 sn | Luca: "Now everyone can see it." | Gentle pull-back |
| 9-11 sn | Kiko: "Together." | Gentle pull-back |
| 11-13 sn | Luca: "Together." | Wide |
| 13-15 sn | Quiet warm final hold, silent | Wide, quiet hold |

---

## Sound

- Quiet ambient wind
- Distant birds
- Soft, warm ending tone

---

## Lighting

Warm morning daylight. Soft preschool light. Low contrast. No harsh shadows.
Match the Episode Colour Master. No lighting change, no golden afternoon shift.

---

## Negative Prompt

low quality, blurry, deformed, extra limbs, text, watermark, subtitles, speech bubbles, captions, photorealistic, horror, scary, dark lighting, violence, weapons, sharp rocks, cliffs, dangerous boulders, realistic quarry, golden afternoon light, sunset, moonlight, extra characters, non-canon characters, redesigned environment, lighting changes, colour grading changes, camera reset, background morphing, disappearing stones, changing path, new houses, modern objects, building, house, door, roof, bench, cave, waterfall, tower, entrance, sign, bridge, pond, river, stream, water feature, stone house, doorway, window, chimney, constructed structure, wooden structure, title card, logo, end card graphics, subscribe button, like button, arrows

## QA Checklist

Reference: 16_VIDEO_QA_SPEC.md

- [ ] Character integrity verified
- [ ] Character consistency verified
- [ ] Object persistence verified
- [ ] No rendering artefacts
- [ ] Camera consistency verified (no reset from Shot 05)
- [ ] Lighting consistency verified (warm morning daylight, no golden shift)
- [ ] Canonical rules followed
- [ ] Ending shares the discovery instead of only keeping the stone
- [ ] Final 2 seconds (13-15s) are clearly silent, warm and peaceful
- [ ] Final frame is clean and YouTube end-screen friendly (uncluttered background/sky space if natural)
- [ ] Stone Hill looks specific, not generic
- [ ] Background stone clusters remain stable
- [ ] No background object morphing
- [ ] Round stone prop remains consistent
- [ ] Same physical location is preserved throughout the shot
- [ ] @image1 continuity preserved from Shot 05 final frame.
- [ ] Both Luca and Kiko remain visible and consistent throughout.
- [ ] The placed round stone remains safely and flat on the mossy patch throughout.
- [ ] No new landmarks, buildings, caves, waterfalls or alternate Stone Hill area appear.
- [ ] No title card, logo, captions, subscribe graphics or end-card graphics are generated inside the video.

## Stronger Ending

End on a warm, shared "Together." The stone stays for everyone to see — the discovery
is shared, not owned. No abrupt cut; hold the peaceful final frame.
