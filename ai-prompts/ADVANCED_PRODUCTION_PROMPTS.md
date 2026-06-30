# Pompom Hills - Advanced Production Prompts

Next-stage AI prompts for motion, camera variation, lighting mood, expression clarity, and global palette references.

Use this file after the base references in `ai-prompts/VISUAL_REFERENCES.md`, the environment prompts in `ai-prompts/ENVIRONMENT_PROMPTS.md`, and the sheet prompts in `ai-prompts/TECHNICAL_SHEETS.md` are approved.

## 1. Advanced Master Style

Append this style line to advanced prompts unless a specific prompt overrides it.

```text
Pompom Hills world, soft 3D cartoon animation style, rounded shapes, pastel colours, warm gentle lighting, soft matte clay texture, toy-like appearance, toddler-safe, emotionally clear, clean composition, no sharp edges, no realistic textures, no scary darkness, no harsh movement, no extra characters, no watermark
```

## 2. Character Expression Sheet - Kiko Emotions

This prompt intentionally adds a nervous/scared expression, but it must remain gentle and preschool-safe.

```text
A 2x3 grid character design sheet of Kiko from Pompom Hills, six isolated headshots on a plain white background. Kiko is a 3-4 year old human girl with a rounded soft face, warm brown hair #8D6E63 in two small pigtails, big brown eyes #795548, rosy cheeks, coral pink long-sleeve shirt #F8BBD0 visible at the collar, and soft toy-like proportions. Six clear child-friendly emotions: 1. Happy, smiling wide; 2. Surprised, eyes wide open and small O-shaped mouth; 3. Sad, tiny teary eyes and pouty lip; 4. Curious, head tilted with gentle raised brow; 5. Sleepy, half-closed eyes and small yawn; 6. Nervous, hands on cheeks with one tiny sweat drop, never scary. Consistent face shape, consistent colours, plush doll texture, studio lighting, 2.5D soft 3D render, no background, no extra characters, 3:2
```

## 3. Action Scene - Rolling Down The Hill

Use this as an action/motion test. Movement should feel playful and slow enough for toddlers, not chaotic.

```text
A dynamic wide shot of Kiko, Mimi, and Opa from Pompom Hills gently rolling down a giant soft round green hill like playful toy balls. Kiko is laughing with rounded arms spread out, wearing her coral pink shirt #F8BBD0, white shorts #FFFFFF, coral socks and shoes; Mimi is a soft blue baby rabbit #90CAF9 wearing a soft yellow t-shirt #FFF59D, floppy ears floating backward; Opa is a compact warm green owl #A5D6A7 with golden glasses #FFD54F slightly tilted, orange beak #FF7043, brown shawl #A1887F, and wings tucked in. Soft motion blur on the grass, gentle curved speed lines, bright sunny sky, everything circular and rounded, 3D claymation style, dynamic low camera angle, vibrant but pastel colours, toddler-safe, no hard impact, no fear, 16:9
```

## 4. Environment - Pompom Hills At Night

Use this to generate the night version of the master valley plate.

```text
The same Pompom Hills valley at magical safe nighttime, soft rounded hills glowing gently in moonlight, the Big Pompom Tree visible in the village square, round houses with warm circular windows, a giant curved crescent moon with a cute sleepy face smiling in the starry sky, small yellow glowing firefly dots floating around a curved treehouse, soft navy blue #5C6BC0 and gentle purple accents, never black, dreamy and cosy atmosphere, soft glowing lighting, 3D animated movie background, no sharp edges, no scary darkness, no characters, calm preschool bedtime mood, 16:9
```

## 5. Top-Down View - The Round World

Use this as a camera-angle and composition reference for the Yuvarlak Dunya theme.

```text
Top-down aerial view, bird's-eye composition of Kiko and Mimi lying on their backs on soft grass in Pompom Hills, holding hands and looking up at the camera. Kiko has warm brown pigtails #8D6E63, coral pink shirt #F8BBD0, white shorts #FFFFFF, coral socks and shoes; Mimi is a soft blue baby rabbit #90CAF9 with long floppy ears, green eyes #66BB6A, pink nose #F48FB1, and soft yellow t-shirt #FFF59D. They are surrounded by round colourful soft toys: a red ball, a yellow hoop, a blue beach ball, and a pastel globe toy. The grass forms a perfect circular shape around them, flat readable composition with soft 3D depth, simplified shapes for animation reference, clear gentle shadows, toddler-safe, 1:1
```

## 6. Camera Angle Guide - Worm's-Eye Hill

Use this to expand beyond front and wide shots while keeping the camera friendly.

```text
Worm's-eye view from the bottom of a soft rounded green hill in Pompom Hills, looking up at Kiko, Mimi, and Opa standing safely at the top edge and smiling down toward the camera. The hill fills the foreground as one large curved shape, the sky is bright light blue #BBDEFB with round white clouds, Kiko is tallest, Mimi slightly shorter, Opa compact and round. Gentle perspective, no danger, no steep cliff feeling, soft 3D cartoon animation style, rounded pastel toy world, clean composition, 16:9
```

## 7. Color Palette Reference - Pompom Hills

This prompt intentionally allows visible labels and hex codes because the goal is a palette reference chart.

```text
A flat-lay design showing 12 square color swatches arranged in a clean 3x4 grid, each swatch clearly labeled with name and hex code. Soft pastel palette for Pompom Hills: Day Sky #BBDEFB, Sunset Pink #FFD1DC, Grass Mint #C8E6C9, Hill Yellow #FFF59D, Tree Green #A5D6A7, Cloud White #FFFFFF, Sun Cream #FFF9C4, Night Blue #5C6BC0, Star Gold #FFD54F, Kiko Coral #F8BBD0, Mimi Blue #90CAF9, Opa Green #A5D6A7. Minimalist white background, rounded square swatches, clean preschool production palette chart, flat vector art, 3:2
```

## 8. Advanced Usage Order

1. Generate the `Color Palette Reference` first if the visual team needs a single palette card.
2. Generate `Kiko Emotions` before episode-specific facial acting.
3. Generate `Pompom Hills At Night` from the approved master valley reference.
4. Generate `Top-Down View` and `Worm's-Eye Hill` as camera-angle tests.
5. Generate `Rolling Down The Hill` last, after character identity and scale are locked.

## 9. Advanced QA Checklist

- Action remains gentle, rounded, and safe.
- Night scenes are blue and cosy, never black or frightening.
- Kiko keeps coral pink #F8BBD0 and white #FFFFFF clothing.
- Mimi stays soft blue #90CAF9 and wears yellow #FFF59D.
- Opa stays compact, round, warm green #A5D6A7, with golden glasses #FFD54F.
- The trio scale remains Kiko tallest, Mimi slightly shorter, Opa compact and round.
- Camera angles add variety without making the scene feel dangerous.
- Palette charts are the only prompts in this pack that should contain visible text.
