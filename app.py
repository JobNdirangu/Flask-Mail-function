# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from email_utils import create_mail_app, send_email

app = Flask(__name__)
app.secret_key = 'your_secret_key'

mail = create_mail_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email_route():
    if request.method == 'POST':
        subject = "traial test"
        recipient = "jobndirangu27@gmail.com"
        body = "testing"

        send_email(mail, subject, recipient, body)

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
