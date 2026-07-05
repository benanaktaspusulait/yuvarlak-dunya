# S01E08 — Building Together v2.0

> **v2.0:** Restructured from 4 shots / 60s to **8 shots / 120s** (spec `s01e08-building-together-8shot`).
> The old 4-shot version is archived in `06_ARCHIVE/OLD_4_SHOT_VERSION/`.

---

## Episode Overview

| Alan | Değer |
| --- | --- |
| Süre | 120 saniye (8 sahne × 15 sn) |
| Başlık | Building Together (alt: "We Build Together") |
| Karakterler | Noah (100), Arda (~85, biraz küçük) |
| Mekan | Central Square |
| Duygu | İş birliği + arkadaşlık + tekrar deneme |
| Tema | Birlikte inşa etmek |
| Mesaj | "Birlikte yapınca daha kolay olur; devrilirse tekrar deneriz." |

---

## Story Summary

Noah Central Square'da sekiz renkli blok bulur; Arda katılır. Şekilleri seçip kule yaparlar ama
ilk kule sallanıp devrilir. Arda biraz üzülür; Noah cesaret verir — birlikte tekrar denerler.
Yeni planla (büyük blok alta, küçük üste) ve iş birliğiyle (biri tutar, biri koyar) kuleyi
yeniden kurarlar. Bu kez ayakta kalır: "Together!"

---

## Shot Inventory (8 shots)

| # | Dosya | Beat |
|---|---|---|
| 01 | `01_SHOTS/shot-01-blocks-are-found.md` | Blocks Are Found (MASTER SETUP) |
| 02 | `01_SHOTS/shot-02-choosing-shapes.md` | Choosing Shapes |
| 03 | `01_SHOTS/shot-03-first-tower-attempt.md` | First Tower Attempt |
| 04 | `01_SHOTS/shot-04-tower-falls.md` | Tower Falls |
| 05 | `01_SHOTS/shot-05-small-feeling-beat.md` | Small Feeling Beat (NEW) |
| 06 | `01_SHOTS/shot-06-new-plan.md` | New Plan (pointing/gaze lock) |
| 07 | `01_SHOTS/shot-07-careful-together-build.md` | Careful Together Build |
| 08 | `01_SHOTS/shot-08-tower-stands.md` | Tower Stands (finale) |

Overview docs: `01-overview.md`, `02-beat-sheet.md`, `03-storyboard.md`, `04-assets.md`,
`05-camera.md`, `06-dialogues.md`, `07-sfx.md`, `08-animation-notes.md`, `09-render-prompts.md`,
`COORDINATE_MAP.md`, `EPISODE_SUMMARY.md`, `EPISODE_SUMMARY_TR.md`.

---

## Production Notes

- **Block Object Model:** 8 blocks (2 large flat + 3 medium flat/rounded + 3 small round/soft), stable colours, tower ≤ head. Only movable prop; seeded in Shot 01. Reusable Block negative-prompt block in `01-overview.md` / `09-render-prompts.md`.
- **Continuity:** Shot 01 master setup; Shots 02–08 use previous shot's final frame as `@image1`. Shot 04→05 preserves scatter positions.
- **Staged gates A–D** and per-shot SAFE/RISKY/NOT READY status — see `EPISODE_SUMMARY.md`. Do not generate all 8 at once.
- **Lighting:** warm morning throughout (no golden/sunset drift). All shots static (no pull-back).
