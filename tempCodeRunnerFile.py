@app.route('/send-email', methods=['POST'])
def send_email_route():
    if request.method == 'POST':
        subject = "traial test"
        recipient = "jobndirangu27@gmail.com"
        body = "testing"

        send_email(mail, subject, recipient, body)

        return redirect(url_for('index'))