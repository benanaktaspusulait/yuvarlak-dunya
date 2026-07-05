# S01E04 - Mimi's Big Yawn
# Object Continuity Map

Purpose:
This file defines every object that must exist before each shot is generated.

A shot is not approved only because an object is mentioned in the prompt.
A shot is approved only if the required object is visible in `@image1` and usable for
the planned action at its existing size, shape, position, and distance.

Core rule:

Characters adapt to the environment.
The environment does not adapt to the characters.

Never enlarge, move, multiply, reshape, replace, or spawn objects to satisfy an action.

If an object is visible but too small, too far away, too crowded, partly cropped, or not
shaped for the planned action, simplify the character action instead of changing the
object.

Environment objects are locked. Trees, grass patches, flowers, hills, stones,
entrances, sky, pillows, furniture, anchors, and props must not move, slide, drift,
grow, shrink, enter frame, leave frame, or reposition.

Only characters may move unless the shot explicitly allows a planned location
transition, such as the Shot 05 entrance crossing.

Every first-frame still, cheap take, and first-frame export must be checked against this
map before spending video credits.

---

## Shot 01 - Master Setup

Required visible objects:
- Mimi's Burrow round blue entrance
- warm interior glow
- exactly 3 round grey stepping stones, fully visible and not cropped
- flower patch usable for Shot 02
- tree / grass area usable for Shot 03
- small flowers on mound
- evening dusk sky, no stars
- Mimi sleepy beside entrance, not blocking entrance
- Kiko nearby, concerned

Usability checks:
- flower patch must be clear enough for Mimi to sit beside or lean toward
- tree/grass area must be visible and reachable without camera movement
- entrance must remain main landmark
- stepping-stone path must not be blocked

Reject if:
- flower patch is only tiny decoration and not usable for Shot 02
- tree/grass area is too far, cropped, or unusable for Shot 03
- fewer or more than 3 stones visible
- Mimi or Kiko blocks entrance or stepping-stone path

---

## Shot 02 - Flower Patch

Required from `@image1`:
- same flower patch
- entrance
- warm glow
- 3 stepping stones
- tree/grass area
- Mimi
- Kiko

Current action object:
- flower patch

Usability:
- Mimi may only interact with the flower patch already visible in `@image1`
- if flower patch is small, Mimi sits beside it or leans cheek/ear toward it
- do not create a new flower bed

Forbidden:
- new flower bed
- flower pile
- flower ring
- flowers appearing under Mimi
- flower patch growing
- flower patch moving

Final frame must support Shot 03:
- tree/grass area visible
- entrance visible
- 3 stones visible

---

## Shot 03 - Tree / Grass

Required from `@image1`:
- tree/grass area
- entrance with warm glow
- 3 stepping stones
- flower patch if visible
- Mimi
- Kiko

Current action object:
- tree/grass area

Usability:
- Mimi may only use the already-visible grass area
- tree must not move closer
- camera must not move to find the tree
- if tree is too far, Mimi sits on visible grass edge near the tree side

Forbidden:
- tree moving
- tree flying into frame
- tree growing larger
- new grass patch
- new flowers
- camera reframe toward tree

Final frame must support Shot 04:
- glowing entrance visible and unblocked

---

## Shot 04 - Doorway Realization

Required from `@image1`:
- glowing round blue entrance
- Mimi
- Kiko
- current environment layout

Current action object:
- entrance

Usability:
- Kiko points to already-visible entrance
- Mimi turns toward entrance
- small character gestures only

Forbidden:
- new objects
- environment correction
- restoring old layout
- entrance enlarging
- camera push-in
- characters entering

Final frame must support Shot 05:
- entrance visible and unblocked
- Mimi and Kiko outside
- ready to enter

---

## Shot 05 - Entrance Crossing / Interior Master

Required from `@image1`:
- entrance
- warm glow
- 3 stepping stones if visible
- Mimi
- Kiko

Required `@image2`:
- approved interior canon reference

Interior must-have final frame:
- round blue pillow
- warm blue walls
- soft green carpet
- warm golden glow

Interior anchors:
- at least one visible: window / shelf / carrot box

Forbidden:
- generating Shot 05 without `@image2`
- entrance becoming door
- cave / tunnel / dark room
- oversized interior
- missing pillow
- missing walls/carpet/glow

Final frame must support Shot 06:
- stable interior master frame
- pillow visible and usable

---

## Shot 06 - Pillow

Required from `@image1`:
- round blue pillow
- warm blue walls
- green carpet
- warm glow
- Mimi
- Kiko
- any visible interior anchors

Current action object:
- pillow

Usability:
- pillow must be large and visible enough for Mimi to touch and sit on
- no new pillow
- no moving pillow

Forbidden:
- pillow spawning
- new blanket
- new bed
- new interior anchors

Final frame must support Shot 07:
- Mimi on or beside pillow
- pillow visible

---

## Shot 07 - Settling Down

Required from `@image1`:
- pillow
- Mimi
- Kiko
- warm interior
- visible anchors only if present

Current action object:
- pillow

Usability:
- Mimi lies/curls on the already-visible pillow
- Kiko gently helps with small gestures

Forbidden:
- blanket spawning
- complex bedding
- new bed
- new props

Final frame must support Shot 08:
- Mimi curled on pillow
- Kiko nearby
- warm glow unchanged

---

## Shot 08 - Goodnight

Required from `@image1`:
- Mimi asleep on pillow
- Kiko nearby
- warm blue walls
- green carpet
- warm glow
- visible anchors only if present

Current action object:
- pillow / sleeping pose

Forbidden:
- new blanket
- stars
- night sky
- moonlight
- darkness falling
- Kiko leaving
- camera pull-back
- new props
