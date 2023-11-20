# import threading
# import time
#
#
# # def a():
# #     time.sleep(5)
# #     print("a")
# # def b():
# #     time.sleep(6)
# #     print("b")
# #
# # start = time.time()
# # t1 = threading.Thread(target=a)
# # t2 = threading.Thread(target=b)
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# # print(time.time()-start)
#
# def a(num):
#     time.sleep(1)
#     print(num)
#
#
# start = time.time()
# l = [1, 2, 3, 4, 5]
# threads = []
# for i in range(1):
#     t = threading.Thread(target=a, args=(i,))
#     t.start()
#     threads.append(t)
#
# for i in threads:
#     i.join()
# print(time.time() - start)


# import smtplib
# import threading
# import time
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# logging.basicConfig(filename="EMAIL.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger()
#
# emails = """leetcodemee23@gmail.com
# akbaralisalohiddinov808@gmail.com
# sarvarismatullayev7@gmail.com
# fazliddinismoilov234@gmail.com
# javoxirmamatayev@gmail.com
# aralovjavoxir@gmail.com
# jahonsaitqulov@gmail.com
# fayzullaxojaevi@gmail.com
# azamovshahboz006082001@gmail
# dadturchi@gmail.com
# ominanuriddinova2212@gmail.com
# sokidjonovabdulbosit53@gmail.com
# behruzpdp@gmail.com
# akhdeveloper777@gmail.com
# nodirovshoxzod717@gmail.com
# ozodbekyarkinov@gmail.com""".split('\n')
#
# def send(receiver_email:str):
#     sender_email = "fazliddinismoilov234@gmail.com"
#     sender_password = "tzyg gfcm secx fdea"
#     subject = "Test E-pochta"
#     message = "Hello world ☑️"
#
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     msg["Subject"] = subject
#
#     msg.attach(MIMEText(message, "plain"))
#
#     smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
#     smtp_server.starttls()
#     smtp_server.login(sender_email, sender_password)
#     text = msg.as_string()
#     smtp_server.sendmail(sender_email, receiver_email, text)
#     smtp_server.quit()
#     logging.info("E-pochta muvaffaqiyatli yuborildi!")
#     print("Xabar yuborildi ✔️️")
#
# start = time.time()
# threads = []
# for i in emails:
#     t = threading.Thread(target=send,args=(i,))
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()
#
# print(time.time()-start)

