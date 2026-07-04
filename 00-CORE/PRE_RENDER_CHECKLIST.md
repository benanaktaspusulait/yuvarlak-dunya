# Pre-Render Checklist — PomPom Hills

---

> **Every render costs credits. Never render before passing the checklist.**

---

## 1. Reference Image Check

- [ ] Is the correct continuity frame uploaded?
- [ ] Is the correct image tag used in the prompt? Example: @image1 or @image2
- [ ] Does the prompt match the actual image tag shown in OpenArt?
- [ ] Is the continuity frame the best transition frame, not just the final frame?
- [ ] Does the frame show the correct characters?
- [ ] Does the frame show enough of the world for continuity?

---

## 2. Frame Lock Check

Every continuation shot must include:

```text
Treat @image1 as the complete visual master reference.
Preserve not only framing, but also colour identity, lighting identity, exposure, white balance, atmosphere, environment identity, character proportions, and character performance.
The viewer must not perceive a shot boundary.

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
- [ ] Frame Lock included
- [ ] First visible frame must be visually indistinguishable from @image1
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
