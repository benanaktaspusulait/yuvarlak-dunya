# Shot 05 — Stepping Inside (Planned Entrance Crossing → Interior Master Setup)

## Shot Contract
- **Episode:** S01E04 — Mimi's Big Yawn
- **Shot:** 05 / 08
- **Duration:** 15 seconds
- **Characters:** Mimi, Kiko
- **Location:** Entrance crossing → Mimi's Burrow interior
- **Time:** Evening dusk outside → warm interior glow inside
- **Camera:** Slow planned push through the round entrance (the ONLY allowed movement in this episode)
- **Purpose:** Canonical entrance crossing; establishes the INTERIOR as the new master setup frame for Shots 06–08

## Why This Shot Is Allowed (Hard Gate — §0, §2)
This is a **planned, canonical location change**, not a camera search or object invention:
- The world spec (`02_WORLD_SPEC/05-mimis-burrow-world-spec.md` § Navigation) states the **entrance crossing must not be skipped** — it is part of the world's canon flow (Exterior → Entrance → Interior).
- The interior and all its props are **canon**, defined in the world spec — they are not invented by the model, they are revealed by a deliberate, slow, planned move through the open round entrance.
- The push is slow and single-purpose (cross the threshold). No searching, no reframing, no drift.
- This shot's approved **final frame becomes the INTERIOR MASTER SETUP** — the `@image1` for Shots 06–08.

## Interior Setup Requirements (final 3 seconds must settle into a stable interior master frame)

**MUST-HAVE (reject if any missing — Shots 06–08 depend on these):**
✅ Round blue plush pillow (#90CAF9) — the sleeping spot for Shots 06–08
✅ Warm blue interior walls (#90CAF9)
✅ Soft green plush carpet (#C8E6C9)
✅ Constant warm golden interior glow — cozy, never dark

**STRONG PREFERRED ANCHORS (at least one must be clearly visible; all three ideally):**
✅ Small round window with white frame
✅ Mini white shelf with books
✅ Round orange carrot box (#FF7043)

> Rationale: seeding all 7 interior props inside a 15s crossing is hard. The four
> must-haves are non-negotiable because Shots 06–08 interact with the pillow and rely
> on the walls/carpet/glow. The three anchors add canon charm; require at least one so
> the interior reads as Mimi's Burrow, and prefer all three when the generation allows.

## Object Continuity Gate
Before generating this shot, check S01E04_OBJECT_CONTINUITY_MAP.md.

Use the actual Shot 04 final frame as @image1.
@image1 controls the first frame, exterior composition, characters, entrance, lighting, and continuity.
@image2 is required and controls only the interior design after the threshold crossing.

Do not restore or correct the exterior layout. Do not add new exterior objects. Do not move, grow, shrink, or reposition the tree, flowers, stones, hills, entrance, or sky before the crossing.

The only allowed change is the planned transition through the already-visible round glowing entrance.

After entering, the interior must be based on @image2 and must include:
- round blue pillow
- warm blue walls
- soft green carpet
- warm golden glow
- at least one canon anchor: window, shelf, or carrot box

No random interior props. No extra rooms. No cave. No dark tunnel. No adult furniture. No new non-canon objects.

## Visual Prompt

```text
Start from @image1: the exterior evening-dusk view of Mimi's Burrow entrance, with Mimi and Kiko standing outside, turned toward the round blue glowing doorway.

Use only the exterior objects already visible in @image1 for the first-frame exterior.
After the planned entrance crossing, use only approved interior objects from @image2.
Do not generate extra objects.
Do not enlarge, move, multiply, reshape, or reposition any environment object.
The current action must adapt to the existing @image1 layout and approved @image2 interior.
Characters may move; environment objects may not, except for the planned Shot 05 threshold crossing.

Hold @image1 for the first 1 second. Then, with a slow, gentle, single planned push, the camera follows Mimi and Kiko as they step across the three round grey stepping stones and through the open round blue entrance into the cozy interior. The movement is smooth, slow and calm — a soft storybook threshold crossing, not a fast dolly.

The shot settles inside Mimi's Burrow: one small continuous underground room with warm blue walls (#90CAF9), a soft green plush carpet (#C8E6C9), and warm golden light filling the space. A round blue plush pillow (#90CAF9) rests as the central, cozy element. A small round window with a white frame lets in a gentle hint of evening light. A mini white shelf with a few books sits low and reachable. A round orange carrot box (#FF7043) sits nearby. Everything is Mimi-sized, rounded, soft and touchable.

Mimi and Kiko stand just inside the warm room, looking relieved and happy to be in the cozy space. Mimi's sleepy eyes soften as she sees her own comfy pillow.

Settle into a stable interior composition for the final 3 seconds so this frame can be used as @image1 for the next shot. No further camera movement after settling. Keep everything warm, cozy, and safe.

{style} = Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity
{camera} = stable 50mm preschool camera, one slow gentle push through the entrance, then static; max 3% frame/sec, no shake
{lighting} = warm golden interior glow, soft warm-blue undertones, cozy, never dark or cold
```

## Dialogue

```
Kiko: See? Warm and cozy!
Mimi: My soft pillow...
```

## Sound Design

No music.
No background music.
No melody.
No song.
No soundtrack.
No musical bed.
No chime.
No ending jingle.
No magical sound effects.
No sparkles, bells, or musical tones.

Use natural ambience only.

Exterior shots:
Use very soft evening meadow ambience:
- gentle breeze
- soft grass rustle
- tiny distant meadow insects
- subtle flower meadow atmosphere
- soft character breathing and tiny movement sounds

Interior shots:
Use very soft cozy room ambience:
- warm quiet room tone
- soft character breathing
- tiny fabric / pillow movement sounds
- gentle footstep or paw movement only when characters move

Keep all ambience quiet, warm, preschool-safe, and bedtime-friendly.
Do not let ambience become loud, dramatic, scary, windy, musical, or distracting.

## Negative Prompt

```text
door, closed door, wooden door, rectangular door, dark hole, cave, tunnel, scary, dark, cold, harsh shadows, black shadows, night sky, stars, moonlight, daytime, bright sun, fast camera, dolly zoom, whip pan, shaky, motion blur, Dutch angle, fisheye, text, logo, watermark, speech bubbles, captions, subtitles, separate rooms, large underground chamber, oversized room, adult furniture, huge furniture, entrance becomes a door, entrance not round, entrance not blue, no warm glow, empty room, no interior anchor visible, all interior anchors missing, missing required pillow, missing required warm blue walls, missing required green carpet, missing required warm golden glow, sharp edges, clutter, random props, metal, plastic, glass, modern objects, city objects, photorealistic, realistic dirt, camera reset, camera searching, camera reframe after settling, background morphing, lighting drift, character scale change, ghost character, duplicate character, transparent duplicate, double exposure, motion smear, character trail, music, background music, melody, song, soundtrack, musical bed, chime, ending jingle, magical sound effects, sparkles, bells, musical tones
```

## OpenArt Settings
- **Aspect Ratio:** 16:9
- **Seed:** (use consistent seed or empty)
- **@image1:** shot-04-kiko-points-doorway final frame — exact exterior first frame continuity source
- **@image2 (REQUIRED before spending video credits on Shot 05):** Mimi's Burrow interior canon reference (Hero View / interior still) — interior design only

**Reference roles (hard rule):**
```
@image1 = exact exterior first frame continuity source from Shot 04.
@image2 = approved Mimi's Burrow interior canon reference only. REQUIRED before generating Shot 05.

@image1 has priority for the first frame, exterior composition, entrance,
characters, lighting and continuity.
@image2 is used ONLY after the threshold crossing to preserve interior design.
Do not use @image2 as the first frame.
Do not copy @image2 camera before entering.
Do not let @image2 override @image1.
```
> If no interior reference (@image2) is available, the model may invent the interior — this is the single highest spawning risk in the episode. Prepare and approve an interior reference (@image2) BEFORE generating Shot 05 — do not spend video credits on Shot 05 without it.
- **Model:** (use current production model)
- **Guidance Scale:** (standard production settings)

## Reject Kontrolü

**REJECT if ANY of these happen:**
- [ ] First second does not match exterior @image1
- [ ] Camera move is fast, shaky, or searches around
- [ ] Entrance becomes a door / not round / not blue
- [ ] Interior is dark, cold, or cave-like
- [ ] Interior room is oversized or has separate rooms
- [ ] MUST-HAVE missing: pillow, walls, carpet, or warm glow (reject)
- [ ] NONE of the anchors (window/shelf/carrot box) visible (reject — need at least one)
- [ ] Interior objects look adult-sized (must be Mimi-sized)
- [ ] Final frame not stable/usable as @image1 for Shot 06
- [ ] New non-canon objects invented

**APPROVE only if:**
- [ ] Opens on exterior @image1, holds 1 second
- [ ] One slow, calm, planned push through the round entrance
- [ ] Settles into a stable, warm, cozy interior for the final 3 seconds
- [ ] MUST-HAVE all present: round blue pillow, warm blue walls, green carpet, warm glow
- [ ] At least one anchor present (window, shelf, or carrot box); ideally all three
- [ ] Interior is Mimi-sized, rounded, warm
- [ ] Final frame is stable and usable as interior @image1
- [ ] Warm golden glow throughout

## Production Notes
- **This is the INTERIOR MASTER SETUP** — Shots 06–08 depend on this frame
- **Only planned movement in the episode:** slow threshold crossing, then static
- **Canonical crossing:** required by world spec; not a camera search
- **Seed everything inside now:** no interior prop may first appear during later dialogue
- **Save the settled interior final frame as @image1** for Shot 06

## Continuity & Safety Locks
- **Character locks:**
  - **Kiko:** approved Kiko character design from the character reference / canon videos, scale 100. Preserve Kiko exactly; do not redesign Kiko and do not turn Kiko into a different creature.
  - **Mimi:** approved soft blue bunny-like character, scale 80, soft blue #90CAF9. Preserve Mimi exactly; sleepy expression, half-closed eyes, drooping ears.
  - Do not change character scale, identity, proportions, or colours.
- **Camera lock:** Start from the same camera position as @image1; the only movement is the single planned slow entrance crossing, then static.
- **Lighting lock:** Match the lighting of @image1 for the first second (exterior dusk), then transition to the canonical warm interior glow. No night, no stars.
- **Character presence:** Both characters are already present; do not introduce any new character after the shot has started.
- **Text safety:** No text. No subtitles. No speech bubbles. No captions.
