#!/bin/bash
# Opa's Storytime EP01 — Episode Combining Script
# Bu script tüm shot'ları, başlık kartını ve bitiş kartını birleştirir.

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "=== Opa's Storytime EP01 — Shot Combining ==="
echo ""

# --- ADIM 1: Shot 5 ses ekleme (Opa sesi) ---
echo "[1/4] Shot 5'e Opa sesi ekleniyor..."
VOICE_DIR="/Users/benanaktas/project/video/yuvarlak-dunya/05-AI-PROMPTS/voice"
OPA_VOICE="$VOICE_DIR/shot-05-opa-not-yet.wav"

if [ -f "$OPA_VOICE" ]; then
    # Shot 5: 0-2.2sn orijinal, 2.2-7sn Opa sesi, 7-15sn orijinal
    ffmpeg -y -i shot-5.mp4 -to 2.2 -c:v libx264 -c:a aac -ar 48000 -ac 2 /tmp/p1.mp4 2>/dev/null
    ffmpeg -y -i shot-5.mp4 -ss 2.2 -to 7 -an -c:v libx264 /tmp/p2v.mp4 2>/dev/null
    ffmpeg -y -i /tmp/p2v.mp4 -i "$OPA_VOICE" \
      -filter_complex "[1:a]aresample=48000,pan=stereo|FL=c0|FR=c0[a]" \
      -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 128k -shortest \
      /tmp/p2.mp4 2>/dev/null
    ffmpeg -y -i shot-5.mp4 -ss 7 -c:v libx264 -c:a aac -ar 48000 -ac 2 /tmp/p3.mp4 2>/dev/null
    
    printf "file 'p1.mp4'\nfile 'p2.mp4'\nfile 'p3.mp4'\n" > /tmp/concat5.txt
    ffmpeg -y -f concat -safe 0 -i /tmp/concat5.txt -c copy shot-5-with-voice.mp4 2>/dev/null
    rm /tmp/p1.mp4 /tmp/p2v.mp4 /tmp/p2.mp4 /tmp/p3.mp4 /tmp/concat5.txt 2>/dev/null
    echo "  Shot 5 Opa sesi eklendi."
else
    echo "  UYARI: Opa ses dosyası bulunamadı, shot-5 orijinal kullanılıyor."
    cp shot-5.mp4 shot-5-with-voice.mp4
fi

# --- ADIM 2: Shot 1-5 birleştir ---
echo "[2/4] Shot 1-5 birleştiriliyor..."
ffmpeg -y \
  -i shot-1.mp4 -i shot-2.mp4 -i shot-3.mp4 -i shot-4.mp4 -i shot-5-with-voice.mp4 \
  -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a]concat=n=5:v=1:a=1[outv][outa]" \
  -map "[outv]" -map "[outa]" -c:v libx264 -c:a aac -ar 48000 -ac 2 \
  /tmp/part-1-5.mp4 2>/dev/null
echo "  Shot 1-5 tamamlandı."

# --- ADIM 3: Shot 6-20 birleştir ---
echo "[3/4] Shot 6-20 birleştiriliyor..."
ffmpeg -y \
  -i shot-6.mp4 -i shot-7.mp4 -i shot-8.mp4 -i shot-9.mp4 -i shot-10.mp4 \
  -i shot-11.mp4 -i shot-12.mp4 -i shot-13.mp4 -i shot-14.mp4 -i shot-15.mp4 \
  -i shot-16.mp4 -i shot-17.mp4 -i shot-18.mp4 -i shot-19.mp4 -i shot-20.mp4 \
  -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a][5:v][5:a][6:v][6:a][7:v][7:a][8:v][8:a][9:v][9:a][10:v][10:a][11:v][11:a][12:v][12:a][13:v][13:a][14:v][14:a]concat=n=15:v=1:a=1[outv][outa]" \
  -map "[outv]" -map "[outa]" -c:v libx264 -c:a aac -ar 48000 -ac 2 \
  /tmp/part-6-20.mp4 2>/dev/null
echo "  Shot 6-20 tamamlandı."

# --- ADIM 4: Tümünü birleştir + başlık ve bitiş ---
echo "[4/4] Tam bölüm oluşturuluyor..."

# Tüm shot'ları birleştir
ffmpeg -y \
  -i /tmp/part-1-5.mp4 -i /tmp/part-6-20.mp4 \
  -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[outv][outa]" \
  -map "[outv]" -map "[outa]" -c:v libx264 -c:a aac -ar 48000 -ac 2 \
  /tmp/all-shots.mp4 2>/dev/null

# Başlık kartı (2.5sn: 1.5sn static + 1sn fade-out)
ffmpeg -y -loop 1 -i giris.png -t 2.5 \
  -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1,fade=t=out:st=1.5:d=1.0" \
  -r 24 -pix_fmt yuv420p /tmp/title.mp4 2>/dev/null

# Shot 1'e fade-in ekle
ffmpeg -y -i shot-1.mp4 -vf "fade=t=in:st=0:d=1.0" -af "afade=t=in:st=0:d=1.0" \
  -r 24 -pix_fmt yuv420p /tmp/shot1-fade.mp4 2>/dev/null

# Shot 2-20
ffmpeg -y \
  -i shot-2.mp4 -i shot-3.mp4 -i shot-4.mp4 -i shot-5-with-voice.mp4 \
  -i shot-6.mp4 -i shot-7.mp4 -i shot-8.mp4 -i shot-9.mp4 -i shot-10.mp4 \
  -i shot-11.mp4 -i shot-12.mp4 -i shot-13.mp4 -i shot-14.mp4 -i shot-15.mp4 \
  -i shot-16.mp4 -i shot-17.mp4 -i shot-18.mp4 -i shot-19.mp4 -i shot-20.mp4 \
  -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a][5:v][5:a][6:v][6:a][7:v][7:a][8:v][8:a][9:v][9:a][10:v][10:a][11:v][11:a][12:v][12:a][13:v][13:a][14:v][14:a][15:v][15:a][16:v][16:a][17:v][17:a][18:v][18:a]concat=n=19:v=1:a=1[outv][outa]" \
  -map "[outv]" -map "[outa]" -c:v libx264 -c:a aac -ar 48000 -ac 2 \
  /tmp/shot1-rest.mp4 2>/dev/null

# Başlık + fade-in shot-1 + shot 2-20
printf "file 'title.mp4'\nfile 'shot1-fade.mp4'\nfile 'shot1-rest.mp4'\n" > /tmp/concat-full.txt
ffmpeg -y -f concat -safe 0 -i /tmp/concat-full.txt \
  -vf "fps=24" -c:v libx264 -c:a aac -ar 48000 -ac 2 -pix_fmt yuv420p \
  episode-no-endcard.mp4 2>/dev/null

# Bitiş kartı (4.5sn: 0.8sn fade-in, 2.5sn static, 1.2sn fade-out)
ffmpeg -y -loop 1 -i cikis.png -t 4.5 \
  -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1,fade=t=in:st=0:d=0.8,fade=t=out:st=3.3:d=1.2" \
  -r 24 -pix_fmt yuv420p /tmp/endcard.mp4 2>/dev/null

# Son 0.8sn kırp + bitiş kartı
TOTAL=$(ffprobe -v error -show_entries format=duration -of csv=p=0 episode-no-endcard.mp4)
TRIM=$(echo "$TOTAL - 0.8" | bc)
ffmpeg -y -i episode-no-endcard.mp4 -t "$TRIM" -c copy /tmp/trimmed.mp4 2>/dev/null

printf "file 'trimmed.mp4'\nfile 'endcard.mp4'\n" > /tmp/concat-end.txt
ffmpeg -y -f concat -safe 0 -i /tmp/concat-end.txt \
  -c:v libx264 -c:a aac -ar 48000 -ac 2 -pix_fmt yuv420p \
  episode-complete.mp4 2>/dev/null

# Temizlik
rm -f /tmp/part-1-5.mp4 /tmp/part-6-20.mp4 /tmp/all-shots.mp4 /tmp/title.mp4 \
  /tmp/shot1-fade.mp4 /tmp/shot1-rest.mp4 /tmp/concat-full.txt /tmp/endcard.mp4 \
  /tmp/trimmed.mp4 /tmp/concat-end.txt /tmp/concat5.txt /tmp/p1.mp4 /tmp/p2v.mp4 \
  /tmp/p2.mp4 /tmp/p3.mp4 /tmp/shot5-with-voice.mp4 episode-no-endcard.mp4 2>/dev/null

echo ""
echo "=== TAMAMLANDI ==="
DURATION=$(ffprobe -v error -show_entries format=duration -of default episode-complete.mp4)
SIZE=$(ls -lh episode-complete.mp4 | awk '{print $5}')
echo "Dosya: episode-complete.mp4"
echo "Süre: $DURATION"
echo "Boyut: $SIZE"
