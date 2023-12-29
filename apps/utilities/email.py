import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings


def send_email(
    receiver_email,
    subject,
    message,
    sender_email=settings.DEFAULT_FROM_EMAIL,
    smtp_server=settings.EMAIL_HOST,
    smtp_port=587,
    username=settings.EMAIL_HOST_USER,
    password=settings.EMAIL_HOST_PASSWORD,
):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        return 0

    except Exception as e:
        return 1

    finally:
        server.quit()
