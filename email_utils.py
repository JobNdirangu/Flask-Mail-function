# email_utils.py

from flask_mail import Mail, Message
from flask import flash

def create_mail_app(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'dirash.techsolutions@gmail.com'  # replace with your Gmail
    app.config['MAIL_PASSWORD'] = 'fslq zfdk iuct qdbn'          # replace with your Gmail password or App Password
    app.config['MAIL_DEFAULT_SENDER'] = 'ndirash.techsoluctions@gmail.com'  # replace with your Gmail

    return Mail(app)

def send_email(mail, subject, recipient, body):
    msg = Message(subject, recipients=[recipient])
    msg.body = body

    try:
        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send email: {str(e)}', 'danger')
