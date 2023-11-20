class ToDo:
    def __init__(self, title: str = None,
                 description: str = None,
                 time: str = None):
        self._title = title
        self._description = description
        self._time = time

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def time(self):
        return self._time

    def add(self, user):
        for i in users:
            if i == user:
                i._todo_list.append(self)
                return i
        return user

    def delete(self, user):
        for i in users:
            if i == user:
                i._todo_list.remove(self)
        print("Successfully delete !")

    def update(self):
        pass


class User:
    def __init__(self,
                 fullname: str = None,
                 username: str = None,
                 password: str = None):
        self._fullname = fullname
        self._username = username
        self._password = password
        self._todo_list: list[ToDo] = []

    @property
    def todo_list(self):
        return self._todo_list

    @todo_list.setter
    def todo_list(self, v):
        self._todo_list = v

    def check_username(self):
        for user in users:
            if user.username == self.username:
                return True

        return False

    def check_login(self):
        for user in users:
            if user.username == self.username and user.password == self.password:
                return user

    def add(self):
        users.append(self)

    def delete(self):
        if self in users:
            users.remove(self)

    def info_check(self):
        if len(self.password) < 4:
            print("Invalid password")
            return False

        return True

    @property
    def fullname(self):
        return self._fullname

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password


users: list[User] = []


class UI:

    def register(self):
        user = {
            "fullname": input("Fullname : "),
            "username": input("Username : "),
            "password": input("Password : ")
        }
        user = User(**user)
        if not user.info_check():
            self.main()
            return

        if user.check_username():
            print(f"Already exists your username : {user.username}")
        else:
            user.add()
            print("Successfully created account")
        self.main()
        return

    def login(self):
        login_info = {
            "username": input("Username: "),
            "password": input("Password: ")
        }
        user = User(**login_info)
        user = user.check_login()
        if not user:
            print("Not found account !")
            self.main()
            return
        self.account(user)

    def todo_crud(self, user):
        menu = """
            1) add 
            2) delete 
            3) update 
            4) todo_list
            5) <-back
            >>>"""
        key = input(menu)
        match key:
            case "1":
                todo = {
                    "title": input("Title:"),
                    "description": input("Description:"),
                    "time": input("Time : ")
                }
                todo = ToDo(**todo)
                user = todo.add(user)
                self.todo_crud(user)

            case "2":
                for i in range(len(user.todo_list)):
                    print("N :", i, (user.todo_list[i].title, user.todo_list[i].description, user.todo_list[i].time))
                key = int(input("N : "))
                for i in range(len(user.todo_list)):
                    if i == key:
                        del user.todo_list[i]
                        print("Succesfuly deleted !")
                        self.todo_crud(user)

            case "3":
                for i in users:
                    print(i)

                # for i in range(len(user.todo_list)):
                #     print("N :", i, (user.todo_list[i].title, user.todo_list[i].description, user.todo_list[i].time))

                # key = int(input("N : "))
                # title_temp = input("Title : ")
                # description_temp = input("Description : ")
                # time_temp = input("Time : ")
                # user[0].todo_list[2].title = title_temp
                # for i in range(len(user.todo_list)):
                #     if i == key:
                #         user.todo_list[i].title = title_temp
                #         user.todo_list[i].description = description_temp
                #         user.todo_list[i].time = time_temp

            case "4":

                for i in user.todo_list:
                    print((i.title, i.description, i.time))
                self.account(user)

            case "5":
                self.account(user)
                return

    def settings(self):
        pass

    def account(self, user):
        menu = """
        1) TODO crud
        2) settings
        3) exit
        >>>"""
        key = input(menu)
        match key:
            case "1":
                self.todo_crud(user)
            case "2":
                self.settings()
            case "3":
                self.main()

    def main(self):
        menu = f"""
        1) register
        2) login
        3) exit
        >>>"""
        key = input(menu)
        match key:
            case "1":
                self.register()

            case "2":
                self.login()
            case "3":
                return


obj = UI()
obj.main()
