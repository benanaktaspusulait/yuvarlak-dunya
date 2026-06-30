# Pompom Hills - Technical Sheet Prompts

Reference-sheet, consistency, prop, expression, and storyboard prompts for locking Pompom Hills character and production continuity.

Use this file with `ai-prompts/VISUAL_REFERENCES.md`. That file defines the locked character descriptions; this file turns those descriptions into repeatable production sheets.

## 1. Reference Asset Naming

Use stable filenames for approved reference images so every prompt can point to the same source.

| Asset | Suggested Name | Purpose |
| --- | --- | --- |
| Master world reference | `pompom-hills_world_master_16x9` | Environment colour, lighting, and shape language |
| Kiko front view | `kiko_front_locked` | Kiko identity reference |
| Mimi front view | `mimi_front_locked` | Mimi identity reference |
| Opa front view | `opa_front_locked` | Opa identity reference |
| Trio scale chart | `trio_scale_locked` | Relative height and body proportions |
| Main style frame | `pompom-hills_style_locked` | Overall render texture and softness |

## 2. Master Style Suffixes

### OpenArt / General Image Tool Suffix

```text
soft 3D cartoon animation style, rounded shapes, pastel colours, warm gentle lighting, soft matte clay texture, toy-like appearance, toddler-safe, clean white or simple pastel background, consistent proportions, no sharp edges, no realistic texture, no text, no watermark
```

### Midjourney v6 Suffix

```text
--style raw --s 250 --v 6.0
```

When reference images exist, append image URLs and weights at the end of the prompt.

```text
--cref [CHARACTER_REFERENCE_IMAGE_URL] --cw 100 --sref [STYLE_REFERENCE_IMAGE_URL] --sw 200
```

For trio and scene prompts, use multiple character reference URLs before the text prompt when the tool supports it.

### SDXL / Stable Diffusion Notes

Use the same positive prompt body plus these settings as a starting point:

```text
steps 30, cfg 6.5, sampler DPM++ 2M Karras, size 1536x1024 for 3:2 sheets, size 1792x1024 for 16:9 scenes
```

Use approved character and style images through IP-Adapter, ControlNet Reference, or the closest available reference-image workflow in the chosen tool.

## 3. Character Turnaround Sheets

### Kiko Turnaround Sheet

```text
Character turnaround sheet of Kiko from Pompom Hills, same character repeated four times on one clean white background: front view, side profile view, back view, and 3/4 view. Kiko is a 3-4 year old human girl with a rounded soft body, round face, warm brown hair #8D6E63 in two small pigtails, brown eyes #795548, rosy cheeks, coral pink long-sleeve shirt #F8BBD0 with round collar, white soft shorts #FFFFFF, coral pink socks, and round coral pink shoes #F8BBD0. Consistent proportions across all views, simple rounded hands with no fingers, soft toy-like appearance, uniform studio lighting, soft 3D cartoon animation style, no shadows on face, no extra characters, 3:2
```

### Mimi Turnaround Sheet

```text
Character turnaround sheet of Mimi from Pompom Hills, same character repeated four times on one clean white background: front view, side profile view, back view, and 3/4 view. Mimi is a cute baby rabbit with rounded soft body, soft blue fur #90CAF9, white belly #FFFFFF, long floppy soft blue ears with pale pink inner ears, green eyes #66BB6A, pink nose #F48FB1, small white tail #FFFFFF, and a soft yellow t-shirt #FFF59D with round collar. Mimi must remain soft blue, never lavender. Consistent proportions, ears stay floppy and rounded, soft toy-like appearance, uniform studio lighting, soft 3D cartoon animation style, no extra characters, 3:2
```

### Opa Turnaround Sheet

```text
Character turnaround sheet of Opa from Pompom Hills, same character repeated four times on one clean white background: front view, side profile view, back view, and 3/4 view. Opa is a medium-sized round wise owl with warm green feathers #A5D6A7, light green belly #C8E6C9, warm brown eyes #795548, round golden glasses #FFD54F, orange beak #FF7043, small orange feet #FF7043, short rounded wings, and a soft brown shawl #A1887F around the shoulders. Consistent compact round proportions, calm gentle expression, soft toy-like appearance, uniform studio lighting, soft 3D cartoon animation style, no extra characters, 3:2
```

## 4. Scale And Proportion Charts

### Trio Scale Chart

```text
Pompom Hills trio height comparison chart on a clean white background with simple pale measuring guide lines and no text: Kiko is tallest, a 3-4 year old human girl with warm brown pigtails #8D6E63, coral pink shirt #F8BBD0, white shorts #FFFFFF, coral pink socks and shoes; Mimi is slightly shorter, a soft blue baby rabbit #90CAF9 with white belly #FFFFFF, green eyes #66BB6A, pink nose #F48FB1, long floppy ears, and soft yellow t-shirt #FFF59D; Opa is medium-sized, compact, and round, with warm green feathers #A5D6A7, light green belly #C8E6C9, golden glasses #FFD54F, orange beak #FF7043, and brown shawl #A1887F. All stand on the same flat baseline, looking at camera, smiling gently, soft 3D cartoon animation style, consistent proportions, 16:9
```

### Hands, Feet, Ears, Wings Detail Sheet

```text
Pompom Hills character detail sheet showing close-up reference details on a clean white background: Kiko's round hands, coral pink shoes, and small pigtails; Mimi's floppy soft blue ears, round paws, white tail, and yellow t-shirt collar; Opa's round golden glasses, soft orange beak, short rounded wings, and brown shawl. All details are soft, plush, rounded, simple, toddler-safe, pastel colours, soft 3D cartoon animation style, no text, no extra characters, 3:2
```

## 5. Expression And Emotion Sheets

### Kiko Emotion Sheet

```text
Kiko expression sheet reference, same Kiko repeated in eight small head-and-shoulder views on one clean white background, unchanged warm brown pigtails #8D6E63, brown eyes #795548, coral pink shirt #F8BBD0 visible at collar, rosy cheeks, soft round face. Expressions: happy, curious, surprised, shy, sleepy, proud, gentle sad, calm. Each expression is instantly readable for toddlers, never scary, soft toy-like 3D cartoon animation style, no text, no extra characters, 3:2
```

### Mimi Emotion Sheet

```text
Mimi expression sheet reference, same soft blue baby rabbit repeated in eight small head-and-shoulder views on one clean white background, unchanged soft blue fur #90CAF9, pale pink inner ears, green eyes #66BB6A, pink nose #F48FB1, soft yellow t-shirt #FFF59D visible at collar. Expressions: happy, curious, surprised, shy, sleepy, excited, gentle sad, calm. Ears help show emotion but stay rounded and soft, soft 3D cartoon animation style, no text, no extra characters, 3:2
```

### Opa Emotion Sheet

```text
Opa expression sheet reference, same warm green round owl repeated in eight small head-and-shoulder views on one clean white background, unchanged golden glasses #FFD54F, warm brown eyes #795548, orange beak #FF7043, light green belly #C8E6C9, soft brown shawl #A1887F visible at shoulders. Expressions: wise smile, encouraging, surprised, concerned, proud, sleepy, happy, calm. Gentle and readable, never stern or scary, soft 3D cartoon animation style, no text, no extra characters, 3:2
```

### Emotion Transition Strip

```text
Four-frame emotion transition strip for Kiko and Mimi in Pompom Hills, clean white background, simple rounded frame boxes with no text. Frame 1 curious, Frame 2 surprised, Frame 3 relieved, Frame 4 happy. Kiko and Mimi keep locked colours and outfits, body language changes only gently, expressions are clear for toddlers, soft 3D cartoon animation style, 16:9
```

## 6. Prop Sheets

### Mimi's Magnifying Glass

```text
Standalone prop sheet of Mimi's child-friendly oversized round magnifying glass, soft pastel blue handle #90CAF9, bright yellow plastic frame #FFF59D, round lens reflecting a tiny soft rainbow, looks like a safe rubber toy with no sharp edges, isolated on a plain soft pink background, studio product photography style, 3D clay render, no character, no text, 1:1
```

### Rolling Apple

```text
Standalone prop sheet of a round red apple for Pompom Hills, oversized toddler-safe toy-like apple with soft glossy surface, tiny rounded green leaf, no hard stem point, shown from front, side, and 3/4 view on a clean white background, soft 3D cartoon animation style, no text, 3:2
```

### Round Balloon

```text
Standalone prop sheet of a soft round balloon for Pompom Hills, pastel yellow balloon with short rounded string, safe toy-like material, gentle shine, shown floating and held low at toddler height, isolated on clean pastel background, soft 3D cartoon animation style, no text, 1:1
```

### Soft Globe Toy

```text
Standalone prop sheet of a soft round globe toy, pastel blue oceans, soft green and yellow rounded continents, no tiny labels, no country borders, plush rubber texture, friendly educational object for the Yuvarlak Dunya theme, isolated on clean white background, soft 3D cartoon animation style, 1:1
```

### Opa's Story Pebbles

```text
Standalone prop sheet of Opa's story pebbles, five smooth round pastel stones arranged in a small circle, each stone has a simple embossed shape icon such as circle, heart, cloud, flower, and star, no written text, soft matte texture, toddler-safe, clean white background, 3D clay render, 1:1
```

## 7. Storyboard Prompts

### Storyboard - The Rolling Apple

```text
A 4-panel storyboard sequence in a single image with rounded panel borders and no written text. Panel 1: Kiko sees a round red apple rolling down a soft green hill in Pompom Hills. Panel 2: Mimi gently chases the apple, ears bouncing, playful but safe. Panel 3: Opa glides down holding the apple softly with rounded wings. Panel 4: Kiko, Mimi, and Opa laugh together while holding the apple. Clear toddler-readable expressions, simple sketchy line art with soft watercolor shading, rounded frames, child book illustration style, 16:9
```

### Storyboard - The Round World Discovery

```text
A 4-panel storyboard sequence in a single image with rounded panel borders and no written text. Panel 1: Kiko finds a soft globe toy in the Oyun Evi playhouse. Panel 2: Mimi rolls the globe gently and watches it turn. Panel 3: Opa points to the round shape with a warm teaching smile. Panel 4: all three hug the globe under floating round stars. Soft watercolor storyboard look, simple clear poses, gentle wonder, toddler-safe, 16:9
```

### Storyboard - Gentle Gravity

```text
A 4-panel storyboard sequence in a single image with rounded panel borders and no written text. Panel 1: Kiko places a soft ball at the top of a rounded hill. Panel 2: the ball rolls slowly down the curved path. Panel 3: Mimi waits at the bottom with open paws. Panel 4: the ball stops safely in a round flower patch and everyone smiles. Simple educational preschool storyboard, soft line art, pastel watercolor shading, 16:9
```

## 8. Sheet QA Checklist

- Every sheet uses the locked names Kiko, Mimi, and Opa.
- Kiko always has coral pink #F8BBD0 and white #FFFFFF clothing.
- Mimi is always soft blue #90CAF9 and wears the yellow t-shirt #FFF59D.
- Opa always has warm green #A5D6A7 feathers, golden glasses #FFD54F, and brown shawl #A1887F.
- Kiko is tallest, Mimi is slightly shorter, and Opa is compact and round.
- Reference sheets use clean backgrounds and avoid extra characters.
- Storyboards use rounded panels and no written text inside the image.
- Props are oversized, soft, and safe for a 3-4 year old audience.
