#!/bin/bash

# Pompom Hills - speaker-aware shot to Short converter.
# Plan format: each row is "segment_end_seconds crop_x" and the final row is
# "default crop_x". Crop X is measured after scale=-2:1920.

set -euo pipefail

INPUT="${1:-}"
OUTPUT="${2:-}"
PLAN="${3:-}"

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
log() { echo -e "${GREEN}[✓]${NC} $1"; }
err() { echo -e "${RED}[✗]${NC} $1" >&2; exit 1; }

[ -n "$INPUT" ] && [ -n "$OUTPUT" ] && [ -n "$PLAN" ] || {
  echo "Usage: $0 <input.mp4> <output.mp4> <crop-plan.txt>" >&2
  exit 1
}
[ -f "$INPUT" ] || err "Input file not found: $INPUT"
[ -f "$PLAN" ] || err "Crop plan not found: $PLAN"
command -v ffmpeg >/dev/null 2>&1 || err "ffmpeg not found"
command -v ffprobe >/dev/null 2>&1 || err "ffprobe not found"

EXPR=$(awk '
  /^[[:space:]]*#/ || NF < 2 { next }
  tolower($1) == "default" { default_x = $2; next }
  { end[++n] = $1; x[n] = $2 }
  END {
    if (n < 1 || default_x == "") exit 2
    expression = default_x
    for (i = n; i >= 1; i--)
      expression = "if(lt(t," end[i] ")," x[i] "," expression ")"
    print expression
  }
' "$PLAN") || err "Invalid crop plan: add timed rows and a final default row"

mkdir -p "$(dirname "$OUTPUT")"
log "Input:  $INPUT"
log "Output: $OUTPUT"
log "Crop:   $EXPR"

ffmpeg -y -i "$INPUT" \
  -vf "scale=-2:1920:flags=lanczos,crop=1080:1920:'$EXPR':0,setsar=1,format=yuv420p" \
  -map 0:v:0 -map 0:a:0? \
  -c:v libx264 -preset slow -crf 18 -profile:v high -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -movflags +faststart "$OUTPUT" || err "ffmpeg conversion failed"

WIDTH=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$OUTPUT")
HEIGHT=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=p=0 "$OUTPUT")
DURATION=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUTPUT")
[ "$WIDTH" = "1080" ] && [ "$HEIGHT" = "1920" ] || err "Output is not 1080x1920"
log "Duration: ${DURATION}s"
log "Done!"
