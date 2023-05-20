#  Create a project that will send an automatic email every 10mins 

import smtplib
from email.message import EmailMessage
import ssl
import datetime
import time

timenow = datetime.datetime.now()
# time.sleep(20)

# Create send_mail function
def send_email():
    sender = 'graceumeayo@gmail.com'
    recipient = 'emanstonepro@gmail.com','emchadexglobal@gmail.com','gracechukwu350@gmail.com'
    mypassword = 'hbftwafgbqhzqnzk'
'  
    subject = 'Timed email testing in python'

   # CREATE THE OBJECT OF THE EMAIL CLASS ;
    email_me = EmailMessage()

    email_me['Subject'] = subject
    email_me['From'] = sender
    email_me['To'] = recipient
    email_me.set_content('This is my first timed email test in python. It sends email every 10mins')

    # OPENNING THE CONNECTION TO GMAIL SERVER AND SAVING IT IN A VARIABLE 'mailme'
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mailme:
        mailme.login(sender, mypassword)
        mailme.sendmail(sender, recipient, email_me.as_string())
        # mailme.send_message(email_me)
    print('email sent!')

    if timenow.second == 20:
        return mailme

# while loop for infinite excecution of send_mail at every time.sleep()
while True:
    send_email()
    time.sleep(600)

send_email()
