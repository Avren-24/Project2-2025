import smtplib
from email.message import EmailMessage

from_email_addr = "1552038394@qq.com"
from_email_pass = "kayyffzchnoohade"
to_email_addr = "1552038394@qq.com"

msg = EmailMessage()

body = "Hello from Raspberry Pi"
msg.set_content(body)

msg['From'] = from_email_addr
msg['To'] = to_email_addr

msg['Subject'] = 'TEST EMAIL'

server = smtplib.SMTP('smtp.qq.com', 587)

server.starttls()

server.login(from_email_addr, from_email_pass)

server.send_message(msg)

print('Email sent')

server.quit()
