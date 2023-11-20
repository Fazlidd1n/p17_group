from auth.main import File, User
from message.main import Message


class UI:
    def main(self):
        self.file = File("users.json")
        menu = """
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

    def register(self):
        user = {
            # "id": self.id,
            "fullname": input("fullname: "),
            "username": input("username: "),
            "password": input("password: "),
            "messages": {}
        }
        user = User(**user)
        user.create_id()
        user.save()
        self.main()

    def login(self):
        username = input("username: ")
        password = input("password: ")
        users = self.file.read()
        for user in users:
            if user.get("username") == username and user.get("password") == password:
                print("Welcome your account !✔️️")
                self.account()
                break
        else:
            print("Not found account !")
            self.main()

    def account(self):
        menu = """
        1) chat
        2) account_settings
        3) <- back
        >>>"""
        key = input(menu)
        match key:
            case "1":
                print("Welcome chat ! ✔️")
                self.chat()
            case "2":
                menu = """
                1) Update-fullname
                2) Update-username
                3) Update-password
                4) <- back
                >>>"""
                key = input(menu)
                match key:
                    case "1":
                        field = input("old fullname: ")
                        new_field = input("new fullname: ")
                        users = self.file.read()
                        for i, user in enumerate(users):
                            if user.get("fullname") == field:
                                users[i]["fullname"] = new_field
                                print("Succesfully update !✔️")
                                self.file.write(users)
                                break
                        self.account()

                    case "2":
                        field = input("old username: ")
                        new_field = input("new username: ")
                        users = self.file.read()
                        for i, user in enumerate(users):
                            if user.get("username") == field:
                                users[i]["username"] = new_field
                                print("Succesfully update !✔️")
                                self.file.write(users)
                                break
                        self.account()

                    case "3":
                        field = input("old password: ")
                        new_field = input("new password: ")
                        users = self.file.read()
                        for i, user in enumerate(users):
                            if user.get("password") == field:
                                users[i]["password"] = new_field
                                print("Succesfully update !✔️")
                                self.file.write(users)
                                break
                        self.account()

                    case "4":
                        self.account()
            case "3":
                self.main()

    def chat(self):
        pass


run = UI()
run.main()
