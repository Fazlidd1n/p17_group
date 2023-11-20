import datetime
import psycopg2


class Students:
    con = psycopg2.connect(database="monitoradmin",
                           user="postgres",
                           password="1",
                           host="localhost",
                           port=5432)

    cur = con.cursor()

    def __init__(self, user_id: int = None,
                 first_name: str = None,
                 last_name: str = None,
                 birth_day: str = None,
                 phone: str = None,
                 username: str = None,
                 password: str = None,
                 is_admin: bool = False
                 ):
        self.userID = user_id
        self.first_name = first_name
        self.lastname = last_name
        self.birth_day = birth_day
        self.phone = phone
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f"{self.__dict__}"

    def insert_student(self):
        query = f'''
            insert into users(
            first_name,
            last_name,
            birth_day,
            phone,
            username,
            password,
            is_admin )
            values (%s, %s, %s, %s, %s, %s, %s)
        '''
        params = (
            self.first_name,
            self.lastname,
            self.birth_day,
            self.phone,
            self.username,
            self.password,
            self.is_admin
        )
        self.cur.execute(query, params)
        self.con.commit()

    def select_active_course(self):
        query = '''
            select course_name from courses where is_active = %s'''
        params = (True,)
        self.cur.execute(query, params)
        active_course = self.cur.fetchall()
        return active_course

    def search_students(self, student_id):
        users = []
        for i in student_id:
            query = '''
            select * from users where user_id = %s
            '''
            params = (i,)
            self.cur.execute(query, params)
            student = self.cur.fetchall()
            users.append(student)
        return users

    # def select_numer_students(self, course_name):
    #     query = """
    #         select number_of_students from courses where course_name = %s and is_active = %s
    #     """
    #     params = (course_name, True)
    #     self.cur.execute(query, params)
    #     a = self.cur.fetchone()
    #     queery = """
    #     update courses set number_of_students = %s where course_name = %s and is_active = truer"""
    #     param = (a[0] + 1,course_name)
    #     self.cur.execute(queery, param)
    #     self.con.commit()

    def check_user(self):
        query = '''
            select * from users where username =  %s and password = %s '''
        params = (self.username, self.password)
        self.cur.execute(query, params)
        user = self.cur.fetchone()
        if not user:
            raise Exception("User not found! ")
        return user

# print(Students().select_active_course())
