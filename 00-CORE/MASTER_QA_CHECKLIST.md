# Master QA Checklist — Pompom Hills

> This checklist runs once before any video is published.
> It covers all layers: world, character, colour, voice, dialogue, animation, and continuity.
> Scene-level QA (`SCENE_QA_CHECKLIST.md`) runs per shot during production.
> This checklist runs on the assembled episode before publish.

---

## When to Run

- After all shots are assembled and synced
- After voice is mixed
- After any revision that touched more than one shot
- Before uploading to YouTube or any platform

---

## QA Priority Order

Run the assembled episode QA in this order:

1. Voice continuity
2. Colour continuity
3. Lighting continuity
4. Intra-shot character continuity
5. Hard background / object identity continuity
6. Character continuity
7. World continuity
8. Story and tempo

If voice, colour or lighting continuity fails, the episode is not production-ready.

Reference: `00-CORE/SHOT_PRODUCTION_STANDARD.md`

---

## 1. World Identity

```
✓ Every shot in this episode uses the correct canonical world?
✓ World silhouette / shape is identical across all shots?
✓ No shot contains a redesigned or regenerated environment?
✓ No modern objects (buildings, roads, fences) anywhere in any frame?
✓ World Asset IDs from ASSET_REGISTRY.md used — no ad-hoc elements?
✓ Locked world elements unchanged from first to last shot?
✓ If this world has sub-zones (e.g. Flower Hill — Nature Field Zone / Home
  Cluster Zone), every shot declares the correct zone, not just the world
  name, and the zone is used consistently within each scene?
```

Reference: `POMPOM_HILLS_PRODUCTION/02_WORLDS/[world]/[world]-bible.md`

---

## 2. Character Identity

```
✓ Character colours unchanged across all shots?
✓ Character proportions consistent — no size fluctuation?
✓ Character outfit unchanged — no colour drift or detail change?
✓ Character facial features consistent — eyes, hair, expression style?
✓ No unexpected character appearing or disappearing mid-episode?
✓ Maximum 3 characters in any single frame?
```

Reference: `01-CHARACTERS/`, `00-CORE/CHARACTER_GUIDE.md`

---

## 3. Colour Identity

```
✓ White balance consistent across all shots — no warm/cool drift?
✓ Exposure consistent — no brightening or darkening between shots?
✓ Colour temperature consistent — no warmer/cooler shot drift?
✓ Saturation consistent — no vivid outlier shots?
✓ Contrast consistent — no HDR or cinematic look in any shot?
✓ Brightness consistent — no perceived brightness jump?
✓ Pastel palette preserved — no neon or oversaturated element?
✓ No cool shift / warm shift / green tint / magenta tint / orange grading in any shot?
✓ Grass colour within canonical range for this world?
✓ Sky colour within canonical range for this world?
✓ Episode reads as one continuous colour-graded film, not a collection of separately generated shots?
```

Reference: `00-CORE/VISUAL_STYLE_GUIDE.md`, world's Colour Identity section

---

## 4. Lighting Identity

```
✓ Light direction consistent — same angle across all shots in a scene?
✓ Light intensity consistent — no sudden brighter/dimmer shot?
✓ Shadow softness consistent — no hard-shadow outlier?
✓ Ambient lighting consistent — no fill-light jump?
✓ Highlight behaviour consistent — no glossy or sparkly outlier?
✓ No hard shadows or dramatic contrast in any shot?
✓ Shadow side of all characters lifted — no pure darkness?
✓ Time of day consistent within each scene?
✓ If morning scene: warm golden light throughout?
✓ If night scene: soft moonlight, never pure black?
✓ Cloud shadows not cast on ground (Cloud Hill rule)?
```

Reference: `00-CORE/VISUAL_STYLE_GUIDE.md`, world's Lighting Identity section

---

## 5. Camera Identity

```
✓ No forbidden camera movements (fast pan, shake, zoom, 360°)?
✓ Camera height consistent with world standard (0.75–0.80 m default)?
✓ Sky visible behind characters in all shots for sky-dominant worlds?
✓ No close-ups that cut off the world entirely?
✓ Scene opens with environment shot before character in first appearance?
✓ Scene closes wider than it began?
✓ No abrupt mid-scene lens change?
```

Reference: `00-CORE/VISUAL_STYLE_GUIDE.md`, world's Camera Identity section

---

## 6. Voice Identity

```
✓ Character voice consistent across all speaking shots?
✓ Same pitch, timbre, and speaking speed throughout?
✓ Same emotional warmth and preschool narration style?
✓ Same pronunciation and accent throughout?
✓ Same recording quality throughout?
✓ Speaking shots sound like the same recording session?
✓ No alternate narrator or different voice appearing in any shot?
✓ Voice volume consistent — no sudden loud or quiet shot?
```

Reference: `00-CORE/AUDIO_GUIDE.md`

---

## 7. Dialogue

```
✓ No dialogue repeated from a previous shot?
✓ No dialogue line contradicted by another shot in the same episode?
✓ Silent shots confirmed silent — no accidental voice line?
✓ Dialogue pacing appropriate — never cut during a spoken line?
✓ Minimum 1 second silence between dialogue lines?
✓ Silence at emotional peaks — not filled with unnecessary dialogue?
```

Reference: `00-CORE/CONTINUITY_RULES.md`

---

## 8. Animation and Motion

```
✓ No sudden or fast movements in any shot?
✓ Grass movement (if animated) consistent with world's wind rules?
✓ Cloud movement (if animated) left-to-right, slow and continuous?
✓ Character idle animations present — characters never fully frozen?
✓ Environmental rhythm consistent — all moving elements on same pace?
✓ No handheld shake or bounce in any shot?
✓ No character disappears or reappears inside the same shot?
✓ No character teleports, regenerates after occlusion, duplicates, or switches sides suddenly?
✓ Every character movement path is continuously readable and physically possible?
✓ No character walks through bushes, planters, flowerbeds, benches, tree trunks, walls or houses?
✓ No full-body occlusion is used as a transition?
✓ Camera movement never hides a character and reveals them elsewhere?
```

Reference: world's Video Generation Rules section

---

## 8B. Pointing, Gaze and Orientation Toward Target

> For every shot that includes pointing, showing, noticing, or directing attention.
> Ref: `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md` §17.

```
✓ Is the intended target clearly defined in the shot document?
✓ Is the target actually visible in frame, if visibility is required?
✓ Does the pointing hand/finger aim toward that target?
✓ Do the pointer's eyes and head also face the same target?
✓ Do the pointer's shoulders and torso also face the same target?
✓ Does the reacting character also reorient (head, eyes, body) toward the same target?
✓ In the final beat, do both characters clearly read as facing the target?
✓ Is neither character pointing/looking at empty space or a wrong off-screen area?
✓ No mismatched orientation (pointing one way while looking/facing another)?
```

If any answer is no, regenerate before approval.

---

## 9. Continuity Between Shots

```
✓ Character position flows naturally between consecutive shots?
✓ Character eyeline direction consistent across shots?
✓ No object appearing or disappearing between shots without story reason?
✓ World layout identical in all shots set in the same location?
✓ Lighting direction identical across shots in the same scene?
✓ No "reset" — world never returns to a differently composed version of itself?
✓ Previous shot final frame and next shot first frame match for all continuity-linked shots?
✓ First 1 second of each continuity-linked shot holds extremely close to @image1?
✓ No visible object changes position, scale, identity or side of frame between linked shots?
✓ Bench/planter/bush/tree/path/house/landmark identities remain stable?
```

Reference: `00-CORE/CONTINUITY_RULES.md`

---

## 9B. Global OpenArt Continuity Locks

```
✓ Hard Background Lock passed?
✓ Intra-Shot Character Continuity Lock passed?
✓ Single Visible Path Rule passed?
✓ Occlusion Is Not A Transition passed?
✓ Camera Must Not Break Continuity passed?
✓ First Second Continuity Hold passed?
✓ Object Identity Lock passed?
✓ Shots with unnecessary walking flagged as higher risk and simplified when needed?
✓ Full video watched once for character continuity?
✓ Full video watched once for background object stability?
```

Reject the episode if any generated shot has intra-shot disappearance, teleporting,
occlusion transition, character regeneration, path break, object morphing, background
layout change, camera reset, unexpected lighting/colour drift, extra characters, or
unauthorized text/logo/caption/title/end-card graphics.

Reference: `00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Global OpenArt Continuity Locks
and `11-DOCS/16_VIDEO_QA_SPEC.md` § Global OpenArt Continuity Gate.

---

## 10. Child Safety

```
✓ No sharp edges, dark shadows, or scary elements in any frame?
✓ No threatening imagery — weather, characters, or sound?
✓ No text burned into any frame (subtitles must be separate track)?
✓ No neon colours or high-contrast frames?
✓ All characters express only positive or gently curious emotions?
✓ No violence, conflict, or distressing content in any shot?
```

Reference: `00-CORE/CHILD_SAFETY_RULES.md`

---

## 11. Audio Mix

```
✓ Ambience level at 20–25% — dialogue always audible above ambience?
✓ No forbidden sounds (traffic, machinery, crowd, thunder, insects)?
✓ Ambient sound matches the world's canonical soundscape?
✓ No abrupt audio cut between shots — smooth fade or continuous loop?
✓ Music (if present) does not overpower dialogue or ambience?
```

Reference: `00-CORE/AUDIO_GUIDE.md`, world's Environmental Sound Identity section

---

## 12. Final World Recognition Test

> Ask these questions as a viewer, not as a producer.

```
✓ Would a child recognise this world from a previous episode?
✓ Do all shots feel like they were filmed in the same place on the same day?
✓ Does the episode feel like one complete, continuous story — not a collection of prompts?
✓ Is the emotional tone consistent from first to last frame?
✓ Would this episode pass the "same world, 2 months later" test — could it air next to an older episode without jarring inconsistency?
```

---

## Sign-Off

| Layer              | Checked By | Date | Pass / Fail |
|--------------------|------------|------|:-----------:|
| World Identity     |            |      |             |
| Character Identity |            |      |             |
| Colour Identity    |            |      |             |
| Lighting Identity  |            |      |             |
| Camera Identity    |            |      |             |
| Voice Identity     |            |      |             |
| Dialogue           |            |      |             |
| Animation          |            |      |             |
| Continuity         |            |      |             |
| Child Safety       |            |      |             |
| Audio Mix          |            |      |             |
| World Recognition  |            |      |             |

**All layers must pass before publish.**

---

*Bu belge her bölüm yayınlanmadan önce çalıştırılacak master kalite kontrol listesidir.*
*Versiyon: 1.0*
*Son güncelleme: 3 Temmuz 2026*
