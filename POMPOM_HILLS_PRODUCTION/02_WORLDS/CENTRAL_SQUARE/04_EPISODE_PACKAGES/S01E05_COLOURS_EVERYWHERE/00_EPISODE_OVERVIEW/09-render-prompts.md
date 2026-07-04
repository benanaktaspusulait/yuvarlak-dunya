# S01E05 — Render Prompts

Use `00-CORE/17_VIDEO_GENERATION_STANDARD.md`.

Use `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHOT_CONTINUITY_WORKFLOW.md`.

Do not create images or videos from this document directly without the approved references.

---

## Global Negative Prompt

```text
low quality, blurry, deformed, extra limbs, text, readable text, watermark, logo, title card, subtitles, captions, speech bubbles, subscribe button, like button, arrows, photorealistic, horror, scary, dark lighting, sunset, moonlight, night sky, stars, crickets, violence, weapons, sharp objects, traffic, cars, roads, modern city, crowded square, extra characters, non-canon characters, redesigned environment, camera reset, background morphing, disappearing objects, changing path, new buildings, readable signs, shops with text, complex city skyline, fountain, water feature, bridge, river, pond

teleporting character, disappearing character, character hidden behind bush, character walking through bushes, character clipping through objects, character emerging from opposite side, moving benches, moving trees, moving planters, shifting bushes, changing object positions, object morphing, layout changing, character occluded by foreground plants, walking through flowerbeds, walking through planters, walking through benches

intra-shot character disappearance, character disappearing within the same shot, character reappearing within the same shot, character teleporting within the same shot, character regenerating after occlusion, character hidden by bushes, character entering bushes, character emerging from bushes, character walking behind plants, character fully occluded, character path break, broken character continuity, character side-switching, character clipping through plants, character clipping through bushes, character walking through planters, foreground plants covering character, occlusion transition, hidden character transition
```

---

## Global Intra-Shot Continuity Add-On

Apply this add-on to every story shot prompt:

```text
The Central Square set behaves like a fixed physical stage. All visible trees, benches, planters, bushes, flowerbeds, rounded paths, stepping-stone ring, paving stones, grass patches, bunting or flags, distant houses, low walls and established landmarks must stay fixed in position and identity.

The first 1 second must hold extremely close to @image1. During this first second, camera angle must not change, character positions must not jump, background objects must not move, no new object may appear, no object may disappear, and no character may teleport or change side.

Kiko and Mimi must remain continuously visible physical characters inside the same 15-second shot. They must not disappear, reappear, regenerate, teleport, duplicate, side-switch, pass behind foreground plants, or be recreated after occlusion.

Each character must stay on one clear visible walkable path. Use rounded paths, paving stones, stepping-stone ring, clear open grass patches, or open space beside benches and planters only. Do not walk through or behind bushes, flowerbeds, planters, benches, tree trunks, walls, houses, foreground plants or dense grass.

The character's movement must be continuous, slow, preschool-safe, and physically possible.

The camera must not create character hiding. Camera movement must stay tiny and stable. Do not pan behind bushes, track a character into foliage, or allow foreground plants to pass across the character's body. Prefer locked-off or nearly locked-off camera. Use pointing, looking, tiny steps, smiling and gentle turns instead of walking across the set.

Reject if any character is fully hidden, reappears from a different side, clips through objects, teleports, or if background objects move, morph, duplicate, disappear or change identity.
```

---

## OpenArt Reference Workflow

- Shot 01: `@image1` = approved Central Square Friends Micro-Opening final frame.
- Shot 01 creates a new story first frame with Kiko already visible.
- Shot 01 approved Kiko-visible still becomes the Episode Colour Master.
- Shot 02: `@image1` = approved Shot 01 final continuity frame.
- Shot 03: `@image1` = approved Shot 02 final continuity frame.
- Shot 04: `@image1` = approved Shot 03 final continuity frame.
- Shot 05: `@image1` = approved Shot 04 final continuity frame.
- Shot 06: `@image1` = approved Shot 05 final continuity frame.
- Shot 07: `@image1` = approved Shot 06 final continuity frame.
- Shot 08: `@image1` = approved Shot 07 final continuity frame.

The first 1 second should visually hold close to @image1 before new action begins.
For Shot 01, this applies to the Central Square environment only; Kiko must already be
visible and `@image1` must not be copied as an empty frame.

---

## Shot Prompts

### Shot 01 — Kiko Sees Red

```text
Use @image1 as the Central Square Friends Micro-Opening final-frame environment reference.
Generate a new story first frame with Kiko already visible in Central Square.

Kiko from Pompom Hills already visible near the Big Pompom Tree and rounded paths, noticing a red rounded planter or red bunting detail already part of the square, curious happy expression, warm morning daylight, soft pastel colours, no other characters, {style} {camera} {lighting}

Preserve the Big Pompom Tree, rounded paths, coloured stepping-stone ring, grass, benches, planters, camera position, lighting and Central Square layout from @image1.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
```

### Shot 02 — Mimi Joins

```text
Use @image1 as the starting continuity frame from Shot 01.

Kiko standing in the same Central Square area near the red detail, Mimi entering gently from the same visible rounded path, Big Pompom Tree in background, warm morning daylight, no other characters, {style} {camera} {lighting}

Mimi must enter naturally through visible motion from the Central Square path; do not make her appear suddenly or pop into the frame.

Preserve Kiko, red detail, Big Pompom Tree, rounded paths, stepping-stone ring, camera position, lighting and Episode Colour Master from @image1.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
```

### Shot 03 — Blue Bench

```text
Use @image1 as the starting continuity frame from Shot 02.

Kiko and Mimi already together in the same Central Square area, noticing the same pastel blue bench established in the Central Square set, visible from the current angle or reached with only a tiny natural camera settle, Big Pompom Tree in background, warm morning daylight, no other characters, {style} {camera} {lighting}

Preserve Kiko, Mimi, Central Square layout, blue bench, Big Pompom Tree, rounded paths, camera position, lighting and Episode Colour Master from @image1.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
```

### Shot 04 — Yellow Flowers

```text
Use @image1 as the starting continuity frame from Shot 03.

Kiko and Mimi already together in the same Central Square area, noticing yellow flowers in an existing rounded planter beside the path, Big Pompom Tree in background, warm morning daylight, no other characters, {style} {camera} {lighting}

Preserve Kiko, Mimi, Central Square layout, existing planter, Big Pompom Tree, rounded paths, camera position, lighting and Episode Colour Master from @image1.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
```

### Shot 05 — Green Grass

```text
Use @image1 as the starting continuity frame from Shot 04.

Kiko and Mimi already together in the same Central Square area, noticing a soft green grass patch beside the rounded paving stones, Big Pompom Tree in background, warm morning daylight, no other characters, {style} {camera} {lighting}

Preserve Kiko, Mimi, Central Square layout, grass/paving relationship, Big Pompom Tree, rounded paths, camera position, lighting and Episode Colour Master from @image1.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
```

### Shot 06 — Purple Flags

```text
Use @image1 as the starting continuity frame from Shot 05.

Kiko and Mimi already together in the same Central Square area, noticing small soft purple bunting or flags already part of Central Square, Big Pompom Tree in background, warm morning daylight, no other characters, {style} {camera} {lighting}

Preserve Kiko, Mimi, Central Square layout, purple bunting or flags, Big Pompom Tree, rounded paths, camera position, lighting and Episode Colour Master from @image1.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
```

### Shot 07 — Colours Together

```text
Use @image1 as the starting continuity frame from Shot 06.

Kiko and Mimi already together in the same Central Square area, gently pointing back across the same visible square to remember the colours they found: red detail, blue bench, yellow flowers, green grass and purple flags, Big Pompom Tree in background, warm morning daylight, no other characters, {style} {camera} {lighting}

Preserve Kiko, Mimi, Central Square layout, visible colour objects, Big Pompom Tree, rounded paths, camera position, lighting and Episode Colour Master from @image1.

If not all colour objects are visible from the camera angle, characters may point gently across the same square; do not reset the camera or move to a new location.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
```

### Shot 08 — Rainbow Moment

```text
Use @image1 as the starting continuity frame from Shot 07.

Kiko and Mimi already together in the same Central Square area, standing warmly near the Big Pompom Tree and seeing the existing colours around the square as a soft rainbow-like feeling, red detail, blue bench, yellow flowers, green grass and purple flags all in the same stable set, warm morning daylight, peaceful final shared moment, no other characters, {style} {camera} {lighting}

Do not generate a literal rainbow beam, magical rainbow, glow effects, sparkles, portal, light beam or fantasy magic. Prefer a warm colour composition using the existing objects in the square.

Preserve Kiko, Mimi, Central Square layout, visible colour objects, Big Pompom Tree, rounded paths, camera position, lighting and Episode Colour Master from @image1.

No logo, no title card, no captions, no subtitles, no subscribe graphics and no end-card graphics inside the generated video.
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
```
