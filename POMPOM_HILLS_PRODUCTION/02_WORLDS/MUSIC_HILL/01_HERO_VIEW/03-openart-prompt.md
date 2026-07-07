# Music Hill — OpenArt World Builder Prompt

> Use this short plain-text prompt in the OpenArt World Builder text field.
> `02-world-spec.md` stays as the full production specification — it is not meant to be pasted directly into OpenArt.
> This file is a compressed, natural-language translation for that one text box.

---

## Honest Limitation — Read This First

OpenArt World Builder does **not** guarantee output that matches our full production standard.

It is a 3D spatial extrapolation tool, not a prompt-following image generator. It reconstructs a navigable 3D space from images — it does not carefully honor a detailed spec the way our render pipeline does. A short text prompt cannot carry the precision of `02-world-spec.md` (exact hex colors, exact positions, the full forbidden list). Some quality and identity loss versus the Bible/Spec standard should be expected.

**The correct input is not a fresh text prompt — it's the already-approved Hero View image.**

We already have a canon Hero View image that passed QA against the Bible. That image is the highest-fidelity representation of Music Hill we have. Feed *that* image into World Builder as the reference, and let the text prompt (below) serve only as a secondary hint — not as the thing trying to recreate the world from scratch.

```
1 image mode  → Upload the approved Hero View. Use the short prompt only as
                supplementary style guidance, not as the primary description.
2–4 image mode → Text prompt disables. The Hero View should be one of the
                 uploaded images (front view). Do not try to redescribe the
                 world in text — the image is the instruction.
```

If World Builder's 3D output still drifts from our identity (wrong tree count, wrong leaf colours, looks like a normal hill), that is an inherent limitation of the extrapolation — not something a better prompt can fully fix. Treat any World Builder output as a rough 3D blockout, and run it through the Production QA checklist before treating any capture from it as canon.

---

## Why a separate file

OpenArt World Builder's text prompt field:

- expects a short natural-language description, not a structured document
- disables itself entirely once 2+ reference images are uploaded (images become the instruction)
- does not parse markdown — tables, headers, and code blocks read as noise or get truncated
- does not understand internal asset IDs like `MH-TREE-01` or `MH-LEAF-CHIME`

The full `02-world-spec.md` (150+ lines, tables, asset IDs) is very likely why generation is failing or producing nothing usable — it's the wrong format for this input, not wrong content.

---

## If uploading 1 image

Use the image as the primary reference and paste this prompt into the text field:

```
A single smooth, gently rounded grass hill under a wide open pastel blue sky. Three to five music trees stand on the hill — each with a soft brown trunk and round, plump clusters of musical-green leaves that look like they could chime in the wind. The tallest tree stands near the summit, others flank at different heights. Melody-pink flowers are scattered naturally at the tree bases. A winding warm-sand path leads from the lower left up toward the summit, with soft coral stepping stones along it. Gentle breeze implied by slight leaf movement. Warm sunlight from the upper left, no harsh shadows. The mood is rhythmic, inviting, and warm — like a place where the trees sing. Children's storybook style, soft matte handcrafted look. No modern instruments, no sharp edges, no realistic trees, no dark shadows, no dramatic sky.
```

## If uploading 2–4 images

Do not rely on the text field — it will be disabled. Instead:

- Image 1 (front): wide shot from the base of the hill looking up, showing the full hill and trees
- Image 2 (back): view from the summit looking down the slope
- Image 3 (left): side view showing the hill's dome silhouette and tree heights
- Image 4 (right, optional): close-up of a music tree's leaf chimes and flowers

All four images must share the same lighting direction, sky colour, and grass colour so OpenArt reads them as one consistent space.

---

## After the world is built

Use `02-world-spec.md` as your production reference when framing shots, placing characters, and running QA inside the generated world — not as an input to the builder itself.
