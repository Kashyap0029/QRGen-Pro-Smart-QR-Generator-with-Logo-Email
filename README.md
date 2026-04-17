# Smart QR Generator

A full-stack web application that allows users to generate customized QR codes from URLs, embed logos inside the QR, and receive the generated QR code via email.

---

## Features

- Generate QR codes from any URL  
- Embed custom logos inside QR codes  
- Send generated QR code directly to email  
- FastAPI-based backend  
- Simple and responsive frontend  

---

## Project Overview

This project demonstrates a real-world full-stack application by integrating:

- **Frontend** → Takes user input (URL, logo, email)  
- **Backend (FastAPI)** → Processes request and generates QR  
- **Image Processing** → Adds logo inside QR  
- **Email Service** → Sends QR as attachment  

The system generates a QR code dynamically and delivers it to the user via email.

---

## Screenshots

### Web Interface
<img width="300" height="400" alt="Screenshot 2026-04-17 at 1 02 59 PM" src="https://github.com/user-attachments/assets/59693490-0eae-4431-a108-4db828b3abf3" />



### Email Output
<img width="250" height="400" alt="image" src="https://github.com/user-attachments/assets/ac57a885-d144-438e-826c-1062eb5d5210" />


---

## Tech Stack

- **Backend:** FastAPI (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Libraries:** qrcode, Pillow, smtplib  
- **Environment Management:** python-dotenv  

---

## Setup Instructions

### Clone Repository
```bash
git clone https://github.com/your-username/smart-qr-generator.git
cd smart-qr-generator
