# Shot 01 — Your Coat Is Ready! — FINAL FIXED

## Production Lock

| Field | Value |
|---|---|
| Duration | 15 seconds |
| Format | 16:9 |
| Model | Seedance |
| Location | Kiko's Home — Entryway |
| Characters | Kiko and Mimi |
| Coat state | Hanging naturally on the wooden rack throughout |
| Camera | Static child-eye medium-wide shot |
| Audio | Indoor room tone only; no music |

## Reference Workflow

### Take Shot only

- `@image1` = canonical Kiko character image
- `@image2` = canonical Mimi character image
- `@image3` = approved Kiko's Home entryway image

### Video only

- Use the approved Shot 01 Take Shot as the **single `@image1`**.
- Do not add the separate character or environment references again.
- Auto Voice OFF.
- Manually select Kiko's canonical voice and Mimi's canonical voice.
- Prompt Enhancer, Cinematic, Auto Camera and Music OFF.

## Take Shot Prompt

```text
@image1 @image2 @image3 Create the clean opening frame for a 15-second 16:9 preschool animation. Preserve the canonical Kiko, Mimi and Kiko's Home entryway exactly. Static child-eye 35mm medium-wide view: the wooden coat rack and one terracotta coat are clearly visible on screen-left; the closed glass-panel front door is visible on screen-right. Kiko stands near centre-left, a safe step away from the coat, with both hands empty and lowered, looking at it with bright curiosity. Mimi stands on screen-right near the door, facing Kiko and the coat with a warm smile. Keep both full characters, the whole coat and its hanger visible with safe margins. The coat hangs naturally with both sleeves down; nobody touches it. Warm soft daytime light, pastel matte handcrafted toy-set materials, medium-low contrast, gentle sharpness, uncluttered floor. No text, no extra props or characters.
```

## Take Shot Hard Gate

- Exactly one terracotta coat is hanging on the rack.
- The whole coat, hanger and both sleeves are visible.
- Kiko and Mimi are fully visible and correctly scaled.
- Kiko's hands are empty and do not touch the coat.
- Kiko is centre-left; Mimi is screen-right.
- The front door stays closed.
- No outdoor clothing is already on Kiko.
- No text, logo, clutter, extra character or extra coat.
- Colour remains warm pastel, matte and medium-low contrast.

## Video Prompt

```text
Create one continuous 15-second 16:9 Seedance frame-to-video shot. Use the approved Shot 01 Take Shot as @image1 and the only visual source. The first frame must match @image1 exactly: Kiko stands centre-left with empty lowered hands, Mimi stands screen-right near the closed door, and exactly one terracotta coat hangs naturally on the wooden rack at screen-left. Keep the entryway, character identities, scale, clothing, lighting and object positions unchanged.

CAMERA AND STAGING LOCK:
Use a completely static child-eye 35mm medium-wide camera for all 15 seconds. Keep both full characters, the whole coat, hanger, rack and closed door visible with safe margins. No cut, zoom, push-in, pan, tilt, orbit, angle change or reframing. Kiko and Mimi remain on their established sides. Mimi does not walk to the coat. The floor and room remain unchanged.

ACTION AND DIALOGUE:
0.0–2.2s: From the first frame, Mimi turns only her eyes and one small open paw toward the hanging coat. At 0.4s Mimi says warmly, “Kiko, your coat is ready!” Only Mimi moves her mouth. Kiko follows Mimi's gesture with her eyes.

2.2–4.5s: Kiko's face brightens; she makes one tiny pleased bounce in place without changing sides. At 2.7s Kiko says, “My cozy coat!” Only Kiko moves her mouth. The coat remains completely still.

4.5–6.9s: Mimi lowers her paw and gives one gentle encouraging nod. At 4.9s Mimi asks, “Would you like to try?” Only Mimi moves her mouth. Kiko looks from Mimi back to the coat.

6.9–9.4s: Kiko nods once and brings both empty hands together briefly in front of her body. At 7.3s Kiko says, “Yes, I want to try!” Only Kiko moves her mouth. She does not touch the coat.

9.4–11.8s: Mimi makes one small slow-down gesture close to her own body. At 9.8s Mimi says, “Nice and slowly.” Only Mimi moves her mouth. Kiko watches and gives a small understanding nod.

11.8–15.0s: At 12.1s Kiko says, “One little step!” Only Kiko moves her mouth. After finishing the line, Kiko takes exactly one short careful step toward the rack, stops with both feet planted, then slowly raises only her nearest empty hand beside the lower edge of the coat. End during this gentle hand-raising motion before contact. Kiko does not grasp, pull, remove or wear the coat. Mimi stays in place and watches proudly.

COAT AND CONTINUITY LOCK:
Exactly one coat remains hanging from the same hanger on the same rack for the entire shot. Both sleeves stay down and empty. The coat never moves, swings, changes size, changes colour, duplicates, disappears or jumps into a hand. No character touches it. Final state: Kiko is one small step closer to the rack with one empty hand raised beside, but not touching, the coat; Mimi remains screen-right; the door remains closed. This clean final state will begin Shot 02.

CHARACTER, VOICE, AUDIO AND STYLE LOCK:
Preserve Kiko and Mimi's canonical faces, hair/fur, clothing, proportions and manually selected saved voices. Only the assigned speaker moves their mouth. No overlapping dialogue, shared voice or voice swap. Keep natural eye movement, breathing and the specified small reactions between lines; no idle dead-air gap longer than 0.8 seconds. Use quiet indoor room tone, very soft clothing movement and one soft footstep only. No birds, music, narration, captions or text. Preserve the soft warm pastel preschool look, matte handcrafted materials, medium-low contrast and gentle sharpness. Do not increase saturation, brightness, contrast, HDR, gloss, harsh shadows or sharpness.
```

## Negative Prompt

```text
coat already in Kiko's hand, coat already worn, half-worn coat, touched coat, pulled coat, removed coat, swinging coat, flying coat, self-moving coat, duplicated coat, extra coat, missing coat, changed coat colour, changed hanger, empty rack, Kiko crossing sides, Mimi crossing sides, Kiko walking more than one short step, character touching door, opening door, outdoor transition, character pop-in, missing character, duplicate character, identity change, clothing change, body distortion, extra limb, fused hand, wrong voice, voice swap, adult voice, inaccurate lip-sync, multiple mouths moving, overlapping dialogue, long silence, idle freeze, frozen ending, camera movement, zoom, push-in, pan, tilt, orbit, angle jump, cut, close-up, cropped character, cropped coat, room redesign, new prop, background animal, bird sound, harsh contrast, oversaturation, HDR, excessive sharpness, glossy plastic, dark lighting, text, captions, logo, watermark, narration, music
```

## Final QA

- Opening frame matches the approved Take Shot exactly.
- First spoken line begins at 0.4 seconds.
- All six lines are present, correctly assigned and non-overlapping.
- Only the speaker's mouth moves.
- No silent/idle interval exceeds 0.8 seconds.
- Exactly one coat remains on the rack for all 15 seconds.
- Kiko takes exactly one short step and never touches the coat.
- Final frame shows Kiko's empty hand rising beside the coat before contact.
- Mimi remains screen-right and the door remains closed.
- Camera is completely static.
- Indoor ambience only; no birds and no music.
- No contrast, saturation, HDR, brightness or sharpness drift.
