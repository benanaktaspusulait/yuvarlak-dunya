#!/bin/bash
# validate-scene.sh — Sahne kalite kontrolü
# Kullanım: bash scripts/validate-scene.sh <sahne_dizini>

SCENE_DIR="${1:-.}"

echo "============================================"
echo "  SAHNE QA KONTROLÜ"
echo "  Dizin: $SCENE_DIR"
echo "============================================"
echo

ERRORS=0
WARNINGS=0

# 1. Dosya Yapısı Kontrolü
echo "1. DOSYA YAPISI"
[ -d "$SCENE_DIR/shots" ] && echo "  ✅ shots/ klasörü var" || { echo "  ❌ shots/ klasörü YOK"; ERRORS=$((ERRORS+1)); }
SHOT_COUNT=$(find "$SCENE_DIR/shots" -name "*.md" 2>/dev/null | wc -l)
[ "$SHOT_COUNT" -ge 4 ] && echo "  ✅ $SHOT_COUNT shot dosyası" || { echo "  ❌ $SHOT_COUNT shot (4 gerekli)"; ERRORS=$((ERRORS+1)); }
[ -f "$SCENE_DIR/09-render-prompts.md" ] && echo "  ✅ render-prompts.md var" || { echo "  ❌ render-prompts.md YOK"; ERRORS=$((ERRORS+1)); }
[ -f "$SCENE_DIR/01-overview.md" ] && echo "  ✅ overview.md var" || echo "  ⚠️  overview.md yok"
echo

# 2. Shot-01 Kontrolü
echo "2. SHOT-01 KONTROLÜ"
SHOT01=$(find "$SCENE_DIR/shots" -name "shot-01*.md" 2>/dev/null | head -1)
if [ -f "$SHOT01" ]; then
    grep -q "Opening Hook" "$SHOT01" && echo "  ✅ Opening Hook" || { echo "  ⚠️  Opening Hook eksik"; WARNINGS=$((WARNINGS+1)); }
    grep -q "6-8%\|Small preschool child" "$SHOT01" && echo "  ✅ Scale talimatı" || echo "  ⚠️  Scale eksik"
    grep -q "No subtitles" "$SHOT01" && echo "  ✅ Text Safety" || { echo "  ❌ Text Safety eksik"; ERRORS=$((ERRORS+1)); }
    grep -q "Negative Prompt\|negative prompt" "$SHOT01" && echo "  ✅ Negative Prompt" || echo "  ⚠️  Negative Prompt eksik"
else
    echo "  ❌ shot-01 bulunamadı"
    ERRORS=$((ERRORS+1))
fi
echo

# 3. Shot-02+ Kontrolü
echo "3. SHOT-02+ KONTROLÜ"
FRAME_LOCK=0
CAMERA_LOCK=0
LIGHTING_LOCK=0
CHAR_PRESENCE=0
TEXT_SAFETY=0

for f in $(find "$SCENE_DIR/shots" -name "shot-0[2-9]*.md" -o -name "shot-1*.md" 2>/dev/null); do
    grep -q "frame zero" "$f" && FRAME_LOCK=$((FRAME_LOCK+1))
    grep -q "identical camera position" "$f" && CAMERA_LOCK=$((CAMERA_LOCK+1))
    grep -q "first frame must preserve" "$f" && LIGHTING_LOCK=$((LIGHTING_LOCK+1))
    grep -q "already present at the beginning" "$f" && CHAR_PRESENCE=$((CHAR_PRESENCE+1))
    grep -q "No subtitles" "$f" && TEXT_SAFETY=$((TEXT_SAFETY+1))
done

TOTAL_SHOTS=$(find "$SCENE_DIR/shots" -name "shot-0[2-9]*.md" -o -name "shot-1*.md" 2>/dev/null | wc -l)

echo "  Frame Lock: $FRAME_LOCK/$TOTAL_SHOTS"
echo "  Camera Lock: $CAMERA_LOCK/$TOTAL_SHOTS"
echo "  Lighting Lock: $LIGHTING_LOCK/$TOTAL_SHOTS"
echo "  Character Presence: $CHAR_PRESENCE/$TOTAL_SHOTS"
echo "  Text Safety: $TEXT_SAFETY/$TOTAL_SHOTS"

[ "$FRAME_LOCK" -eq "$TOTAL_SHOTS" ] || { echo "  ❌ Frame Lock eksik"; ERRORS=$((ERRORS+1)); }
[ "$CAMERA_LOCK" -eq "$TOTAL_SHOTS" ] || { echo "  ❌ Camera Lock eksik"; ERRORS=$((ERRORS+1)); }
[ "$LIGHTING_LOCK" -eq "$TOTAL_SHOTS" ] || { echo "  ❌ Lighting Lock eksik"; ERRORS=$((ERRORS+1)); }
[ "$CHAR_PRESENCE" -eq "$TOTAL_SHOTS" ] || { echo "  ❌ Character Presence eksik"; ERRORS=$((ERRORS+1)); }
[ "$TEXT_SAFETY" -eq "$TOTAL_SHOTS" ] || { echo "  ❌ Text Safety eksik"; ERRORS=$((ERRORS+1)); }
echo

# 4. Close-up Kontrolü
echo "4. CLOSE-UP KONTROLÜ"
CLOSEUPS=$(grep -rl "Close-up\|close-up" "$SCENE_DIR/shots"/*.md 2>/dev/null | wc -l)
[ "$CLOSEUPS" -eq 0 ] && echo "  ✅ Close-up yok" || { echo "  ❌ $CLOSEUPS dosyada close-up var"; ERRORS=$((ERRORS+1)); }
echo

# Sonuç
echo "============================================"
if [ $ERRORS -eq 0 ]; then
    echo "  ✅ TÜM KONTROLLER GEÇTİ"
    echo "  Sahne production-ready."
else
    echo "  ❌ $ERRORS hata bulundu"
    echo "  Sahne production-ready DEĞİL."
fi
echo "============================================"

exit $ERRORS
