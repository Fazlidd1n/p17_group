class ToDo:
    def __init__(self, title: str, description: str, time: str):
        self._title = title
        self._description = description
        self._time = time


class User:
    def __init__(self,
                 fullname: str = None,
                 username: str = None,
                 password: str = None):
        self._fullname = fullname
        self._username = username
        self._password = password
        self._todo_list: list[ToDo] = []

    def check_username(self):
        for user in users:
            if user.username == self.username:
                return True

        return False

    def check_login(self):
        for user in users:
            if user.username == self.username and user.password == self.password:
                return True
        return False

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

    def add_todo(self):
        todo = {
            "title": input("Title : "),
            "description": input("Description : "),
            "time": input("Time : ")
        }
        todo = ToDo(**todo)
        self._todo_list.append(todo)
        print("Successfully added todo")

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
        if not user.check_login():
            print("Not found account !")
            self.main()
            return
        self.account()

    def todo_crud(self):
        menu = f"""
        1) Create - TODO
        2) Delete - TODO
        3) Update - Todo
        4) TODOS - Dates
        >>> """
        key = input(menu)
        match key:
            case "1":
                self.add_todo()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass

    def settings(self):
        pass

    def account(self):
        print("Welcome")
        menu = f"""
        1) TODO crud
        2) settings
        3) exit
        >>>"""
        key = input(menu)
        match key:
            case "1":
                self.todo_crud()
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
