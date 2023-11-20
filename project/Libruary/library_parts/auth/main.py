import datetime
import random

datetime.datetime.now()


class File:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self):
        with open(self.filename , "r") as f:
            return f.read()
    def write(self , data : str):
        with open(self.filename , "a") as f:
            f.write(data)

    def update(self , data: str):
        with open(self.filename , "w") as f:
            f.write(data)

    def clear(self):
        self.update("")

class User:
    def __init__(self,
                 card_id=None,
                 first_name = None ,
                 phone_number = None,
                 join_at = datetime.datetime.now()):
        self.card_id = card_id
        self.first_name = first_name
        self.phone_number = phone_number
        self.join_at = str(join_at)
        self.f = File("users.txt")

    def random_card_id(self):
        return str(random.randrange(1 , 1_000_000_000))
    def save(self):
        self.card_id = self.random_card_id().zfill(10)
        self.f.write("|".join(list(self.__dict__.values())[:-1])+"\n")
        return self.card_id

    def edit(self , field , new_val):
        users = self.f.read().split("\n")

        for i , user in enumerate(users):
            if user.split('|')[0] == self.card_id:
                s = user.split('|')
                if field == "first_name":
                    s[1] = new_val
                elif field == "phone_number":
                    s[2] = new_val
                users[i] = '|'.join(s)
                self.f.update('')
                for user in users:
                    self.f.write(user + "\n")


    def delete(self):
        users = self.f.read().split("\n")[:-1]
        for i, user in enumerate(users):
            if user.split('|')[0] == self.card_id:
                del users[i]
                self.f.update('')
                for user in users:
                    self.f.write(user + "\n")


    def isvalid(self):
        if not self.first_name.isalpha():
            raise Exception("First name must be alpha !")

        if len(self.phone_number) != 12:
            if len(self.phone_number) !=9:
                raise Exception("Phone number invalid : length must be 12 or 9")

    def select(self):
        users = self.f.read().split('\n')
        for user in users:
            s = user.split('|')
            if s[0] == self.card_id:
                return User(*s)

        else:
            raise Exception("User not found !")

# user1 = User("1234" , "Komil" , "998973277677")
#
# try:
#     user1.isvalid()
#     user1.save()
# except Exception as e:
#     print(e)

# user2 = User("1235" , "Botirjon" , "9777877777")
# user3 = User("1236" , "Murod" , "977776577")
# user4 = User("1237" , "Jasur" , "977754777")
# user2.delete()
# user1.delete()
# user1.save()
# user2.save()
# user3.save()
# user4.save()















