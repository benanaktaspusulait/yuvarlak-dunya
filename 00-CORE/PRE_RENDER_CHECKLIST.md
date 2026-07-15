# Pre-Render Checklist — PomPom Hills

---

> **Every render costs credits. Never render before passing the checklist.**

---

## 1. Reference Image Check

- [ ] Is the shot's Production Mode recorded before generation?
- [ ] Is the correct mode-approved start source uploaded (fresh canonical still or linked frame)?
- [ ] Is the correct image tag used in the prompt? Example: @image1 or @image2
- [ ] Does the prompt match the actual image tag shown in OpenArt?
- [ ] If linked, is the source the exact original generated final frame and has it passed QA?
- [ ] If fresh, was the source built from canonical World and character references?
- [ ] Does the frame show the correct characters?
- [ ] Does the frame show enough of the world for continuity?

---

## 2. Frame Lock Check

Every explicitly linked shot must include:

```text
Treat @image1 as the complete visual master reference.
Preserve not only framing, but also colour identity, lighting identity, exposure, white balance, atmosphere, environment identity, character proportions, and character performance.
For this linked shot, the viewer must not perceive a shot boundary.

The first visible frame must be visually indistinguishable from @image1.
Not similar. Not close. Identical.

Treat @image1 as frame zero.

The animation begins only after the first frame has matched @image1 perfectly.
```

- [ ] Is Frame Lock included?
- [ ] Is the correct @image number used?
- [ ] Does the prompt treat @image1 as the complete visual master reference?
- [ ] Does the prompt require the first visible frame to be visually indistinguishable from @image1?
- [ ] Does the prompt prevent camera repositioning before motion starts?
- [ ] Is the linked chain count within normal maximum 2 / exceptional maximum 3?
- [ ] If the previous linked frame degraded, was linkage rejected and a fresh reset scheduled?

---

## 3. Camera Check

- [ ] Does the shot preserve camera distance?
- [ ] Does it avoid close-up unless absolutely required?
- [ ] Does it avoid dramatic push-in or pull-back?
- [ ] Does pull-back stay inside the existing scene?
- [ ] Does the prompt say not to create a new establishing shot?

---

## 4. World Continuity Check

- [ ] Is the world name correct?
- [ ] If this world has sub-zones (e.g. Flower Hill — Nature Field Zone / Home Cluster Zone), is the correct zone specified rather than just the world name?
- [ ] Is the world treated as an established set?
- [ ] Does the prompt prevent environment redesign?
- [ ] Does it preserve major landmarks?
- [ ] For Opa's Tree, does it preserve:
  - [ ] trunk shape
  - [ ] canopy silhouette
  - [ ] platforms
  - [ ] tree house opening
  - [ ] lantern placement
  - [ ] surrounding hill

---

## 4B. Required Global QA Locks Check

Every video prompt must explicitly pass these global OpenArt continuity locks:

- [ ] Hard Background Lock
- [ ] Intra-Shot Character Continuity Lock
- [ ] Single Visible Path Rule
- [ ] Occlusion Is Not A Transition
- [ ] Camera Must Not Break Continuity
- [ ] First Second Continuity Hold for continuity-linked shots
- [ ] Object Identity Lock

Before render, confirm:

- [ ] All visible background objects keep position, scale, identity and layout.
- [ ] Characters remain continuously visible physical characters inside the same shot.
- [ ] Character path is visible frame-to-frame and physically possible.
- [ ] No character walks through bushes, planters, benches, houses, walls, dense grass or foreground plants.
- [ ] No full-body occlusion is used as a transition.
- [ ] Camera movement cannot hide a character or regenerate the environment.
- [ ] If the shot has occlusion or teleport risk, action is reduced to pointing, looking, tiny steps, small turns or shared still moments.
- [ ] Negative prompt includes the global disappearance / occlusion / object morphing terms from `00-CORE/NEGATIVE_PROMPTS.md`.

---

## 5. Lighting Check

- [ ] Does the prompt match lighting from the continuity frame?
- [ ] Does it lock:
  - [ ] light direction
  - [ ] light intensity
  - [ ] shadow softness
  - [ ] ambient lighting
  - [ ] highlight behaviour
  - [ ] cloud brightness
  - [ ] grass brightness
  - [ ] exposure
  - [ ] brightness
  - [ ] colour temperature
- [ ] Does it prevent the scene becoming brighter, darker, warmer, cooler, harsher or more cinematic?
- [ ] Does it say: "Do not reinterpret the lighting. Continue it."

---

## 6. Colour Identity Check

- [ ] Does the prompt match colour grading from the previous shot?
- [ ] Does it lock:
  - [ ] white balance
  - [ ] exposure
  - [ ] colour temperature
  - [ ] saturation
  - [ ] contrast
  - [ ] brightness
  - [ ] pastel palette
- [ ] Does it prevent cool shift and warm shift?
- [ ] Does it prevent green tint, magenta tint or orange grading?
- [ ] Does it prevent HDR look or cinematic LUT?
- [ ] Will the episode feel colour graded as one continuous film?

---

## 7. Character Check

- [ ] Are the correct characters selected in OpenArt?
- [ ] Are they already present if continuing from the previous shot?
- [ ] Does the prompt prevent character re-entry or sudden appearance?
- [ ] Are characters kept at the correct scale?

---

## 8. Text Safety Check

Every prompt must include:

```text
Do not display dialogue as on-screen text.
No speech bubbles.
No captions.
No subtitles.
No text.
```

---

## 9. Audio Check

- [ ] Do not rely on OpenArt shot music.
- [ ] Shot audio may contain ambience only.
- [ ] Episode music will be added later during editing.
- [ ] Avoid shot-level background music resets.

---

## 10. Voice Continuity Check

For every speaking shot:

- [ ] Is the same character Voice ID or voice reference selected?
- [ ] Is the previous shot audio treated as the voice reference when available?
- [ ] Does the shot include a Voice Continuity section?
- [ ] Does the prompt require the same voice identity, timbre, pitch, speaking speed, warmth and preschool energy?
- [ ] Does the prompt require the same pronunciation, accent, age impression, emotional tone and recording quality?
- [ ] Does the prompt say all speaking shots must sound as if recorded during the same recording session?
- [ ] Does it reject a different narrator or alternate voice?

---

## 11. Final Go / No-Go

Before pressing Generate Video, confirm:

- [ ] Correct world
- [ ] Correct characters
- [ ] Correct @image tag
- [ ] Production Mode matches the approved reset schedule
- [ ] Fresh shot uses canonical clean references; linked shot uses a QA-approved frame within chain limit
- [ ] Clean Start State documented
- [ ] Complete Main Action begins and finishes in this shot
- [ ] Completed End State documented
- [ ] Stable Final Anchor reserves the final 1–2 seconds
- [ ] Next-Shot Dependency documented and exact dependency justified
- [ ] Linked chain count checked; reset inserted when required
- [ ] Lighting Lock included
- [ ] Colour Identity Lock included
- [ ] Camera Lock included
- [ ] Voice Continuity checked for speaking shots
- [ ] Previous shot audio / Voice ID checked for speaking shots
- [ ] No close-up risk
- [ ] No world redesign risk
- [ ] No colour shift risk
- [ ] No voice drift risk
- [ ] No lighting reinterpretation risk
- [ ] No perceivable shot-boundary risk
- [ ] No intra-shot character disappearance risk
- [ ] No occlusion transition risk
- [ ] No character path break risk
- [ ] No background object morphing risk
- [ ] No object identity swap risk
- [ ] No text risk
- [ ] No shot-level music dependency

**If any item fails, do not render.**

**Fix the prompt first.**

---

## Core Rule

```
Every render costs credits.

Never render before passing the checklist.
```

---

*Bu belge her video üretimi öncesi zorunlu kontroldür.*
*Son güncelleme: 3 Temmuz 2026*
