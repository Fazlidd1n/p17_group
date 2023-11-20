class User:
    def __init__(self,
                 fullname: str = None,
                 age: int = None,
                 phone: str = None,
                 gender: str = None,
                 email: str = None,
                 password: str = None,
                 address: str = None) -> None:
        self.fullname = fullname
        self.age = age
        self.phone = phone
        self.gender = gender
        self.email = email
        self.password = password
        self.address = address

    def add(self):
        database.append(self)

    def delete(self):
        pass

    def update(self):
        pass

    def select(self):
        return database


class Util(User):
    def __init__(self,
                 fullname: str = None,
                 age: int = None,
                 phone: str = None,
                 gender: str = None,
                 email: str = None,
                 password: str = None,
                 address: str = None) -> None:
        super().__init__(fullname, age, phone, gender, email, password, address)

    def check_email(self):
        for user in database:
            if user.email == self.email:
                return True
        else:
            return False

    def check_login(self, email, password):
        for user in database:
            if user.email == email and user.password == password:
                return True


database: list[User] = []


class UI:
    def register(self):
        user_dict = {"fullname": input("Fullname: "),
                     "age": int(input("Age: ")),
                     "phone": input("Phone: "),
                     "gender": input("Gender (M/F): "),
                     "email": input("Email: "),
                     "password": input("Password: "),
                     "address": input("Address: ")}
        user = User(**user_dict)
        check_email: bool = Util(**user_dict).check_email()
        if check_email:
            print("Already exists your email !")
        else:
            user.add()
            print("Create account successfully")
        self.main()
        return

    def login(self, email, password):
        email = input("email : ")
        password = input("password : ")
        obj = Util(email=email, password=password)
        user: User = obj.check_login()
        if not user:
            print("Not found your account !")
        print(f"Welcome to {user.fullname} account !")

    def main(self):
        menu = """
        1. register
        2. login
        3. users
        4. exit
        >>>"""
        key = input(menu)
        match key:
            case "1":
                self.register()
            case "2":

                self.login()
            case "3":
                user = User()
                for i in user.select():
                    print(i.fullname)
                self.main()
                return


run = UI()
run.main()
