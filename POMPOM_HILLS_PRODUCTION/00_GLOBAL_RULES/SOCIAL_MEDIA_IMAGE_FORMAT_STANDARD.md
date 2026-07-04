# Social Media Image Format Standard

> This is a global production standard for static social media images (Facebook, Instagram,
> YouTube Community). It does not cover video Reels/Shorts formats (see
> `07-BRANDING/campaigns/pompom-hills-event/prompts.md` for the event campaign precedent and
> `00-CORE/30_YOUTUBE_METADATA_STANDARD.md` for Shorts metadata). It does not redesign any
> character or world — it governs layout, safe margins and per-platform recomposition only.

---

## Text Safety Exception (Reference)

Static social media images are allowed to carry on-screen text under the same exception
already established for campaign posters: `CONTRIBUTING.md` § Prompt Ekleme Kuralları
madde 6 ("Görselde yazı sadece moodboard, poster veya palette card gibi özellikle
belirtilen assetlerde kullanılabilir") and
`07-BRANDING/campaigns/pompom-hills-event/prompts.md` § Text Safety İstisnası. This does
not apply to master video renders — `00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Text
Safety remains unchanged for video.

---

## Core Rule

**Never create one image and reuse it for Facebook, Instagram and YouTube without
checking the platform ratio.**

Each social post must have separate platform-safe image versions. Do not just crop one
version automatically — each version must be recomposed for its platform. All versions
keep the same campaign idea, character, colours and branding, but the layout changes to
fit the platform.

Required versions for every social image campaign:

1. Facebook / Instagram Story version
2. Instagram Feed / Facebook Feed version
3. YouTube Community / YouTube post version

---

## 1. Facebook / Instagram Story

**Use for:** Facebook Story, Instagram Story, vertical story sharing.

| Field | Value |
|---|---|
| Aspect ratio | 9:16 vertical |
| Recommended size | 1080 x 1920 px |
| Output naming | `<campaign-name>_story_9x16.png` |

**Safe margins:**

| Edge | Margin |
|---|---|
| Top | 180 px |
| Bottom | 250 px |
| Left | 80 px |
| Right | 80 px |

Keep all important text, faces, logos, props and character bodies inside the central
safe area. Do not place important text at the very top or very bottom.

**Reason:** Stories can be covered by profile UI, buttons, reply bar, stickers, captions,
and platform controls.

**Composition rules:**

- Vertical layout.
- Main character large and readable.
- Main title in upper-middle, not at extreme top.
- Supporting text in middle or lower-middle, not at extreme bottom.
- Character face must not be under UI zones.
- Avoid tiny text.
- Avoid important details near edges.

---

## 2. Instagram Feed / Facebook Feed

**Use for:** Instagram feed post, Facebook feed post, carousel image, general square
social image.

| Field | Value |
|---|---|
| Aspect ratio | 1:1 square |
| Recommended size | 1080 x 1080 px |
| Output naming | `<campaign-name>_feed_1x1.png` |

**Safe margins** (central 80% safe area):

| Edge | Margin |
|---|---|
| Top | 90 px |
| Bottom | 120 px |
| Left | 90 px |
| Right | 90 px |

**Composition rules:**

- Do not use tall vertical story layout.
- Do not place title at the extreme top edge.
- Do not place bottom labels near the bottom edge.
- Main character should be centered.
- Text should be large and readable.
- Avoid collage elements that extend outside crop.
- Keep character face, title, ball/prop and logo fully visible.

---

## 3. YouTube Community / YouTube Post

**Use for:** YouTube Community post image, YouTube image post, YouTube preview where
square crop may be applied.

| Field | Value |
|---|---|
| Primary aspect ratio | 1:1 square |
| Recommended size | 1080 x 1080 px |
| Output naming | `<campaign-name>_youtube_1x1.png` |

**Important:** YouTube may preview or crop images aggressively depending on surface.

**Safe margins** (larger than Feed, central safe zone):

| Edge | Margin |
|---|---|
| Top | 130 px |
| Bottom | 160 px |
| Left | 120 px |
| Right | 120 px |

**Composition rules:**

- Do not create a vertical story image for YouTube.
- Do not place title near the top edge.
- Do not place CTA near the bottom edge.
- Avoid decorative borders that depend on full image visibility.
- Keep title, character face, prop and logo inside the center.
- Use fewer text elements than the Story version.
- Prefer one bold readable title and one short subtitle only.
- Avoid small text blocks.

---

## Optional Extra Version — YouTube Thumbnail / Wide Preview

Use only when explicitly requested for a YouTube thumbnail or wide video preview.

| Field | Value |
|---|---|
| Aspect ratio | 16:9 horizontal |
| Recommended size | 1280 x 720 px |
| Output naming | `<campaign-name>_youtube_thumbnail_16x9.png` |

This is a separate, opt-in output — it is not part of the default three-version set. See
`07-BRANDING/THUMBNAIL_TEMPLATE.md` for the existing episode-thumbnail standard this
should stay consistent with when used for video previews.

---

## Global Social Image Generation Rules

For every social media image campaign, create the small platform set:

- Story 9:16
- Feed 1:1
- YouTube 1:1

Do not just crop one version automatically. Each version must be recomposed for its
platform. All versions should keep the same campaign idea, character, colours and
branding, but layout must change to fit the platform.

---

## Text Rules

Text must be:

- short
- large
- readable
- inside safe area
- not touching image edges
- not hidden by platform UI

Avoid:

- long paragraphs
- tiny captions
- text near the top edge
- text near the bottom edge
- too many labels
- text inside busy background areas

For toddler-friendly posts, prefer simple text like:

```
Meet Arda!
Let's play!
Kick • Laugh • Play
New story in Pompom Hills
Come play with Arda!
```

---

## Character Rules

Character must:

- be fully visible unless intentionally close-up
- have face inside safe area
- not be cropped at forehead, chin, hands, or feet unless close-up is planned
- not be too close to edges
- stay recognizable
- match approved character reference (`01-CHARACTERS/{character}.md`)

**Example — Arda** (see `01-CHARACTERS/04-arda.md` for the full canon):

- soft fluffy dark brown hair
- big warm brown eyes
- round toddler face
- sky blue shirt with tiny warm-brown logo patch
- light blue soft pants
- tan cozy shoes
- cheerful football energy
- soft football prop allowed

This is a worked example, not a substitute for the character's own canon file. Always
check `01-CHARACTERS/{character}.md` for the character actually being used.

---

## Background Rules

Use a simple Pompom Hills environment. Do not overload the frame with too many details.

**For Central Square / Pompom Hills social posts, safe background elements:**

- Big Pompom Tree
- rounded paths
- colourful stepping stones
- pastel houses
- soft flowers
- blue sky
- fluffy clouds
- soft football
- warm sunny preschool-safe mood

**Avoid:**

- too many signs
- readable world signs unless explicitly needed
- complex posters
- crowded characters
- small unreadable text
- cluttered collage
- busy lower third
- text placed over detailed flowers

---

## Platform-Specific Prompt Template

When creating social image prompts, always generate three separate prompts.

### A) Story 9:16 Prompt

```text
Create a vertical 9:16 Facebook and Instagram Story image, 1080x1920.

Keep all important elements inside story safe margins: top 180 px, bottom 250 px, left 80 px, right 80 px.

Do not place text at the extreme top or bottom.

Main subject: [character / campaign idea]

Text: [short title] [short subtitle]

Composition: Vertical story layout, character large and readable, face in upper-middle safe area, main action in center, CTA or small label in lower-middle safe area.

Style: Soft 3D preschool animation, warm pastel colours, rounded shapes, Pompom Hills look.

Negative: cropped text, cropped face, cropped character, text too close to edge, tiny unreadable text, busy layout, cluttered collage, watermark, logo error, distorted letters
```

### B) Feed 1:1 Prompt

```text
Create a square 1:1 Instagram/Facebook feed image, 1080x1080.

Keep all important elements inside the central 80% safe area.

Do not use vertical story composition.

Main subject: [character / campaign idea]

Text: [short title] [short subtitle]

Composition: Square layout, character centered, title safely in upper-middle, subtitle safely below, prop visible, background simple and readable.

Style: Soft 3D preschool animation, warm pastel colours, rounded shapes, Pompom Hills look.

Negative: vertical crop, cropped text, cut off title, cut off character, text near edges, cluttered border, unreadable small text, watermark, distorted letters
```

### C) YouTube 1:1 Prompt

```text
Create a YouTube Community-safe square image, 1080x1080.

All important content must fit inside the central safe zone.

Leave large margins: top 130 px, bottom 160 px, left 120 px, right 120 px.

Do not use a tall story layout.

Main subject: [character / campaign idea]

Text: [one large title] [one short subtitle only]

Composition: Simple square poster, character centered, face clearly visible, title inside upper-middle safe zone, football/prop inside central safe zone, no important details near edges.

Style: Soft 3D preschool animation, warm pastel colours, rounded shapes, Pompom Hills look.

Negative: cropped text, cropped title, cropped character, text near top edge, text near bottom edge, vertical story layout, too many text blocks, cluttered collage, watermark, distorted letters
```

---

## QA Checklist for Social Images

Before approving any generated social image, check:

- [ ] Correct platform ratio used
- [ ] Important text is inside safe area
- [ ] Character face is not cropped
- [ ] Character body is not awkwardly cropped
- [ ] Main prop is visible
- [ ] Text is readable on mobile
- [ ] No important detail near platform UI zones
- [ ] No distorted letters
- [ ] No unreadable small text
- [ ] No unwanted characters
- [ ] No watermark
- [ ] No wrong logo
- [ ] No auto-crop risk
- [ ] Image works as a thumbnail
- [ ] Image works on mobile screen

---

## Rejection Criteria

Reject a social image if:

- one image is used for all platforms without recomposition
- a story image is uploaded to YouTube and gets cropped
- title is cut off
- bottom text is cut off
- character face is cut off
- prop is cut off
- text is too close to edge
- too much important content is outside the central safe zone
- platform auto-crop would remove key content
- text is unreadable
- letters are distorted
- image is too cluttered
- wrong character appears
- non-canon characters appear

---

## Worked Example — Arda Campaign

**Campaign:** Meet Arda / Let's play

**Three versions:**

1. `meet-arda_story_9x16.png`
2. `meet-arda_feed_1x1.png`
3. `meet-arda_youtube_1x1.png`

| Version | Text |
|---|---|
| Story | Meet Arda! / Let's go! |
| Feed | Meet Arda! / Kick • Laugh • Play |
| YouTube | Meet Arda! / Let's play! |

**Visual:** Arda smiling with a soft football in Pompom Hills / Central Square. Keep
Arda's face, football, and text safely inside each platform's crop area.

---

## Requesting a Social Image Set

To request a platform set for a character or campaign, use this pattern:

```text
[Character] için social media platform set üretim promptları hazırla:
1 Story 9:16
1 Feed 1:1
1 YouTube 1:1

Aynı kampanya ama her platform için yeniden kompozisyon.
En önemli kural: tek görsel üretip üç platforma koymayacağız. Her platform için ayrı kompozisyon.
```

---

*This document is the single source of truth for social media image formats, safe
margins, naming conventions and per-platform recomposition rules.*
*Version: 1.0 — 4 Temmuz 2026*
