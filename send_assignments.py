import os
from pathlib import Path
from random import shuffle
from dotenv import load_dotenv
from send_email import send_email
from participants import participants
from email.message import EmailMessage

load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# email details
EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT")

# load the template
template_path = Path("email_template.html")
html_template = template_path.read_text(encoding="utf-8")

# shuffle the participant list twice to be safe :D
shuffle(participants)
shuffle(participants)

# send the assignments
for i in range(len(participants)):
    cur_participant = participants[i - 1]
    next_participant = participants[i]
    # build the body (fallback if HTML is not rendered)
    body = f"Hola {cur_participant['name']}, te tocó : {next_participant['name']}"
    # build the message
    message = EmailMessage()
    message['From'] = SENDER_EMAIL
    message['To'] = cur_participant["email"]
    message['Subject'] = EMAIL_SUBJECT
    message.set_content(body)
    html_msg = (
        html_template
            .replace("{{participant_name}}", cur_participant["name"])
            .replace("{{recipient_name}}", next_participant["name"])
    )
    message.add_alternative(html_msg, subtype="html")
    send_email(SENDER_EMAIL, SENDER_PASSWORD, cur_participant["email"], message)




