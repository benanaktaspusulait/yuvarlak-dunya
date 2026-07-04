# Opa's Storytime — Opening Bumper Render Prompts v1.0

> OpenArt render prompt'ları, ortak açılış bumper'ı için.
> Bir kez üretilir, her bölümde tekrar kullanılır. Spesifikasyon: `opening-bumper.md`.
> Kurallar: `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §4a,
> `00-CORE/17_VIDEO_GENERATION_STANDARD.md` §Text Safety.
>
> Yer-nötr: belirli bir dünya gösterilmez, böylece her bölümde tekrar kullanılabilir.
> `{style} {camera} {lighting}` değişkenleri `00-CORE/VARIABLES.md`'den çözülür.
>
> Kapanış çifti: `POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/CLOSING_BUMPER/render-prompts.md`

---

## Opening Bumper (3–4 sn)

### Frame / Still (image)

```text
A single rounded, handcrafted preschool storybook resting on a soft neutral warm surface, closed, gentle warm pastel light, rounded soft shapes, cozy storytime feeling, plain uncluttered warm background (no specific location), no readable text on the cover, {style} {camera} {lighting}

Do not display any on-screen text. No title text. No speech bubbles. No captions. No subtitles. No readable text on the book.
```

### Video (3–4 sn)

```text
Use the opening bumper still (@image1) as frame zero. The rounded storybook gently opens a little; warm pastel light softly spills from the pages; one small soft sparkle drifts upward. Slow, gentle, calm motion only. Hold warm and cozy. No characters required (an optional soft adult hand may rest on the book edge).

Camera: static or an extremely slow push-in, child-eye-level, 35mm, no fast zoom, no shake, no whip pan.
Duration feel: 3–4 seconds, ends ready to cut into the episode's own opening beat.

No readable text on the pages. No on-screen title text by default (a 1–2s "Opa's Storytime" soft rounded title is optional ONLY if production approves — see `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` §5).
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles.
```

### Sound

- One soft chime as the book opens; very light warm ambience underneath. No loud music, no stinger.

---

## Negative Prompt

```text
low quality, blurry, deformed, text, watermark, readable text, title text, logo, brand mark, subscribe button, like button, arrows, end card graphics, photorealistic, horror, scary, dark lighting, harsh contrast, neon colours, cinematic LUT, HDR look, fast motion, flashing, loud effect, specific recognizable location, cluttered background, extra objects
```

---

## Production Notes

- Render the still first, then the 3–4 sn video clip; store once and reuse across all Opa's Storytime episodes.
- Keep visually matched with the closing bumper (same book, same surface, same warm palette) for series recognition.
- Colour identity should match the gentle Opa's Storytime pastel look; do not let the reused clip drift in colour between uploads (`00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Colour Continuity).

---

*Referans: `opening-bumper.md`, `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §4a.*
*Versiyon: 1.0 — Opening/closing render prompt dosyaları ayrıldı. 4 Temmuz 2026*
