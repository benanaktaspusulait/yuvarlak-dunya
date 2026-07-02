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
The first frame of this video must match @image exactly.

Treat @image as frame zero.

The animation begins only after the first frame has matched @image exactly.
```

- [ ] Is Frame Lock included?
- [ ] Is the correct @image number used?
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
  - [ ] exposure
  - [ ] brightness
  - [ ] moonlight intensity
  - [ ] colour temperature
  - [ ] colour grading
- [ ] Does it prevent the scene becoming brighter or darker?

---

## 6. Character Check

- [ ] Are the correct characters selected in OpenArt?
- [ ] Are they already present if continuing from the previous shot?
- [ ] Does the prompt prevent character re-entry or sudden appearance?
- [ ] Are characters kept at the correct scale?

---

## 7. Text Safety Check

Every prompt must include:

```text
Do not display dialogue as on-screen text.
No speech bubbles.
No captions.
No subtitles.
No text.
```

---

## 8. Audio Check

- [ ] Do not rely on OpenArt shot music.
- [ ] Shot audio may contain ambience only.
- [ ] Episode music will be added later during editing.
- [ ] Avoid shot-level background music resets.

---

## 9. Final Go / No-Go

Before pressing Generate Video, confirm:

- [ ] Correct world
- [ ] Correct characters
- [ ] Correct @image tag
- [ ] Frame Lock included
- [ ] Lighting Lock included
- [ ] Camera Lock included
- [ ] No close-up risk
- [ ] No world redesign risk
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
*Son güncelleme: 2 Temmuz 2026*
