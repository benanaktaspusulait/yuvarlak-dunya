# VIDEO QA SPECIFICATION

> *Canonical quality assurance specification for AI-generated video.*
> *Source of truth for: QA process, detection categories, severity levels, regeneration guidelines.*
> *Implementation-independent — works with any AI video generation tool.*

---

## Purpose

The goal of QA is NOT to judge creativity.

The goal is to detect technical problems introduced by AI generation.

The reviewer should behave like a senior animation QA engineer.

---

## General Principles

The review must focus only on production quality.

Never review:

- Story
- Dialogue
- Pacing
- Educational value
- Acting
- Music

Only review technical consistency.

---

## QA Philosophy

A scene is considered production-ready only when:

- Characters remain visually consistent
- Objects behave consistently
- The world remains coherent
- Voice identity remains identical across speaking shots
- Colour identity remains identical across all shots
- Lighting identity continues without reinterpretation
- Camera movement feels believable
- Animation artefacts are absent or negligible

Voice, colour and lighting continuity are production gates.

If any of these fail, reject the affected shot even if story, acting and composition are otherwise strong.

---

## Review Levels

### Level 1 — Frame QA

Inspect individual frames.

Focus: Static visual quality per frame.

| Check | What to Look For |
|-------|------------------|
| Character appearance | Correct colours, proportions, features |
| Object presence | All expected objects visible |
| Environment | Correct world, correct lighting |
| Rendering quality | No ghosting, no tearing, no corruption |

### Level 2 — Shot QA

Inspect each continuous shot (15 seconds).

Focus: Temporal consistency within a single shot.

| Check | What to Look For |
|-------|------------------|
| Character movement | Smooth, natural, no jitter |
| Object behaviour | Consistent position, no teleportation |
| Camera movement | Believable, no sudden jumps |
| Physics | Gravity respected, no floating objects |

### Level 3 — Scene QA

Inspect transitions between shots.

Focus: Continuity across cuts.

| Check | What to Look For |
|-------|------------------|
| Character position | Matches between shots |
| Object position | Matches between shots |
| Lighting | Consistent across shots |
| Colour identity | White balance, exposure, saturation and contrast match |
| Voice identity | Same speaking character sounds identical across shots |
| Environment | No layout changes between shots |

### Level 4 — Episode QA

Inspect consistency across the entire episode.

Focus: Global coherence.

| Check | What to Look For |
|-------|------------------|
| Character consistency | Same character throughout |
| World consistency | Same world throughout |
| Voice identity | Same character voice throughout |
| Colour identity | Episode feels colour graded as one continuous film |
| Lighting consistency | Same time of day throughout |
| Prop consistency | Same objects throughout |

---

## Production Continuity Gate

Run this gate before evaluating story, tempo or emotional flow.

Reference: `00-CORE/SHOT_PRODUCTION_STANDARD.md`

### Voice QA

| Check | Requirement |
|-------|-------------|
| Voice identity | Same character voice throughout |
| Pitch | No higher or lower drift between shots |
| Timbre | Same vocal texture and body |
| Speaking speed | Same pace and rhythm |
| Emotional tone | Same warmth and preschool energy |
| Pronunciation | Same pronunciation style |
| Accent | Same accent |
| Recording quality | Same clarity, dryness and processing |
| Narrator safety | No alternate narrator replaces the character |

### Colour QA

| Check | Requirement |
|-------|-------------|
| White balance | Identical across shots |
| Exposure | No brighter or darker shot drift |
| Colour temperature | No warmer or cooler drift |
| Saturation | Same soft pastel saturation |
| Contrast | Same low-contrast preschool finish |
| Brightness | Same perceived brightness |
| Palette | Same pastel palette |
| Grading safety | No cool shift, warm shift, green tint, magenta tint, orange grading, HDR look or cinematic LUT |

### Lighting QA

| Check | Requirement |
|-------|-------------|
| Light direction | Same direction across continuation shots |
| Light intensity | Same intensity |
| Shadow softness | Same soft preschool shadows |
| Ambient lighting | Same ambient fill |
| Highlight behaviour | Same highlight rolloff and sparkle level |
| Cloud brightness | Same brightness relationship to sky |
| Grass brightness | Same brightness relationship to environment |

Reject the shot if any Voice QA, Colour QA or Lighting QA item fails.

---

## Global OpenArt Continuity Gate

Run this gate on every generated video before approval. These checks apply to all future
Pompom Hills episodes and all worlds, not only Central Square.

### Hard Background Lock QA

Every shot must treat the environment as a fixed physical stage. Reject if any visible
background object changes position, scale, identity or layout inside the shot or between
continuity-linked shots.

Objects covered by this gate include trees, tree trunks, benches, planters, bushes,
flowerbeds, rounded paths, paving stones, stepping stones, grass patches, bunting,
flags, houses, walls, landmarks and any object visible in the first frame.

Reject if a bench becomes a planter, bush becomes tree, flowerbed becomes grass mound,
path becomes road, planter changes side of frame, object duplicates, object disappears,
or a landmark resizes, shifts, duplicates, disappears or changes silhouette.

### Intra-Shot Character Continuity QA

Character continuity must remain unbroken inside the same video clip. This applies
within a single shot, not only between shots.

Reject if any character disappears inside the same shot, reappears inside the same shot,
regenerates after occlusion, teleports, duplicates, switches sides suddenly, jumps
position, changes scale suddenly, changes identity, or becomes hidden and then appears
elsewhere.

Each character must follow one clear visible path inside the shot. The path must be
readable frame-to-frame.

### Single Visible Path QA

Characters must stay on visible walkable areas only: clear paths, paving stones,
stepping stones, clear open grass patches and open visible areas beside objects.

Reject if a character walks through bushes, flowerbeds, planters, tree trunks, benches,
houses, walls, dense grass, foreground plants, decorative objects, or any object that
should physically block them.

Reject if a character enters from one side, disappears behind an object, and exits from
another side, or changes walking direction without a clearly visible turn.

### Occlusion Is Not A Transition QA

Do not use occlusion as a transition.

Characters must not be hidden behind bushes, flowers, benches, tree trunks, planters,
walls, houses, flags or foreground plants as a way to continue or reset motion.

A tiny natural partial overlap is acceptable only if it lasts less than half a second,
does not hide the character's full body, does not hide the direction of travel, and the
character does not reappear somewhere else after the overlap.

Reject if foreground objects fully cover a character or if a character appears
regenerated after being hidden.

### Camera Continuity QA

Camera movement must protect continuity. Allowed motion is tiny push-in, tiny settle,
very slow stable drift, or nearly locked-off camera.

Reject if camera movement causes object shifting, layout morphing, character hiding,
character regeneration, camera reset, fast pan, whip pan, orbit, fast zoom, sudden angle
jump, a tracking move that changes the set layout, a reveal of a different location, or
an environment that feels regenerated.

For preschool continuity, stable visible action is more important than cinematic
movement.

### First Second Continuity Hold QA

For every continuity-linked shot, compare the previous shot final frame with the next
shot first frame. The first 1 second must hold extremely close to `@image1`.

During the first 1 second, reject if camera angle, camera height, lens feel, character
positions, character scale, background object positions, lighting or colour grading
changes; reject if any new object appears, any object disappears, any character
teleports, or any character switches sides.

After the first second, only small character motion and tiny camera settle are allowed.

### Character Action Reduction QA

If a shot has background morphing, occlusion or teleport risk, reduce character
movement. Prefer pointing, looking, head turn, tiny step, smiling, gentle reaction,
small body turn and shared still moment.

Flag shots with unnecessary walking as higher risk, especially walking across the set,
crossing behind objects, entering/exiting frame, moving behind bushes/benches/planters,
using foreground objects as transitions, or travelling from object to object inside one
short shot.

---

## Global QA Workflow For Generated Shots

For every generated shot:

1. Export first frame.
2. Export final frame.
3. Watch the full video once only for character continuity.
4. Watch the full video again only for background object stability.
5. Compare previous shot final frame with current shot first frame.
6. Check character path continuity inside the shot.
7. Check whether any character becomes fully hidden.
8. Check whether any object moves, morphs, disappears, duplicates, or changes identity.
9. Check colour and lighting against the Episode Colour Master.
10. Approve only if all checks pass.

For same-shot character continuity, QA must not only inspect first and final frames. The
full video must be watched because disappearance can happen inside the shot.

---

## Detection Categories

### 1. Object Duplication

Detect duplicated instances of the same object.

| What to Detect | Example |
|----------------|---------|
| Duplicated balls | Character throws a ball, another ball remains |
| Duplicated toys | Two identical toys appear |
| Duplicated books | Same book appears twice |
| Duplicated shoes | Two left shoes |
| Duplicated hats | Two hats on one character |
| Duplicated cups | Two cups on one table |
| Duplicated tools | Two identical tools |
| Duplicated props | Any prop appearing twice |

### 2. Object Persistence

Detect objects that behave incorrectly over time.

| What to Detect | Example |
|----------------|---------|
| Objects disappearing | Book vanishes between frames |
| Objects appearing | Chair materialises from nowhere |
| Objects changing colour | Red ball becomes blue |
| Objects changing size | Small cup becomes large |
| Objects teleporting | Object jumps from one position to another |

### 3. Character Integrity

Detect structural problems with character bodies.

| What to Detect | Example |
|----------------|---------|
| Extra fingers | 6 fingers instead of 5 |
| Missing fingers | 4 fingers instead of 5 |
| Extra arms | 3 arms visible |
| Missing arms | 1 arm instead of 2 |
| Extra legs | 3 legs visible |
| Missing legs | 1 leg instead of 2 |
| Extra ears | 3 ears on a rabbit |
| Duplicated tails | 2 tails on one character |
| Duplicated clothing | 2 shirts on one character |
| Floating accessories | Hat floating above head |
| Distorted faces | Warped or melted facial features |
| Incorrect facial symmetry | Eyes at different sizes |

### 4. Character Consistency

Detect changes in character appearance over time.

| What to Detect | Example |
|----------------|---------|
| Colour changes | Shirt changes from pink to red |
| Size changes | Character grows or shrinks |
| Clothing changes | Shorts change colour |
| Shoe changes | Shoes change style |
| Eye colour changes | Brown eyes become blue |
| Fur changes | Fur colour shifts |
| Tail changes | Tail shape or colour changes |
| Accessories changing | Glasses appear or disappear |
| Height inconsistencies | Character taller in next shot |

### 5. Movement Consistency

Detect unnatural or impossible movement.

| What to Detect | Example |
|----------------|---------|
| Sliding feet | Feet slide across ground |
| Foot skating | Feet don't match walking speed |
| Teleportation | Character jumps position instantly |
| Floating | Character lifts off ground |
| Broken walking cycles | Legs move unnaturally |
| Impossible running | Running mechanics wrong |
| Body popping | Body jerks suddenly |
| Animation jitter | Shaking or vibrating |
| Duplicated motion trails | Ghost copies of movement |

### 6. Asset Consistency

Detect when AI changes an object's identity instead of duplicating it.

| What to Detect | Example |
|----------------|---------|
| Object identity change | Red ball becomes blue ball |
| Object type change | Football becomes basketball |
| Object material change | Wooden chair becomes metal chair |
| Object style change | Round cup becomes angular cup |
| Object size change | Small book becomes large book |
| Missing unique features | Backpack loses its distinctive buckle |
| Added features | Chair gains arms it didn't have |
| Property swap | Two objects exchange colours |

**Note:** This is different from Object Duplication. Here the object doesn't duplicate — it transforms into something else.

### 7. Spatial Continuity

Detect breaks in spatial logic between shots.

| What to Detect | Example |
|----------------|---------|
| Exit direction mismatch | Character exits left, enters from right |
| Door inconsistency | Exits front door, appears at back door |
| Position jump | Character was at table, suddenly at door |
| Distance inconsistency | Walked 2 metres, appeared 10 metres away |
| Facing direction error | Was facing camera, now facing away without turning |
| Room transition error | Was in living room, appears in bedroom without walking |
| Path continuity break | Was on path, appears off-path |

### 8. World Navigation

Detect problems with how characters move through the world.

| What to Detect | Example |
|----------------|---------|
| Impossible entry | Character appears inside without using door |
| Impossible exit | Character leaves through wall |
| Missing transition | Character teleports between rooms |
| Path violation | Character walks through furniture |
| Door misuse | Door opens inward when it should open outward |
| Window passage | Character enters through window |
| Gravity defiance | Character walks up vertical surface |

### 9. Canonical Violations

Detect when the world's established rules are broken.

| What to Detect | Example |
|----------------|---------|
| Colour canonical violation | House colour changes from pink to blue |
| Shape canonical violation | Round door becomes square |
| Material canonical violation | Soft texture becomes hard/metallic |
| Lighting canonical violation | Warm light becomes cold/harsh |
| Character canonical violation | Character wears wrong outfit |
| World canonical violation | World layout changes |
| Scale canonical violation | House becomes twice as large |
| Style canonical violation | Toy-like style becomes realistic |

### 10. Rendering Artefacts

Detect AI-specific rendering problems.

| What to Detect | Example |
|----------------|---------|
| Ghosting | Semi-transparent duplicates |
| Double exposure | Two images overlaid |
| Blur artefacts | Unintentional blurring |
| Melting geometry | Objects lose shape |
| Texture corruption | Surfaces render incorrectly |
| Background tearing | Background rips or stretches |
| Frame glitches | Visual errors in single frames |
| AI hallucinations | Objects or features that shouldn't exist |

### 11. Physics

Detect changes in the environment over time.

| What to Detect | Example |
|----------------|---------|
| Moving windows | Window changes position |
| Changing doors | Door changes colour or size |
| Changing trees | Tree shape or position changes |
| Changing fences | Fence style changes |
| Changing furniture | Table moves or changes |
| Environment deformation | World warps or stretches |
| Changing textures | Wall texture changes |
| Layout changes | Room arrangement changes |

### 12. Lighting Consistency

Detect lighting problems.

| What to Detect | Example |
|----------------|---------|
| Light direction changes | Shadow direction shifts |
| Light intensity changes | Same scene suddenly becomes brighter or dimmer |
| Colour temperature changes | Warm light becomes cool |
| Shadow inconsistencies | Shadows appear or disappear |
| Shadow softness changes | Soft preschool shadows become hard or dramatic |
| Ambient lighting changes | Gentle fill becomes dark or contrasty |
| Highlight behaviour changes | Matte finish becomes glossy or sparkly |
| Cloud brightness changes | Clouds suddenly become too bright or dark |
| Grass brightness changes | Grass jumps brighter or darker than previous shot |
| Sudden exposure shifts | Image suddenly brightens or darkens |
| Flickering | Rapid brightness changes |
| Time-of-day inconsistencies | Night becomes day mid-scene |

### 13. Colour Identity Consistency

Detect colour grading drift between shots.

| What to Detect | Example |
|----------------|---------|
| White balance changes | Warm white balance becomes cool |
| Warmth drift | Shot 2 is yellow, Shot 3 is orange, Shot 4 is cool |
| Colour temperature changes | Same scene becomes warmer or cooler |
| Saturation changes | Pastel palette becomes vivid or washed out |
| Exposure mismatch | One shot is visibly brighter or darker |
| Contrast shift | Low contrast becomes cinematic or harsh |
| Brightness mismatch | Perceived brightness jumps between shots |
| Blue tint | Warm preschool scene becomes cold |
| Green tint | Interior or skin tones become greenish |
| Magenta tint | Neutral colours become pink/purple |
| Orange shift | Warm light becomes overly orange |
| Warm shift | Shot becomes noticeably warmer than the previous shot |
| Cool shift | Shot becomes noticeably cooler than the previous shot |
| HDR look | Matte handcrafted finish becomes glossy/high dynamic range |
| Cinematic LUT | Preschool palette becomes filmic/dramatic |

### 14. Voice Identity Consistency

Detect voice drift between speaking shots.

| What to Detect | Example |
|----------------|---------|
| Voice identity change | Kiko sounds like a different performer |
| Pitch change | Child voice becomes lower or older |
| Timbre change | Round warm voice becomes thin or nasal |
| Speaking speed change | Calm pace becomes rushed |
| Age impression change | Same character sounds older or younger |
| Personality change | Warm curious voice becomes narrator-like |
| Warmth change | Gentle delivery becomes flat or harsh |
| Rhythm change | Speaking cadence no longer matches prior shots |
| Pronunciation change | Same character pronounces words with different diction |
| Accent change | Same character suddenly has a different accent |
| Recording quality change | One shot sounds wetter, noisier, more processed or less clear |
| Alternate narrator | A new unseen narrator speaks for the character |

### 15. Camera Consistency

Detect camera problems.

| What to Detect | Example |
|----------------|---------|
| Teleporting camera | Camera jumps position |
| Sudden focal length changes | Lens zooms abruptly |
| Impossible camera movement | Camera passes through objects |
| Camera clipping | Camera enters geometry |
| Camera shaking | Unintended camera shake |
| Unexpected zooms | Zoom without narrative reason |
| Broken continuity | Camera position doesn't match between shots |

---

## Severity Levels

| Level | Definition | Action |
|-------|------------|--------|
| **Critical** | Breaks viewer immersion. Character or world fundamentally wrong. | Must fix before publish |
| **High** | Noticeable on first watch. Distracting but not immersion-breaking. | Should fix before publish |
| **Medium** | Visible on close inspection. May not be noticed by casual viewer. | Fix if time allows |
| **Low** | Barely visible. Only detectable by trained QA reviewer. | Log for future improvement |

---

## Report Format

For every issue, report:

```
Issue #[Number]

Timestamp: [HH:MM:SS]
Category: [Object Duplication / Character Integrity / etc.]
Severity: [Critical / High / Medium / Low]
Shot: [Shot number]
Description: [What is wrong]
Impact: [How it affects the viewer]
Recommendation: [What to do about it]
```

---

## Regeneration Guidelines

### When to Regenerate One Shot

- Single object duplication in one shot
- Single character integrity issue in one shot
- Single rendering artefact in one shot
- Issue is isolated and doesn't affect other shots

### When to Regenerate Multiple Shots

- Character consistency breaks across 2+ shots
- Object persistence fails across 2+ shots
- Camera continuity breaks between shots
- Lighting changes between shots
- Colour identity changes between shots
- Voice identity changes between speaking shots
- First frame of a continuation shot is visibly different from @image1

### When to Regenerate Entire Scene

- Environment consistency fails across all shots
- Character appears fundamentally different across scene
- Character voice appears fundamentally different across scene
- Colour grade drifts across the scene
- Lighting identity drifts across the scene
- Camera movement is impossible throughout
- Multiple critical issues across all shots

### When to Regenerate Entire Video

- World changes between scenes
- Character is unrecognisable
- Character voice identity is inconsistent throughout
- Episode colour grade does not feel continuous
- Multiple scenes affected by same systemic issue
- Quality score below 80

---

## Quality Score

| Score | Rating | Action |
|-------|--------|--------|
| 100 | Perfect | Publish |
| 95+ | Production Ready | Publish |
| 90+ | Minor Fixes | Fix issues, then publish |
| 80+ | Needs Regeneration | Regenerate affected shots, re-QA |
| Below 80 | Reject | Full regeneration required |

### Scoring Calculation

| Category | Weight |
|----------|--------|
| Voice Identity | 15% |
| Colour Identity | 15% |
| Lighting Continuity | 15% |
| Character Integrity | 15% |
| Character Consistency | 10% |
| Environment Consistency | 10% |
| Object Persistence | 10% |
| Camera Consistency | 5% |
| Rendering Quality | 5% |

---

## Regeneration Cost

Her yeniden üretim kararı için maliyet tahmini.

| Scope | Cost | Definition |
|-------|:----:|------------|
| Single shot | LOW | 1 shot yeniden üretilir, diğerleri korunur |
| Multiple shots | MEDIUM | 2-4 shot yeniden üretilir |
| Full scene | HIGH | Tüm sahne yeniden üretilir |
| Full video | VERY HIGH | Tüm video yeniden üretilir |

### Cost Calculation Factors

| Factor | Low | Medium | High |
|--------|:---:|:------:|:----:|
| Number of shots affected | 1 | 2-4 | 5+ |
| Character complexity | Simple pose | Multiple characters | Complex interaction |
| Environment complexity | Static | Moderate movement | Dynamic |
| Root cause | Isolated | Pattern-based | Systemic |

### Recommended Action Format

```
Recommended Action:

Regenerate:
  Shot 03

Reason:
  Critical object duplication

Estimated Cost:
  LOW

Keep:
  Shot 01, 02, 04 unchanged
```

---

## Root Cause Analysis

Her hata için kök neden analizi. Bu, zamanla bir AI bug database oluşturur.

| Root Cause | Description | Prevention |
|------------|-------------|------------|
| Motion prediction artifact | AI incorrectly predicts object trajectory | Reduce motion complexity |
| Rotation interpolation failure | AI fails to interpolate rotation correctly | Reduce turning speed |
| Temporal attention collapse | AI loses track of objects over time | Shorter shots |
| Style drift | AI gradually changes visual style | Stronger reference anchoring |
| Hallucination | AI invents objects that don't exist | Stronger negative prompts |
| Reference confusion | AI confuses multiple reference images | Fewer references per shot |
| Frame inconsistency | AI generates each frame independently | Continuity frame workflow |
| Prompt misinterpretation | AI misunderstands the prompt | Simplify prompt language |

### Root Cause Report Format

```
Problem:
  Duplicated football

Likely Cause:
  AI motion prediction artifact

Fix Strategy:
  Regenerate Shot 04 with reduced motion

Prevention:
  Use shorter motion sequences in future prompts
```

---

## Final Decision

The reviewer must always end with:

```
=== QA REPORT ===

Video: [Name]
Duration: [Length]
Date: [Date]
Reviewer: [Name]

Overall Quality Score: [Score]

Production Ready: YES / NO

Critical Issues: [Count]
High Issues: [Count]
Medium Issues: [Count]
Low Issues: [Count]

Recommended Regeneration Strategy:
[Which shots to regenerate, which to keep]

Notes:
[Any additional observations]
```

---

## Pompom Hills Specific Rules

In addition to general QA rules, Pompom Hills content must pass these checks:

### Character Rules

- Characters must remain soft and rounded
- Eyes must remain expressive
- Pastel colour palette must remain stable
- No realistic textures on characters
- No horror-like artefacts
- No frightening facial distortions

### Object Rules

- No broken toys
- No duplicated children's objects
- No duplicated shoes
- No duplicated balls
- No duplicated books
- No duplicated clothing
- All props must remain round and soft

### World Rules

- The world should always feel warm, safe, and handcrafted
- No sharp edges appearing
- No dark shadows appearing
- No realistic environments
- No modern objects (cars, electronics)
- No frightening elements

### Colour Rules

- White balance must remain unchanged across shots
- Exposure must remain unchanged across shots
- Colour temperature must remain unchanged across shots
- Saturation must remain unchanged across shots
- Contrast must remain unchanged across shots
- Brightness must remain unchanged across shots
- Pastel palette must remain stable
- No cool shift, warm shift, green tint, magenta tint or orange grading
- No HDR look
- No cinematic LUT
- The episode must feel like one continuous colour grade

### Voice Rules

- Voice must match the previous speaking shot
- Same voice identity must be preserved
- Same pitch must be preserved
- Same timbre must be preserved
- Same speaking speed must be preserved
- Same age impression must be preserved
- Same personality must be preserved
- Same warmth must be preserved
- Same speaking rhythm must be preserved
- Same pronunciation must be preserved
- Same accent must be preserved
- Same recording quality must be preserved
- Same Voice ID or approved voice reference must be used when available
- Previous shot audio must be used as voice reference when available
- No different narrator or alternate voice

### Emotional Safety Rules

- No distorted faces that could frighten children
- No sudden dark frames
- No aggressive movement artefacts
- No objects that appear threatening
- No characters appearing to be in danger

---

## Future Expansion

This specification is designed to accommodate additional QA categories:

| Future Category | Description |
|-----------------|-------------|
| Lip Sync QA | Verify mouth movement matches dialogue |
| Subtitle QA | Verify timing, placement, readability |
| Advanced Audio QA | Verify sound sync, levels, ambience and final mix quality |
| Continuity QA | Verify cross-episode consistency |
| Localization QA | Verify multi-language consistency |
| Accessibility QA | Verify colour contrast, text readability |

---

## QA Pipeline Integration

```
AI Generation
    ↓
Level 1: Frame QA
    ↓ (pass)
Level 2: Shot QA
    ↓ (pass)
Level 3: Scene QA
    ↓ (pass)
Level 4: Episode QA
    ↓ (pass)
Quality Score Calculated
    ↓
Final Decision
    ↓ (if issues)
Regeneration Loop
    ↓
Re-QA
    ↓ (pass)
Publish
```

---

*This document is the canonical QA specification for Pompom Hills.*
*Source of truth for: QA process, detection, severity, regeneration.*
*Implementation-independent — works with any AI video tool.*
*Last updated: 2 Temmuz 2026*
