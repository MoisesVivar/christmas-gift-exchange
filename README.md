# 🎄 Christmas Gift Exchange

A simple Python application for organizing a Christmas gift exchange and automatically notifying participants by email.

The project generates valid assignments, sends personalized HTML emails, and can optionally remove sent messages from Gmail after delivery.

## Features

- Random gift exchange assignment generation
- Personalized HTML email notifications
- Optional cleanup of sent emails using IMAP
- Environment\-based configuration
- Lightweight and easy to run

## Requirements

- Python 3.10\+
- Gmail account
- Gmail App Password

## Gmail Setup

This project uses Gmail SMTP to send email notifications.

Google may require an **App Password** instead of your regular Gmail password. App Passwords are 16-character passwords generated specifically for third-party applications and require 2-Step Verification to be enabled on your Google account.

Example:

```env
SENDER_EMAIL=john.doe@gmail.com
SENDER_PASSWORD=abcd efgh ijkl mnop
```

For instructions on creating an App Password, see:

https://support.google.com/mail/answer/185833

## Installation

```
git clone https://github.com/MoisesVivar/christmas-gift-exchange.git

cd christmas-gift-exchange

pip install \-r requirements.txt
```

## Configuration

Create a .env file at the root of the project:

```
SENDER_EMAIL="<youremail@something.com>"
SENDER_PASSWORD="XXXX XXXX XXXX XXXX"
EMAIL_SUBJECT="You subject"
DELETE_ASSIGNMENTS=True
```

Set `DELETE_ASSIGNMENTS=False` if you want to keep the sent emails.

Update the `participant.py` list according to your needs.

## Usage

Run the following command at the root of the project

```
python send_assignments.py
```

The application will:

1. Generate exchange assignments.
2. Send a personalized email to each participant.
3. Optionally remove the sent emails from Gmail.

## Security

Participant assignments are generated and distributed automatically. If email cleanup is enabled, sent notifications can be removed from the sender's mailbox after delivery.

## License

MIT

