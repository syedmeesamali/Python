import smtplib
server = smtplib.SMTP('smtp-mail.outlook.com:587')
print(type(server))
server.ehlo()
server.starttls()
try:
    server.login("my_email_address", "my_password")
except SMTPAuthenticationError:
    print("MTPAuthenticationError")
server.sendmail('my_email_address', 'recipient_Email', 'Subject: Email from python')
print("Email sent successfully")
server.quit()
