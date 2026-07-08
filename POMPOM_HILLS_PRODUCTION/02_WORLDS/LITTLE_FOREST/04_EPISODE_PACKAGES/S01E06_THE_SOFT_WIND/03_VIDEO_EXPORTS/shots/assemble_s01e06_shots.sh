#!/bin/bash
# ============================================================
# Pompom Hills — S01E06 The Soft Wind — Video Assembly
# Finds all shot-*.mp4 files in this folder and joins them
# with 0.2s black gaps between shots.
# Adapted from assemble_season_begins_test.sh
# ============================================================

BLACK_GAP=0.2
OUTPUT_NAME="s01e06-the-soft-wind-all-shots.mp4"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_PATH="${SCRIPT_DIR}/${OUTPUT_NAME}"

RED='\033[0;31m'; GREEN='\033[0;32m'; NC='\033[0m'
log() { echo -e "${GREEN}[✓]${NC} $1"; }
err() { echo -e "${RED}[✗]${NC} $1"; exit 1; }

command -v ffmpeg &>/dev/null || err "ffmpeg not found"

# Find all shot videos, sorted naturally
SHOTS=($(ls "${SCRIPT_DIR}"/shot-*.mp4 "${SCRIPT_DIR}"/shot0*.mp4 2>/dev/null | grep -v 'all-shots' | sort -t'-' -k2 -n))
[ ${#SHOTS[@]} -eq 0 ] && err "No shot-*.mp4 files found"
log "Found ${#SHOTS[@]} shots:"
for s in "${SHOTS[@]}"; do log "  $(basename "$s")"; done

# Get video properties from first shot
W=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "${SHOTS[0]}")
H=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=p=0 "${SHOTS[0]}")
FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "${SHOTS[0]}")
SR=$(ffprobe -v error -select_streams a:0 -show_entries stream=sample_rate -of csv=p=0 "${SHOTS[0]}")
CH=$(ffprobe -v error -select_streams a:0 -show_entries stream=channels -of csv=p=0 "${SHOTS[0]}")
LAYOUT=$(ffprobe -v error -select_streams a:0 -show_entries stream=channel_layout -of csv=p=0 "${SHOTS[0]}" 2>/dev/null || echo "stereo")

log "Resolution: ${W}x${H} | FPS: ${FPS} | ${CH}ch ${SR}Hz"

# Temp files
TBLACK="${SCRIPT_DIR}/.tmp_black.mp4"
TCONCAT="${SCRIPT_DIR}/.tmp_concat.txt"
trap 'rm -f "$TBLACK" "$TCONCAT"' EXIT

# Create black gap
log "Creating ${BLACK_GAP}s black gap..."
ffmpeg -y -hide_banner -loglevel warning \
    -f lavfi -i "color=c=black:s=${W}x${H}:r=${FPS}:d=${BLACK_GAP}" \
    -f lavfi -i "anullsrc=r=${SR}:cl=${LAYOUT}" \
    -t "$BLACK_GAP" \
    -c:v libx264 -pix_fmt yuv420p \
    -c:a aac -ar "$SR" -ac "$CH" \
    "$TBLACK" || err "Black gap failed"

# Build concat file: shot1 + gap + shot2 + gap + ... + shotN
log "Building concat list..."
> "$TCONCAT"
for i in "${!SHOTS[@]}"; do
    echo "file '${SHOTS[$i]}'" >> "$TCONCAT"
    if [ $i -lt $((${#SHOTS[@]}-1)) ]; then
        echo "file '${TBLACK}'" >> "$TCONCAT"
    fi
done

log "Concatenating ${#SHOTS[@]} shots..."
ffmpeg -y -hide_banner -loglevel warning \
    -f concat -safe 0 -i "$TCONCAT" \
    -c:v libx264 -pix_fmt yuv420p \
    -c:a aac -ar "$SR" -ac "$CH" \
    "$OUTPUT_PATH" || err "Concat failed"

DUR=$(ffprobe -v error -select_streams v:0 -show_entries format=duration -of csv=p=0 "$OUTPUT_PATH")
echo ""
log "Output: ${OUTPUT_PATH}"
log "Duration: ${DUR}s"
log "Done!"
