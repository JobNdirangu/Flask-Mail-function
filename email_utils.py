# email_utils.py

from flask_mail import Mail, Message
from flask import flash

def send_email(mail, subject, recipient, body):
    msg = Message(subject, recipients=[recipient])
    msg.body = body

    try:
        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send email: {str(e)}', 'danger')
