# import smtplib
# import ssl
#
# # SSL - Secore Socket Layer
# # 465-port
# port = 465
# smtplib_server = "smtp.gmail.com"
# from_email = "fazliddinismoilov234@gmail.com"
# receiver_email = "absaitovdev@gmail.com"
# password = "ntqvwchqiutirwrm"
# message = "Qondayey !"
# context = ssl.create_default_context()
#
# with smtplib.SMTP_SSL(smtplib_server, port, context=context) as server:
#     print(server.login(from_email, password))
#     server.sendmail(from_email, receiver_email, message)


# import smtplib
# import ssl
#
# # SSL - Secure Socket Layer
# # 465 - port
# port = 587
# smtplib_server = "smtp.gmail.com"
# from_email = "fazliddinismoilov234@gmail.com"
# receiver_email = "fazliddinismoilov234@gmail.com"
# password = "pwlmnerozucosqgs"
# message = "Qonday !"
# ssl_cert_path = ssl.get_default_verify_paths().openssl_cafile
# context = ssl.create_default_context(cafile=ssl_cert_path)
# print(ssl_cert_path)
# with smtplib.SMTP_SSL(smtplib_server, port , context=context) as server:
#     print(server.login(from_email, password))
#     server.sendmail(from_email, receiver_email, message)


# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# sender_email = "fazliddinismoilov234@gmail.com"
# receiver_email = "absaitovdev@gmail.com"
# password = "pwlmnerozucosqgs"
#
# message = MIMEMultipart("alternative")
# message["Subject"] = "multipart test"
# message["From"] = sender_email
# message["To"] = receiver_email
#
# text = """\
# Hi,
# How are you?
# Real Python has many great tutorials:
# www.realpython.com"""
# html = """\
# <html>
#   <body>
#     <p>Hi,<br>
#        How are you?<br>
#        <a href="http://www.realpython.com">Real Python</a>
#        has many great tutorials.
#     </p>
#   </body>
# </html>
# """
#
# part1 = MIMEText(text, "plain")
# part2 = MIMEText(html, "html")
#
# message.attach(part1)
# message.attach(part2)
#
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(
#         sender_email, receiver_email, message.as_string()
#     )


import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'fazliddinismoilov234@gmail.com'
sender_password = 'plprxybajsujybwj'
receiver_email = 'fazliddinismoilov234@gmail.com'
subject = 'Email Subject'
message = 'Qonday Doston!'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = sender_email
smtp_password = sender_password

while True:
    # time.sleep(3)
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print('Error sending email:', str(e))



