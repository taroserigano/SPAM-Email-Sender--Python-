import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'I am NOT Spam!'
email['to'] = 'kim.13charls@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name':'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('kim.13charls@gmail.com', 'tarodesu123')
    smtp.send_message(email)
    print('Email Sent successfully, Boss! :)')







