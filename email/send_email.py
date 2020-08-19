import os
import smtplib

EMAIL_ADDRESS = "mail"
EMAIL_PASSWORD = "pass"

EMAIL_RECIEVER = "mail"
subject = "Test send email"
body = "how are you"

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    msg = f'Subject:{subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_RECIEVER, msg)
