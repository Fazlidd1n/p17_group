import datetime

from sqlite_DB import User

class UI:
    def main(self):
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
        try:
            user = {
                "name" : input("name :"),
                "username": input("username :"),
                "password": input("password :"),
                "created_at": datetime.date.today(),
                "updated_at": datetime.datetime.now()
            }
            user = User(**user)
            user.is_validate()
            user.insert()
            print("Succesfully register ✅")
            self.main()
        except Exception as e:
            print(e)
            self.main()

    def login(self):
        user = {
            "username": input("username :"),
            "password": input("password :")
        }
        user = User(**user).select()
        if not user:
            raise Exception("Not found account ❗️")
        else:
            print("Welcome ✅")
            self.main()

run = UI()
run.main()