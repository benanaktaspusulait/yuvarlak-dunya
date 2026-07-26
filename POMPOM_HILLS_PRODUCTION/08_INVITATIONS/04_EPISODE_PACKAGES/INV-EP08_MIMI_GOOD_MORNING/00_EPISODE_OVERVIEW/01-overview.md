# INV-EP08: Mimi — Good Morning

## General Info
- **Series:** Pompom Hills Invitations
- **Episode:** EP08 — Mimi: Good Morning
- **Duration:** 5 seconds (1 shot × 5 sec)
- **Character:** Mimi
- **Location:** Mimi's Burrow
- **Format:** 9:16 vertical
- **Loop:** First and last frame connected

## Character Reference
- **Mimi:** #90CAF9 (soft blue), rabbit, floppy ears
- **Catchphrase:** "Let's see!"

## Production Notes
- Two-step process: still image first, then video
- @image1 = empty burrow image (provided)
- No World, no Image 2
- Camera: Fully locked

---

## Step 1: Take Shot — Generate Sleeping Mimi Still

### Purpose
Create a clean static first frame showing Mimi sleeping in the burrow.

### Take Shot Prompt (OpenArt)
```text
Use @image1 as the exact locked burrow, camera angle and composition.

Add exactly one canonical Mimi sleeping naturally in the burrow beneath the soft blanket. Mimi is a small preschool rabbit with soft blue fur #90CAF9, long floppy ears, white belly, green eyes, pink nose, soft rounded Pompom Hills proportions and her established facial design. Her head rests naturally on the pillow; both eyes are gently closed and her mouth is closed with a peaceful sleeping expression. Only her head, ears, upper body and a small part of her arms are visible above the blanket. Her correctly proportioned body lies naturally beneath the blanket.

Preserve @image1 exactly: same burrow, pillows, blanket, window, decorations, lighting, camera angle and framing. Do not move, replace, add or remove any burrow element. Preserve the warm morning sunlight. Apply the soft Pompom Hills 3D look: gentle pastel colours, medium-low contrast, matte rounded materials, soft clean surfaces and gentle sharpness.

Create one clean static first frame for Shot 01. No motion, text or captions.
```

### Negative Prompt
```text
awake Mimi, open eyes, sitting, standing, open mouth, teeth, extra character, duplicate Mimi, wrong ears, missing floppy ears, adult proportions, oversized Mimi, tiny Mimi, floating body, body outside burrow, malformed hands, extra limbs, blanket covering face, burrow redesign, changed bed, moved furniture, new props, camera change, photorealism, harsh contrast, oversaturation, HDR, excessive sharpness, glossy plastic, dark lighting, blur, text, watermark
```

### OpenArt Settings
- Mode: Take Shot (still image)
- @image1: Empty burrow image (provided)
- World: None
- Image 2: None
- Prompt enhancer: Off
- Cinematic/auto camera: Off

---

## Step 2: Video Shot 01 — Good Morning

### Purpose
Mimi wakes up in burrow, ears perk up, smiles, sits up.

### Visual Prompt (OpenArt)
```text
Duration: 5 seconds.

Use @image1 as the exact locked first frame and only visual continuity source. Preserve Mimi, the burrow, blanket, window, lighting, colours, proportions and camera exactly; do not redesign or reframe.

Mimi soft blue #90CAF9 with long floppy ears begins asleep in the cozy burrow exactly as in @image1. At 0.3s she gently opens both eyes once, ears perk up with curiosity. At 0.8s Mimi says clearly in her canonical voice: "Good morning!" While speaking, she makes one small cozy stretch. At 3.2s she smoothly sits upright and turns her open-eyed gaze toward the sunny window. End with Mimi still seated safely in the burrow, mouth closed, smiling softly. Stable camera; warm pastel morning light; soft matte surfaces; no music, text or captions.
```

### Negative Prompt
```text
low quality, blur, facial distortion, extra limbs, duplicate character, sudden hopping, jumping, running, teleporting, pose snap, camera movement, angle change, burrow redesign, prop changes, harsh contrast, oversaturation, HDR, excessive sharpness, glossy plastic surfaces, dark lighting, text, captions, watermark, background music
```

### Dialogue
Mimi: "Good morning!"

### OpenArt Settings
- Duration: 5 seconds
- @image1: Generated sleeping Mimi still from Step 1
- Prompt enhancer: Off
- Cinematic/auto camera: Off

---

*Created: 26 July 2026*
