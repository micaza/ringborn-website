#!/usr/bin/env python3
"""Generate The Last Sideran business card front and back (3.5" x 2" @ 300 DPI)."""

from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
PIXEL_FONT = ROOT / "PressStart2P-Regular.ttf"
W, H = 1050, 600  # 3.5" x 2" at 300 DPI
URL = "https://pixeldogames.com/thelastsideran"
GOLD = (255, 210, 58)
GOLD_BRIGHT = (255, 220, 40)
GOLD_DARK = (240, 160, 20)
GOLD_URL = (210, 145, 0)  # darker gold — readable on white cardstock
WHITE = (255, 255, 255)
MUTED = (180, 182, 205)
BG = (5, 5, 16)
BLACK = (0, 0, 0)
TRANSPARENT_FILL = None  # outline only — no ink for white fill


def load_pixel_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(PIXEL_FONT), size)


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def fit_cover(img: Image.Image, width: int, height: int) -> Image.Image:
    src_w, src_h = img.size
    scale = max(width / src_w, height / src_h)
    resized = img.resize((int(src_w * scale), int(src_h * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - width) // 2
    top = (resized.height - height) // 2
    return resized.crop((left, top, left + width, top + height))


def draw_text_with_shadow(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    shadow: tuple[int, int, int] = (0, 0, 0),
    offset: int = 3,
) -> None:
    x, y = xy
    draw.text((x + offset, y + offset), text, font=font, fill=shadow)
    draw.text((x, y), text, font=font, fill=fill)


def draw_arcade_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int] | None,
    outline: int = 4,
    drop_shadow: bool = True,
) -> None:
    """Pixel-game style text with thick outline and optional drop shadow."""
    x, y = xy
    for ox in range(-outline, outline + 1):
        for oy in range(-outline, outline + 1):
            if ox * ox + oy * oy <= outline * outline:
                draw.text((x + ox, y + oy), text, font=font, fill=BLACK)
    if drop_shadow:
        draw.text((x + 6, y + 6), text, font=font, fill=GOLD_DARK)
    if fill is not None:
        draw.text((x, y), text, font=font, fill=fill)


def white_to_transparent(img: Image.Image, threshold: int = 240) -> Image.Image:
    """Turn near-white pixels fully transparent to avoid white ink when printing."""
    rgba = img.convert("RGBA")
    pixels = rgba.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, a = pixels[x, y]
            if r >= threshold and g >= threshold and b >= threshold:
                pixels[x, y] = (r, g, b, 0)
    return rgba


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def make_front() -> Image.Image:
    source = Image.open(ROOT / "rebecca-card-source.jpg").convert("RGB")
    card = fit_cover(source, W, H)

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    for x in range(W // 2, W):
        alpha = int(140 * ((x - W // 2) / (W // 2)))
        odraw.line([(x, 0), (x, H)], fill=(0, 0, 0, alpha))

    card = Image.alpha_composite(card.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(card)

    font_bored = load_pixel_font(52)
    font_sub = load_pixel_font(18)

    bored_text = "BORED?"
    sub_text = "SURVIVE"
    sub2_text = "THE SPIKES"

    bored_w = text_width(draw, bored_text, font_bored)
    sub_w = max(text_width(draw, sub_text, font_sub), text_width(draw, sub2_text, font_sub))
    block_w = max(bored_w, sub_w)
    block_x = W - block_w - 72
    bored_y = 155
    sub_y = bored_y + 82

    draw_arcade_text(draw, (block_x, bored_y), bored_text, font_bored, GOLD, outline=5)
    draw_arcade_text(draw, (block_x + (block_w - text_width(draw, sub_text, font_sub)) // 2, sub_y), sub_text, font_sub, WHITE, outline=3, drop_shadow=False)
    draw_arcade_text(
        draw,
        (block_x + (block_w - text_width(draw, sub2_text, font_sub)) // 2, sub_y + 34),
        sub2_text,
        font_sub,
        WHITE,
        outline=3,
        drop_shadow=False,
    )

    return card.convert("RGB")


def make_qr(size: int) -> Image.Image:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img = img.resize((size, size), Image.Resampling.NEAREST)
    return white_to_transparent(img)


def make_back() -> Image.Image:
    card = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)

    logo = Image.open(ROOT.parent / "thelastsideran" / "images" / "title.png").convert("RGBA")
    logo_w = 520
    logo_h = int(logo.height * (logo_w / logo.width))
    logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
    card.paste(logo, ((W - logo_w) // 2, 36), logo)

    font_url = load_font(26, bold=True)
    font_scan = load_font(22)
    url_text = "pixeldogames.com/thelastsideran"
    url_y = 36 + logo_h + 10
    url_w = text_width(draw, url_text, font_url)
    url_x = (W - url_w) // 2
    draw_arcade_text(draw, (url_x, url_y), url_text, font_url, GOLD_URL, outline=2, drop_shadow=False)

    qr = make_qr(220)
    qr_x = (W - qr.size[0]) // 2
    qr_y = 36 + logo_h + 58
    card.paste(qr, (qr_x, qr_y), qr)

    scan_text = "Scan to learn more"
    scan_bbox = draw.textbbox((0, 0), scan_text, font=font_scan)
    scan_w = scan_bbox[2] - scan_bbox[0]
    draw.text(((W - scan_w) // 2, qr_y + qr.size[1] + 18), scan_text, font=font_scan, fill=MUTED)

    return card


def main() -> None:
    front = make_front()
    back = make_back()
    front_path = ROOT / "business-card-front.png"
    back_path = ROOT / "business-card-back.png"
    front.save(front_path, dpi=(300, 300))
    back.save(back_path, dpi=(300, 300))
    print(f"Saved {front_path}")
    print(f"Saved {back_path}")


if __name__ == "__main__":
    main()