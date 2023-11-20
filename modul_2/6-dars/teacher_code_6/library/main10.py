from abc import ABC, abstractmethod
import datetime
import random




class File:
    def __init__(self, filename: str = None):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return f.read()

    def write(self, data: str):
        with open(self.filename, "a") as f:
            f.write(data)

    def update(self, data: str):
        with open(self.filename, "w") as f:
            f.write(data)

    def clear(self):
        with open(self.filename, "w") as f:
            f.write('')


class AbstractCRUD(ABC):
    def __init__(self, joint_at: str = None):
        self.joint_at = joint_at

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class User(AbstractCRUD):

    def __init__(self,
                 card_id: int = None,
                 fullname: str = None,
                 age: str = None,
                 phone_number: str = None,
                 join_at: str = None
                 ):
        self.card_id = card_id
        self.fullname = fullname
        self.age = age
        self.phone_number = phone_number
        super().__init__(join_at)

    def data_check(self):
        if len(self.fullname.split()) < 2:
            raise Exception("Fullname invalid")
        if len(self.phone_number) != 12:
            if len(self.phone_number) != 9:
                raise Exception("Phone number invalid")

        if self.age.isdigit() and int(self.age) < 18:
            raise Exception("Age invalid")





    def create(self):
        file = File("users.txt")
        data = " | ".join(self.__dict__.values()) + "\n"
        file.write(data)


        print("Successfully created !")

    def select(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
session_user : User = None

class Book(AbstractCRUD):

    def __init__(self,
                 name: str = None,
                 author: str = None,
                 category: str = None,
                 join_at: str = None
                 ):
        self.name = name
        self.author = author
        self.category = category
        super().__init__(join_at)

    def create(self):
        pass

    def select(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class Util:
    def check_key(self, key, start, end, function):
        if not (key.isdigit() and start <= int(key) <= end):
            raise Exception("Invalid key")

    def random_card_id(self):
        card_id = str(random.randrange(1_000_000_000 , 9_999_999_999))
        return card_id

    def check_card_id(self , card_id , function):
        file = File("users.txt")
        for user in file.read().split("\n"):
            if user.split("|")[0] == card_id:
                return User(*user.split("|"))

        else:
            print("Not found card id !")
            function()
            return False



class UI:




    def main(self):
        menu = """
        1) register
        2) login
        3)exit
        >>>
        """
        key = input(menu)
        try:
            Util().check_key(key, 1, 3, self.main)

            match key:
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except Exception as e:
            print(e)
            self.main()

    def register(self):
        user = {
            "fullname" : input("Full name :"),
            "age": input("Age : "),
            "card_id": Util().random_card_id(),
            "phone_number": input("Phone number"),
            "join_at": str(datetime.datetime.now())
        }

        user = User(**user)
        try:
            user.data_check()
            user.create()
            self.main()
        except Exception as e:
            print(e)
            self.main()



    def login(self):
        global session_user
        card_id = input("Card id : ")
        is_valid =  Util().check_card_id(card_id , self.main)
        if not is_valid:
            return
        session_user = is_valid
        self.account()

    def user_settings(self):
        print(f"your fullname : {session_user.fullname}")
        print(f"your age : {session_user.age}")
        print(f"your phone_number : {session_user.phone_number}")

        field = f"""
                        1) Fullname
                        2) age
                        3) phone_number
                        4) back
                        >>>"""
        key = input(field)
        Util().check_key(key, 1, 4, self.user_settings)
        match key:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                self.account()


    def account(self):
        menu = """
        1) book
        2) settings
        3) exit
        """

        key = input(menu)
        Util().check_key(key , 1 , 3 , self.account)
        match key:
            case "1":
                pass
            case "2":
                self.user_settings()
            case "3":
                self.main()
                return



run = UI()
run.main()

