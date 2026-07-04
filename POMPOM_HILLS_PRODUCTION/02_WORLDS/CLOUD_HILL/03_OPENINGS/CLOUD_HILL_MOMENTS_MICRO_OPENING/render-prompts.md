# Cloud Hill Moments — Micro-Opening Render Prompts v1.0

> OpenArt render prompt'ları, Cloud Hill world micro-opening için.
> Bir kez üretilir, Cloud Hill'de geçen 90-120 sn'lik bölümlerde tekrar kullanılır.
> Spesifikasyon: `opening-cloud-hill-moments.md`.
> Kurallar: `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B,
> `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9c, `00-CORE/17_VIDEO_GENERATION_STANDARD.md` §Text Safety.
>
> World-specific: Cloud Hill'in kendi world identity'sini gösterir (yer-nötr DEĞİL).
> Karakter yoktur — bkz. `MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B "no characters by default".
> `{style} {camera} {lighting}` değişkenleri `00-CORE/VARIABLES.md`'den çözülür.
>
> Kapanış eşleniği yok — normal Cloud Hill bölümleri kendi final shot'unda kapanır
> (bkz. `MICRO_OPENING_AND_CLOSING_STANDARD.md` §3).
>
> Referans görsel: `POMPOM_HILLS_PRODUCTION/02_WORLDS/CLOUD_HILL/01_HERO_VIEW/00-hero-view.png`
> (Canon Hero View v1, onaylı — bkz. `00-CANON/01-world-bible.md`). Bu görsel birincil referans
> olarak kullanılmalı, metin promptu yalnızca destekleyici bilgidir.

---

## World Micro-Opening (3–4 sn)

### Frame / Still (image)

```text
Wide establishing view of Cloud Hill in Pompom Hills, single smooth dome-shaped grass hill in soft open green #A5D6A7, CH-STONE-01 smooth pale grey summit sitting stone #ECEFF1 slightly right of centre, 3 large soft white cumulus clouds #F5F5F5 in the sky (large upper-left, small centre, medium upper-right near the sun), sun in the upper right quadrant, soft and not a hard disc, pale blue sky #BBDEFB occupying about 62% of frame, horizon at 35-40% from frame bottom, low pastel hill silhouettes on the distant horizon #C8E6C9, no characters, {style} {camera} {lighting}

Do not display any on-screen text. No title card. No logo. No speech bubbles. No captions. No subtitles. No text.
```

### Video (3–4 sn)

```text
Use the Cloud Hill micro-opening still (@image1) as frame zero. A single, very slow camera glide drifts across the summit area, or a gentle push-in toward the open sky. The 3 clouds drift very slowly left to right. Small grass tufts near the summit move very slightly in a soft breeze. No characters appear. No reveal, no action — just a calm, sky-dominant atmosphere.

Camera: gentle glide or extremely slow push-in, 35mm equivalent, camera height 0.75-0.80m, no fast zoom, no shake, no whip pan, no crane drop.
Duration feel: 3–4 seconds, final frame should visually connect into the episode's own first story shot (climb path or summit arrival — same dome silhouette, same sky ratio, same Episode Colour Master).

No readable text anywhere in the frame. No title card. No logo animation.
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles.
```

### Sound

- A soft, airy 3–4 second music motif: airy pad, one soft chime, and a light breath-like wind
  sound, layered under soft continuous wind (low, smooth, slightly breathy — CH-WIND-AMB) and
  a distant single melodic bird call (CH-BIRD-01) every 8-12 seconds.
- Music sits low under the ambience (music ≈ -12 dB, ambience ≈ -18 dB per
  `00-CORE/AUDIO_GUIDE.md` § Ses Seviyesi Kuralları). Non-vocal, simple, repeatable.
- No loud jingle, no logo sting, no fast whoosh, no drums, no lyrics, no spoken branding.

---

## Negative Prompt

```text
low quality, blurry, deformed, text, watermark, readable text, title text, logo, brand mark, subscribe button, like button, arrows, end card graphics, photorealistic, horror, scary, dark storm clouds, lightning, harsh contrast, neon colours, cinematic LUT, HDR look, fast motion, flashing, loud effect, characters, extra characters, empty plain hill with no landmark, generic meadow, harsh mountain, cliffs, too many flowers, houses on the summit, busy village elements, sky ratio below 60%, more than 4 clouds, zero clouds, jagged or pointed hill silhouette, cool blue shift, oversaturated colours
```

(Consistent with `00-CORE/NEGATIVE_PROMPTS.md` § Common Negative Prompt and the Cloud Hill
Forbidden list in `01-world-bible.md` § Forbidden / § World Identity Lock.)

---

## Production Notes

- Render the still first, then the 3–4 sn video clip; store once and reuse across all Cloud
  Hill world-based episodes (90–120 sn length only — see `MICRO_OPENING_AND_CLOSING_STANDARD.md` §4).
- Do not use for Shorts. Avoid for 60-second episodes unless trimmed to 1–2 seconds.
- Verify sky ratio (≥60%) and cloud count (2–3, never more than 4) before accepting any
  generation — these are the most common Cloud Hill failure points per `01-world-bible.md`
  § Production Summary.
- Keep colour identity matched to the Cloud Hill palette (grass #A5D6A7, sky #BBDEFB, clouds
  #F5F5F5) so the reused clip does not drift between episodes
  (`00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Colour Continuity).
- This package has no closing counterpart. Do not create a `CLOSING_BUMPER/` folder for Cloud
  Hill — the final story shot of each episode serves as the closing (§3 of the global standard).

---

*Referans: `opening-cloud-hill-moments.md`, `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B, `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9c.*
*Versiyon: 1.0 — 4 Temmuz 2026*
