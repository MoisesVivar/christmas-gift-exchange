import os
import imaplib
from dotenv import load_dotenv

load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(SENDER_EMAIL, SENDER_PASSWORD)


def get_sent_folder():
    status, mailboxes = imap.list()

    for mailbox in mailboxes:
        mailbox_str = mailbox.decode()
        if r"\Sent" in mailbox_str:
            return mailbox_str.split('"')[-2]

    raise RuntimeError("Could not find Sent mailbox")


def print_subjects(msg_ids):
    for msg_id in msg_ids:
        status, header = imap.fetch(msg_id, '(BODY.PEEK[HEADER.FIELDS (SUBJECT TO)])')
        print(header)


def delete_exchange_emails(campaign_id):
    sent_folder = get_sent_folder()
    imap.select(sent_folder)
    status, data = imap.search(None, f'HEADER X-Exchange-Id "{campaign_id}"')

    if status != "OK":
        return 0

    deleted = 0
    msg_ids = data[0].split()

    # print message subjects. Audit only
    print_subjects(msg_ids)

    for msg_id in msg_ids:
        imap.store(msg_id, "+FLAGS", "\\Deleted")
        deleted += 1

    imap.expunge()

    return deleted







