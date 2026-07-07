# Rosie's Rose Garden — OpenArt World Builder Prompt

> Use this short plain-text prompt in the OpenArt World Builder text field.
> `02-world-spec.md` stays as the full production specification — it is not meant to be pasted directly into OpenArt.
> This file is a compressed, natural-language translation for that one text box.

---

## Honest Limitation — Read This First

OpenArt World Builder does **not** guarantee output that matches our full production standard.

It is a 3D spatial extrapolation tool, not a prompt-following image generator. It reconstructs a navigable 3D space from images — it does not carefully honor a detailed spec the way our render pipeline does. A short text prompt cannot carry the precision of `02-world-spec.md` (exact hex colors, exact bed positions, the full forbidden list). Some quality and identity loss versus the Bible/Spec standard should be expected.

**The correct input is not a fresh text prompt — it's the already-approved Hero View image.**

We already have a canon Hero View image that passed QA against the Bible. That image is the highest-fidelity representation of Rosie's Rose Garden we have. Feed *that* image into World Builder as the reference, and let the text prompt (below) serve only as a secondary hint — not as the thing trying to recreate the world from scratch.

```
1 image mode  → Upload the approved Hero View. Use the short prompt only as
                supplementary style guidance, not as the primary description.
2–4 image mode → Text prompt disables. The Hero View should be one of the
                 uploaded images (front view). Do not try to redescribe the
                 world in text — the image is the instruction.
```

If World Builder's 3D output still drifts from our identity (wrong heart shape, thorns appearing, fence missing), that is an inherent limitation of the extrapolation — not something a better prompt can fully fix. Treat any World Builder output as a rough 3D blockout, and run it through the Production QA checklist before treating any capture from it as canon.

---

## Why a separate file

OpenArt World Builder's text prompt field:

- expects a short natural-language description, not a structured document
- disables itself entirely once 2+ reference images are uploaded (images become the instruction)
- does not parse markdown — tables, headers, and code blocks read as noise or get truncated
- does not understand internal asset IDs like `RG-BEDS-HEART-01` or `RG-FOUNTAIN-01`

The full `02-world-spec.md` (150+ lines, tables, asset IDs) is very likely why generation is failing or producing nothing usable — it's the wrong format for this input, not wrong content.

---

## If uploading 1 image

Use the image as the primary reference and paste this prompt into the text field:

```
A gentle enclosed rose garden surrounded by a low white rounded fence with ball-top finials. Twin heart-shaped flower beds at the centre — one filled with soft pink roses, the other with warm red roses, joined by a small cluster of yellow flowers. A small white rounded fountain sits at the heart of the garden with gentle water flow. Winding soft sand-coloured paths curve between the rose beds. Butterflies with thin pink-purple gradient wings drift gently through the air. Warm pastel sunlight, soft and even, no harsh shadows. Children's storybook style, soft matte handcrafted look, warm and safe atmosphere. No thorns anywhere, no dark lighting, no modern objects, no sharp edges, no square or oval beds.
```

## If uploading 2–4 images

Do not rely on the text field — it will be disabled. Instead:

- Image 1 (front): wide view of the garden with twin heart beds, fountain, and fence
- Image 2 (back): view from the fence gate looking inward
- Image 3 (left): side view showing the maze path structure
- Image 4 (right, optional): close-up of the heart beds with butterflies

All four images must share the same lighting direction, grass color, and rose colors so OpenArt reads them as one consistent space.

---

## After the world is built

Use `02-world-spec.md` as your production reference when framing shots, placing characters, and running QA inside the generated world — not as an input to the builder itself.
