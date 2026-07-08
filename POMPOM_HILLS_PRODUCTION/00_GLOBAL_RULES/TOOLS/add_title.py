import sys
import os
from PIL import Image, ImageDraw, ImageFont
import subprocess
import tempfile

def add_title(input_path, output_path, title1="Pompom Hills", title2="The Soft Wind", duration=5.0):
    # Create title frame as image
    tmp_img = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    
    # Get video dimensions
    probe = subprocess.run(
        ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_streams', input_path],
        capture_output=True, text=True
    )
    import json
    info = json.loads(probe.stdout)
    width = int(info['streams'][0]['width'])
    height = int(info['streams'][0]['height'])
    
    # Create transparent overlay image
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Load font
    try:
        font1 = ImageFont.truetype("/System/Library/Fonts/SFNSRounded.ttf", 48)
        font2 = ImageFont.truetype("/System/Library/Fonts/SFNSRounded.ttf", 34)
    except:
        font1 = ImageFont.load_default()
        font2 = ImageFont.load_default()
    
    # Calculate positions — bottom center
    bbox1 = draw.textbbox((0, 0), title1, font=font1)
    w1 = bbox1[2] - bbox1[0]
    bbox2 = draw.textbbox((0, 0), title2, font=font2)
    w2 = bbox2[2] - bbox2[0]
    
    x1 = (width - w1) // 2
    y1 = int(height * 0.88)
    x2 = (width - w2) // 2
    y2 = y1 + 50
    
    # Draw shadow (warm brown for forest feel)
    draw.text((x1+2, y1+2), title1, font=font1, fill=(60, 40, 20, 120))
    draw.text((x2+1, y2+1), title2, font=font2, fill=(60, 40, 20, 90))
    
    # Draw text (warm cream/golden)
    draw.text((x1, y1), title1, font=font1, fill=(255, 245, 220, 250))
    draw.text((x2, y2), title2, font=font2, fill=(255, 240, 210, 230))
    
    overlay.save(tmp_img.name)
    
    # Create ffmpeg filter for fade in/out
    fade_filter = (
        f"overlay=0:0:enable='between(t,0.5,{duration})',"
        f"fade=t=in:st=0.5:d=0.5,fade=t=out:st={duration-0.5}:d=0.5"
    )
    
    # Build ffmpeg command with proper filter complex
    cmd = [
        'ffmpeg', '-y',
        '-i', input_path,
        '-i', tmp_img.name,
        '-filter_complex',
        f"[0:v][1:v]overlay=0:0:enable='between(t,0.5,{duration})'[outv]",
        '-map', '[outv]',
        '-map', '0:a',
        '-c:v', 'libx264', '-crf', '18', '-preset', 'slow',
        '-c:a', 'copy',
        output_path
    ]
    
    print(f"Processing: {os.path.basename(input_path)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr[-200:]}")
    else:
        print(f"Done: {os.path.basename(output_path)}")
    
    os.unlink(tmp_img.name)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    add_title(input_file, output_file)
