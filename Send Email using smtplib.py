#!/usr/bin/python3

# When using gmail make sure you turn on  "allow less secure appps"
# you can do that here: https://myaccount.google.com/lesssecureapps

import smtplib

content = "The message content"

Sender = "sender@email.com"
Receiver = "receiver@email.com"
Password = "password of the sender"

message = """From: sender@email.com
To: <receiver@email.com>
Subject: SMTP e-mail test

{0} 
""".format(content)

# if the sender is a gmail account , here are to configurations
s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
s.login(Sender, Password)
s.sendmail(Sender, Receiver, message)
s.quit()


