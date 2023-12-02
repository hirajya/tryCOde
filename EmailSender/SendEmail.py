import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'email sender address'
email_password = 'generated password in app password google acc'
email_receivers = []

def extract_username(email):
    return email.split('@')[0]

for email_receiver in email_receivers:

    name_email = extract_username(email_receiver)
    subject = f"[email python testing bulk sending 2] Hello {name_email}"
    body = """
    Don't hate the play, hate the game. rodney to fr.
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    print(f"Email sent to {email_receiver} successfully!")