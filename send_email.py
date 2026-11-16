import ssl
import smtplib
from email.message import EmailMessage


def send_email(sender_email: str, sender_password: str, receiver: str, message: EmailMessage):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, receiver, message.as_string())

