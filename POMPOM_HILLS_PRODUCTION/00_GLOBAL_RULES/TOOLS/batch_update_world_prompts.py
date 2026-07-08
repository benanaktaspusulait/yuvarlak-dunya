#!/usr/bin/env python3
"""
Batch update hero view openart prompts to production-safe format.
Updates S01 worlds that haven't been updated yet.
"""

import os
import glob

BASE = "/Users/benanaktas/project/video/yuvarlak-dunya/POMPOM_HILLS_PRODUCTION/02_WORLDS"
DONE = {"BUTTERFLY_MEADOW", "RAINBOW_BRIDGE", "MUSIC_HILL"}

# S01 worlds that need updating
S01_WORLDS = [
    "CENTRAL_SQUARE",
    "KIKOS_HOME", 
    "FLOWER_HILL",
    "MIMIS_BURROW",
    "LITTLE_FOREST",
    "STONE_HILL",
    "OPA_TREE",
    "CLOUD_HILL",
]


def read_bible_summary(world_dir):
    """Read first 80 lines of bible to get world identity."""
    bible_dir = os.path.join(world_dir, "00_CANON")
    if not os.path.exists(bible_dir):
        return None
    bible_files = glob.glob(os.path.join(bible_dir, "*bible*.md"))
    if not bible_files:
        return None
    with open(bible_files[0], 'r') as f:
        return f.read()[:3000]


def read_existing_prompt(prompt_path):
    """Read existing prompt to extract the text prompt section."""
    with open(prompt_path, 'r') as f:
        content = f.read()
    return content


def generate_production_safe_prompt(world_name, bible_summary, existing_prompt):
    """Generate a production-safe prompt based on world identity."""
    
    # Extract key identity elements from bible
    identity_elements = []
    forbidden_elements = []
    
    if bible_summary:
        low = bible_summary.lower()
        
        # Detect world type
        if 'meadow' in low or 'çimenlik' in low:
            world_type = "meadow"
        elif 'hill' in low or 'tepe' in low:
            world_type = "hill"
        elif 'forest' in low or 'orman' in low:
            world_type = "forest"
        elif 'bridge' in low or 'köprü' in low:
            world_type = "bridge"
        elif 'tree' in low or 'ağaç' in low:
            world_type = "tree"
        elif 'pond' in low or 'gölet' in low:
            world_type = "pond"
        elif 'home' in low or 'ev' in low:
            world_type = "home"
        elif 'garden' in low or 'bahçe' in low:
            world_type = "garden"
        else:
            world_type = "world"
    
    return f"""# {world_name.replace('_', ' ').title()} — OpenArt World Builder Prompt

## Purpose

This file is only the OpenArt World Builder input guide for {world_name.replace('_', ' ')}.

- The approved {world_name.replace('_', ' ')} Hero View is the primary input.
- Text is secondary only.
- `02-world-spec.md` remains the full production reference.
- Do not paste the full spec into OpenArt World Builder.

---

## World Builder Reality Check

OpenArt World Builder is a 3D spatial extrapolation tool. It may not perfectly follow detailed prompt rules. It may reinterpret objects, flatten space, sharpen textures, or add unwanted clutter. Because of this, the approved Hero View image must be treated as the highest-fidelity source.

---

## Required Input Method

### Best Method — 1 Image Mode

- Upload the approved {world_name.replace('_', ' ')} Hero View.
- Use the prompt below only as a supplementary style and layout hint.
- The image is the primary instruction.
- Do not add character references.
- Do not add episode shots.
- Do not add failed generations.

### 2–4 Image Mode

- If OpenArt disables the text field after uploading multiple images, that is expected.
- In that case, the images become the instruction.
- Use only canon-consistent views.
- All images must match lighting, colour palette, material style, and camera height.
- Do not mix different styles or generations.

Recommended views:

- Image 1 / Front: approved Hero View, all identity elements visible.
- Image 2 / Back: reverse view, same palette.
- Image 3 / Left: side view showing layout and depth.
- Image 4 / Right optional: closer detail, not macro.

---

## OpenArt Text Prompt — Use Only In 1 Image Mode

```
Create a soft, preschool-friendly world called {world_name.replace('_', ' ')}. Use the uploaded approved Hero View as the primary reference and preserve its layout, lighting, colour palette, camera feeling, and soft toy-like handcrafted style.

The world should feel warm, safe, and inviting. Keep the composition wide, readable, and reusable as a permanent world reference. Child-eye camera height, warm morning light, soft sky, gentle natural depth, medium-low contrast, matte handcrafted toy-set materials, rounded shapes, no sharp realism.

Preserve the same warm sunlight direction as the uploaded Hero View. Keep shadows soft and gentle.

Pompom Hills preschool animation style: soft pastel colours, matte handcrafted toy-like surfaces, rounded safe shapes, gentle storybook charm, warm and peaceful atmosphere.

No characters. No children. No rabbits. No animals. No birds. No giant foreground objects. No cropped edge objects. No buildings. No signs. No text. No labels. No arrows. No fences. No roads. No cars. No modern objects. No dark shadows. No sharp corners. No clutter. No HDR. No glossy plastic. No harsh shadows. No high contrast. No oversharpening. No saturated neon colours.
```

---

## Negative Prompt / Forbidden Output

```
characters, children, Kiko, Mimi, Noah, Arda, Luca, Opa, rabbits, animals, birds, giant flowers, foreground flower close-up, cropped flowers at frame edge, cropped objects, clutter, dense forest, dark forest, buildings, houses, signs, labels, readable text, arrows, fences, roads, vehicles, water, river, stream, pond, bridge, waterfall, night, sunset, moon, stars, harsh shadows, high contrast, HDR, glossy plastic, glossy CGI, oversharpened, realistic textures, photorealism, sharp corners, neon colours, over-saturated colours
```

---

## Identity Lock

{world_name.replace('_', ' ')} must read as:

- its own unique identity from the approved Hero View
- soft pastel Pompom Hills style
- warm, safe, preschool atmosphere
- matte handcrafted toy-set materials

It must NOT read as:

- a different Pompom Hills world
- a realistic environment
- a generic stock location
- a dark or scary place

---

## Production QA After World Build

- [ ] Is the world still recognisable as {world_name.replace('_', ' ')} from silhouette and layout?
- [ ] Are there no characters or animals?
- [ ] Are there no giant foreground objects or cropped edge objects?
- [ ] Is the style still soft pastel, matte, toy-like, preschool-safe?
- [ ] Is contrast medium-low?
- [ ] Is there no HDR, glossy CGI, oversharpening, or harsh shadow drift?
- [ ] Is there no text, sign, symbol, fence, road, building, or water?
- [ ] Does it match the approved Hero View more than the text prompt?

---

## Final Usage Note

Use the generated World Builder output only after QA. If it adds unwanted elements, glossy/HDR contrast, or drifts from the approved Hero View, reject the world and regenerate. Do not treat a failed world as canon.
"""


def main():
    updated = 0
    
    for world_name in S01_WORLDS:
        if world_name in DONE:
            continue
            
        world_dir = os.path.join(BASE, world_name)
        prompt_path = os.path.join(world_dir, "01_HERO_VIEW", "03-openart-prompt.md")
        
        if not os.path.exists(prompt_path):
            print(f"⚠️ {world_name}: No openart prompt found")
            continue
        
        # Read existing content
        with open(prompt_path, 'r') as f:
            old_content = f.read()
        
        # Read bible for identity
        bible_summary = read_bible_summary(world_dir)
        
        # Generate new content
        new_content = generate_production_safe_prompt(world_name, bible_summary, old_content)
        
        # Only update if significantly different
        if len(new_content) > len(old_content) * 1.5:
            with open(prompt_path, 'w') as f:
                f.write(new_content)
            print(f"✅ {world_name}: Updated ({len(old_content)} → {len(new_content)} chars)")
            updated += 1
        else:
            print(f"⏭️ {world_name}: Already adequate ({len(old_content)} chars)")
    
    print(f"\nUpdated {updated}/{len(S01_WORLDS)} worlds")


if __name__ == "__main__":
    main()
