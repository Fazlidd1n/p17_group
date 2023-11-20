import psycopg2
from project.Lesson_3.auth.user.main import Students

class Admin:
    con = psycopg2.connect(database="monitoradmin",
                           user="postgres",
                           password="1",
                           host="localhost",
                           port=5432)
    cur = con.cursor()

    def __init__(self, course_id: int = None,
                 course_name : str = None,
                 group_name : str = None,
                 number_of_students: int = None,
                 is_active: bool = True):
        self.courseID = course_id
        self.course_name = course_name
        self.group_name = group_name
        self.number_of_students = number_of_students
        self.is_active = is_active


    def create_course(self):
        query = '''
            INSERT INTO courses (course_name, group_name, is_active)
            VALUES (%s, %s, %s)
        '''
        params = (self.course_name, self.group_name, self.is_active)
        self.cur.execute(query, params)
        self.con.commit()

    def students_table(self, courseID):
        return Many().select_users(courseID)

    def select_student_course(self, name):
        query = """
            select course_id, group_name from courses where course_name =%s"""
        params = (name, )
        self.cur.execute(query, params)
        students = self.cur.fetchall()
        return students

    def select_group_name(self):
        query = """
            select distinct course_name from courses """
        self.cur.execute(query)
        name_group = self.cur.fetchall()
        return name_group


    def select_active_course_id(self, name):
        query = """
                    select course_id, group_name from courses where course_name =%s and is_active = %s"""
        params = (name, True)
        self.cur.execute(query, params)
        students = self.cur.fetchall()
        return students

    def select_groups_name(self, courseId):
        a=[]
        for i in courseId:
            query = f"""
                select course_name, group_name from courses where course_id = %s"""
            params = (i, )
            self.cur.execute(query, params)
            datas = self.cur.fetchall()
            a.append(*datas)
        return a

    def update_number_of_students(self, course_ID):
        query = """
            select number_of_students from courses where course_id = %s"""
        params = (course_ID,)
        self.cur.execute(query, params)
        num_st = self.cur.fetchone()
        num_st = num_st[0] + 1
        return num_st

    def updt_num(self, course_ID):
        a = self.update_number_of_students(course_ID)
        query1 = """
                    update courses set number_of_students=%s where course_id =%s
                    """
        params1 = (a, course_ID)
        self.cur.execute(query1, params1)
        if a == 5:
            query1 = """
                update courses set is_active=%s where course_id =%s
                """
            params1 = (False, course_ID)
            self.cur.execute(query1, params1)
            self.con.commit()
        self.con.commit()

class Many:
    con = psycopg2.connect(database="monitoradmin",
                           user="postgres",
                           password="1",
                           host="localhost",
                           port=5432)
    cur = con.cursor()

    def insert_table_many(self, user_id, course_id):
        query = '''
            insert into users_courses (user_id, course_id)
            values (%s, %s)'''
        params = (user_id, course_id)
        self.cur.execute(query, params)
        self.con.commit()

    def select_users(self, course_ID):
        query = '''
            select user_id from users_courses where course_id = %s  '''
        params = (course_ID, )
        self.cur.execute(query, params)
        studentsID = self.cur.fetchall()
        return Students().search_students(studentsID)

    def user_courses(self, userid):
        query = '''
                   select course_id from users_courses where user_id = %s  '''
        params = (userid, )
        self.cur.execute(query, params)
        course_id = self.cur.fetchall()
        if not course_id:
            raise Exception("Not course! ")
        else:
            return Admin().select_groups_name(course_id)

# Many().create_table_many()

# print(Admin().select_group_name())