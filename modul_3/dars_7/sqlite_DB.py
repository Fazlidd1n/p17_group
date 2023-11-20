import datetime
import sqlite3
from abc import ABC, abstractmethod


class DB(ABC):
    con = sqlite3.connect("test.sqlite")
    cur = con.cursor()

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self, field, new_val):
        pass


class User(DB):
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 username: str = None,
                 password: str = None,
                 created_at: str = None,
                 updated_at: str = None):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

    def is_validate(self):
        if len(self.password) < 4:
            raise Exception("Password invalid ❗️")

    def insert(self):
        try:
            query = """
                insert into users(name ,username,password,created_at,updated_at) values (?,?,?,?,?)
            """
            params = (self.name, self.username, self.password, self.created_at, self.updated_at)
            self.cur.execute(query, params)
            self.con.commit()
        except:
            raise Exception("Username or password invalid ❗️")

    def select(self):
        quary = """
            select * from users where username = ? and password = ?;
        """
        params = (self.username, self.password)
        self.cur.execute(quary, params)
        user = self.cur.fetchone()
        if user:
            return User(*user)
        return "Not found account ❗️"

    def delete(self):
        quary = """
            delete from users where username = ?;
        """
        params = (self.username,)
        self.cur.execute(quary, params)
        self.con.commit()

    def update(self, field, new_val):
        quary = f"""
            update users set {field} = ? where id = ?;
        """
        params = (new_val, self.id)
        self.cur.execute(quary, params)
        self.con.commit()


# user = {
#     "name": input("name:"),
#     "username": input("username:"),
#     "password": input("password:"),
#     "created_at": datetime.date.today(),
#     "updated_at": datetime.datetime.now()
# }
# User(**user).insert()


# user = {
#     "username": input("username:"),
#     "password": input("password:"),
# }
# print(User(**user).select().id)


# user = {
#     "username": input("username:"),
# }
# User(**user).delete()

session = {
    "id": 4,
}
User(**session).update("name", "Rustam")
