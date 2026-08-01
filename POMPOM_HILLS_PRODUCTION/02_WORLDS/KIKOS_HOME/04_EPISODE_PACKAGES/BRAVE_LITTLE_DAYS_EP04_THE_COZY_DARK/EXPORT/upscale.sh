#!/usr/bin/env bash
#
# upscale.sh — Video çözünürlük yükseltme aracı
#
# Verilen video dosyalarını (veya bir klasördeki tüm .mp4'leri) hedef
# çözünürlüğe yükseltir. En-boy oranı hedeften farklıysa bozulma olmaması
# için "cover" mantığıyla ölçekler ve fazlalığı ortadan minimal kırpar.
# Ses, kare hızı ve süre korunur.
#
# Kullanım:
#   ./upscale.sh dosya1.mp4 [dosya2.mp4 ...]      # belirtilen dosyalar
#   ./upscale.sh -d /yol/klasor                    # klasördeki tüm .mp4'ler
#   ./upscale.sh -r 3840x2160 dosya.mp4            # hedef çözünürlük değiştir
#   ./upscale.sh -s dosya.mp4                       # orijinali koru (üzerine yazma)
#
# Seçenekler:
#   -r WxH   Hedef çözünürlük (varsayılan: 1920x1080)
#   -d DIR   Klasördeki tüm .mp4 dosyalarını işle
#   -s       Güvenli mod: orijinali silme, *_hd.mp4 olarak kaydet
#   -c CRF   x264 kalite (varsayılan: 18, düşük = daha kaliteli)
#   -h       Bu yardımı göster
#
set -euo pipefail

TARGET="1920x1080"
CRF=18
SAFE=0
DIR=""

usage() { sed -n '2,26p' "$0"; exit "${1:-0}"; }

while getopts ":r:d:c:sh" opt; do
  case "$opt" in
    r) TARGET="$OPTARG" ;;
    d) DIR="$OPTARG" ;;
    c) CRF="$OPTARG" ;;
    s) SAFE=1 ;;
    h) usage 0 ;;
    \?) echo "Bilinmeyen seçenek: -$OPTARG" >&2; usage 1 ;;
    :) echo "-$OPTARG bir değer bekliyor" >&2; usage 1 ;;
  esac
done
shift $((OPTIND - 1))

command -v ffmpeg  >/dev/null 2>&1 || { echo "HATA: ffmpeg bulunamadı." >&2; exit 1; }
command -v ffprobe >/dev/null 2>&1 || { echo "HATA: ffprobe bulunamadı." >&2; exit 1; }

TW="${TARGET%x*}"
TH="${TARGET#*x}"
if ! [[ "$TW" =~ ^[0-9]+$ && "$TH" =~ ^[0-9]+$ ]]; then
  echo "HATA: Geçersiz çözünürlük '$TARGET' (örn. 1920x1080)." >&2
  exit 1
fi

# İşlenecek dosya listesini topla
FILES=()
if [[ -n "$DIR" ]]; then
  [[ -d "$DIR" ]] || { echo "HATA: Klasör yok: $DIR" >&2; exit 1; }
  while IFS= read -r -d '' f; do FILES+=("$f"); done \
    < <(find "$DIR" -maxdepth 1 -type f -name '*.mp4' -print0 | sort -z)
fi
FILES+=("$@")

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "HATA: İşlenecek dosya belirtilmedi." >&2
  usage 1
fi

process() {
  local in="$1"
  [[ -f "$in" ]] || { echo "  ! atlandı (dosya yok): $in" >&2; return; }

  # Mevcut çözünürlük
  local dims w h
  dims="$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
          -of csv=p=0 "$in" 2>/dev/null || true)"
  w="${dims%,*}"; h="${dims#*,}"

  if [[ -z "$w" || -z "$h" ]]; then
    echo "  ! atlandı (video akışı okunamadı, bozuk olabilir): $in" >&2
    return
  fi

  if [[ "$w" -ge "$TW" && "$h" -ge "$TH" ]]; then
    echo "  = zaten yeterli (${w}x${h} >= ${TW}x${TH}), atlanıyor: $(basename "$in")"
    return
  fi

  local dir base tmp
  dir="$(dirname "$in")"
  base="$(basename "${in%.*}")"
  tmp="${dir}/${base}_hd.mp4"

  echo "  > ${w}x${h} -> ${TW}x${TH}: $(basename "$in")"

  # cover ölçek + ortadan minimal crop (en-boy korunur, bozulma olmaz)
  ffmpeg -y -loglevel error -i "$in" \
    -vf "scale=${TW}:${TH}:force_original_aspect_ratio=increase:flags=lanczos,crop=${TW}:${TH}" \
    -c:v libx264 -preset slow -crf "$CRF" -pix_fmt yuv420p \
    -c:a aac -b:a 130k \
    "$tmp"

  if [[ "$SAFE" -eq 1 ]]; then
    echo "    kaydedildi: $(basename "$tmp") (orijinal korundu)"
  else
    mv -f "$tmp" "$in"
    echo "    güncellendi: $(basename "$in")"
  fi
}

echo "Hedef çözünürlük: ${TW}x${TH} | CRF: ${CRF} | Güvenli mod: $([[ $SAFE -eq 1 ]] && echo açık || echo kapalı)"
for f in "${FILES[@]}"; do
  process "$f"
done
echo "Bitti."
