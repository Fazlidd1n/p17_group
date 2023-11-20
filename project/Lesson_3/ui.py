from project.Lesson_3.auth.user.main import Students
from project.Lesson_3.auth.admin.main import *


class Function():
    def check_key(self, start, key, end):
        if key < start and key > end:
            raise Exception("Invalid key !")

    def register(self):
        data = {
            "first_name": input("First name : "),
            "last_name": input("Last name : "),
            "birth_day": input("Birthday : "),
            "phone": input("Phone : "),
            "username": input("User name : "),
            "password": input("Password : ")
        }
        if data.get("birth_day") == "":
            data["birth_day"] = None
        reg_n = data.get("first_name")
        data = Students(**data)
        data.insert_student()
        print(f"Hi {reg_n}! You are registered ✅")
        UI().main()

    def login(self):
        data = {
            "username": input("Username: "),
            "password": input("Password: ")
        }
        user = Students(**data).check_user()
        if user[-1] == False:

            UI().user_account(user)
        else:
            UI().admin_account(user)

    def active_course_add(self, name_course, userid):
        course_data = Admin().select_active_course_id(name_course)
        if course_data:
            Many().insert_table_many(userid, course_data[0][0])
            print(f"Your added {course_data[0][1]} group ✅")
        else:
            raise Exception("Not found course !")


class UI:
    def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) Exit 
                ------> """
            key = int(input(menu))
            Function().check_key(1, key, 3)
            match key:
                case 1:
                    Function().register()
                case 2:
                    Function().login()
                case 3:
                    return

        except Exception as e:
            print(e)
            self.main()

    def user_account(self, user):
        try:
            menu = """
            1. Active courses
            2. COURSE ENROLLMENT
            3. MY course 
            4. Log out
            -----------> """
            key = input(menu)
            Function().check_key("1", key, "4")
            match key:
                case "1":
                    for i in Students().select_active_course():
                        print(*i)
                    self.user_account(user)
                case "2":
                    name_course = input("Enter course name: ")
                    course_id = Function().active_course_add(name_course,user[0])
                    Admin().updt_num(course_id)
                    Function().active_course_add(name_course, user[0])
                    self.user_account(user)
                case "3":
                    for i in Many().user_courses(user[0]):
                        print(f"{i[0]} - {i[1]}")
                    self.user_account(user)
                case "4":
                    self.main()
        except Exception as e:
            print(e)
            self.user_account(user)

    def admin_account(self, user):
        try:
            menu = """
            1. Created course
            2. View the list of students enrolled in courses
            3. Log out
            ---------> """
            key = input(menu)
            Function().check_key(1, int(key), 3)
            match key:
                case "1":
                    group_cr = {
                        "course_name": input("Course: "),
                        "group_name": input("Group: ")
                    }
                    Admin(**group_cr).create_course()
                    print("Group created ✅")
                    self.admin_account(user)

                case "2":
                    # for i in Admin().select_student_course():
                    #     print(f"{i[0]}, {i[1]}")
                    #
                    # a = int(input("cours id sini kiriting : "))
                    #
                    # for i in Admin().students_table(a):
                    #     print(*Students(*i[0]).__dict__.items())
                    #
                    # self.admin_account(user)
                    nimadir = []
                    s = 0
                    for i in Admin().select_group_name():
                        print(f"{s} - {i[0]}")
                        s += 1
                        nimadir.append(*i)

                    a = int(input("cours id sini kiriting : "))
                    Function().check_key(0, a, s)

                    for i in Admin().select_student_course(nimadir[a]):
                        print(f"{i[0]} - {i[1]}")
                    b = int(input("Enter group id: "))
                    for i in Admin().students_table(b):
                        print(*Students(*i[0]).__dict__.items())
                    self.admin_account(user)
                case "3":
                    self.main()
        except Exception as e:
            print(e)
            self.admin_account(user)


run = UI()
run.main()
