#!/usr/bin/env python3
"""Compose YouTube trailer thumbnail — Rebecca art + title on the right."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent
SRC = Path(
    "/Users/marcosicaza/.grok/sessions/%2FUsers%2Fmarcosicaza%2Fdevelopment%2Fringborn-website/"
    "019ed744-bc56-7162-897d-5818d5c72df7/assets/image-88df84d3-c5af-4a09-a990-be51666b907c.jpg"
)
TITLE_PNG = ROOT / "title.png"
FONT_PATH = ROOT.parent.parent / "cards" / "PressStart2P-Regular.ttf"
OUT = ROOT / "trailer-thumbnail.jpg"

W, H = 1280, 720


def load_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size)


def draw_outlined_text(draw, xy, text, font, fill, outline=(0, 0, 0), width=3):
    x, y = xy
    for dx in range(-width, width + 1):
        for dy in range(-width, width + 1):
            if dx * dx + dy * dy <= width * width:
                draw.text((x + dx, y + dy), text, font=font, fill=outline)
    draw.text((x, y), text, font=font, fill=fill)


def main():
    base = Image.open(SRC).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)

    # Slight vignette on the right for title legibility over stars.
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    for x in range(W // 2, W):
        t = (x - W // 2) / (W // 2)
        alpha = int(35 + 90 * (t ** 1.4))
        ov_draw.line([(x, 0), (x, H)], fill=(4, 8, 22, alpha))
    base = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")

    canvas = base.copy()
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    # Game title logo (transparent PNG).
    title = Image.open(TITLE_PNG).convert("RGBA")
    logo_w = 520
    logo_h = int(title.height * (logo_w / title.width))
    title = title.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
    logo_x = W - logo_w - 56
    logo_y = 168
    layer.paste(title, (logo_x, logo_y), title)

    font_trailer = load_font(28)
    font_date = load_font(18)
    font_tag = load_font(14)

    text_x = logo_x + 8
    draw_outlined_text(
        draw,
        (text_x, logo_y + logo_h + 36),
        "OFFICIAL TRAILER",
        font_trailer,
        fill=(120, 230, 255),
        outline=(0, 20, 40),
        width=4,
    )
    draw_outlined_text(
        draw,
        (text_x, logo_y + logo_h + 88),
        "COMING JULY 2026",
        font_date,
        fill=(255, 210, 90),
        outline=(40, 25, 0),
        width=3,
    )
    draw_outlined_text(
        draw,
        (text_x, logo_y + logo_h + 132),
        "STEAM · APP STORE",
        font_tag,
        fill=(220, 225, 240),
        outline=(0, 0, 0),
        width=2,
    )
    draw_outlined_text(
        draw,
        (text_x, logo_y + logo_h + 158),
        "GOOGLE PLAY",
        font_tag,
        fill=(220, 225, 240),
        outline=(0, 0, 0),
        width=2,
    )

    result = Image.alpha_composite(canvas.convert("RGBA"), layer).convert("RGB")
    result.save(OUT, "JPEG", quality=95, subsampling=0)
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()