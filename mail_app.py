
# Online Python - IDE, Editor, Compiler, Interpreter
from email.message import EmailMessage
# from app2 import password
import os
from dotenv import load_dotenv
import ssl
import smtplib

load_dotenv()

password = os.getenv('PASSWORD')

email_sender = "kapilesh1@gmail.com"
email_password = password

email_receiver = "pemora2469@otodir.com"

subject = "Dont forget to subscribe"

body = """
when you watch a video please hit the subscribe button
"""

em = EmailMessage()
em['from'] =email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())