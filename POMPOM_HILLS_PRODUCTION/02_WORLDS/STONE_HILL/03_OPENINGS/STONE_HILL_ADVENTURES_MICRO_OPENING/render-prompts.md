# Stone Hill Adventures — Micro-Opening Render Prompts v1.2

> OpenArt render prompt'ları, Stone Hill world micro-opening için.
> Bir kez üretilir, Stone Hill'de geçen 90-120 sn'lik bölümlerde tekrar kullanılır.
> Spesifikasyon: `opening-stone-hill-adventures.md`.
> Kurallar: `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B,
> `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9c, `00-CORE/17_VIDEO_GENERATION_STANDARD.md` §Text Safety.
>
> World-specific: Stone Hill'in kendi world identity'sini gösterir (yer-nötr DEĞİL — Opa's
> Storytime bumper'ının tersine, bu sadece Stone Hill bölümlerinde kullanılır).
> Karakter yoktur — bkz. `MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B "no characters by default".
> `{style} {camera} {lighting}` değişkenleri `00-CORE/VARIABLES.md`'den çözülür.
>
> Kapanış eşleniği yok — normal Stone Hill bölümleri kendi final shot'unda kapanır
> (bkz. `MICRO_OPENING_AND_CLOSING_STANDARD.md` §3).

---

## World Micro-Opening (3–4 sn)

Two valid production workflows are documented below. See `opening-stone-hill-adventures.md`
§ Production Workflow for when to use each. **Shot-first (Option B) is the preferred
practical default** when OpenArt video/shot generation is available.

### Option A — Still-First Workflow

#### Frame / Still (image)

```text
Calm empty establishing view of Stone Hill in Pompom Hills, rounded stone discovery area, smooth round toy-like stones in warm grey with soft pastel pink and lavender accents, soft pebble path, warm moss patches, small grass tufts, gentle slope, child-safe rounded rock clusters, peaceful and tactile, warm morning daylight, no characters, {style} {camera} {lighting}

Do not display any on-screen text. No title card. No logo. No speech bubbles. No captions. No subtitles. No text.
```

#### Video (3–4 sn) using @image1

```text
Use the Stone Hill micro-opening still (@image1) as frame zero. A single, very slow establishing camera glide or soft push-in drifts gently over the rounded stone clusters and pebble path. Small grass and moss tufts move very slightly in a soft breeze. No characters appear. No reveal, no action — just a calm tactile atmosphere.

Camera: gentle glide or extremely slow push-in, child-eye-level, 28-35mm, no fast zoom, no shake, no whip pan.
Duration feel: 3–4 seconds, final frame should visually connect into the episode's own Shot 01 (same Stone Hill set, same warm morning daylight, same warm morning Stone Hill colour identity).

No readable text anywhere in the frame. No title card. No logo animation.
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles.
```

### Option B — Shot-First Workflow

Generate the 3–4 second opening shot directly, without a separate still-approval step first.

> **v1.2 fix:** an earlier OpenArt generation attempt from this prompt produced a
> building/house/cave-like hill with a door, roof, bench and waterfall. The prompt below
> was tightened to explicitly rule out constructed structures and water features, since
> Stone Hill Adventures must remain an empty natural rounded-stone discovery area only.

```text
Create a 3–4 second Stone Hill Adventures micro-opening for Pompom Hills.

Empty natural Stone Hill discovery area only.

Show a calm preschool-safe Stone Hill environment with smooth rounded toy-like stones, a soft pebble path, warm moss patches, small grass tufts, a gentle slope and warm morning daylight.

The scene should feel peaceful, tactile, safe and curious.

No characters appear.

A single very slow camera glide or soft push-in moves gently over the rounded stones and pebble path. Small grass and moss tufts move very slightly in a soft breeze.

No reveal. No story action. No building. No house. No door. No roof. No bench. No cave. No waterfall. No tower. No entrance. No signs. No readable text. No logo. No characters. No animals. No modern objects. No sharp rocks. No cliffs.

Camera: gentle glide or extremely slow push-in, child-eye-level, 28–35mm, no fast zoom, no shake, no whip pan.

Duration: 3–4 seconds.

The final frame should visually connect into the episode's own Shot 01: same natural Stone Hill discovery area, same warm morning daylight, same warm morning Stone Hill colour identity.

Do not display any readable text anywhere in the frame. No title card. No logo. No speech bubbles. No captions. No subtitles. No text.
```

Use the same Negative Prompt (below) for Option B as for Option A.

### Sound (applies to both options)

- A soft warm 3–4 second music motif: gentle marimba or rounded wooden tones, one tiny
  pebble-like chime, layered under very light ambient wind and soft distant birdsong.
- Music sits low under the ambience (music ≈ -12 dB, ambience ≈ -18 dB per
  `00-CORE/AUDIO_GUIDE.md` § Ses Seviyesi Kuralları). Non-vocal, simple, repeatable.
- No loud jingle, no logo sting, no fast whoosh, no drums, no lyrics, no spoken branding.

---

## Approval Checklist

**Accept if:**

- Stone Hill identity is clear.
- Rounded toy-like stones are visible.
- Pebble path is visible.
- Warm moss and small grass tufts are visible.
- Lighting is warm morning daylight.
- No characters appear.
- No readable text appears.
- No logo or title card appears.
- No caves, waterfalls, cliffs or sharp rocks appear.
- Camera movement is slow and stable.
- Final frame can cut naturally into Shot 01.

**Reject if:**

- It looks like a generic rocky field.
- It introduces characters.
- It includes readable text, logo, title or subtitle.
- It becomes dark, cinematic, sunset, moonlight or cave-like.
- It adds waterfall/cave imagery.
- It has fast zoom, shake, whip pan or action reveal.
- It cannot visually connect into a Stone Hill episode.
- It shows a house, building, door, roof, bench, cave, waterfall, tower or entrance.
- It looks like a stone house, cave home, garden house or waterfall hill.
- Stone Hill is not an empty natural rounded-stone discovery area.

---

## Saved Assets

After approval, save:

- `stone-hill-adventures-opening-video.mp4`
- `stone-hill-adventures-opening-first-frame.png`
- `stone-hill-adventures-opening-final-frame.png`

The final frame can be used to check the transition into an episode's Shot 01. The first
frame can be reused as a still reference if future regeneration is needed.

---

## Negative Prompt

```text
low quality, blurry, deformed, text, watermark, readable text, title text, logo, brand mark, subscribe button, like button, arrows, end card graphics, photorealistic, horror, scary, dark lighting, sunset, golden afternoon light, moonlight, harsh contrast, neon colours, cinematic LUT, HDR look, fast motion, flashing, loud effect, characters, extra characters, sharp-edged or jagged stones, dark or maze-like cave, generic grey rock pile, muddy or murky water, modern objects, ropes, climbing gear, cluttered background, extra objects, house, building, door, roof, bench, cave, waterfall, tower, entrance, sign, readable sign, hut, stone house, doorway, window, chimney, constructed structure, wooden structure, bridge, pond, river, stream, water feature
```

(Consistent with `00-CORE/NEGATIVE_PROMPTS.md` § Common Negative Prompt and the Stone Hill
Forbidden Clutter list in `27-stone-hill-bible.md` § Visual Richness & World Charm.)

---

## Production Notes

- Produce via Option A (still-first) or Option B (shot-first) — see above. Store the
  approved result once and reuse across all Stone Hill world-based episodes (90–120 sn
  length only — see `MICRO_OPENING_AND_CLOSING_STANDARD.md` §4).
- Do not use for Shorts. Avoid for 60-second episodes unless trimmed to 1–2 seconds.
- Keep colour identity matched to the Stone Hill palette (warm grey/pink/purple stones, soft
  green grass #C8E6C9) so the reused clip does not drift between episodes
  (`00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Colour Continuity).
- This package has no closing counterpart. Do not create a `CLOSING_BUMPER/` folder for Stone
  Hill — the final story shot of each episode serves as the closing (§3 of the global standard).
- If OpenArt adds buildings, doors, caves or waterfalls, reject the result and rerun with the
  stricter Option B prompt. Stone Hill micro-opening must remain a natural rounded-stone
  discovery area, not a home, cave, tower or waterfall location.

---

*Referans: `opening-stone-hill-adventures.md`, `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B, `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9c.*
*Versiyon: 1.2 — Tightened Option B prompt and Negative Prompt after a failed generation
produced a building/cave/waterfall hill instead of an empty natural stone discovery area.
Added house/building/cave/waterfall rejection criteria to Approval Checklist and Production
Notes. 4 Temmuz 2026*

For the approved-frame-to-video OpenArt copy/paste prompt, use:
`openart-frame-to-video-prompt.md`
