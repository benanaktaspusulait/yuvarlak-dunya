#!/bin/bash
# validate-scene.sh — Sahne kalite kontrolü
# Kullanım: bash scripts/validate-scene.sh <sahne_dizini>
# Desteklenen yapılar:
#   - Tek dosya: EPISODE.md (yeni standart)
#   - Klasör yapısı: shots/ + overview + render-prompts (eski standart)

SCENE_DIR="${1:-.}"

echo "============================================"
echo "  SAHNE QA KONTROLÜ"
echo "  Dizin: $SCENE_DIR"
echo "============================================"
echo

ERRORS=0
WARNINGS=0

# Yapı tespiti
SINGLE_FILE=0
if [ -f "$SCENE_DIR/EPISODE.md" ]; then
    SINGLE_FILE=1
    echo "  📄 Yapı: Tek dosya (EPISODE.md)"
else
    echo "  📂 Yapı: Klasör (shots/ + dosyalar)"
fi
echo

# ============================================
# TEK DOSYA YAPISI
# ============================================
if [ "$SINGLE_FILE" -eq 1 ]; then
    TARGET="$SCENE_DIR/EPISODE.md"

    # 1. Dosya Yapısı
    echo "1. DOSYA YAPISI"
    SIZE=$(wc -c < "$TARGET")
    [ "$SIZE" -gt 500 ] && echo "  ✅ EPISODE.md var ($SIZE byte)" || { echo "  ❌ EPISODE.md çok küçük"; ERRORS=$((ERRORS+1)); }
    echo

    # 2. İçerik Kontrolü
    echo "2. İÇERİK KONTROLÜ"
    grep -qi "Shot 01\|Shot 02\|Shot 03\|Shot 04" "$TARGET" && echo "  ✅ Shot yapısı" || { echo "  ❌ Shot yapısı eksik"; ERRORS=$((ERRORS+1)); }
    grep -qi "dialogue\|Kiko:" "$TARGET" && echo "  ✅ Dialogue" || { echo "  ❌ Dialogue eksik"; ERRORS=$((ERRORS+1)); }
    grep -qi "render prompt\|Create a cinematic\|OPENART" "$TARGET" && echo "  ✅ Render Prompt" || { echo "  ❌ Render Prompt eksik"; ERRORS=$((ERRORS+1)); }
    grep -qi "scale\|8%\|SMALL preschool" "$TARGET" && echo "  ✅ Scale" || echo "  ⚠️  Scale eksik"
    grep -qi "No subtitles\|No text" "$TARGET" && echo "  ✅ Text Safety" || { echo "  ❌ Text Safety eksik"; ERRORS=$((ERRORS+1)); }
    grep -qi "negative\|NEGATIVE\|reject" "$TARGET" && echo "  ✅ Negative Prompt" || echo "  ⚠️  Negative Prompt eksik"
    grep -qi "continuity\|previous shot\|continuity frame" "$TARGET" && echo "  ✅ Continuity" || echo "  ⚠️  Continuity eksik"
    grep -qi "QA\|quality" "$TARGET" && echo "  ✅ QA bölümü" || echo "  ⚠️  QA eksik"
    echo

    # 3. Karakter
    echo "3. KARAKTER KONTROLÜ"
    grep -qi "Kiko\|karakter" "$TARGET" && echo "  ✅ Karakter tanımlı" || { echo "  ❌ Karakter eksik"; ERRORS=$((ERRORS+1)); }
    grep -qi "coral pink\|#F8BBD0\|pigtails\|mitten" "$TARGET" && echo "  ✅ Karakter detayları" || echo "  ⚠️  Karakter detayları eksik"
    echo

    # 4. Mekan
    echo "4. MEKAN KONTROLÜ"
    grep -qi "Kiko's Home\|front garden\|bahçe\|Pompom Hills" "$TARGET" && echo "  ✅ Mekan tanımlı" || { echo "  ❌ Mekan eksik"; ERRORS=$((ERRORS+1)); }
    grep -qi "LOCKED\|locked\|DO NOT redesign" "$TARGET" && echo "  ✅ World Lock" || echo "  ⚠️  World Lock eksik"
    echo

    # 5. Production
    echo "5. PRODUCTION KURALLARI"
    grep -qi "low stimulation\|gentle\|preschool\|warm" "$TARGET" && echo "  ✅ Production kuralları" || echo "  ⚠️  Production kuralları eksik"
    grep -qi "ONE episode\|tek episode\|15 saniye\|15 seconds" "$TARGET" && echo "  ✅ Tek episode belirtilmiş" || echo "  ⚠️  Episode yapısı belirsiz"

# ============================================
# KLASÖR YAPISI
# ============================================
else
    # 1. Dosya Yapısı
    echo "1. DOSYA YAPISI"
    [ -d "$SCENE_DIR/shots" ] && echo "  ✅ shots/ klasörü var" || { echo "  ❌ shots/ klasörü YOK"; ERRORS=$((ERRORS+1)); }
    SHOT_COUNT=$(find "$SCENE_DIR/shots" -name "*.md" 2>/dev/null | wc -l)
    [ "$SHOT_COUNT" -ge 1 ] && echo "  ✅ $SHOT_COUNT shot dosyası" || { echo "  ❌ $SHOT_COUNT shot (minimum 1 gerekli)"; ERRORS=$((ERRORS+1)); }
    [ -f "$SCENE_DIR/09-render-prompts.md" ] && echo "  ✅ render-prompts.md var" || { echo "  ❌ render-prompts.md YOK"; ERRORS=$((ERRORS+1)); }
    [ -f "$SCENE_DIR/01-overview.md" ] && echo "  ✅ overview.md var" || echo "  ⚠️  overview.md yok"
    echo

    # 2. Shot-01 Kontrolü
    echo "2. SHOT-01 KONTROLÜ"
    SHOT01=$(find "$SCENE_DIR/shots" -name "shot-01*.md" 2>/dev/null | head -1)
    if [ -f "$SHOT01" ]; then
        grep -qi "Opening Hook\|Hook\|ilk saniye\|first second" "$SHOT01" && echo "  ✅ Opening Hook" || echo "  ⚠️  Opening Hook eksik"
        grep -qi "6-8%\|SMALL preschool\|scale\|%.*frame" "$SHOT01" && echo "  ✅ Scale talimatı" || echo "  ⚠️  Scale eksik"
        grep -qi "No subtitles\|No text\|no on-screen" "$SHOT01" && echo "  ✅ Text Safety" || { echo "  ❌ Text Safety eksik"; ERRORS=$((ERRORS+1)); }
        grep -qi "Negative Prompt\|negative prompt\|NEGATIVE\|reject" "$SHOT01" && echo "  ✅ Negative Prompt" || echo "  ⚠️  Negative Prompt eksik"
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
        grep -qi "frame zero\|continuity frame\|previous shot" "$f" && FRAME_LOCK=$((FRAME_LOCK+1))
        grep -qi "identical camera\|same camera\|continuity" "$f" && CAMERA_LOCK=$((CAMERA_LOCK+1))
        grep -qi "first frame must preserve\|lighting.*identical\|same lighting" "$f" && LIGHTING_LOCK=$((LIGHTING_LOCK+1))
        grep -qi "already present\|character.*present\|Kiko" "$f" && CHAR_PRESENCE=$((CHAR_PRESENCE+1))
        grep -qi "No subtitles\|No text\|no on-screen" "$f" && TEXT_SAFETY=$((TEXT_SAFETY+1))
    done

    TOTAL_SHOTS=$(find "$SCENE_DIR/shots" -name "shot-0[2-9]*.md" -o -name "shot-1*.md" 2>/dev/null | wc -l)

    if [ "$TOTAL_SHOTS" -gt 0 ]; then
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
    fi
    echo

    # 4. Close-up Kontrolü
    echo "4. CLOSE-UP KONTROLÜ"
    CLOSEUPS=$(grep -rli "Close-up\|close-up" "$SCENE_DIR/shots/" 2>/dev/null | wc -l)
    [ "$CLOSEUPS" -eq 0 ] && echo "  ✅ Close-up yok" || { echo "  ❌ $CLOSEUPS dosyada close-up var"; ERRORS=$((ERRORS+1)); }
fi

echo
echo "============================================"
if [ $ERRORS -eq 0 ]; then
    echo "  ✅ TÜM KONTROLLER GEÇTİ"
    echo "  Sahne production-ready."
else
    echo "  ❌ $ERRORS hata bulundu"
    echo "  Sahne production-ready DEĞİL."
fi
[ $WARNINGS -gt 0 ] && echo "  ⚠️  $WARNINGS uyarı"
echo "============================================"

exit $ERRORS
