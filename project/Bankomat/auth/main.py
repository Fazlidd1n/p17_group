from project.Bankomat.DB.main import DB
import sqlite3

class User:
    def __init__(self,
                 id:int = None,
                 name: str = None,
                 username: str = None,
                 password: str = None,
                 created_at: str = None,
                 updated_at: str = None
                 ):
        self.id = id
        self.name =name
        self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

    def check_password(self):
        if not len(self.password) < 4:
            raise Exception("Invalid password ❌")

    def insert(self):
        try:
            query = """
                        insert into users(name , username , password,created_at , update_at)
                        values (?,?,?,?,?)
                    """
            params = (self.name, self.username, self.password, self.created_at, self.updated_at)
            self.cur.execute(query, params)
            self.con.commit()
        except:
            raise Exception("username or name invalid !")
