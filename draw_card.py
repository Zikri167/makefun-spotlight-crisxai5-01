#!/usr/bin/env python3
"""Draw the spotlight card for @crisxai5 (1200x675 PNG) with PIL.

Design: dark premium card, navy-to-violet vertical gradient, mint glow
accents, a network of glowing nodes in the corners, a big sharp
@crisxai5 handle as the hero, a short tagline, four topic pills and a
follow call-to-action. Phone-readable: large type, high contrast.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 675
OUT = "graphic.png"

NOTO = "/usr/share/fonts/truetype/noto/"
F_BLACK = NOTO + "NotoSans-Black.ttf"
F_XBOLD = NOTO + "NotoSans-ExtraBold.ttf"
F_BOLD = NOTO + "NotoSans-Bold.ttf"
F_MED = NOTO + "NotoSans-Medium.ttf"
F_REG = NOTO + "NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def make_gradient(w, h):
    top = (10, 12, 34)        # deep navy
    mid = (24, 18, 64)        # violet
    bot = (8, 10, 26)         # near-black navy
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        c = lerp(top, mid, t * 1.4) if t < 0.5 else lerp(mid, bot, (t - 0.5) * 2)
        for x in range(w):
            px[x, y] = c
    return img


def glow_dot(base, cx, cy, r, color, alpha=110):
    """Soft radial glow dot drawn on an overlay layer."""
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    steps = 24
    for i in range(steps, 0, -1):
        rr = r * i / steps
        a = int(alpha * (1 - i / steps) ** 2)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr],
                  fill=color + (a,))
    layer = layer.filter(ImageFilter.GaussianBlur(2))
    base.alpha_composite(layer)


def draw_network(d, base, nodes, color, line_alpha=70):
    """Connect nearby nodes with faint lines, then draw glowing dots."""
    for i, (x1, y1, _r1) in enumerate(nodes):
        for x2, y2, _r2 in nodes[i + 1:]:
            if math.hypot(x2 - x1, y2 - y1) < 190:
                d.line([x1, y1, x2, y2], fill=color + (line_alpha,), width=2)
    for x, y, r in nodes:
        glow_dot(base, x, y, r * 3, color, alpha=90)
        d.ellipse([x - r, y - r, x + r, y + r], fill=color + (255,))


def centered(d, y, text, fnt, fill, x_center=W // 2):
    w = d.textlength(text, font=fnt)
    d.text((x_center - w / 2, y), text, font=fnt, fill=fill)
    return w


def main():
    random.seed(7)
    img = make_gradient(W, H).convert("RGBA")
    d = ImageDraw.Draw(img, "RGBA")

    mint = (64, 224, 178)      # mint green accent
    cyan = (86, 180, 255)      # cyan accent
    violet = (168, 120, 255)   # violet accent
    white = (255, 255, 255)
    soft = (205, 210, 235)     # soft grey-blue body text
    dim = (150, 158, 190)

    # --- corner network clusters -------------------------------------
    left_nodes = [(random.randint(20, 260), random.randint(30, 260)) for _ in range(7)]
    left_nodes = [(x, y, random.randint(3, 6)) for x, y in left_nodes]
    right_nodes = [(random.randint(940, 1180), random.randint(420, 650)) for _ in range(7)]
    right_nodes = [(x, y, random.randint(3, 6)) for x, y in right_nodes]
    draw_network(d, img, left_nodes, cyan)
    draw_network(d, img, right_nodes, mint)

    # big soft glows behind the hero area
    glow_dot(img, 600, 300, 260, (80, 60, 200), alpha=60)
    glow_dot(img, 180, 120, 160, (30, 120, 200), alpha=55)
    glow_dot(img, 1030, 560, 160, (20, 160, 130), alpha=55)

    # --- top eyebrow badge -------------------------------------------
    badge = "SPOTLIGHT  •  MUST-FOLLOW"
    bf = font(F_BOLD, 30)
    bw = d.textlength(badge, font=bf)
    bx0, by0 = (W - bw) / 2 - 28, 52
    bx1, by1 = (W + bw) / 2 + 28, 52 + 58
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=29,
                        outline=mint + (255,), width=3)
    d.text(((W - bw) / 2, by0 + 11), badge, font=bf, fill=mint + (255,))

    # --- headline ------------------------------------------------------
    centered(d, 138, "ONE FOLLOW", font(F_BLACK, 96), white + (255,))
    centered(d, 238, "THAT PAYS.", font(F_BLACK, 96), mint + (255,))

    # --- hero handle ----------------------------------------------------
    handle = "@crisxai5"
    hf = font(F_XBOLD, 92)
    hw = d.textlength(handle, font=hf)
    # dark pill behind the handle for contrast
    px0, py0 = (W - hw) / 2 - 34, 352
    px1, py1 = (W + hw) / 2 + 34, 352 + 118
    d.rounded_rectangle([px0, py0, px1, py1], radius=24,
                        fill=(12, 16, 40, 235), outline=cyan + (255,), width=3)
    d.text(((W - hw) / 2, py0 + 10), handle, font=hf, fill=white + (255,))

    # --- tagline ---------------------------------------------------------
    centered(d, 496, "AI agents. Crypto alpha. Web3 tooling.",
             font(F_MED, 34), soft + (255,))
    centered(d, 540, "On-chain automation — signal, not noise.",
             font(F_MED, 34), soft + (255,))

    # --- four topic pills -------------------------------------------------
    pills = ["AI AGENTS", "CRYPTO ALPHA", "WEB3", "ON-CHAIN AUTOMATION"]
    pf = font(F_BOLD, 26)
    widths = [d.textlength(p, font=pf) + 44 for p in pills]
    gap = 18
    total = sum(widths) + gap * (len(pills) - 1)
    x = (W - total) / 2
    y0, y1 = 596, 596 + 52
    accents = [mint, cyan, violet, mint]
    for p, w, ac in zip(pills, widths, accents):
        d.rounded_rectangle([x, y0, x + w, y1], radius=26,
                            outline=ac + (255,), width=2)
        d.text((x + 22, y0 + 12), p, font=pf, fill=white + (255,))
        x += w + gap

    img.convert("RGB").save(OUT, "PNG")
    print(f"saved {OUT} {W}x{H}")


if __name__ == "__main__":
    main()
