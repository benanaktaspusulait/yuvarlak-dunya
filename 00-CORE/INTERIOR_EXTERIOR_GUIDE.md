# Interior-Exterior Continuity Guide

---

## The Problem

When the camera moves from outside a house to inside, AI video generation often:

- Regenerates the interior from scratch
- Changes proportions (walls, furniture, ceiling height)
- Changes lighting (from daylight to artificial)
- Creates a different "feel" than the exterior
- Loses the sense of being in the same world

**The result:** The interior feels like a different location, breaking immersion.

---

## The Solution

The exterior and interior must be treated as **one continuous environment**, not two separate scenes.

### Rule 1: One World, Two Views

```
EXTERIOR ← same world → INTERIOR

The interior is simply a different view of the same world.
It is NOT a new environment.
It is NOT a new scene.
It is the SAME space, seen from inside.
```

### Rule 2: Consistent Visual Language

| Element | Exterior | Interior | Must Match |
|---------|----------|----------|------------|
| Wall colour | Coral pink | Coral pink | ✅ Same |
| Door style | Round, white | Round, white | ✅ Same |
| Window style | Round, white frame | Round, white frame | ✅ Same |
| Floor material | Soft, rounded | Soft, rounded | ✅ Same |
| Lighting tone | Warm daylight | Warm daylight | ✅ Same |
| Proportions | Child-scale | Child-scale | ✅ Same |

### Rule 3: Transition Frame

The transition from exterior to interior should use a **single continuous shot** or a **matched cut**:

**Option A: Continuous Shot (Preferred)**
```
Camera follows Kiko through the door.
Same shot, same lighting, same proportions.
No cut. No regeneration.
```

**Option B: Matched Cut**
```
Shot 01: Exterior — Kiko approaches door
Shot 02: Interior — Kiko is already inside, same lighting, same proportions

The cut must be invisible.
The interior must look like it belongs to the same house.
```

---

## Production Rules for Interior-Exterior

### Before Generating

1. **Load BOTH references:**
   - Exterior world reference
   - Interior world reference

2. **Ensure visual consistency:**
   - Same colour palette
   - Same lighting tone
   - Same proportion scale
   - Same material style

3. **Write the prompt to connect them:**
   ```
   Remain inside the same house.
   The interior matches the exterior in colour, lighting, and proportions.
   Do not redesign the interior.
   ```

### During Generation

4. **Use continuity reference:**
   - If transitioning from exterior, use the exterior frame as reference
   - The interior must feel like a natural continuation

5. **Lock the world:**
   ```
   The interior is part of the same established world.
   Do not create a new environment.
   Do not change the lighting.
   Do not change the proportions.
   ```

### After Generating

6. **Verify consistency:**
   - Does the interior match the exterior's colour palette?
   - Does the lighting feel continuous?
   - Do the proportions match?
   - Does it feel like the same house?

---

## Prompt Template for Interior Shots

```text
Continue from the exterior shot.

Remain inside the same house.

The interior matches the exterior in:
- colour palette
- lighting tone
- proportion scale
- material style

Do not redesign the interior.
Do not create a new environment.
Do not change the lighting.
Do not change the proportions.

The interior should feel like a natural continuation of the exterior.
It is the SAME space, seen from inside.

Preserve:
- wall colours
- door style
- window style
- floor material
- furniture proportions
- lighting warmth

No other characters.
{style} {camera} {lighting}

Do not display dialogue as on-screen text.
No speech bubbles.
No captions.
No subtitles.
No text.
```

---

## Common Mistakes

| Mistake | Why It Happens | Fix |
|---------|---------------|-----|
| Interior looks different | AI regenerates from scratch | Use continuity reference |
| Lighting changes | No lighting lock | Add lighting lock |
| Proportions change | No scale reference | Add proportion lock |
| Feels like a new room | No world connection | State "same house" |
| Furniture moves | No layout lock | Add furniture positions |

---

## Example: Kiko's Home

### Exterior Shot
```
Kiko stands in front of her coral-pink round house.
Garden path, flowers, soft grass, rounded fence.
Warm morning light.
```

### Interior Shot (Transition)
```
Continue from the exterior.
Remain inside the same house.
The interior matches the coral-pink exterior.
Same warm lighting.
Same child-scale proportions.
Round furniture, soft colours, cozy atmosphere.
Do not redesign the interior.
Do not create a new environment.
```

---

## Checklist for Interior-Exterior Shots

- [ ] Both exterior and interior references loaded
- [ ] Colour palette matches
- [ ] Lighting tone matches
- [ ] Proportions match
- [ ] Material style matches
- [ ] Prompt states "same house"
- [ ] Prompt locks interior design
- [ ] No new environment created
- [ ] Continuity frame used (if transitioning)

---

*This guide ensures interior-exterior transitions feel like one continuous world.*
*Last updated: 3 Temmuz 2026*
