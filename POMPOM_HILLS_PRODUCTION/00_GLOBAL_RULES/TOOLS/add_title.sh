#!/bin/bash

# Pompom Hills — Title Card Generator
# Usage: ./add_title.sh <input.mp4> <output.mp4> ["Title Line 1"] ["Title Line 2"]

INPUT="$1"
OUTPUT="$2"
TITLE1="${3:-Pompom Hills}"
TITLE2="${4:-The Soft Wind}"
DURATION="${5:-5}"

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: $0 <input.mp4> <output.mp4> [\"Title 1\"] [\"Title 2\"] [duration]"
  exit 1
fi

TMPDIR=$(mktemp -d)
OVERLAY="$TMPDIR/overlay.png"

# Get video dimensions
WIDTH=$(ffprobe -v quiet -print_format json -show_streams "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin)['streams'][0]['width'])")
HEIGHT=$(ffprobe -v quiet -print_format json -show_streams "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin)['streams'][0]['height'])")

# Create overlay image with Python PIL
python3 << PYEOF
from PIL import Image, ImageDraw, ImageFont

w, h = $WIDTH, $HEIGHT
overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

try:
    font1 = ImageFont.truetype("/System/Library/Fonts/SFNSRounded.ttf", 48)
    font2 = ImageFont.truetype("/System/Library/Fonts/SFNSRounded.ttf", 34)
except:
    font1 = ImageFont.load_default()
    font2 = ImageFont.load_default()

title1 = "$TITLE1"
title2 = "$TITLE2"

bbox1 = draw.textbbox((0, 0), title1, font=font1)
w1 = bbox1[2] - bbox1[0]
bbox2 = draw.textbbox((0, 0), title2, font=font2)
w2 = bbox2[2] - bbox2[0]

x1 = (w - w1) // 2
y1 = int(h * 0.82)
x2 = (w - w2) // 2
y2 = y1 + 50

draw.text((x1+2, y1+2), title1, font=font1, fill=(60, 40, 20, 120))
draw.text((x2+1, y2+1), title2, font=font2, fill=(60, 40, 20, 90))
draw.text((x1, y1), title1, font=font1, fill=(255, 245, 220, 250))
draw.text((x2, y2), title2, font=font2, fill=(255, 240, 210, 230))

overlay.save("$OVERLAY")
PYEOF

# Overlay with fade in/out
FADE_OUT_START=$(echo "$DURATION - 0.5" | bc)

ffmpeg -y -i "$INPUT" -i "$OVERLAY" \
  -filter_complex "[0:v][1:v]overlay=0:0:enable='between(t,0.5,$DURATION)'[outv]" \
  -map "[outv]" -map "0:a" \
  -c:v libx264 -crf 18 -preset slow -c:a copy \
  "$OUTPUT" 2>/dev/null

rm -rf "$TMPDIR"
echo "✓ $OUTPUT"
