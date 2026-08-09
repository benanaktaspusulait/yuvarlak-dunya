# Opa's Book Tells the Wrong Story — Start-Frame Image Generation Prompt

## ChatGPT Image / OpenArt Image Generation

Use this prompt to generate the `@image1` start-frame still for the shot.
After generation, save the approved image to this directory as `start-frame.png`.

---

### Reference Images (attach these when generating)

1. **Opa identity**: `01-CHARACTERS/drawings/opa.png`
2. **Opa's Tree hero view**: `POMPOM_HILLS_PRODUCTION/02_WORLDS/OPA_TREE/01_HERO_VIEW/hero-view.png`

---

### Prompt

```text
Vertical 9:16 preschool animation still (1080x1920).

A small round owl character named Opa sits securely on a wide rounded tree branch. Opa has warm green feathers (#A5D6A7), a light-green belly (#C8E6C9), large warm-brown eyes (#795548), round golden glasses (#FFD54F), a small orange beak (#FF7043), orange feet, short rounded wings, and a soft brown shawl (#A1887F) around his shoulders.

Opa holds one closed rounded storybook in his wings. The book has a plain warm-brown cover (#A1887F) with no title, letters, symbols or readable text. The book is about 40% of Opa's body size.

The branch is wide, safe and rounded — part of a gigantic ancient pompom tree with a thick soft-brown trunk (#A1887F) and a large fluffy green canopy (#81C784). Soft green grass (#C8E6C9) and small round flowers (pink, yellow, purple) are visible at the tree base. Warm dappled sunlight filters through the leaves with soft golden rays.

Camera: medium vertical composition, child-eye level, Opa centred in the frame. Opa and the book fill approximately 50-60% of the vertical frame. The branch extends left and right. The canopy fills the upper third.

Style: premium Pixar-quality 3D preschool animation. Rounded plush-clay shapes, matte handcrafted materials, soft pastel colours, warm dappled sunlight, medium-low contrast, gentle soft shadows. Toddler-safe emotional clarity. Calm, peaceful, wise mood.

No text, no letters, no words, no watermark, no logo, no caption. No other characters. No extra objects on the branch.
```

---

### Negative prompt

```text
realistic owl, photorealistic bird, sharp feathers, angular face, small eyes, reading glasses on forehead, open book, visible text, letters, words, handwriting, title on cover, second character, extra animal, multiple books, bookshelf, indoor scene, dark lighting, high contrast, harsh shadows, HDR, glossy plastic, oversaturated, neon colours, scary mood, text overlay, watermark, logo
```

---

### Settings

| Setting | Value |
|---|---|
| Aspect ratio | 9:16 (vertical) |
| Resolution | 1080×1920 |
| Style | Illustration / 3D animation |
| Quality | High |

---

### After generation

1. Review Opa's identity against `01-CHARACTERS/drawings/opa.png`
2. Verify the book is closed, warm-brown, no text
3. Verify branch, tree and background match Opa's Tree hero view
4. Save approved image as `start-frame.png` in this directory
5. Use `start-frame.png` as `@image1` in the OpenArt Frame-to-Video prompt
