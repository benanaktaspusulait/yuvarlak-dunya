#!/bin/bash

# Screenshot from MP4 — color-safe
# Usage: ./screenshot.sh <video.mp4> [output.png] [seconds_from_end]

INPUT="$1"
OUTPUT="${2:-${INPUT%.mp4}.png}"
SEEK="${3:-0.1}"

if [ -z "$INPUT" ]; then
  echo "Usage: $0 <video.mp4> [output.png] [seconds_from_end]"
  exit 1
fi

ffmpeg -sseof "-$SEEK" -i "$INPUT" -frames:v 1 \
  -vf "scale=in_color_matrix=bt709:out_color_matrix=bt709" \
  -pix_fmt rgb24 \
  "$OUTPUT" -y 2>/dev/null

echo "✓ $OUTPUT"
