# N2
# import datetime
#
# def datetime_secund(date):
#     e = datetime.datetime(1970, 1, 1)
#     d = date - e
#     s = d.total_seconds()
#     return int(s)
#
# try:
#     datetime_ = "2009-02-12 21:37:58"
#     time_ = datetime.datetime.strptime(datetime_, "%Y-%m-%d %H:%M:%S")
#     result = datetime_secund(time_)
#     print(result)
#
# except:
#     print("Xato")

# N3
# import threading
# import smtplib,time
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
#
# def send_email(email):
#     sender_email = "fazliddinismoilov234@gmail.com"
#     sender_password = "bwml ffmd rfrw veup"
#     receiver_email = email
#     subject = "Test E-pochta"
#     message = "Hello world ✅"
#
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     msg["Subject"] = subject
#
#     msg.attach(MIMEText(message, "plain"))
#
#     try:
#         smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
#         smtp_server.starttls()
#         smtp_server.login(sender_email, sender_password)
#         text = msg.as_string()
#         smtp_server.sendmail(sender_email, receiver_email, text)
#         smtp_server.quit()
#         print("Xabar yuborildi ✔️️")
#     except Exception as e:
#         print("Xabar yuborlmadi ✖️")
#
#
# emails = ["fazliddinismoilov234@gmail.com", "botir@gmail.com"]
# threads = []
# start = time.time()
# for i in emails:
#     t = threading.Thread(target = send_email,args=(i,))
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()
#
# print(time.time()-start)

# N4
"""1) barcha funksiya yoki wunga oxwaw narsalarni bir vaqtta yuborish uchun vaqtan yutish uchun yordam beradi !"""

# import requests, sqlite3, asyncio
#
# async def read():
#     url = "https://jsonplaceholder.typicode.com/comments"
#     datas = requests.get(url)
#     return datas
#
# con = sqlite3.connect("datas.sqlite")
# cur = con.cursor()
# query = """
#     create table if not exists datas(
#     postId integer not null,
#     id integer not null,
#     name varchar(255)not null ,
#     email varchar(255)not null,
#     body varchar (255)not null
#     )
# """
# cur.execute(query)
# con.commit()
#
# async def insert(data: dict):
#     q = """
#         insert into datas(postId,id,name,email,body)values (?,?,?,?,?)
#     """
#     params = (data.get("postId"), data.get("id"), data.get("name"), data.get("email"), data.get("body"))
#     cur.execute(q, params)
#     con.commit()
#     print("save")
#
# for i in asyncio.run(read()).json():
#     asyncio.run(insert(i))


# N5
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# l = [8, 4, 5, 7, 4, 2, 4, 6, 7]
# head = Node(0)
# tmp = head
# for i in l:
#     tmp.next = Node(i)
#     tmp = tmp.next
#
# tmp = head.next
# s = 0
# while tmp:
#     s += 1
#     tmp = tmp.next
#
# tmp = head.next
# if s % 2 == 0:s = s // 2
# else:s = (s - 1) // 2
# c = 0
# while tmp:
#     if s == c:
#         print(tmp.value)
#     c += 1
#     tmp = tmp.next
