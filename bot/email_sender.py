import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config import GMAIL_PASSWORD

def send_email(sender_email, receiver_email, subject, body, file_path=None):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, GMAIL_PASSWORD)
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body))

        if file_path:
            with open(file_path, "rb") as attachment:
                file_part = MIMEBase("application", "octet-stream")
                file_part.set_payload(attachment.read())
                encoders.encode_base64(file_part)
                file_part.add_header("Content-Disposition", f"attachment; filename={file_path}")
                msg.attach(file_part)

        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Email sent successfully to {receiver_email}")
