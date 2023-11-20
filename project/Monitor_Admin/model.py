from project.Monitor_Admin.DB import DB


class User(DB):
    def __init__(self,
                 id: int = None,
                 first_name: str = None,
                 last_name: str = None,
                 phone: str = None,
                 birth_day: str = None,
                 username: str = None,
                 password: str = None,
                 is_admin: bool = False):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.birth_day = birth_day
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def select(self):
        super().select()

    def is_login(self):
        query = """
            select * from users where username = %s and password = %s
        """
        params = (self.username, self.password)
        self.cur.execute(query, params)
        user = self.cur.fetchone()
        return user

    def insert(self):
        query = """
            insert into users(first_name,last_name,phone,birth_day,username,password)
            values (%s,%s,%s,%s,%s,%s)
        """
        p = self.__dict__.copy()
        p.pop('id')
        params = tuple(*p.values())
        self.cur.execute(query, params)
        self.con.commit()

    def update(self):
        super().update()
