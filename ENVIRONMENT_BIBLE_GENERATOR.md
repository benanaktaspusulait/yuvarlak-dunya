# ENVIRONMENT BIBLE GENERATOR PROMPT v3.0

---

## Kullanım

Bu prompt'u Claude, ChatGPT veya Gemini'ye ver. **3 adımda** çalışır:

1. `WORLD_BUILD_DESCRIPTION.md`'yi ver (context)
2. Bu prompt'u ver
3. Sadece 3 değişkeni doldur: `LOCATION NAME`, `ENVIRONMENT ID`, `HERO IMAGE`

**500+ satırlık prompt hiç değişmez.** 24 mekan için aynı kalite, aynı format.

---

## Değişkenler (Sadece bunları değiştir)

```text
LOCATION NAME = Central Square
ENVIRONMENT ID = ENV-001
HERO IMAGE = 1-central-square.png
```

---

## Prompt

```text
You are a Senior Environment Artist, Production Designer, World Builder and Art Director at Pixar Animation Studios.

Your task is to create ONE COMPLETE ENVIRONMENT BIBLE for the world of Pompom Hills.

This is NOT a story.

This is NOT concept art.

This is NOT an image prompt.

Your job is to create the official production documentation for ONE location that will be reused consistently across hundreds of episodes.

The audience is:

• OpenArt AI
• Environment Artists
• Storyboard Artists
• Animators
• Children's Book Illustrators
• Game Designers

The location must NEVER visually change between episodes.

--------------------------------------------------

REFERENCE DOCUMENTS

The WORLD_BUILD_DESCRIPTION.md is the absolute source of truth.

Never contradict it.

Never invent another visual language.

Never change colors.

Never change proportions.

Never change atmosphere.

Use it as the master reference.

--------------------------------------------------

LOCATION

Environment Name:
**{LOCATION NAME}**

Environment ID:
**{ENVIRONMENT ID}**

Hero Image:
**{HERO IMAGE}**

--------------------------------------------------

GOAL

Create a complete Environment Bible detailed enough that another artist could rebuild this location WITHOUT ever seeing the original artwork.

Length is not important.

Completeness is important.

Never repeat yourself.

Prefer structured information over prose.

Avoid unnecessary explanations.

Focus on reproducible visual information.

Every sentence should help an AI recreate the environment consistently.

--------------------------------------------------

WRITE THE DOCUMENT IN MARKDOWN.

Use the following structure.

# 1. Basic Information

Environment Name

Environment ID

Version

Purpose

Story Function

Keywords

Primary Emotion

Secondary Emotion

Educational Purpose

Visual Identity

Environment Category

--------------------------------------------------

# 2. World Position

Describe exactly where this environment is located inside Pompom Hills.

Include:

Neighbour environments

Walking paths

Distances

Travel times

Visible landmarks

Hidden landmarks

Connections

Navigation logic

How children normally arrive.

--------------------------------------------------

# 3. Visual DNA

This is the most important section.

Describe the fundamental visual building blocks.

Primary Shapes:
Circle percentage
Oval percentage
Rectangle percentage
Triangle percentage

Forbidden Shapes:
List all shapes that must NEVER appear.

Roundedness Rules:
How rounded everything must be.

Silhouette Rules:
How silhouettes must read.

Negative Space Rules:
How much empty space is required.

Shape Language:
What shapes communicate.

--------------------------------------------------

# 4. Object Inventory

List EVERY object that exists in this environment.

Count each object type.

Format:

[Number] [Object Name]

Examples:
1 Big Pompom Tree
8 Flower Beds
14 Stepping Stones
2 Wooden Benches
1 Mailbox
3 Bushes
18 Round Flowers
4 Paths

This ensures OpenArt generates consistent object counts.

--------------------------------------------------

# 5. Hero View

Describe the iconic hero composition.

Camera position

Lens

Height

Angle

Foreground

Middle ground

Background

Lighting

Color balance

Composition

Mood

Negative space

Visual hierarchy

--------------------------------------------------

# 6. Camera Safe Zones

Define which camera angles work and which to avoid.

Hero Camera:
Always works. Describe why.

North Camera:
Works or Avoid. Explain.

South Camera:
Works or Avoid. Explain.

East Camera:
Works or Avoid. Explain.

West Camera:
Works or Avoid. Explain.

Low Angle:
Works or Avoid. Explain.

High Angle:
Works or Avoid. Explain.

Close-Up Safe:
Which objects can be close-up.

Close-Up Forbidden:
Which objects must never be close-up.

--------------------------------------------------

# 7. 360 Degree Reference

Create separate descriptions for:

Front View

Back View

Left View

Right View

Top View

Bird's Eye View

Ground View

Child Eye Level

Close Detail View

Each description must explain EXACTLY what can be seen.

--------------------------------------------------

# 8. Spatial Layout

Describe the environment like an architectural plan.

Ground shape

Relative positions

Tree placement

Flower beds

Paths

Entrances

Exits

Distances

Safe play areas

Interaction zones

Everything.

--------------------------------------------------

# 9. Exterior Design

Describe every visual element.

Ground

Grass

Textures

Colors

Trees

Leaves

Flowers

Sky visibility

Cloud visibility

Rocks

Stones

Paths

Shadows

Background

Silhouettes

Visual rhythm

Shape language

--------------------------------------------------

# 10. Permanent Objects

Everything that always exists.

Describe every object.

Location

Material

Color

Scale

Purpose

Never changing.

--------------------------------------------------

# 11. Optional Props

Objects that may appear depending on the story.

Placement rules.

Maximum quantity.

Purpose.

Frequency.

--------------------------------------------------

# 12. Vegetation

Every plant.

Every flower.

Grass.

Bushes.

Tree species.

Seasonal changes.

Movement.

Density.

Colors.

--------------------------------------------------

# 13. Materials

Describe every material.

Grass

Stone

Wood

Leaves

Flowers

Water

Paint

Clay

Fabric

Glass

Everything.

--------------------------------------------------

# 14. Lighting Bible

Morning

Late Morning

Noon

Afternoon

Golden Hour

Sunset

Blue Hour

Night

Moonlight

Rain

Fog

Snow

Shadow behavior

Color temperature

Bounce light

Ambient light

--------------------------------------------------

# 15. Weather

Sunny

Rain

Wind

Fog

Snow

Rainbow

How the environment changes.

--------------------------------------------------

# 16. Seasons

Spring

Summer

Autumn

Winter

Describe how every object changes.

Describe what never changes.

--------------------------------------------------

# 17. Environment Motion

Everything that moves.

Trees

Leaves

Flowers

Grass

Clouds

Birds

Butterflies

Fireflies

Wind

Animation timing

Animation loops

--------------------------------------------------

# 18. Sound Design

Near sounds

Far sounds

Morning

Evening

Night

Weather sounds

Ambient loops

Random sounds

Forbidden sounds

--------------------------------------------------

# 19. Smell

Morning smell

Rain smell

Summer smell

Winter smell

Describe the atmosphere using scent.

--------------------------------------------------

# 20. Camera Rules

Hero Shot

Wide Shot

Medium Shot

Close Shot

Tracking Shot

Establishing Shot

Top Shot

Forbidden Angles

Lens suggestions

Camera height

--------------------------------------------------

# 21. Character Interaction Map

Define exactly where characters interact with this environment.

Kiko: Where does she usually stand? Where does she enter?

Mimi: Where does he usually stand? Where does he enter?

Opa: Where does he land? Where does he observe from?

Children: Where do they play? Where do they sit?

Adults: Where do they stand? Where do they never go?

Interaction zones

Safe areas

Forbidden areas

Eye directions

Blocking rules

--------------------------------------------------

# 22. Story Possibilities

Generate at least 30 story ideas that naturally happen ONLY inside this environment.

--------------------------------------------------

# 23. World Rules

Things always true.

Things never happen.

Forbidden objects.

Forbidden architecture.

Forbidden colors.

Forbidden technology.

--------------------------------------------------

# 24. Negative Prompt Rules

Define what must NEVER be generated for this environment.

List specific objects, textures, colors, and elements to avoid.

Format:

Never generate:
[list]

Never show:
[list]

Never include:
[list]

This section is critical for OpenArt consistency.

--------------------------------------------------

# 25. AI Consistency Rules

Write practical rules that guarantee OpenArt recreates exactly the same location every time.

Focus on:

Object counts

Color consistency

Spatial relationships

Camera angles

Lighting consistency

Material consistency

--------------------------------------------------

# 26. OpenArt Environment Module

Finally write a professional OpenArt Environment Module.

Length: 250–350 words.

This module will always be placed AFTER the MASTER CORE prompt.

Do NOT repeat information already contained in the MASTER WORLD.

Describe ONLY this specific environment.

Focus on:

Geometry

Composition

Spatial consistency

Object consistency

Camera consistency

Color consistency

--------------------------------------------------

WRITING STYLE

Write like a Pixar production bible.

Everything must be visually reproducible.

Every sentence should help another artist recreate the location perfectly.

Never write generic descriptions.

Never use vague words.

Describe exact visual relationships.

Think like a Production Designer, not a storyteller.

The final document should become the definitive visual reference for this location.
```

---

## v2.0'dan Farklar

| Alan | v2.0 | v3.0 |
|---|---|---|
| Uzunluk talimatı | "3000-5000 words" | "Completeness is important" |
| Visual DNA | Yok | ✅ Eklendi |
| Object Inventory | Yok | ✅ Eklendi |
| Camera Safe Zones | Yok | ✅ Eklendi |
| Character Interaction Map | Yok | ✅ Eklendi |
| Negative Prompt Rules | Yok | ✅ Eklendi |
| OpenArt Module odakı | Genel | Geometry + Composition + Consistency |

---

## Kullanım Sırası

### Adım 1: Context ver

```
[WORLD_BUILD_DESCRIPTION.md içeriğini yapıştır]
```

### Adım 2: Prompt'u ver

```
[Bu promptun tamamını yapıştır]
```

### Adım 3: Değişkenleri doldur

```
LOCATION NAME = Butterfly Meadow
ENVIRONMENT ID = ENV-020
HERO IMAGE = 17-butterfly-meadow.png
```

### Sonuç

Profesyonel Environment Bible + Visual DNA + Object Inventory + Camera Safe Zones + Negative Prompt.

---

## 24 Environment Listesi

| # | Location Name | Environment ID | Hero Image |
|---|---|---|---|
| 1 | Central Square | ENV-001 | 1-central-square.png |
| 2 | Cloud Hill | ENV-002 | 2-cloud-hill.png |
| 3 | Flower Hill | ENV-003 | 3-flower-hill.png |
| 4 | Kiko's Home | ENV-004 | 3-kikos-home.png |
| 5 | Sun Hill | ENV-005 | 4-sun-hill.png |
| 6 | Mimi's Burrow | ENV-006 | 5-mimis-burrow.png |
| 7 | Tree Hill | ENV-007 | 5-tree-hill.png |
| 8 | Opa's Tree | ENV-008 | 6-opas-tree.png |
| 9 | Stone Hill | ENV-009 | 6-stone-hill.png |
| 10 | Tillo's Garden | ENV-010 | 7-tillos-garden.png |
| 11 | Lulu's Greenhouse | ENV-011 | 8-lulus-greenhouse.png |
| 12 | Poppy's Bakery | ENV-012 | 9-poppys-bakery.png |
| 13 | Benny's Playground | ENV-013 | 10-bennys-playground.png |
| 14 | Tillo's Treehouse | ENV-014 | 11-tillos-treehouse.png |
| 15 | Milo's Pond | ENV-015 | 12-milos-pond.png |
| 16 | Rosie's Rose Garden | ENV-016 | 13-rosies-rose-garden.png |
| 17 | Lily's Lavender Farm | ENV-017 | 14-lilys-lavender-farm.png |
| 18 | Rainbow Bridge | ENV-018 | 15-rainbow-bridge.png |
| 19 | Friendship Meadow | ENV-019 | 16-friendship-meadow.png |
| 20 | Butterfly Meadow | ENV-020 | 17-butterfly-meadow.png |
| 21 | Little Forest | ENV-021 | 18-little-forest.png |
| 22 | Rainbow Creek | ENV-022 | 19-rainbow-creek.png |
| 23 | Wish Pond | ENV-023 | 20-wish-pond.png |
| 24 | Camping Grove | ENV-024 | 21-camping-grove.png |
| 25 | Story Circle | ENV-025 | 22-story-circle.png |
| 26 | Art Corner | ENV-026 | 23-art-corner.png |
| 27 | Adventure Trail | ENV-027 | 24-adventure-trail.png |

---

## Sonuç

Bu prompt bir kez yazılır.

27 kez çalıştırılır.

Sadece 3 satır değişir.

Gerisi sabittir.

Tutarlılık garantilidir.

OpenArt için optimize edilmiştir.
