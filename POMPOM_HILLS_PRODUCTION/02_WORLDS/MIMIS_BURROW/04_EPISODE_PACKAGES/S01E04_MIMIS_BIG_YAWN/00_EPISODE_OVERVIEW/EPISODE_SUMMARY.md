# S01E04 — Mimi's Big Yawn (Mimi's Burrow Version)

## Episode Concept
Mimi feels sleepy but can't find the perfect spot to nap. Kiko helps her try a few spots outside, but none are cozy enough. Then Kiko notices the warm glow of Mimi's own burrow — the coziest place of all is home. They go inside, and Mimi falls peacefully asleep on her soft pillow.

## Structure (8-shot, 120 seconds)
Redesigned for production safety (frame-supported action only) while keeping full episode length. Two master setup frames anchor the whole episode: an EXTERIOR master (Shot 01) and an INTERIOR master (Shot 05, via the canonical entrance crossing).

### EXTERIOR — Shot 01 is the master setup

#### Shot 01 — Mimi Yawns Near Her Burrow (15s) — EXTERIOR MASTER SETUP
- **Location:** Outside Mimi's Burrow entrance
- **Seeds ALL exterior objects:**
  - Mimi's Burrow entrance (round blue frame, warm glow — the eventual destination)
  - Exactly three grey stepping stones
  - Small flower patch nearby (tried in Shot 02)
  - Soft tree with grass area under it (tried in Shot 03)
  - Flowers on top of the entrance mound
  - Evening dusk sky (soft golden light, no stars)
- **Action:** Mimi yawns hugely, Kiko notices with concern

#### Shot 02 — Try the Flower Patch (15s)
- **Action:** Mimi tries the flower patch (seeded in Shot 01); flowers tickle her
- **Result:** Not comfortable, she gets up

#### Shot 03 — Try the Grass Under the Tree (15s)
- **Action:** Mimi tries the soft grass under the tree (seeded in Shot 01); too breezy/exposed
- **Result:** Soft but not cozy enough; Kiko wonders where is warm and cozy

#### Shot 04 — Kiko Points to the Cozy Doorway (15s)
- **Action:** Kiko notices the warm glow of the burrow entrance (seeded in Shot 01) and points; Mimi realizes home is the coziest spot
- **Result:** Both turn toward the entrance, ready to go inside (no crossing yet)

### TRANSITION → INTERIOR

#### Shot 05 — Stepping Inside (15s) — PLANNED ENTRANCE CROSSING → INTERIOR MASTER SETUP
- **Action:** The ONE planned camera move — a slow, calm push through the round blue entrance into the interior (canonical crossing per world spec)
- **Seeds ALL interior objects:** warm blue walls, green carpet, round blue pillow, small window, mini white shelf with books, orange carrot box, warm golden glow
- **Result:** Settled interior final frame becomes the @image1 for Shots 06–08

### INTERIOR — Shot 05 final frame is the master

#### Shot 06 — The Cozy Pillow (15s)
- **Action:** Mimi moves to her round blue pillow (seeded in Shot 05), feels how soft and warm it is
- **Result:** The cozy spot she needed — her own pillow

#### Shot 07 — Settling Down (15s)
- **Action:** Mimi lies down fully; Kiko gently helps her settle (small sleepy yawn callback)
- **Result:** Nearly asleep, warm and safe

#### Shot 08 — Goodnight (15s)
- **Action:** Mimi fully asleep on her pillow; Kiko whispers goodnight
- **Ending:** Peaceful bedtime; warm interior glow held (no night/stars)

## Production Safety Notes

### Frame-Supported Action (Hard Gate — §0, §2 of Preflight System)
Every shot only interacts with objects visible in its @image1:
- **Exterior objects** (entrance, stones, flower patch, tree, grass, glow) are all seeded in Shot 01.
- **Interior objects** (pillow, window, shelf, carrot box, walls, carpet) are all seeded in Shot 05.
- No shot asks for an object that is not already visible or seeded → no object spawning.

### Critical Changes from Original 8-shot Version:
1. **Location moved** Flower Hill → Mimi's Burrow (better fits the sleep theme)
2. **Stream removed** (high risk: water motion, sound, landmark spawning)
3. **Bench removed** (unnecessary, was not seeded)
4. **Two master setups** instead of relying on the model to invent spaces
5. **Only one planned camera move** (the canonical entrance crossing in Shot 05); all other shots static
6. **Consistent lighting** (evening dusk outside; warm interior glow inside — no sudden night/stars)
7. **Final sleeping spot is the canonical interior pillow**, not an invented outdoor leaf blanket

### OpenArt Safety Rules Applied:
1. **@image1 continuity:** exterior chain (Shots 01–04) + interior chain (Shots 06–08), bridged by the planned crossing (Shot 05)
2. **No unplanned camera movement:** only the Shot 05 threshold crossing, then static
3. **Object seeding:** all interaction objects visible in a master setup frame before use
4. **Lighting consistency:** dusk outside, warm glow inside; no lighting jump
5. **Character limits:** only Kiko and Mimi, simple interactions
6. **No complex audio:** natural ambience only, no music/melody

## Characters
- **Mimi:** Sleepy, gentle, needs help finding comfort
- **Kiko:** Observant, helpful, caring friend

## World Alignment
Uses the **Mimi's Burrow World Specification** (exterior + interior):
- Round blue entrance (#90CAF9), warm interior glow, exactly 3 stepping stones
- Interior: warm blue walls, green carpet, round blue pillow, window, shelf, carrot box
- Mimi-sized scale, soft cozy atmosphere, preschool-safe toy-set world
- Canonical Exterior → Entrance → Interior navigation (crossing not skipped)

## Staged Production Gates (DO NOT generate all 8 shots at once)

This episode is production-ready **only as a staged sequence**. Shot 01 and Shot 05 are the two production gates — if either fails, the rest of the episode collapses even with good prompts.

**Gate A — Exterior master setup (Shot 01 only)**
Generate ONLY Shot 01 first. Approve before anything else. Approve criteria:
- Mimi's Burrow entrance clear (round blue frame, warm glow)
- Exactly 3 stepping stones
- Flower patch visible
- Soft tree + grass area visible
- Mimi sleepy, Kiko concerned
- No stars / no night (evening dusk)
- Entrance still the main landmark, not cluttered/hidden
- After approving, check: are the flower patch and tree close enough that Mimi can reach them with a small move inside a STATIC frame? If not, fix Shot 01 setup — not the Shot 02/03 prompts.

**Gate B — Exterior mini arc (Shots 02 → 03 → 04)**
Only after Shot 01 is approved. For each shot, before moving on, ask: is the next shot's required object still visible and usable in this final frame?

**Gate C — Interior crossing (Shot 05) — highest risk**
Do NOT generate Shot 05 blindly. First approve Shot 04's final frame. Then prepare/approve a **Mimi's Burrow Interior reference** and use it as `@image2` (interior canon only). Reject Shot 05 if any MUST-HAVE (pillow, walls, carpet, warm glow) is missing.

**Gate D — Interior ending (Shots 06 → 07 → 08)**
Relatively easy once Shot 05's interior final frame is correct.

## Episode Metadata
- **Duration:** 8 shots × 15s = 120 seconds
- **Target Audience:** 3-4 year olds
- **Educational Focus:** Recognizing sleepiness, friendship, comfort, "home is cozy"
- **Emotional Arc:** Problem (sleepy) → Search outside (fails) → Realization (home) → Solution (own pillow) → Resolution (peaceful sleep)
- **Production risk:** Medium — main blockers are Shot 01 setup quality + Shot 05 interior crossing
- **Recommended workflow:** Staged production (Gates A–D), not all at once
