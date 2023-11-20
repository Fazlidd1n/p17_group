import sqlite3


con = sqlite3.connect("test.sqlite")
cur = con.cursor()
# quary = """
#     insert into users(name,username,password)
#     values('Kamol','kamol_07','12345');
# """
# cur.execute(quary)
# con.commit()
#
# product_table = """
#     create table products(
#         id         integer primary key autoincrement,
#         name       varchar (255) not null,
#         year       varchar (255) not null,
#         expire     datetime default current_timestamp ,
#         amount     integer not null
#     )
# """
# cur.execute(product_table)
# con.commit()
