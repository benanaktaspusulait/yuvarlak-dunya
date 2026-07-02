# Pompom Hills — Production Pipeline (Gold Master)

Bu dosya, tüm sahnelerin uyması gereken **tek kaynak** production pipeline'ıdır.
OpenArt bir görsel üretici değil, **prodüksiyon motorudur**. Her sahne yalnızca mevcut,
onaylı dünyaya karakter/prop yerleştirir.

> **Sahne dosyaları için kural:** Her sahne markdown'u en üstte `Follow PRODUCTION_PIPELINE.md`
> yazar ve yalnızca **sahneye özgü** veriyi (Production Lock, koordinatlar, beat, shot plan,
> diyalog, kısa Visual Prompt, continuity) içerir. Ortak kurallar burada tutulur; sahnelerde
> tekrar edilmez.

İlişkili dosyalar: `PRODUCTION_RULES.md` (kamera/mekan/ışık/ses/zaman sürekliliği),
`NEGATIVE_PROMPTS.md` (araç bazlı negative listeleri), `VARIABLES.md` (prompt değişkenleri),
`CHARACTER_REFERENCE_GUIDE_v2.1.md` ve `WORLD_BIBLE_v2.1.md` (kilit referanslar).

---

# Production Philosophy

Pompom Hills is being developed as a long-term animation series.

The goal of the first production phase is NOT to create long episodes.

The goal is to build a professional, repeatable and reliable production pipeline.

Every 1-minute episode is considered a production experiment.

Each episode should help validate or improve one or more production rules.

Examples include:

- character consistency
- world consistency
- shot-to-shot continuity
- camera language
- prompt structure
- production documentation
- pacing
- sound design
- editing workflow
- YouTube publishing workflow

Do not introduce major workflow changes during an active episode.

Finish the episode first.

Review the completed episode.

Only then update the production pipeline.

A production rule is considered stable only after it has been successfully validated across multiple completed episodes.

---

# Phase 1 — Production Lab

Goal:

Create multiple 1-minute episodes.

The objective is to strengthen the production system rather than increase story complexity.

Keep stories intentionally simple.

Use:

- one world whenever possible
- two or three characters maximum
- one emotional idea
- one simple lesson
- four connected shots

Focus on learning every detail of the production process.

Do not rush into longer stories.

---

# Phase 2 — Stable Production

Begin only after the production pipeline has proven to be reliable.

Continue using the same production rules.

Increase production speed while maintaining quality.

---

# Phase 3 — Story Expansion

Only after the production pipeline has matured.

Expand naturally into longer stories.

Begin producing approximately 2-minute episodes.

The workflow should remain the same.

Only the storytelling becomes more complex.

Do not redesign the pipeline.

Scale the existing pipeline.

---

# Core Principle

Never scale complexity before scaling reliability.

A strong production pipeline is more valuable than a long episode.

Every improvement should make future episodes easier to produce.

The production system itself is the first product.

The animated episodes are built on top of that system.

---

## 1. Reference Priority

```
Character Reference
        ↓
World Reference
        ↓
Director Prompt
```

If any conflict exists, **Character Reference and World Reference always override the Director
Prompt**. OpenArt must preserve the approved production assets above any textual interpretation.

---

## 2. Character Rules

**Character Reference is ABSOLUTE. It overrides every prompt.**
If the prompt and the character reference conflict, **follow the character reference.**

Locked and identical across every scene (no redesign allowed):

- Hair
- Eyes
- Face
- Body
- Clothes
- Colors
- Scale

Character sheets live in `characters/pompom-hills/` and `characters/drawings/`.

---

## 3. World Rules / Environment Lock

**World Reference is ABSOLUTE. The prompt can never modify the world.**

- The environment is **LOCKED**. Never regenerate. Never redesign. Scenes only insert
  characters and scene props into the existing world.
- Use a **CLEAN world render only** — no titles, labels, arrows, frames or layouts.
- Never use an **Environment Sheet** as a world reference. OpenArt interprets sheets as
  physical objects and will place them inside the scene.
- Each World has its own **Hero Pack**: **Hero View · Right View · Back View · Top View**.
- Maintain identical: **layout, architecture, trees, flowers, paths, benches, lamp posts,
  lighting, landmark positions.**
- The **Giant Pompom Tree** keeps its designed pompom colors and shape — never brown, never
  redesigned.

Explicit OpenArt directives:

```
DO NOT redesign environment.
DO NOT regenerate environment.
Maintain identical layout, architecture, trees, flowers, paths, benches, lamp posts, lighting, landmark positions.
```

---

## 4. Scale Rules

- The character occupies approximately **10–12%** of the final frame.
- The environment occupies approximately **85–90%** of the composition.
- The audience should notice the **world first**, then naturally discover the character.
- Preserve realistic scale between the character and: benches, stepping stones, flowers,
  houses, lamp posts, and the Giant Pompom Tree.
- Never generate an oversized character.

---

## 5. Camera Rules

- Environment first, character second.
- Wide compositions.
- **35mm default lens.**
- Eye level.
- Large negative space.
- The world should always feel large and explorable.

---

## 6. OpenArt Rules

- OpenArt is our **production engine**, not an image generator.
- **Consistency > beauty. Production quality > speed.**
- Use the existing World. Do NOT regenerate the world. Do NOT redesign the environment.
- Only insert the scene's character(s) and the scene's props.
- Negatives: apply `NEGATIVE_PROMPTS.md`; do not duplicate its entries inside scene prompts.

---

## 7. Reject & Regenerate Rules

- If the character appears larger than **~12% of the frame** → reject and regenerate with
  stronger scale instruction (target 10–12%; environment 85–90%).
- If the **Giant Pompom Tree** changes in any way (color, shape, becomes brown) → reject.
- If **architecture** changes → reject.
- If **flowers, paths or benches** (or lamp posts, stepping stones) change → reject.
- If the **world layout** changes or the environment is regenerated → reject.
- If an **Environment Sheet appears inside the scene** → reject.
- If **random unreadable text or signs** appear → reject (accept only if tiny and unreadable
  in video).
- If the **lighting** differs from the locked warm daylight → reject.

---

## 8. Production Order

```
1. Load Character Reference
        ↓
2. Load World Reference
        ↓
3. Open Director
        ↓
4. Insert Character
        ↓
5. Generate Shot
        ↓
6. Check Reject Rules
        ↓
7. Accept
        ↓
8. Proceed to next shot
```

Artık prompt yazmıyoruz; **pipeline çalıştırıyoruz.**

---

## 9. Director Workflow (per scene)

1. Open the scene markdown; read its **Production Lock** (scene-specific character, location,
   scale, weather, frame ratio).
2. Load the locked **Character Reference** and **World Reference (Hero Pack)** for that scene.
3. Use the scene's short **Visual Prompt** only to describe the action, mood and framing.
4. Insert the character and scene props into the existing world.
5. Generate the shot, then run the **Reject & Regenerate Rules** (Section 7).
6. Accept only when scale, world, tree, architecture and lighting are preserved.
7. Proceed to the next shot / next scene.

---

## 10. How Scene Files Reference This

Every scene file:

- States `Follow PRODUCTION_PIPELINE.md` at the top.
- Contains only scene-specific data + a short scene-description Visual Prompt.
- Does **not** repeat Environment Lock, Reference Priority, Scale, Camera, OpenArt or Reject
  rules — those live here, in one authoritative place.

Change a rule once here → the whole project (all scenes, all environments, all characters)
updates consistently.

---

# Episode 1 Production Lessons

Bu bölümler, "Goodnight, Tree" (E11) bölümünün üretim sürecinde edinilen dersleri içerir.

---

## Story Structure

- Start with 1-minute episodes.
- Each episode consists of 4 shots.
- Each shot is approximately 15 seconds.
- Use only one world whenever possible.
- Prefer only 2-3 characters per episode.
- Each episode should communicate one simple emotional idea or lesson.

---

## Shot Workflow

Shot 01 is the only shot that starts from a newly created Take Shot.

Every following shot continues from the previous shot.

Never create a new Take Shot for Shot 02, Shot 03 or Shot 04.

---

## Reference Frame Rule

Do not automatically use the final frame of the previous video.

Instead, choose the frame that creates the smoothest visual continuity for the next shot.

The best continuity frame may occur before the last frame.

Always prioritize continuity over choosing the most beautiful frame.

---

## Reference Images

Each new shot uses:

- Previous shot continuity frame
- Required character references
- Existing world

Never recreate the world from scratch.

---

## Prompt Rules

Production documents are written for humans.

Visual Prompts are written for AI.

Visual Prompts should describe only visible actions.

Do not describe spoken dialogue inside the Visual Prompt.

Dialogue belongs only inside the Dialogue section.

---

## Camera Rules

Shot 01 establishes the camera.

Subsequent shots continue naturally from the previous framing.

Avoid dramatic camera changes.

Camera movement should remain slow, calm and cinematic.

---

## Continuity Rules

Maintain:

- character appearance
- environment
- lighting
- proportions
- camera composition

Never redesign existing environments.

---

## Production Philosophy

Complete the episode before improving the pipeline.

Do not redesign the production system during an active episode.

Review the finished episode first.

Improve the pipeline only after the episode is complete.

---

## Long-term Roadmap

**Phase 1**

Create several 1-minute episodes.

Focus on production quality and workflow consistency.

**Phase 2**

Move to approximately 2-minute episodes using the same production pipeline.

Expand storytelling without changing the core workflow.

The pipeline should scale naturally from 1-minute episodes to longer stories.
