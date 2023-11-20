import psycopg2


class Bot_User():
    def __init__(self,
                 telegram_id,
                 fullname,
                 username):
        self.telegram_id = telegram_id
        self.fullname = fullname
        self.username = username
        self.con = psycopg2.connect(
            dbname="project_bot",
            user="postgres",
            password="1",
            host="localhost",
            port=5432,
        )
        self.cur = self.con.cursor()

    def bot_users_list(self):
        query = """
        select * from bot_users;
        """
        self.cur.execute(query)
        users = self.cur.fetchall()
        return users

    def bot_user_save(self):
        insert_query = """
        insert into bot_users(telegram_id,fullname,username)
        values (%s,%s,%s)
        """
        params = (self.telegram_id, self.fullname, self.username)
        for i in self.bot_users_list():
            if self.telegram_id == i[1]:
                return
        else:
            self.cur.execute(insert_query, params)
            self.con.commit()


class User_Save():
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.con = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1",
            host="localhost",
            port=5432,
        )
        self.cur = self.con.cursor()

    def user_list(self):
        query = """
        select * from users;
        """
        self.cur.execute(query)
        users = self.cur.fetchall()
        return users

    def user_save(self):
        insert_query = """
        insert into users(name,age,phone_number)
        values (%s,%s,%s)
        """
        params = (self.name, self.age, self.phone_number)
        for i in self.user_list():
            if params == i[1:]:
                return "Kechirasiz oldin ro'yxatdan o'tgansiz ❗️"
        else:
            self.cur.execute(insert_query, params)
            self.con.commit()
            return "Muvafqiyatli saqlandi ✅️"


