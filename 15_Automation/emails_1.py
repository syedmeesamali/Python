import smtplib
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(type(smtpObj))
