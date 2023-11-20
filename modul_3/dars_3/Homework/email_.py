import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig(filename="EMAIL.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

sender_email = "fazliddinismoilov234@gmail.com"
sender_password = "tzyg gfcm secx fdea"
receiver_email = "fazliddinismoilov234@gmail.com"
subject = "Test E-pochta"
message = "☑️😂"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain"))

try:
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)
    text = msg.as_string()
    smtp_server.sendmail(sender_email, receiver_email, text)
    smtp_server.quit()
    logging.info("E-pochta muvaffaqiyatli yuborildi!")
    print("Xabar yuborildi ✔️️")
except Exception as e:
    logging.error(f"E-pochta yuborilmadi. Xatolik: {str(e)}")
    print("Xabar yuborlmadi ✖️")
