#!/bin/bash
# validate-scene.sh — Sahne kalite kontrolü (v2)
# Kullanım: bash scripts/validate-scene.sh <sahne_dizini>

SCENE_DIR="${1:-.}"

echo "============================================"
echo "  SAHNE QA KONTROLÜ v2"
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

    echo "1. DOSYA YAPISI"
    SIZE=$(wc -c < "$TARGET")
    [ "$SIZE" -gt 500 ] && echo "  ✅ EPISODE.md var ($SIZE byte)" || { echo "  ❌ EPISODE.md çok küçük"; ERRORS=$((ERRORS+1)); }
    echo

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

    echo "3. KARAKTER KONTROLÜ"
    grep -qi "Kiko\|karakter" "$TARGET" && echo "  ✅ Karakter tanımlı" || { echo "  ❌ Karakter eksik"; ERRORS=$((ERRORS+1)); }
    grep -qi "coral pink\|#F8BBD0\|pigtails\|mitten" "$TARGET" && echo "  ✅ Karakter detayları" || echo "  ⚠️  Karakter detayları eksik"
    echo

    echo "4. MEKAN KONTROLÜ"
    grep -qi "Kiko's Home\|front garden\|bahçe\|Pompom Hills" "$TARGET" && echo "  ✅ Mekan tanımlı" || { echo "  ❌ Mekan eksik"; ERRORS=$((ERRORS+1)); }
    grep -qi "LOCKED\|locked\|DO NOT redesign" "$TARGET" && echo "  ✅ World Lock" || echo "  ⚠️  World Lock eksik"
    echo

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
        grep -qi "Reference Usage\|reference image\|world reference" "$SHOT01" && echo "  ✅ Reference Usage" || echo "  ⚠️  Reference Usage eksik"
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
    DIALOG_CONFLICT=0
    OVERLOADED=0

    for f in $(find "$SCENE_DIR/shots" -name "shot-0[2-9]*.md" -o -name "shot-1*.md" 2>/dev/null); do
        # Frame Lock
        grep -qi "frame zero\|@image1\|continuity frame\|previous shot" "$f" && FRAME_LOCK=$((FRAME_LOCK+1))
        
        # Camera Lock
        grep -qi "identical camera\|same camera\|continuity\|camera position" "$f" && CAMERA_LOCK=$((CAMERA_LOCK+1))
        
        # Lighting Lock
        grep -qi "first frame must preserve\|lighting.*identical\|same lighting\|colour grading" "$f" && LIGHTING_LOCK=$((LIGHTING_LOCK+1))
        
        # Character Presence
        grep -qi "already present\|character.*present\|Do not introduce" "$f" && CHAR_PRESENCE=$((CHAR_PRESENCE+1))
        
        # Text Safety
        grep -qi "No subtitles\|No text\|no on-screen" "$f" && TEXT_SAFETY=$((TEXT_SAFETY+1))
        
        # Dialogue Conflict (hem diyalog var hem "no dialogue" denmiş)
        HAS_DIALOG=$(grep -c "^Kiko:\|^Mimi:\|^Opa:\|^Luca:\|^Noah:\|^Arda:" "$f" 2>/dev/null)
        HAS_NO_DIALOG=$(grep -qi "no dialogue\|This shot has no dialogue" "$f" 2>/dev/null && echo "1" || echo "0")
        if [ "$HAS_NO_DIALOG" = "1" ] && [ "$HAS_DIALOG" -gt 0 ]; then
            DIALOG_CONFLICT=$((DIALOG_CONFLICT+1))
        fi
        
        # Overloaded check (6+ diyalog satırı)
        DIALOG_LINES=$(grep -c "^Kiko:\|^Mimi:\|^Opa:\|^Luca:\|^Noah:\|^Arda:" "$f" 2>/dev/null)
        if [ "$DIALOG_LINES" -gt 5 ]; then
            OVERLOADED=$((OVERLOADED+1))
        fi
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
    echo

    # 5. Dialogue Continuity
    echo "5. DIALOGUE CONTINUITY"
    [ "$DIALOG_CONFLICT" -eq 0 ] && echo "  ✅ Dialogue çelişkisi yok" || { echo "  ❌ $DIALOG_CONFLICT dosyada dialogue çelişkisi var"; ERRORS=$((ERRORS+1)); }
    echo

    # 6. Shot Duration Feasibility
    echo "6. SHOT DURATION FEASIBILITY"
    [ "$OVERLOADED" -eq 0 ] && echo "  ✅ Shot süreleri gerçekçi" || { echo "  ⚠️  $OVERLOADED dosyada aşırı yüklü shot var"; WARNINGS=$((WARNINGS+1)); }
    echo

    # 7. Render Prompts Kontrolü
    echo "7. RENDER PROMPTS KONTROLÜ"
    if [ -f "$SCENE_DIR/09-render-prompts.md" ]; then
        RP_SIZE=$(wc -c < "$SCENE_DIR/09-render-prompts.md")
        [ "$RP_SIZE" -gt 200 ] && echo "  ✅ Render prompts yeterli ($RP_SIZE byte)" || echo "  ⚠️  Render prompts çok kısa ($RP_SIZE byte)"
        grep -qi "@image1\|@image2\|@image" "$SCENE_DIR/09-render-prompts.md" && echo "  ✅ Image reference kullanılıyor" || echo "  ⚠️  Image reference eksik"
        grep -qi "No subtitles\|No text" "$SCENE_DIR/09-render-prompts.md" && echo "  ✅ Text Safety" || echo "  ⚠️  Text Safety eksik"
    fi
    echo

    # 8. World Continuity
    echo "8. WORLD CONTINUITY"
    grep -qi "LOCKED\|locked\|DO NOT redesign\|Do not redesign" "$SCENE_DIR/shots/"*.md 2>/dev/null | head -1 > /dev/null && echo "  ✅ World Lock" || echo "  ⚠️  World Lock eksik"
    echo

    # 9. Visual Continuity Rules
    echo "9. VISUAL CONTINUITY RULES"
    VC_RULES=0
    VC_TOTAL=7
    
    # Color Continuity
    grep -qi "colour\|color\|pastel\|warm.*light\|soft.*shadow" "$SCENE_DIR/shots/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Color Continuity eksik"
    
    # Lighting Continuity
    grep -qi "lighting\|moonlight\|sunlight\|exposure\|shadow" "$SCENE_DIR/shots/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Lighting Continuity eksik"
    
    # Camera Continuity
    grep -qi "camera\|35mm\|50mm\|eye level\|wide shot" "$SCENE_DIR/shots/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Camera Continuity eksik"
    
    # Scale Continuity
    grep -qi "scale\|6-8%\|SMALL preschool\|%.*frame\|environment hero" "$SCENE_DIR/shots/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Scale Continuity eksik"
    
    # Character Continuity
    grep -qi "already present\|character.*present\|Do not introduce\|consistency" "$SCENE_DIR/shots/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Character Continuity eksik"
    
    # World Continuity
    grep -qi "LOCKED\|locked\|Do not redesign\|Do not regenerate\|same place" "$SCENE_DIR/shots/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  World Continuity eksik"
    
    # Frame Continuity
    grep -qi "frame zero\|@image1\|continuity frame\|previous shot" "$SCENE_DIR/shots/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Frame Continuity eksik"
    
    echo "  Visual Continuity: $VC_RULES/$VC_TOTAL kural uygulanmış"
    [ "$VC_RULES" -eq "$VC_TOTAL" ] && echo "  ✅ Tüm Visual Continuity kuralları uygulanmış" || { echo "  ⚠️  $((VC_TOTAL-VC_RULES)) kural eksik"; WARNINGS=$((WARNINGS+1)); }
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
