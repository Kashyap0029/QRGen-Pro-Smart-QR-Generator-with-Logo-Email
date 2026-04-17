from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import base64

from qr_utils import generate_qr_with_logo
from email_utils import send_email

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(url: str = Form(...), email: str = Form(...), logo: UploadFile = File(None)):
    logo_bytes = await logo.read() if logo else None

    qr_bytes = generate_qr_with_logo(url, logo_bytes)

    try:
        send_email(email, qr_bytes)
    except Exception as e:
        print("Email error:", e)

    qr_base64 = base64.b64encode(qr_bytes).decode()
    return {"qr_image": qr_base64}
