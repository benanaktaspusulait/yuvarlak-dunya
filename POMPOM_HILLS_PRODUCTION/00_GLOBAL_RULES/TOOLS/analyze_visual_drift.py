#!/usr/bin/env python3
"""analyze_visual_drift.py — Hızlı görsel drift analizi."""
import sys, os, json, argparse
from PIL import Image, ImageStat

def analyze(img):
    small = img.resize((160, 90))
    gray = small.convert('L')
    stat = ImageStat.Stat(gray)
    px = list(gray.getdata())
    n = len(px)
    sx = sorted(px)
    
    return {
        'mean': round(stat.mean[0], 1),
        'median': round(stat.median[0], 1),
        'p10': sx[n//10],
        'p90': sx[int(n*0.9)],
        'shadow': sx[int(n*0.05)],
        'contrast': round(stat.stddev[0], 1),
        'black_clip': round(sum(1 for p in px if p<5)/n*100, 3),
        'white_clip': round(sum(1 for p in px if p>250)/n*100, 3),
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--refs', nargs='+', required=True)
    p.add_argument('--master', required=True)
    p.add_argument('--output-dir', default='.')
    args = p.parse_args()
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    master = analyze(Image.open(args.master))
    print(f'Master: mean={master["mean"]}, contrast={master["contrast"]}')
    
    results = []
    for ref in args.refs:
        m = analyze(Image.open(ref))
        name = os.path.basename(ref)
        
        drift = {}
        for k in ['mean', 'median', 'p10', 'p90', 'contrast']:
            if master[k] != 0:
                drift[k] = round((m[k] - master[k]) / abs(master[k]) * 100, 1)
            else:
                drift[k] = 0
        
        verdict = all(abs(v) <= t for v, t in [
            (drift['mean'], 5), (drift['contrast'], 100)
        ])
        
        results.append({'name': name, 'metrics': m, 'drift': drift, 'pass': verdict})
        print(f'{name}: mean={m["mean"]}, contrast={m["contrast"]} | drift: {drift} | {"PASS" if verdict else "FAIL"}')
    
    # Progressive drift
    if len(results) >= 2:
        f, l = results[0]['metrics'], results[-1]['metrics']
        print(f'\nProgressive: mean {f["mean"]}→{l["mean"]} ({(l["mean"]-f["mean"])/f["mean"]*100:+.1f}%)')
        print(f'Progressive: contrast {f["contrast"]}→{l["contrast"]} ({(l["contrast"]-f["contrast"])/f["contrast"]*100:+.1f}%)')
    
    with open(os.path.join(args.output_dir, 'drift-report.json'), 'w') as fh:
        json.dump({'master': master, 'results': results}, fh, indent=2)

if __name__ == '__main__':
    main()
