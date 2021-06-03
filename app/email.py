from threading import Thread
from flask_mailman import EmailMessage
from app import mail, app
from flask import render_template
from mailjet_rest import Client

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, text_body, from_email, to, reply_to):
    msg = EmailMessage(subject=subject, body=text_body, from_email=from_email, to=to.split(), reply_to=reply_to)
    Thread(target=send_async_email, args=(app, msg)).start()

def send_inquiry_email(user, message):
    api_key = app.config['MAILJET_KEY']
    api_secret = app.config['MAILJET_SECRET']
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
      'Messages': [
        {
          "From": {
            "Email": app.config['ADMINS'][0],
            "Name": "SarahsATX.com"
          },
          "To": [
            {
              "Email": app.config['ADMINS'][0],
            }
          ],
          "Subject": "Contact Form Submission: " + user.first_name,
          "TextPart": render_template('email/inquiry-form.txt',
                                   user=user, message=message),
        }
      ]
    }

    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
