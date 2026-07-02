# VIDEO CONTINUATION RULES — OpenArt

---

## Continuation Reference

When a continuation frame reference is provided (e.g. @image2),

that image represents the FINAL FRAME of the previous video.

It is NOT an inspiration image.

It is NOT a style reference.

It is NOT a mood board.

Treat it as Frame 0 of the new video.

---

## Camera Continuity

The first second of the new video must begin from exactly the same:

- Camera angle
- Focal length
- Framing
- Composition
- Environment
- Lighting
- Character pose

shown in @image2.

Never restart the scene.

Never create a new establishing shot.

Never change framing before the first spoken line.

---

## Character Continuity

Continue character motion naturally.

The first movement should feel like the next animation frame.

Maintain identical:

- Character position
- Character pose
- Character expression
- Character scale
- Character clothing
- Character colors

---

## Environment Continuity

Do not redesign the environment.

Do not move objects.

Do not regenerate the world.

Do not change lighting.

Do not change shadows.

Do not change weather.

The environment is LOCKED.

---

## Shot Continuity

Maintain cinematic continuity exactly as if the previous video never ended.

The transition between videos should be invisible to the viewer.

---

## Reference Usage

| Reference | Purpose | Priority |
|---|---|---|
| @image1 | World Lock (environment) | Highest |
| @image2 | Continuation Frame (previous final frame) | High |
| @image3+ | Character reference | Medium |

**Conflict resolution:** If there is ANY conflict between references, ALWAYS preserve @image1 (World Lock) first.

---

## Dialogue Continuity Rule

Continuation scenes must not repeat dialogue that was already spoken in the previous video.

Before writing a continuation scene, check the previous scene dialogue and final spoken line.

If the previous video already included a greeting such as "Hi", "Hello", or "Hey", the continuation must NOT start with another greeting.

The continuation should begin naturally from the previous spoken context.

Use bridging lines instead of repeated greetings.

Examples:

Wrong:
Previous scene: "Hi!"
Continuation: "Hi! I'm Noah."

Correct:
Previous scene: "Hi!"
Continuation: "I'm Noah. I love building new things."

Wrong:
Previous scene: "Let's make it fun!"
Continuation: "Let's make it fun!"

Correct:
Previous scene: "Let's make it fun!"
Continuation: "Let's make it even better!"

Continuation dialogue should feel like the next sentence, not a restart.

---

## Common Mistakes

```
✗ Using file names instead of @image tokens
✗ Recreating the environment from scratch
✗ Starting with a new establishing shot
✗ Changing camera angle in first frame
✗ Moving character position
✗ Changing lighting direction
✗ Regenerating the world
✗ Adding new objects
✗ Removing existing objects
```

---

## Scene File Format

Scene MD files that use continuation should include:

```markdown
## Continuation Rules

Follow: `VIDEO_CONTINUATION_RULES.md`

References:
- @image1: World Lock (Central Square)
- @image2: Final frame from previous scene

Continue directly from the final frame.
```

---

*Bu belge OpenArt video continuation kuralları için referansıdır.*
