import qrcode
from PIL import Image
from io import BytesIO

def generate_qr_with_logo(
    url: str,
    logo_bytes=None,
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white"
):
    if not url.strip():
        raise ValueError("URL cannot be empty.")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")

    if logo_bytes:
        logo = Image.open(BytesIO(logo_bytes)).convert("RGBA")
        qr_width, qr_height = img.size
        logo_size = int(qr_width * 0.25)
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
        pos = ((qr_width - logo_size)//2, (qr_height - logo_size)//2)
        img.paste(logo, pos, mask=logo)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()
