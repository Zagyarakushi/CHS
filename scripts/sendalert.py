import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

email = 'xxxx@xxxx.com'
password = 'xxxx'
send_to_emails = ['xxxx@xxxx.com', 'xxxx@xxxx.com'] # List of email addresses
subject = 'xxxx'
message = 'xxxx'
file_location = 'xxxx'

while True:
    filename = None
    for files in os.listdir(file_location):
        if os.path.isfile(os.path.join(file_location, files)):
            filename = files
    
    if filename != None:
        attachment = open(file_location+filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)

        for send_to_email in send_to_emails:
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))
            msg.attach(part)

            server.sendmail(email, send_to_email, msg.as_string()) 

        os.remove(file_location+filename)
        server.quit()
