"""นำเข้าท่าโจมตีจาก Grok ให้เข้ากับไฟล์ sprite เดิม

ภาพจาก Grok: ตัวละคร 4 ท่าเรียงแนวนอนในภาพเดียว พื้นหลังสีเดียว (เช่น ชมพู)
สคริปต์จะ: ลบพื้นหลัง → แยก 4 เฟรม → ย่อให้สูงเท่าภาพ facing เดิม
→ วางเท้าที่บรรทัด 371 → บันทึกเป็น assets/dragon/attack/<char>/<dir>/00-03.png
→ สร้าง atlas ใหม่ (tools/build_sprites.py) เกมจะสลับจากท่าพุ่งตัวมาใช้ท่านี้เอง

ใช้:
  python tools/import_attack.py <ภาพจาก_grok> <ตัวละคร> <ทิศ>
  python tools/import_attack.py grok/spear_s.png spear s
  python tools/import_attack.py --check            # ตรวจว่าท่าโจมตีครบหรือยัง
"""
import argparse
import json
import os
import sys

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8")  # คอนโซล Windows พิมพ์ภาษาไทยได้
except Exception:
    pass

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "dragon")
DIRS = ["s", "sw", "w", "nw", "n", "ne", "e", "se"]
CHARS = ["female", "male", "chief", "spear", "archer", "elite", "leader"]
ATTACKERS = ["male", "chief", "spear", "archer", "elite", "leader"]
CANVAS_H = 394
BASELINE = 371  # แถวพิกเซลล่างสุดของเท้า
PAD = 6


def detect_bg(im):
    w, h = im.size
    pts = [(2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3), (w // 2, 2), (w // 2, h - 3)]
    px = [im.getpixel(p)[:3] for p in pts]
    px.sort(key=lambda c: sum(c))
    r, g, b = px[len(px) // 2]
    return r, g, b


def key_out(im, bg, inner=60, outer=130):
    """ลบพื้นหลังตามระยะสี พร้อมขอบนุ่มและลดสีพื้นหลังที่ติดขอบ"""
    im = im.convert("RGBA")
    br, bgg, bb = bg
    data = list(im.get_flattened_data() if hasattr(im, "get_flattened_data") else im.getdata())
    out = []
    for r, g, b, a in data:
        d = ((r - br) ** 2 + (g - bgg) ** 2 + (b - bb) ** 2) ** 0.5
        if d <= inner:
            out.append((0, 0, 0, 0))
            continue
        if d < outer:
            t = (d - inner) / (outer - inner)
            # despill: ดึงสีพื้นหลังออกจากพิกเซลขอบ
            r = int(max(0, min(255, (r - br * (1 - t)) / max(t, 0.05))))
            g = int(max(0, min(255, (g - bgg * (1 - t)) / max(t, 0.05))))
            b = int(max(0, min(255, (b - bb * (1 - t)) / max(t, 0.05))))
            out.append((r, g, b, int(a * t)))
        else:
            out.append((r, g, b, a))
    im.putdata(out)
    return im


def split_frames(im, n=4):
    """หาแถบว่างแนวตั้งเพื่อแยกเฟรม ถ้าหาไม่ได้ครบจะแบ่งเท่า ๆ กัน"""
    a = im.getchannel("A")
    w, h = im.size
    cols = [0] * w
    px = a.load()
    for x in range(w):
        c = 0
        for y in range(0, h, 2):
            if px[x, y] > 40:
                c += 1
        cols[x] = c
    runs, start = [], None
    for x in range(w):
        if cols[x] > 0 and start is None:
            start = x
        elif cols[x] == 0 and start is not None:
            runs.append([start, x])
            start = None
    if start is not None:
        runs.append([start, w])
    runs = [r for r in runs if r[1] - r[0] > 6]  # ตัดจุดเล็ก ๆ
    # รวมชิ้นที่ใกล้กันจนเหลือ n ชิ้น (อาวุธที่หลุดจากตัว ฯลฯ)
    while len(runs) > n:
        gaps = [runs[i + 1][0] - runs[i][1] for i in range(len(runs) - 1)]
        i = gaps.index(min(gaps))
        runs[i] = [runs[i][0], runs[i + 1][1]]
        del runs[i + 1]
    if len(runs) != n:
        print(f"  ! หาช่องว่างระหว่างเฟรมได้ {len(runs)} ชิ้น แบ่งเท่า ๆ กันแทน")
        step = w / n
        runs = [[int(i * step), int((i + 1) * step)] for i in range(n)]
    frames = []
    for x0, x1 in runs:
        crop = im.crop((x0, 0, x1, h))
        bb = crop.getchannel("A").getbbox()
        frames.append(crop.crop(bb) if bb else crop)
    return frames


def solid_bbox(im, thr=128):
    return im.getchannel("A").point(lambda v: 255 if v >= thr else 0).getbbox()


def feet_center(im):
    """จุดกึ่งกลางเท้า: ค่ากลางแนวนอนของ 12% ล่างของตัว"""
    bb = solid_bbox(im)
    a = im.getchannel("A").load()
    y0 = bb[3] - max(8, int((bb[3] - bb[1]) * 0.12))
    xs = [x for y in range(y0, bb[3]) for x in range(bb[0], bb[2]) if a[x, y] >= 128]
    xs.sort()
    return xs[len(xs) // 2] if xs else (bb[0] + bb[2]) / 2


def import_strip(src, char, d, ref_frame=3):
    if char not in CHARS or d not in DIRS:
        sys.exit(f"ตัวละครต้องเป็น {CHARS} ทิศต้องเป็น {DIRS}")
    raw = Image.open(src).convert("RGBA")
    bg = detect_bg(raw)
    print(f"{src}: {raw.size} พื้นหลัง {bg}")
    keyed = key_out(raw, bg)
    frames = split_frames(keyed)

    ref = Image.open(os.path.join(ROOT, "facing", char, d + ".png"))
    rb = solid_bbox(ref)
    ref_h = rb[3] - rb[1]
    nb = solid_bbox(frames[ref_frame])
    scale = ref_h / (nb[3] - nb[1])
    print(f"  ย่อ x{scale:.3f} (เฟรม {ref_frame:02d} สูงเท่า facing/{char}/{d} = {ref_h}px)")

    scaled = []
    for f in frames:
        f = f.resize((max(1, round(f.size[0] * scale)), max(1, round(f.size[1] * scale))), Image.LANCZOS)
        scaled.append(f)

    # วางทุกเฟรมบนผืนกว้างเท่ากัน จุดเท้าตรงกลาง เท้าที่ BASELINE
    placed = []
    half = 0
    for f in scaled:
        bb = solid_bbox(f)
        cx = feet_center(f)
        half = max(half, cx - 0, f.size[0] - cx)
        top = BASELINE - bb[3]
        if top < 0:
            print(f"  ! เฟรมสูงเกินผืน {-top}px จะถูกตัดหัว")
        placed.append((f, cx, top))
    width = int(2 * half + 2 * PAD)
    width += width % 2
    out_dir = os.path.join(ROOT, "attack", char, d)
    os.makedirs(out_dir, exist_ok=True)
    for i, (f, cx, top) in enumerate(placed):
        if top < 0:  # สูงเกินผืน ตัดส่วนบนทิ้ง
            f = f.crop((0, -top, f.size[0], f.size[1]))
            top = 0
        canvas = Image.new("RGBA", (width, CANVAS_H), (0, 0, 0, 0))
        canvas.alpha_composite(f, (int(round(width / 2 - cx)), top))
        p = os.path.join(out_dir, f"{i:02d}.png")
        canvas.save(p, optimize=True)
    print(f"  บันทึก attack/{char}/{d}/00-03.png ผืน {width}x{CANVAS_H}")
    update_manifest()
    import build_sprites  # อยู่โฟลเดอร์ tools เดียวกัน
    print("สร้าง atlas ใหม่ เกมจะใช้ท่าโจมตีนี้แทนท่าพุ่งตัวเอง")
    build_sprites.main()


def update_manifest():
    base = os.path.join(ROOT, "attack")
    chars = sorted(c for c in os.listdir(base) if os.path.isdir(os.path.join(base, c)))
    sizes = {}
    for c in chars:
        for d in DIRS:
            p = os.path.join(base, c, d, "00.png")
            if os.path.exists(p):
                sizes[f"{c}/{d}"] = list(Image.open(p).size)
    manifest = {
        "meaning": "ท่าโจมตี 8 ทิศ 4 เฟรม เล่นครั้งเดียวต่อการโจมตีหนึ่งครั้ง",
        "frames": ["00", "01", "02", "03"],
        "phase": ["ง้าง / เตรียม", "ปะทะ (จังหวะสร้างดาเมจ)", "ตามแรง", "กลับท่ายืน"],
        "hit_frame": "01",
        "fps": 10,
        "loop": False,
        "baseline": BASELINE,
        "anchor": "กึ่งกลางแนวนอนของผืน = จุดกึ่งกลางเท้า",
        "directions": DIRS,
        "characters": chars,
        "canvas": sizes,
    }
    with open(os.path.join(base, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)


def check():
    missing = []
    for c in ATTACKERS:
        done = [d for d in DIRS if all(os.path.exists(os.path.join(ROOT, "attack", c, d, f"{i:02d}.png")) for i in range(4))]
        todo = [d for d in DIRS if d not in done]
        print(f"{c:7s} ครบ {len(done)}/8" + (f"  ยังขาด: {' '.join(todo)}" if todo else ""))
        missing += [(c, d) for d in todo]
    return missing


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", nargs="?")
    ap.add_argument("char", nargs="?")
    ap.add_argument("dir", nargs="?")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--ref-frame", type=int, default=3, help="เฟรมท่ายืนตรงที่ใช้เทียบความสูง (ค่าเริ่มต้น 3)")
    a = ap.parse_args()
    if a.check or not a.src:
        check()
    else:
        import_strip(a.src, a.char, a.dir, a.ref_frame)
