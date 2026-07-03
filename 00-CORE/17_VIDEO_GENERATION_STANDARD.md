# 17 — Video Generation Standard

> Tüm shot dosyaları bu standarttan üretir.
> Her shot bu dosyaya atıfta bulunur, aynı kuralları tekrar etmez.

---

## Production Pipeline

Gerçek üretim akışı:

```
Shot 01 Image
    ↓
Frame to Video
    ↓
Shot 01 Video
    ↓
Shot 02 (Video Reference: Shot 01 Video)
    ↓
Shot 02 Video
    ↓
Shot 03 (Video Reference: Shot 02 Video)
    ↓
...devam eder
```

---

## First Frame Continuity

Shot 01 uses the approved original first-frame still.
Shot 02 and onward use the previous shot as the Video Reference.
If a still continuity frame is used, it must be the exported/downloaded original frame, not a screenshot.

The opening frame of each continuation shot should continue seamlessly from the previous shot reference.

The opening frame must continue seamlessly from the previous shot video reference or exported continuity frame. The viewer should not perceive a shot boundary.

Maintain:
- character position
- camera height
- framing
- lighting
- colour grading
- world identity

---

## Voice Continuity

The speaking voices MUST remain identical across the whole episode.

Maintain:
- same voice identity per character
- same pitch
- same timbre
- same speaking speed
- same warmth
- same preschool naturalness

Do not generate a narrator.
Do not generate alternate voices.

---

## Colour Continuity

Match the colour grading of the previous shot exactly.

The previous shot is the colour master reference. Never rebalance colours between shots.

CRITICAL: Do NOT desaturate between shots. Do NOT make colours softer or paler.
Each shot must maintain the SAME saturation level as the first shot.

Maintain:
- identical white balance
- identical warmth
- identical exposure
- identical saturation (DO NOT reduce)
- identical pastel palette (DO NOT soften)
- identical contrast

Avoid:
- blue tint
- green tint
- orange shift
- desaturation
- softening of colours
- fading of colours
- HDR look
- cinematic LUT

The entire episode must appear colour graded as one continuous film.

---

## Reference Source Policy

Never use screenshots as production reference images.

Do not use:
- browser screenshots
- macOS screenshots
- screen captures
- preview-window captures
- compressed viewer images
- social media exports
- images copied from the screen

Use only:
- original downloaded PNG/JPG from the generation tool
- exported original video frame
- exported final frame from the previous shot
- approved production stills from the asset folder

Reason:

Screenshots can change colour through browser rendering, monitor colour profiles, Display P3 vs sRGB conversion, OS screenshot processing, compression, scaling and preview rendering.

Screenshots can cause:
- faded colour
- lower saturation
- incorrect brightness
- shifted white balance
- generational colour drift

If only a screenshot exists, do not use it as a production reference. Re-export or re-download the original frame/image.

---

## Episode Colour Master

Every episode must have one approved Episode Colour Master.

Usually this is the approved original first-frame still from Shot 01.

The Episode Colour Master defines:
- white balance
- exposure
- saturation
- contrast
- warmth
- pastel palette
- shadow softness
- highlight behaviour

Continuation shots must use two forms of reference:

1. Previous Shot Reference
   Purpose:
   - action continuity
   - character position
   - camera continuity
   - motion continuity

2. Episode Colour Master
   Purpose:
   - colour stability
   - white balance stability
   - exposure stability
   - saturation stability
   - preventing generational colour drift

Do not let each shot rebalance colour from the previous generated shot alone.

Every shot must remain visually matched to the Episode Colour Master.

Add this exact line to the Production Standard section of every shot:

Colour master: use the approved original Shot 01 still as the Episode Colour Master. Do not use a screenshot. Do not allow colour to fade, desaturate, cool down, warm up, brighten, darken or drift from the Episode Colour Master.

---

## Colour Drift Prevention

Generative video can lose saturation or shift colour across multiple shot generations.

To prevent this:

- Use the Episode Colour Master in every shot.
- Use the previous shot only for continuity of action and placement.
- Do not use a screenshot as colour reference.
- Do not allow the model to "improve" or "rebalance" the image.
- Do not allow automatic exposure correction.
- Do not allow automatic white balance correction.
- Do not allow a new colour grade.
- Do not allow fading or desaturation between shots.

Every continuation shot must maintain:
- same white balance
- same exposure
- same colour temperature
- same saturation
- same contrast
- same pastel palette
- same shadow softness
- same highlight behaviour
- same warm morning feeling

Reject if:
- colour looks more faded than the Episode Colour Master
- saturation drops
- image becomes cooler
- image becomes more grey
- image becomes more orange
- contrast changes visibly
- lighting looks like a different time of day

---

## Lighting Continuity

Preserve the lighting from the previous shot exactly.

Maintain:
- identical light direction
- identical light intensity
- identical shadow softness
- identical ambient lighting
- identical highlight behaviour

Do not reinterpret the lighting. Continue it.

---

## Camera Rules

- Child eye level throughout
- Gentle 35mm framing
- Slow stable movement
- No zoom
- No handheld motion
- No sudden camera reset
- No tight framing

---

## Text Safety

Do not display dialogue as on-screen text.

No speech bubbles.
No captions.
No subtitles.
No text.

---

## Ball Continuity

The same round yellow ball must persist through the entire episode.

The ball must not change colour, size, texture, or shape.

---

## World Continuity

Central Square must remain visually consistent.

- Big Pompom Tree in background whenever composition allows
- Warm morning light throughout
- Soft pastel colours
- Safe open play space
- No new environment
- No extra characters
- No redesign

---

## Scale

Characters should feel small and childlike within Central Square, but must remain readable for facial expression and action.

Use wide framing for environment identity and medium framing for emotional beats.

---

## Animation Quality

- All movements slow and natural
- No sudden gestures
- No fast cuts
- Characters never fully frozen — idle animations present
- Grass moves gently in wind
- Environmental rhythm consistent

---

## Child Safety

- No sharp edges or dark shadows
- No threatening imagery
- All characters express only positive or gently curious emotions
- No violence, conflict, or distressing content
- Soft and safe throughout

---

## Spatial Continuity

The previous video reference alone is not enough to guarantee exact location continuity.

The AI may understand the general environment but place the characters in a similar, incorrect area.

Therefore every continuation shot must explicitly restate the physical location using environment anchors.

Spatial continuity means:

- same physical place
- same relative camera direction
- same major landmarks
- same character-to-landmark relationship
- same prop position
- same environment identity
- no relocation within the world unless the shot explicitly shows movement

Every shot must include a short section named:

## Environment Anchors

This section describes the stable landmarks and their relative positions.

For example:

- Big Pompom Tree remains in the background.
- Luca and Noah remain in the open grass play area in front of the tree.
- The round yellow ball remains between or near the children.
- The camera remains at child eye level.
- The shot does not relocate to another part of Central Square.
- No new path, building, bush, flowerbed, bench or object is introduced unless already part of Central Square canon.

Add this rule:

Do not let the AI infer the location from the previous video reference alone. Always describe the local physical environment in the shot prompt.

---

## Intra-Shot Background Persistence

Every generated video shot must preserve the background objects visible in its first frame.

Background landmarks are not decorative.
They are part of the physical location.

If an object is visible in the first frame, it must not:
- disappear
- transform
- be replaced
- change position
- change scale
- change identity
- become a different object
- be swapped with a tree, bush, house, path, flowerbed, or bench

This applies to:
- benches
- trees
- bushes
- paths
- lamps
- flowerbeds
- distant houses
- fences if canon
- landmarks
- props
- large background shapes

A bench must remain a bench.
A tree must remain the same tree.
A path must remain the same path.
A visible landmark must remain in the same relative position.

The AI must not repaint or reinterpret the background during the video.

Only character motion, prop motion, and explicitly requested camera motion may change.

---

## First Frame Object Lock

The first visible frame of every video shot defines the physical set for that shot.

Lock the following from the first frame:

- character positions
- prop positions
- background objects
- landmark positions
- camera angle
- camera height
- camera side
- lighting
- colour grade
- depth layout

The video may animate movement, but it must not regenerate the set.

If the first frame contains:
- a bench on the right,
- a bench on the left,
- Big Pompom Tree in the background,
- a path behind the characters,
- a yellow ball between the characters,

then those objects must remain consistent throughout the shot.

Objects may only leave the frame if the camera physically pans away from them.
They must not vanish while still inside the visible area.

---

## Background Drift Prevention

Generative video models may accidentally repaint the background during movement.

To prevent this:

- Keep camera movement minimal.
- Avoid unnecessary pans when background continuity matters.
- Avoid "reveal" language unless the shot truly reveals a new area.
- Do not allow the model to invent new background objects.
- Do not allow a bench to become a tree.
- Do not allow a tree to become a bush.
- Do not allow a path to change shape.
- Do not allow background houses to shift.
- Do not allow landmarks to slide or morph.

Use language such as:

"The background is locked from the first frame. Do not repaint the set. Maintain all visible benches, trees, paths and landmarks in the same relative positions throughout the shot."

---

## How to Use This Standard

In each shot file, replace the repeated sections with:

```text
Use the production generation standard (00-CORE/17_VIDEO_GENERATION_STANDARD.md).

Reference source:
Use original downloaded/exported production media only. Never use screenshots.

Episode Colour Master:
Approved original Shot 01 still.

Continuity Reference:
Previous shot video reference or exported final frame.

Previous Shot: Use the previous shot as Video Reference.
Location: Central Square.
Lighting: Warm morning light.
Ball: Same round yellow ball.
```

This keeps shot files short and maintainable.

---

## Mandatory Application Rule

This standard applies to ALL episodes and ALL shots.

Every shot file must include:
- Background Object Lock section (after Environment Anchors or after the episode-specific environment description)
- Background persistence sentence in the Visual Prompt
- Intra-shot background drift QA checklist items

No shot may omit these sections.

No episode may skip background persistence rules.

This rule was added after discovering intra-shot background drift in generated video.

---

*Bu belge tüm shot'lar için tek kaynaktır.*
*Versiyon: 4.0 — Intra-Shot Background Persistence Fix*
