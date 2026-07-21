# Coordinate Map — EP08 "Cozy Coat, Click Click"

## Character Coordinates

### Kiko

| Parameter | Value | Notes |
|-----------|-------|-------|
| Units | 100 | Reference unit for all measurements |
| Base Position | Screen-left, 30-45% from left edge | Consistent throughout |
| Height | 100 units (full character) | Child height at 0.75m eye level |
| Width | ~40 units | Slim child proportions |
| Shoulder Width | ~25 units | Narrow child shoulders |
| Arm Length | ~30 units | Proportional to body |

**Position per Shot:**

| Shot | X Position (%) | Y Position | Z Depth | Notes |
|------|----------------|------------|---------|-------|
| 01 | 30% | Center | Mid-ground | Looking at coat |
| 02 | 35% | Center | Mid-ground | Trying to put on coat |
| 03 | 40% | Center | Mid-ground | Closer to Mimi |
| 04 | 45% | Center | Mid-ground | One arm in |
| 05 | 45% | Center | Mid-ground | Both arms in |
| 06 | 50% | Center | Foreground | Close-up with Mimi |
| 07 | 40% | Center | Mid-ground | Standing in coat |
| 08 | 40% | Center | Mid-ground | Waving proudly |

### Mimi

| Parameter | Value | Notes |
|-----------|-------|-------|
| Units | ~70 | 70% of Kiko's height (rabbit proportions) |
| Base Position | Screen-right, 60-70% from left edge | Consistent throughout |
| Height | 70 units | Slightly shorter than Kiko |
| Width | ~35 units | Slim rabbit proportions |
| Ear Height | +15 units | Ears extend above head |

**Position per Shot:**

| Shot | X Position (%) | Y Position | Z Depth | Notes |
|------|----------------|------------|---------|-------|
| 01 | 70% | Center | Mid-ground | Near door |
| 02 | 65% | Center | Background | Watching Kiko |
| 03 | 60% | Center | Mid-ground | Closer to Kiko |
| 04 | 55% | Center | Mid-ground | Guiding Kiko |
| 05 | 55% | Center | Mid-ground | Proud of Kiko |
| 06 | 50% | Center | Foreground | Helping with snap |
| 07 | 60% | Center | Mid-ground | Beside Kiko |
| 08 | 60% | Center | Mid-ground | Affirming Kiko |

## Prop Coordinates

### Coat

| State | Position | X (%) | Y | Z Depth | Notes |
|-------|----------|-------|---|---------|-------|
| On rack | Hanging | 25% | Mid-height | Background | Shot 01 |
| Half-on | Kiko's body | 35% | Center | Mid-ground | Shots 02-03 |
| One arm in | Kiko's body | 45% | Center | Mid-ground | Shot 04 |
| Both arms in | Kiko's body | 45% | Center | Mid-ground | Shot 05 |
| Snapped | Kiko's body | 50% | Center | Foreground | Shot 06 |
| Fully worn | Kiko's body | 40% | Center | Mid-ground | Shots 07-08 |

### Coat Rack

| Parameter | Value | Notes |
|-----------|-------|-------|
| Position | Screen-left, 20% from left edge | Background |
| Height | 150 units | Tall enough for coat |
| Width | ~20 units | Slim stand |
| Depth | Background | Behind Kiko |

### Snap Mechanism

| Parameter | Value | Notes |
|-----------|-------|-------|
| Position | Center of coat front | When worn |
| Size | ~5 units | Small but visible |
| State | Open → Closed | Shot 06 |

## Staging Per Shot Group

### Chain A: Shots 01-04

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   [Coat Rack]                    [Door with Glass]      │
│        │                              │                 │
│        ▼                              ▼                 │
│   ┌─────────┐                    ┌─────────┐            │
│   │  Kiko   │                    │  Mimi   │            │
│   │  100u   │                    │  70u    │            │
│   │ (30-45%)│                    │ (60-70%)│            │
│   └─────────┘                    └─────────┘            │
│                                                         │
│   [Potted Plant]              [Warm Light Direction]    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Staging Notes:**
- Kiko: Screen-left, near coat rack
- Mimi: Screen-right, near door
- Coat: Transitions from rack to Kiko's body
- Light: Streaming from door (screen-right)

### Chain B: Shots 05-08

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                    [Door with Glass]                     │
│                         │                               │
│                         ▼                               │
│              ┌─────────────────────┐                    │
│              │                     │                    │
│         ┌────┤      Kiko + Mimi    ├────┐              │
│         │    │    (Closer Together) │    │              │
│         │    └─────────────────────┘    │              │
│         │                               │              │
│         ▼                               ▼              │
│   [Coat on Kiko]                [Proud Moment]         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Staging Notes:**
- Characters closer together (support and success)
- Coat fully on Kiko's body
- Focus on emotional resolution
- Final frame: both characters proud and happy

## Spatial Relationships

### Character-to-Character Distance

| Shot | Distance (units) | Notes |
|------|------------------|-------|
| 01 | 80 | Separated, establishing |
| 02 | 70 | Slightly closer |
| 03 | 50 | Mimi approaching |
| 04 | 40 | Close, guiding |
| 05 | 40 | Close, celebrating |
| 06 | 10 | Very close, helping |
| 07 | 30 | Standing together |
| 08 | 30 | Standing together |

### Character-to-Prop Relationships

| Shot | Kiko-Coat | Mimi-Coat | Notes |
|------|-----------|-----------|-------|
| 01 | 50 units | 100 units | Kiko near, Mimi far |
| 02 | 0 units | 80 units | Kiko wearing, Mimi watching |
| 03 | 0 units | 60 units | Kiko wearing, Mimi closer |
| 04 | 0 units | 40 units | Kiko wearing, Mimi guiding |
| 05 | 0 units | 40 units | Kiko wearing, Mimi proud |
| 06 | 0 units | 10 units | Both touching coat |
| 07 | 0 units | 30 units | Kiko wearing, Mimi beside |
| 08 | 0 units | 30 units | Kiko wearing, Mimi beside |

## Coordinate Validation

- [ ] Kiko stays screen-left throughout
- [ ] Mimi stays screen-right throughout
- [ ] Character heights are consistent (Kiko 100u, Mimi 70u)
- [ ] Coat state tracks correctly across shots
- [ ] Characters get closer as support increases
- [ ] Final shots show characters standing together
- [ ] No coordinate conflicts or overlaps
