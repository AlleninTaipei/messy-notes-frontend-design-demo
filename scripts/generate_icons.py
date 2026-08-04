"""Generate PWA / iOS home screen icons for 認識股票.frontend-design.html.

Draws a passbook (存摺) glyph in the page's own palette: an ink-blue book
with gold ledger rules, overlapped by a seal-red chop stamped with "股".
One full-bleed composition is reused for every size and every manifest
purpose (any + maskable) since the motif already sits inside a safe zone.
"""

from PIL import Image, ImageDraw, ImageFont

PAPER = (242, 237, 225, 255)
INK_BLUE = (27, 58, 92, 255)
SEAL_RED = (178, 58, 46, 255)
GOLD = (201, 166, 107, 255)

CANVAS = 512
FONT_PATH = r"C:\Windows\Fonts\kaiu.ttf"

OUT_DIR = "assets/icons"

SIZES_ANY = [512, 192, 180, 167, 152, 120]
FAVICON_SIZES = [32, 16]


def draw_master():
    img = Image.new("RGBA", (CANVAS, CANVAS), PAPER)
    draw = ImageDraw.Draw(img)

    book_w, book_h = 300, 360
    bx0 = (CANVAS - book_w) // 2 - 18
    by0 = (CANVAS - book_h) // 2 - 10
    bx1, by1 = bx0 + book_w, by0 + book_h
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=26, fill=INK_BLUE,
                            outline=GOLD, width=7)

    for i in range(3):
        ly = by0 + 70 + i * 34
        draw.line([(bx0 + 34, ly), (bx1 - 34, ly)], fill=(201, 166, 107, 130), width=4)

    seal_r = 92
    scx, scy = bx1 - 24, by1 - 40
    draw.ellipse([scx - seal_r, scy - seal_r, scx + seal_r, scy + seal_r],
                 fill=SEAL_RED, outline=PAPER, width=6)
    draw.ellipse([scx - seal_r + 14, scy - seal_r + 14, scx + seal_r - 14, scy + seal_r - 14],
                 outline=PAPER, width=3)

    font = ImageFont.truetype(FONT_PATH, 90)
    text = "股"
    tb = draw.textbbox((0, 0), text, font=font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    draw.text((scx - tw / 2 - tb[0], scy - th / 2 - tb[1]), text, font=font, fill=PAPER)

    return img


def draw_favicon_master():
    img = Image.new("RGBA", (CANVAS, CANVAS), PAPER)
    draw = ImageDraw.Draw(img)
    r = 210
    cx = cy = CANVAS // 2
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SEAL_RED, outline=PAPER, width=14)
    font = ImageFont.truetype(FONT_PATH, 220)
    text = "股"
    tb = draw.textbbox((0, 0), text, font=font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    draw.text((cx - tw / 2 - tb[0], cy - th / 2 - tb[1]), text, font=font, fill=PAPER)
    return img


def main():
    import os
    os.makedirs(OUT_DIR, exist_ok=True)

    master = draw_master().convert("RGB")
    for size in SIZES_ANY:
        resized = master.resize((size, size), Image.LANCZOS)
        resized.save(f"{OUT_DIR}/icon-{size}.png")

    fav_master = draw_favicon_master().convert("RGB")
    for size in FAVICON_SIZES:
        resized = fav_master.resize((size, size), Image.LANCZOS)
        resized.save(f"{OUT_DIR}/favicon-{size}.png")

    print("done")


if __name__ == "__main__":
    main()
