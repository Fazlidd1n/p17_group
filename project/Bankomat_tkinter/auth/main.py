import datetime
import json
# import sys
# sys.path.append("/Users/macbookpro/PycharmProjects/p17_group/modul_3/dars_4")
from project.Bankomat_tkinter.DB.main import File


class User:
    def __init__(self,
                 id: str = None,
                 fullname: str = None,
                 email: str = None,
                 password: str = None,
                 balance: int = None,
                 card_number: int = None
                 ):
        self.id = id  # unique
        self.fullname = fullname
        self.email = email  # unique
        self.password = password
        self.balance = balance
        self.card_number = card_number  # unique
        self.created_at = str(datetime.datetime.now())
        self.update_at = str(datetime.datetime.now())
        self.file = File("users.json")

    def is_valid(self):
        users = self.file.read()
        for user in users:
            if user.get("email") == self.email:
                raise Exception("Already exits email ❗️")
            # if len(user.get("fullname").split()) != 2:
            #     raise Exception("Invalid fullname ❗️")

    def check_login(self):
        users = self.file.read()
        for user in users:
            if user.get("cardnumber") == self.card_number and user.get("password") == self.password:
                return User(**user)
        else:
            raise Exception("Not Found account ❗️")

    def create_id(self):
        users = self.file.read()
        if not users:
            self.id = 1
        else:
            self.id = users[-1].get("id") + 1

    def save(self):
        print(self.created_at,type(self.created_at))
        users = self.file.read()
        user = self.__dict__.copy()
        del user['file']
        users.append(user)
        self.file.write(users)

    # def delete(self):
    #     users = self.file.read()
    #     for i, user in enumerate(users):
    #         if user.get("id") == self.id:
    #             del users[i]
    #     self.file.write(users)

    # def edit(self, field, new_val):
    #     users = self.file.read()
    #     for i, user in enumerate(users):
    #         if user.get("id") == self.id:
    #             users[i][field] = new_val
    #     self.file.write(users)
