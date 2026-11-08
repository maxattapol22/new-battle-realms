"""สร้าง sprite atlas ขนาดเล็กสำหรับเกม จากภาพต้นฉบับใน assets/<เผ่า>/

ภาพต้นฉบับสูงราว 300px แต่ในเกมตัวละครสูงแค่ ~38px จึงย่อแล้วรวมเฟรมของตัวละคร
แต่ละตัวไว้ในภาพเดียว ให้มือถือโหลดเร็ว พร้อมบันทึกตำแหน่งเฟรมและจุดเท้า

ใช้:
  python tools/build_sprites.py

อ่าน:
  assets/<เผ่า>/facing/<ตัวละคร>/<ทิศ>.png          ท่ายืน
  assets/<เผ่า>/walk/<ตัวละคร>/<ทิศ>/00-03.png      ท่าเดิน
  assets/<เผ่า>/attack/<ตัวละคร>/<ทิศ>/00-03.png    ท่าโจมตี (มีเมื่อไหร่ เกมใช้เอง)
เขียน:
  assets/<เผ่า>/atlas/<ตัวละคร>.png
  assets/sprites.js     (index.html โหลดไฟล์นี้ ใช้ได้ทั้งเปิดไฟล์ตรงและบนเว็บ)
"""
import hashlib
import io
import json
import os
import sys

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets"))
OUT_JS = os.path.join(ASSETS, "sprites.js")
DIRS = ["s", "sw", "w", "nw", "n", "ne", "e", "se"]
FRAMES = ["00", "01", "02", "03"]
SCALE = 0.25    # px ใน atlas ต่อ px ต้นฉบับ (เกมวาดตัวสูง 38px บนจอ dpr 2)
ATLAS_W = 1024
GUTTER = 2      # ช่องว่างกันสีเฟรมข้าง ๆ ซึมเวลาย่อ/ขยาย


def solid_mask(im, thr=128):
    return im.getchannel("A").point(lambda v: 255 if v >= thr else 0)


def feet_point(im):
    """จุดเท้า: x = ค่ากลางของพิกเซลในแถบล่าง 12% ของตัว, y = ขอบล่างสุดของเท้า"""
    a = solid_mask(im)
    bb = a.getbbox()
    if not bb:
        return im.size[0] / 2, im.size[1]
    band = max(6, int((bb[3] - bb[1]) * 0.12))
    px = a.load()
    xs = [x for y in range(bb[3] - band, bb[3]) for x in range(bb[0], bb[2]) if px[x, y]]
    xs.sort()
    cx = xs[len(xs) // 2] if xs else (bb[0] + bb[2]) / 2
    return cx, bb[3]


def shrink(im):
    """ย่อแบบ premultiplied alpha กันขอบดำ แล้วตัดพื้นที่ว่างออก"""
    w, h = im.size
    nw, nh = max(1, round(w * SCALE)), max(1, round(h * SCALE))
    small = im.convert("RGBa").resize((nw, nh), Image.LANCZOS).convert("RGBA")
    bb = small.getchannel("A").point(lambda v: 255 if v > 2 else 0).getbbox() or (0, 0, nw, nh)
    return small.crop(bb), nw / w, nh / h, bb


def load_set(paths):
    """โหลดเฟรมชุดเดียวกัน (ทิศเดียวกัน) ใช้จุดเท้าร่วมกัน ภาพจะไม่สั่นระหว่างเฟรม"""
    ims = [Image.open(p).convert("RGBA") for p in paths]
    pts = [feet_point(im) for im in ims]
    ax = sum(p[0] for p in pts) / len(pts)
    bottoms = sorted(p[1] for p in pts)
    ay = bottoms[len(bottoms) // 2]
    out = []
    for im in ims:
        small, sx, sy, bb = shrink(im)
        out.append({"img": small, "ax": ax * sx - bb[0], "ay": ay * sy - bb[1]})
    return out


def pack(items):
    items = sorted(items, key=lambda it: -it["img"].size[1])
    x = y = GUTTER
    row_h = 0
    for it in items:
        w, h = it["img"].size
        if x + w + GUTTER > ATLAS_W:
            x = GUTTER
            y += row_h + GUTTER
            row_h = 0
        it["x"], it["y"] = x, y
        x += w + GUTTER
        row_h = max(row_h, h)
    return y + row_h + GUTTER


def build_char(clan_dir, char):
    sets = {"idle": {}, "walk": {}, "attack": {}}
    for d in DIRS:
        p = os.path.join(clan_dir, "facing", char, d + ".png")
        if os.path.exists(p):
            sets["idle"][d] = load_set([p])
        for kind in ("walk", "attack"):
            ps = [os.path.join(clan_dir, kind, char, d, f + ".png") for f in FRAMES]
            if all(os.path.exists(p) for p in ps):
                sets[kind][d] = load_set(ps)
    if len(sets["idle"]) < 8:
        print(f"  ข้าม {char}: ท่ายืนมีไม่ครบ 8 ทิศ")
        return None, None
    items = [it for kind in sets.values() for frames in kind.values() for it in frames]
    height = pack(items)
    atlas = Image.new("RGBA", (ATLAS_W, height), (0, 0, 0, 0))
    for it in items:
        atlas.alpha_composite(it["img"], (it["x"], it["y"]))

    def rect(it):
        w, h = it["img"].size
        return [it["x"], it["y"], w, h, round(it["ax"], 1), round(it["ay"], 1)]

    meta = {"idle": {d: rect(fr[0]) for d, fr in sets["idle"].items()}}
    for kind in ("walk", "attack"):
        if sets[kind]:
            meta[kind] = {d: [rect(it) for it in fr] for d, fr in sets[kind].items()}
    return atlas, meta


def main():
    data = {}
    total = 0
    for clan in sorted(os.listdir(ASSETS)):
        clan_dir = os.path.join(ASSETS, clan)
        if not os.path.isdir(os.path.join(clan_dir, "facing")):
            continue
        chars = sorted(c for c in os.listdir(os.path.join(clan_dir, "facing"))
                       if os.path.isdir(os.path.join(clan_dir, "facing", c)))
        out_dir = os.path.join(clan_dir, "atlas")
        os.makedirs(out_dir, exist_ok=True)
        clan_meta = {"scale": SCALE, "chars": {}}
        print(f"เผ่า {clan}")
        for char in chars:
            atlas, meta = build_char(clan_dir, char)
            if not atlas:
                continue
            buf = io.BytesIO()
            # 256 สี: ที่ขนาดในเกมมองไม่ออกว่าต่างจากภาพเต็ม แต่ไฟล์เล็กลง ~4 เท่า
            atlas.quantize(256, method=Image.Quantize.FASTOCTREE).save(buf, "PNG", optimize=True)
            png = buf.getvalue()
            with open(os.path.join(out_dir, char + ".png"), "wb") as fh:
                fh.write(png)
            ver = hashlib.md5(png).hexdigest()[:8]
            meta["src"] = f"assets/{clan}/atlas/{char}.png?v={ver}"
            clan_meta["chars"][char] = meta
            total += len(png)
            atk = meta.get("attack", {})
            print(f"  {char:7s} ยืน 8 ทิศ · เดิน {len(meta.get('walk', {}))} ทิศ · โจมตี {len(atk)} ทิศ"
                  f" · {atlas.size[0]}x{atlas.size[1]} · {len(png) // 1024} KB")
        data[clan] = clan_meta
    with open(OUT_JS, "w", encoding="utf-8") as fh:
        fh.write("// สร้างอัตโนมัติโดย tools/build_sprites.py ห้ามแก้ด้วยมือ\n")
        fh.write("window.NBR_SPRITES = ")
        json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write(";\n")
    print(f"รวม atlas {total // 1024} KB → {os.path.relpath(OUT_JS, os.path.join(ASSETS, '..'))}")


if __name__ == "__main__":
    main()
