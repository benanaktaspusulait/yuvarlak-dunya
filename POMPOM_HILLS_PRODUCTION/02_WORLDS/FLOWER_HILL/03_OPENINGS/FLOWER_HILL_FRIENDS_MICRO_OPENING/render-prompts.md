# Flower Hill Friends — Micro-Opening Render Prompts v1.0 (DRAFT — Pending Hero View)

> OpenArt render prompt'ları, Flower Hill Home Cluster Zone world micro-opening için.
> Spesifikasyon: `opening-flower-hill-friends.md`.
> Kurallar: `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B,
> `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9c, `00-CORE/17_VIDEO_GENERATION_STANDARD.md` §Text Safety.
>
> ⚠️ **DRAFT STATUS:** Flower Hill'in Canon Hero View'ı henüz onaylanmadı (bkz.
> `25-flower-hill-bible.md` § Generation Workflow — "Hero View: 🟡 Legacy images exist,
> Canon Hero View approval pending"). Bu prompt paketi world spec'e göre yazıldı ama
> production'da kullanılmadan önce world'ün kendi Hero View onayı beklenmelidir. Hero View
> onaylandığında bu dosyanın "DRAFT" etiketi kaldırılıp v1.0 → v1.1 olarak güncellenmelidir.
>
> World-specific: Flower Hill'in Home Cluster Zone kimliğini gösterir (yer-nötr DEĞİL).
> Karakter yoktur — bkz. `MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B "no characters by default".
> `{style} {camera} {lighting}` değişkenleri `00-CORE/VARIABLES.md`'den çözülür.
>
> Kapanış eşleniği yok — normal Flower Hill bölümleri kendi final shot'unda kapanır
> (bkz. `MICRO_OPENING_AND_CLOSING_STANDARD.md` §3).

---

## World Micro-Opening (3–4 sn) — Home Cluster Zone

### Frame / Still (image)

```text
Flower Hill Home Cluster Zone in Pompom Hills, flower-covered hill, pink main dome home, two smaller pastel dome homes nearby, central smooth grey stone path #E0E0E0 leading toward the homes, soft flower fences, flower pots along the path, warm preschool home charm, warm morning daylight from the upper left, no characters, {style} {camera} {lighting}

Do not display any on-screen text. No title card. No logo. No speech bubbles. No captions. No subtitles. No text.
```

### Video (3–4 sn)

```text
Use the Flower Hill Home Cluster Zone micro-opening still (@image1) as frame zero. A very slow camera glide moves along the stone path toward the homes, or a gentle push-in. Soft vines sway very slightly. Flower heads sway gently in a soft breeze. No characters appear. No reveal, no action — just a calm, warm home atmosphere.

Camera: gentle glide or extremely slow push-in, 24-35mm equivalent, camera height ~0.85-1.20m, no fast zoom, no shake, no whip pan, no Dutch angle.
Duration feel: 3–4 seconds, final frame should visually connect into the episode's own first story shot of the Home Cluster Zone.

No readable text anywhere in the frame. No title card. No logo animation. No readable sign.
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles.
```

### Sound

- A light, cheerful 3–4 second music motif: bells or glockenspiel, a soft flower-breeze sound,
  layered under soft continuous wind mixed with light flower/leaf rustle and a distant single
  melodic bird call every 8-12 seconds (per `25-flower-hill-bible.md` § Environmental Sound
  Identity).
- Music sits low under the ambience (music ≈ -12 dB, ambience ≈ -18 dB per
  `00-CORE/AUDIO_GUIDE.md` § Ses Seviyesi Kuralları). Non-vocal, simple, repeatable.
- No loud jingle, no logo sting, no fast whoosh, no drums, no lyrics, no spoken branding.

---

## Negative Prompt

```text
low quality, blurry, deformed, text, watermark, readable text, readable sign, title text, logo, brand mark, subscribe button, like button, arrows, end card graphics, photorealistic, horror, scary, dark lighting, sunset, golden-hour, harsh contrast, neon colours, cinematic LUT, HDR look, fast motion, flashing, loud effect, characters, extra characters, top-down map view, large bridge, dominant river, ducks, fish, rainbow, realistic village, sharp fences, busy clutter, random non-canon props, redesigned Kiko's Home silhouette, redesigned Mimi's Burrow silhouette, generic meadow, dry brown grass
```

(Consistent with `00-CORE/NEGATIVE_PROMPTS.md` § Common Negative Prompt and the Flower Hill
Forbidden Clutter list in `25-flower-hill-bible.md` § Visual Richness & World Charm.)

---

## Production Notes

- **Do not render a final reusable clip until Flower Hill's Canon Hero View is approved.**
  This prompt package may be used to help generate Hero View candidates, but the resulting
  clip should not be treated as a locked, reusable micro-opening until the world itself is
  locked.
- Once approved, render the still first, then the 3–4 sn video clip; store once and reuse
  across all Flower Hill Home Cluster Zone episodes (90–120 sn length only — see
  `MICRO_OPENING_AND_CLOSING_STANDARD.md` §4).
- Do not use for Shorts. Avoid for 60-second episodes unless trimmed to 1–2 seconds.
- Keep colour identity matched to the Flower Hill palette (five flower colours, grass
  #C8E6C9, path #E0E0E0) so the reused clip does not drift between episodes
  (`00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Colour Continuity).
- This package has no closing counterpart. Do not create a `CLOSING_BUMPER/` folder for
  Flower Hill — the final story shot of each episode serves as the closing (§3 of the
  global standard).

---

*Referans: `opening-flower-hill-friends.md`, `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B, `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9c.*
*Versiyon: 1.0 DRAFT — Pending Flower Hill Canon Hero View approval. 4 Temmuz 2026*
