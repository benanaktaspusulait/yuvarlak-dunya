# Standalone Shot + In-File Post-Production Transition Standard

> This is a global production standard. It applies to **every multi-shot Pompom Hills video**,
> especially when shots are generated separately in different worlds and later edited together.
> It is not tied to one episode.
>
> This document does NOT rewrite existing stories, does NOT change character canon
> (`00-CORE/CHARACTER_GUIDE.md`, `01-CHARACTERS/*`), does NOT change world canon
> (`00-CORE/WORLD_BIBLE.md`, `POMPOM_HILLS_PRODUCTION/02_WORLDS/*`), does NOT add new
> transition scenes, and does NOT ask OpenArt to generate transitions.
>
> It builds on top of `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHOT_CONTINUITY_WORKFLOW.md`
> (the `@image1` shot-to-shot chain and Transition QA) and `00-CORE/17_VIDEO_GENERATION_STANDARD.md`
> (Text Safety, Hard Background Lock). Where the continuity workflow governs shots inside the
> same world/episode, this standard governs how any multi-shot video — including videos that
> move between different worlds — keeps every shot clean and standalone while all transitions
> are handled later in editing.

---

## 1. Purpose

Pompom Hills videos are often created as separate OpenArt shots and then combined in editing.
When a video moves between different worlds, hard cuts can feel abrupt.

However, asking OpenArt to generate transitions between worlds is dangerous because it can
cause:

- world mixing
- location drift
- surprise objects
- surprise characters
- camera reveal errors
- collage-like backgrounds
- wrong lighting
- continuity confusion

Therefore, every shot must be generated as a clean standalone shot, and all transition
instructions must be handled as post-production notes inside the shot file.

---

## 2. Core Rule

Each shot file must contain both:

- OpenArt generation instructions
- Production / editing instructions

But these must be clearly separated.

OpenArt must generate only the current shot.

OpenArt must NOT generate:

- transitions
- crossfades
- cream dips
- fades
- dissolves
- wipes
- moving between worlds
- travel shots
- camera transitions from one location to another
- split-screen transitions
- portals
- magical transition effects
- transition cards
- text overlays
- logos

World changes are handled later in editing.

---

## 3. Required Section: OpenArt vs Edit Instruction Boundary

Every multi-shot file must include this section near the top, after Scene Context:

```markdown
## OpenArt vs Edit Instruction Boundary

This file contains both OpenArt generation instructions and production/editing notes.

When generating the video in OpenArt, use only:
- Visual Prompt
- Camera Direction
- Dialogue
- Natural Character Motion Rule
- Lighting
- Negative Prompt

Do NOT paste production/editing sections into OpenArt.

The following sections are for production review and editing only:
- First-Frame Generation Gate
- No Salvage Before Output Rule
- Edit-Safe Opening and Ending Rule
- Post-Production Transition Note
- QA Checklist
- Final Internal Consistency QA

OpenArt must generate only this single standalone shot.

Transitions between worlds are handled later in editing, not inside OpenArt.
```

---

## 4. Required Section: Edit-Safe Opening and Ending Rule

Every shot in a multi-shot video must include:

```markdown
## Edit-Safe Opening and Ending Rule

This shot will be edited together with other separately generated shots.

The first 0.5 seconds must be visually stable:
- no sudden character movement
- no new gesture starting immediately
- no camera movement
- no character entering
- no object appearing
- location already clear from the first frame

The final 0.5 seconds must be a calm edit-safe hold:
- no new gesture starts
- no character changes position
- no object appears
- no camera movement
- no abrupt expression change
- no sudden lighting change

This allows a soft 0.4–0.6 second transition in editing.
```

For a final shot, replace the final 0.5 seconds hold with an end-screen-safe hold:

```markdown
The final 3 seconds must be a calm end-screen-safe hold:
- no new gesture starts
- no character changes position
- no object appears
- no camera movement
- no abrupt expression change
- no sudden lighting change
```

---

## 5. Required Section: Post-Production Transition Note

Every shot **except the final shot** must include a Post-Production Transition Note.

This note must describe how the shot should transition into the next shot during editing.
It must be inside the shot file.

Do NOT create a separate transition plan unless the user specifically asks for one.

Template:

```markdown
## Post-Production Transition Note

This shot ends at [CURRENT LOCATION] and transitions to the next shot at [NEXT LOCATION].

Recommended edit transition after this shot:
- warm cream dip or soft crossfade
- 0.4–0.6 seconds
- no text
- no logo
- no sparkle
- no magical effect
- no wipe
- no camera zoom

Audio:
- gently crossfade current ambience into next-shot ambience
- no music
- no chime
- no whoosh
- no hard audio cut

Important:
This transition is done in editing only.
Do not ask OpenArt to generate the transition.
Do not include transition wording inside the OpenArt Visual Prompt.
```

For **same-location** transitions, prefer:

```markdown
Recommended edit transition after this shot:
- very soft crossfade
- 0.3–0.5 seconds
- no dramatic transition
```

For **different-world** transitions, prefer:

```markdown
Recommended edit transition after this shot:
- warm cream dip
- 0.4–0.6 seconds
```

---

## 6. Required Section: Final Shot Post-Production Ending Note

The final shot must include:

```markdown
## Post-Production Transition Note

This is the final shot of the video.

Recommended ending:
- hold the final 3 seconds as a calm end-screen-safe tableau
- no abrupt cut
- no sudden fade during dialogue
- optional very soft fade out after the final hold
- no text unless added later as platform-specific end-screen graphics
- no logo inside the generated video
- no music

Audio:
- keep natural ambience soft and steady
- optional gentle ambience fade out at the very end
- no musical sting
- no chime
- no whoosh

Important:
This ending is handled in editing only.
Do not ask OpenArt to generate end-screen graphics, text, logos, fade-outs, or transitions.
```

---

## 7. Visual Prompt Restriction

Inside the Visual Prompt text block, never include:

- transition
- crossfade
- cream dip
- edit
- editing
- next shot
- previous shot
- cut to
- fade
- dissolve
- montage

These words may appear only in:

- Edit-Safe Opening and Ending Rule
- Post-Production Transition Note
- QA Checklist
- production/editing notes

They must never appear in OpenArt-facing Visual Prompt text.

This is consistent with the Text Safety rule in `00-CORE/17_VIDEO_GENERATION_STANDARD.md`:
OpenArt is never asked to render text, logos, or transition effects inside the generated video.

---

## 8. OpenArt Prompt Extraction Rule

When preparing the final OpenArt prompt, use only:

- Visual Prompt
- Camera Direction
- Dialogue
- Natural Character Motion Rule
- Lighting
- Negative Prompt

Do NOT paste these into OpenArt:

- OpenArt vs Edit Instruction Boundary
- First-Frame Generation Gate
- No Salvage Before Output Rule
- Edit-Safe Opening and Ending Rule
- Post-Production Transition Note
- QA Checklist
- Final Internal Consistency QA
- Fallback Plan
- Any instruction mentioning crossfade, cream dip, transition, next shot, previous shot,
  montage, cut, dissolve, or moving between worlds

These are production/editing instructions only.

---

## 9. Required QA Additions

Every multi-shot shot file must add these QA checklist items:

```markdown
- [ ] First 0.5s is stable and edit-safe
- [ ] Final 0.5s is calm and transition-safe
- [ ] No new action begins in the final 0.5s
- [ ] Post-production transition note is present
- [ ] Transition instructions are not inside the OpenArt Visual Prompt
```

For final shots:

```markdown
- [ ] First 0.5s is stable with all approved characters visible
- [ ] Final 3s is calm and end-screen-safe
- [ ] Post-production ending note is present
- [ ] Ending/edit instructions are not inside the OpenArt Visual Prompt
```

---

## 10. Final Production Reminder

Every shot file must end with:

```markdown
## Final Production Reminder

This shot is generated as a clean standalone OpenArt video.
Do not generate transitions inside OpenArt.
Do not combine this world with the previous or next world.
Do not paste editing notes into OpenArt.
World changes are handled later in editing using the Post-Production Transition Note.
```

For final shots:

```markdown
## Final Production Reminder

This shot is generated as a clean standalone OpenArt video.
Do not generate endings, text, logos, or transitions inside OpenArt.
Do not paste editing notes into OpenArt.
Final hold and any fade-out are handled later in editing using the Post-Production Transition Note.
```

---

## 11. Practical Example

If a video goes:

```text
Central Square → Mimi's Burrow → Central Square → Opa's Tree → Central Square
```

Do not ask OpenArt to show the travel between these places.

Instead:

- generate each shot cleanly in its own locked location
- hold the first and final 0.5 seconds stable
- use warm cream dip / soft crossfade in editing
- crossfade ambience naturally
- never add text, logos, magical wipes, portals, or transition effects inside OpenArt

---

## 12. Final Rule Summary

For all future Pompom Hills multi-shot productions:

- Every shot is generated standalone.
- Every world transition is edited later.
- Every shot file contains its own post-production transition note.
- No separate transition plan is required unless specifically requested.
- OpenArt never receives transition/editing instructions.

---

*This document is the single source of truth for standalone-shot generation and in-file
post-production transition notes across multi-shot Pompom Hills videos, including videos that
move between different worlds.*
*It complements `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHOT_CONTINUITY_WORKFLOW.md` (the
`@image1` continuity chain and Transition QA) and does not override it.*
*Version: 1.0 — 5 Temmuz 2026*
