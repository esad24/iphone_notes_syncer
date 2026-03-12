import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

def trigger_phone():
    msg = MIMEText("send notes")
    msg['Subject'] = '[SEND_NOTES]'
    msg['From'] = MY_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(MY_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        print("Trigger email sent")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    trigger_phone()
