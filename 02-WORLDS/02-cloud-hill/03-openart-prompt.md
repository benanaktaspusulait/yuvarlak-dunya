# Cloud Hill — OpenArt World Builder Prompt

> Use this short plain-text prompt in the OpenArt World Builder text field.
> `02-world-spec.md` stays as the full production specification — it is not meant to be pasted directly into OpenArt.
> This file is a compressed, natural-language translation for that one text box.

---

## Honest Limitation — Read This First

OpenArt World Builder does **not** guarantee output that matches our full production standard.

It is a 3D spatial extrapolation tool, not a prompt-following image generator. It reconstructs a navigable 3D space from images — it does not carefully honor a detailed spec the way our render pipeline does. A short text prompt cannot carry the precision of `02-world-spec.md` (exact hex colors, exact 62% sky ratio, exact stone position, the full forbidden list). Some quality and identity loss versus the Bible/Spec standard should be expected.

**The correct input is not a fresh text prompt — it's the already-approved Hero View image.**

We already have a canon Hero View image that passed QA against the Bible. That image is the highest-fidelity representation of Cloud Hill we have. Feed *that* image into World Builder as the reference, and let the text prompt (below) serve only as a secondary hint — not as the thing trying to recreate the world from scratch.

```
1 image mode  → Upload the approved Hero View. Use the short prompt only as
                supplementary style guidance, not as the primary description.
2–4 image mode → Text prompt disables. The Hero View should be one of the
                 uploaded images (front view). Do not try to redescribe the
                 world in text — the image is the instruction.
```

If World Builder's 3D output still drifts from our identity (wrong grass color, wrong cloud count, stone missing), that is an inherent limitation of the extrapolation — not something a better prompt can fully fix. Treat any World Builder output as a rough 3D blockout, and run it through the Production QA checklist before treating any capture from it as canon.

---

## Why a separate file

OpenArt World Builder's text prompt field:

- expects a short natural-language description, not a structured document
- disables itself entirely once 2+ reference images are uploaded (images become the instruction)
- does not parse markdown — tables, headers, and code blocks read as noise or get truncated
- does not understand internal asset IDs like `CH-STONE-01` or `CH-GRASS-01`

The full `02-world-spec.md` (150+ lines, tables, asset IDs) is very likely why generation is failing or producing nothing usable — it's the wrong format for this input, not wrong content.

---

## If uploading 1 image

Use the image as the primary reference and paste this prompt into the text field:

```
A single smooth, gently rounded grass hill under a wide open pastel blue sky. Soft white fluffy rounded clouds, three of them, spaced apart, upper half of the sky. Warm soft sunlight from the upper right, no harsh shadows. Short, even, plush green grass. A small smooth flat grey stone sits at the top of the hill, slightly right of center. A few small white daisies scattered sparsely on the slope. Low pastel-colored hills on the distant horizon. Sky takes up most of the frame, hill silhouette fills the width of the frame. Children's storybook style, soft matte handcrafted look, warm and safe atmosphere. No buildings, no fences, no roads, no modern objects, no sharp rocks, no dark clouds.
```

## If uploading 2–4 images

Do not rely on the text field — it will be disabled. Instead:

- Image 1 (front): wide shot of the hill from below, matching the description above
- Image 2 (back): view from the summit looking back down the slope
- Image 3 (left): side view of the hill showing the dome silhouette
- Image 4 (right, optional): summit close-up showing the stone and grass

All four images must share the same lighting direction, sky color, and grass color so OpenArt reads them as one consistent space.

---

## After the world is built

Use `02-world-spec.md` as your production reference when framing shots, placing characters, and running QA inside the generated world — not as an input to the builder itself.
