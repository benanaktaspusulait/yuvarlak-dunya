#!/bin/bash
# validate-scene.sh — Sahne kalite kontrolü (v3)
# Kullanım: bash scripts/validate-scene.sh <sahne_dizini>

SCENE_DIR="${1:-.}"

# Layout resolution — supports both the classic 04-SCENES layout and the
# world-based POMPOM_HILLS_PRODUCTION episode-package layout.
#   classic  : <dir>/shots/            + <dir>/01-overview.md + <dir>/09-render-prompts.md
#   package  : <dir>/01_SHOTS/         + <dir>/00_EPISODE_OVERVIEW/{01-overview,09-render-prompts}.md
if [ -d "$SCENE_DIR/01_SHOTS" ]; then
    SHOTS_DIR="$SCENE_DIR/01_SHOTS"
else
    SHOTS_DIR="$SCENE_DIR/shots"
fi

if [ -f "$SCENE_DIR/01-overview.md" ]; then
    OVERVIEW_FILE="$SCENE_DIR/01-overview.md"
else
    OVERVIEW_FILE="$SCENE_DIR/00_EPISODE_OVERVIEW/01-overview.md"
fi

if [ -f "$SCENE_DIR/09-render-prompts.md" ]; then
    RENDER_FILE="$SCENE_DIR/09-render-prompts.md"
else
    RENDER_FILE="$SCENE_DIR/00_EPISODE_OVERVIEW/09-render-prompts.md"
fi

echo "============================================"
echo "  SAHNE QA KONTROLÜ v3"
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
    grep -qi "scale\|SMALL preschool\|%.*frame.*only\|%.*entire frame" "$TARGET" && echo "  ✅ Scale" || echo "  ⚠️  Scale eksik"
    grep -qi "No subtitles\|No text" "$TARGET" && echo "  ✅ Text Safety" || { echo "  ❌ Text Safety eksik"; ERRORS=$((ERRORS+1)); }
    grep -qi "negative\|NEGATIVE" "$TARGET" && echo "  ✅ Negative Prompt" || echo "  ⚠️  Negative Prompt eksik"
    grep -qi "continuity\|previous shot\|continuity frame\|Video Reference" "$TARGET" && echo "  ✅ Continuity" || echo "  ⚠️  Continuity eksik"
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
    [ -d "$SHOTS_DIR" ] && echo "  ✅ shot klasörü var ($(basename "$SHOTS_DIR")/)" || { echo "  ❌ shot klasörü YOK"; ERRORS=$((ERRORS+1)); }
    SHOT_COUNT=$(find "$SHOTS_DIR" -name "*.md" 2>/dev/null | wc -l)
    [ "$SHOT_COUNT" -ge 1 ] && echo "  ✅ $SHOT_COUNT shot dosyası" || { echo "  ❌ $SHOT_COUNT shot (minimum 1 gerekli)"; ERRORS=$((ERRORS+1)); }
    [ -f "$RENDER_FILE" ] && echo "  ✅ render-prompts.md var" || { echo "  ❌ render-prompts.md YOK"; ERRORS=$((ERRORS+1)); }
    [ -f "$OVERVIEW_FILE" ] && echo "  ✅ overview.md var" || echo "  ⚠️  overview.md yok"
    echo

    # 2. Shot-01 Kontrolü
    echo "2. SHOT-01 KONTROLÜ"
    SHOT01=$(find "$SHOTS_DIR" -name "shot-01*.md" 2>/dev/null | head -1)
    if [ -f "$SHOT01" ]; then
        grep -qi "Opening Hook\|## Hook\|ilk saniye\|first 3.*second\|first 3-5" "$SHOT01" && echo "  ✅ Opening Hook" || echo "  ⚠️  Opening Hook eksik"
        grep -qi "Scale\|SMALL preschool\|characters.*small\|childlike.*frame" "$SHOT01" && echo "  ✅ Scale talimatı" || echo "  ⚠️  Scale eksik"
        grep -qi "No subtitles\|No text\|no on-screen\|No speech bubbles" "$SHOT01" && echo "  ✅ Text Safety" || { echo "  ❌ Text Safety eksik"; ERRORS=$((ERRORS+1)); }
        grep -qi "## Negative Prompt\|negative prompt\|NEGATIVE\|Reject immediately" "$SHOT01" && echo "  ✅ Negative Prompt" || echo "  ⚠️  Negative Prompt eksik"
        grep -qi "## Reference Usage\|reference image\|world reference\|first-frame still" "$SHOT01" && echo "  ✅ Reference Usage" || echo "  ⚠️  Reference Usage eksik"
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

    for f in $(find "$SHOTS_DIR" -name "shot-0[2-9]*.md" -o -name "shot-1*.md" 2>/dev/null); do
        # Frame Lock
        grep -qi "frame zero\|@image1\|continuity frame\|previous shot\|Video Reference\|Use.*Shot.*as\|Use the previous shot\|approved.*frame\|Continuity" "$f" && FRAME_LOCK=$((FRAME_LOCK+1))
        
        # Camera Lock
        grep -qi "identical camera\|same camera\|camera position\|Continue from the exact framing\|seamlessly continue\|Camera Direction\|stable.*camera\|locked.*camera\|same.*framing\|Camera Continuity\|camera preserves\|Do not pull back\|Do not reframe\|composition.*stable" "$f" && CAMERA_LOCK=$((CAMERA_LOCK+1))
        
        # Lighting Lock
        grep -qi "first frame must preserve\|lighting.*identical\|same lighting as\|colour grading exactly\|Match the lighting\|Lighting Identity\|warm.*light\|soft.*shadow\|lighting.*locked\|Colour/lighting\|lighting match\|lighting.*drift\|Sky and Lighting\|Lighting Absolute\|lighting must be\|colour grading" "$f" && LIGHTING_LOCK=$((LIGHTING_LOCK+1))
        
        # Character Presence
        grep -qi "already present\|Do not introduce any character\|characters are already in frame\|Do not redesign\|Background locked\|Background Object Lock\|LOCKED\|locked\|Do not create\|Do not invent\|Do not move\|Do not replace" "$f" && CHAR_PRESENCE=$((CHAR_PRESENCE+1))
        
        # Text Safety
        grep -qi "No subtitles\|No text\|no on-screen\|No speech bubbles\|Do not display dialogue\|No captions" "$f" && TEXT_SAFETY=$((TEXT_SAFETY+1))
        
        # Dialogue Conflict (hem diyalog var hem "no dialogue" denmiş)
        HAS_DIALOG=$(grep -c "^Kiko:\|^Mimi:\|^Opa:\|^Luca:\|^Noah:\|^Arda:" "$f" 2>/dev/null)
        HAS_NO_DIALOG=$(grep -qi "^This shot has no dialogue\|^This scene has no dialogue\|^No dialogue\.$\|^Dialogue: None" "$f" 2>/dev/null && echo "1" || echo "0")
        if [ "$HAS_NO_DIALOG" = "1" ] && [ "$HAS_DIALOG" -gt 0 ]; then
            DIALOG_CONFLICT=$((DIALOG_CONFLICT+1))
        fi
        
        # Overloaded check (6+ diyalog satırı)
        DIALOG_LINES=$(grep -c "^Kiko:\|^Mimi:\|^Opa:\|^Luca:\|^Noah:\|^Arda:" "$f" 2>/dev/null)
        if [ "$DIALOG_LINES" -gt 5 ]; then
            OVERLOADED=$((OVERLOADED+1))
        fi
    done

    TOTAL_SHOTS=$(find "$SHOTS_DIR" -name "shot-0[2-9]*.md" -o -name "shot-1*.md" 2>/dev/null | wc -l)

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
    # Sadece "close-up" kullanımı kontrol et; "not a close-up", "no close-up" gibi
    # negatif talimatları sayma.
    CLOSEUPS=$(grep -rli "close-up\|Close-up" "$SHOTS_DIR/" 2>/dev/null | wc -l)
    CLOSEUP_POSITIVE=$(grep -rci "close-up\|Close-up" "$SHOTS_DIR/" 2>/dev/null | grep -v ":0$" | while read line; do
        file=$(echo "$line" | cut -d: -f1)
        count=$(echo "$line" | cut -d: -f2)
        neg=$(grep -ci "not.*close-up\|no close-up\|do not.*close-up\|must not.*close-up\|avoid.*close-up\|foreground close-up\|oversized\|cropped" "$file" 2>/dev/null)
        pos=$((count - ${neg:-0}))
        [ "$pos" -gt 0 ] && echo "$file"
    done | wc -l)
    [ "$CLOSEUP_POSITIVE" -eq 0 ] && echo "  ✅ Close-up yok" || { echo "  ❌ $CLOSEUP_POSITIVE dosyada close-up var"; ERRORS=$((ERRORS+1)); }
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
    if [ -f "$RENDER_FILE" ]; then
        RP_SIZE=$(wc -c < "$RENDER_FILE")
        [ "$RP_SIZE" -gt 200 ] && echo "  ✅ Render prompts yeterli ($RP_SIZE byte)" || echo "  ⚠️  Render prompts çok kısa ($RP_SIZE byte)"
        grep -qi "@image1\|@image2\|@image\|Video Reference\|Use.*Shot.*as\|Use the previous shot\|first-frame still" "$RENDER_FILE" && echo "  ✅ Image reference kullanılıyor" || echo "  ⚠️  Image reference eksik"
        grep -qi "No subtitles\|No text\|No speech bubbles\|No captions" "$RENDER_FILE" && echo "  ✅ Text Safety" || echo "  ⚠️  Text Safety eksik"
    fi
    echo

    # 8. World Continuity
    echo "8. WORLD CONTINUITY"
    grep -qi "LOCKED\|locked\|DO NOT redesign\|Do not redesign" "$SHOTS_DIR/"*.md 2>/dev/null | head -1 > /dev/null && echo "  ✅ World Lock" || echo "  ⚠️  World Lock eksik"
    echo

    # 9. Visual Continuity Rules
    echo "9. VISUAL CONTINUITY RULES"
    VC_RULES=0
    VC_TOTAL=8
    
    # Color Continuity
    grep -qi "colour\|color\|pastel\|warm.*light\|soft.*shadow" "$SHOTS_DIR/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Color Continuity eksik"
    
    # Lighting Continuity
    grep -qi "lighting\|sunlight\|exposure\|shadow" "$SHOTS_DIR/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Lighting Continuity eksik"
    
    # Camera Continuity
    grep -qi "camera\|35mm\|50mm\|eye level\|wide shot" "$SHOTS_DIR/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Camera Continuity eksik"
    
    # Scale Continuity
    grep -qi "Scale\|SMALL preschool\|characters.*small\|childlike.*frame\|environment hero" "$SHOTS_DIR/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Scale Continuity eksik"
    
    # Character Continuity
    grep -qi "already present\|Do not introduce any character\|characters are already in frame\|consistency" "$SHOTS_DIR/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Character Continuity eksik"
    
    # World Continuity
    grep -qi "LOCKED\|locked\|Do not redesign\|Do not regenerate\|same place" "$SHOTS_DIR/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  World Continuity eksik"
    
    # Frame Continuity
    grep -qi "frame zero\|@image1\|continuity frame\|previous shot\|Video Reference\|Use.*Shot.*as\|Use the previous shot" "$SHOTS_DIR/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Frame Continuity eksik"
    
    # Anti-Desaturation
    grep -qi "Do NOT desaturate\|Maintain FULL saturation\|vibrant\|saturation.*DO NOT" "$SHOTS_DIR/"*.md 2>/dev/null | head -1 > /dev/null && VC_RULES=$((VC_RULES+1)) || echo "  ⚠️  Anti-Desaturation eksik"
    
    echo "  Visual Continuity: $VC_RULES/$VC_TOTAL kural uygulanmış"
    [ "$VC_RULES" -eq "$VC_TOTAL" ] && echo "  ✅ Tüm Visual Continuity kuralları uygulanmış" || { echo "  ⚠️  $((VC_TOTAL-VC_RULES)) kural eksik"; WARNINGS=$((WARNINGS+1)); }
    echo

    # 10. Time of Day Consistency (shot'lar arası ışık/zaman driftini yakalar)
    echo "10. TIME OF DAY CONSISTENCY"
    TOD=$(grep -rh '^[[:space:]]*|[[:space:]]*Time of Day' "$SHOTS_DIR/"*.md 2>/dev/null \
        | sed -E 's/^[^|]*\|[^|]*\|([^|]*)\|.*/\1/' \
        | sed 's/^ *//;s/ *$//' \
        | tr '[:upper:]' '[:lower:]' \
        | sort -u | grep .)
    TOD_COUNT=$(printf '%s\n' "$TOD" | grep -c .)
    if [ "$TOD_COUNT" -le 1 ]; then
        echo "  ✅ Time of Day tutarlı"
    else
        echo "  ⚠️  Shot'lar arası Time of Day tutarsız ($TOD_COUNT farklı değer):"
        printf '%s\n' "$TOD" | sed 's/^/     - /'
        WARNINGS=$((WARNINGS+1))
    fi
    echo

    # 11. Shot Count / Duration Tutarlılığı
    echo "11. SHOT COUNT / DURATION"
    if [ -f "$OVERVIEW_FILE" ]; then
        DECLARED=$(grep -oiE '[0-9]+[[:space:]]*shots?' "$OVERVIEW_FILE" 2>/dev/null | head -1 | grep -oE '[0-9]+')
        # shot-00* is a story-external micro-opening (§9c/§9d); exclude it from the story shot count.
        ACTUAL=$(find "$SHOTS_DIR" -name "shot-*.md" ! -name "shot-00*" 2>/dev/null | wc -l | tr -d ' ')
        OPENER=$(find "$SHOTS_DIR" -name "shot-00*.md" 2>/dev/null | wc -l | tr -d ' ')
        [ "$OPENER" -gt 0 ] && echo "  ℹ️  Micro-opening (shot-00) mevcut — hikaye-dışı, sayıma dahil değil"
        if [ -n "$DECLARED" ]; then
            if [ "$DECLARED" -eq "$ACTUAL" ]; then
                echo "  ✅ Shot sayısı overview ile uyumlu ($ACTUAL shot)"
            else
                echo "  ⚠️  Overview $DECLARED shot diyor, ama $ACTUAL shot dosyası var"
                WARNINGS=$((WARNINGS+1))
            fi
        else
            echo "  ⚠️  Overview'da shot sayısı belirtilmemiş"
        fi
    else
        echo "  ⚠️  01-overview.md yok, shot sayısı doğrulanamadı"
    fi
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
