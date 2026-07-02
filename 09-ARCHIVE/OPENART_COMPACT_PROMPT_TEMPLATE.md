# OpenArt Compact Prompt Template v1.0

## Purpose
When 3-4 reference images are loaded into OpenArt, the prompt field becomes too small for long Production MD documents. Therefore, each scene must have a **compact prompt** (600-800 characters) specifically optimized for OpenArt.

**Important:** Production MD is for humans and Codex. OpenArt receives ONLY the Compact Prompt.

## Template Structure

### 1. Selected World
`Use the supplied [Environment Name] reference (@image1) as the FINAL background plate.`

### 2. Selected Character  
`Insert [Character Name] (@image2) into the existing world. Never redesign. Never regenerate.`

### 3. Scene Action
`[Character Name] [action description]. Natural movement. No posing for camera.`

### 4. Environment Lock
`World LOCKED: Do not repaint. Do not regenerate. Do not replace objects. Background pixels unchanged except where character overlaps.`

### 5. Character Lock
`Character LOCKED: Use @image2 exactly. No costume/hairstyle/facial changes.`

### 6. Scale / Framing
`[Character Name] is SMALL preschool child (~4-6% of frame). Environment is hero (~94-96%). Never visually dominant.`

### 7. Camera
`Keep original world camera. Do not zoom. Do not crop. Do not recompose.`

### 8. Dialogue / Voice
`[Character Name] speaks: "[dialogue line]". Voice: [voice description].`

### 9. Negative Constraints
`Reject if: character too large, environment regenerated, world changes, camera moves, wrong proportions.`

---

## Complete Example (Noah - Central Square)

```
Use Central Square (@image1) as FINAL background. Insert Noah (@image2). Noah sits on stepping stones, building blocks. Natural movement. World LOCKED: Do not repaint/regenerate/replace. Background pixels unchanged. Character LOCKED: Use @image2 exactly. Noah is SMALL preschool child (~4-6% frame). Environment hero (~94-96%). Keep original camera. No zoom/crop. Noah: "Let's make it fun!" Voice: creative, cheerful, childlike. Reject if Noah too large, environment regenerated, world changes, camera moves.
```

**Character count:** 560

---

## Frame Continuity Rule
When previous scene final frame is provided (@image3):
`Start EXACTLY from @image3. Continue camera/composition/pose/lighting from previous frame. Do not recreate scene.`

---

## Reference Priority (for Complex Scenes)
1. World reference (@image1)
2. Previous frame (@image3) - if provided
3. Character reference (@image2)
4. This prompt

Always preserve Priority 1 first. Never modify world to satisfy character.

---

## Optimization Tips

1. **Be specific, not verbose** - Use strong commands (LOCKED, NEVER, EXACTLY)
2. **Use token references** - @image1, @image2, @image3 instead of file names
3. **Focus on constraints** - What NOT to do is as important as what to do
4. **Keep under 800 chars** - Ideal: 600-700 characters
5. **One idea per line** - Makes it easier for AI to parse
6. **Use preschool metrics** - "SMALL child", "Environment hero", not just percentages

---

## Quality Checklist
- [ ] Under 800 characters
- [ ] Uses @image tokens
- [ ] Contains LOCKED commands
- [ ] Defines scale clearly
- [ ] Specifies camera restrictions
- [ ] Includes negative constraints
- [ ] Maintains reference priority
- [ ] Optimized for OpenArt limitations

---

## Integration with Production MD
Each scene MD should end with:

```markdown
## OpenArt Compact Prompt

[600-800 character optimized prompt here]
```

This ensures:
- Production team has full documentation
- OpenArt receives optimized, constraint-rich prompt
- Consistency across all scenes
- Easy copy-paste workflow