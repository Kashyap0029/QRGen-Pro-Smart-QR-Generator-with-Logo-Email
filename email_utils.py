import os
import smtplib
from email.message import EmailMessage

def send_email(receiver, qr_bytes):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    if not sender or not password:
        raise ValueError("EMAIL_USER or EMAIL_PASS not set in environment.")

    msg = EmailMessage()
    msg["Subject"] = "Your QR Code"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Attached is your QR code.")

    msg.add_attachment(qr_bytes, maintype="image", subtype="png", filename="qr.png")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
