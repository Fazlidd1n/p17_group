# class User:
#     name = "Kamol"
#     age = 24
#     join = ""
#
#
# user1 = User()
# user2 = User()
# print(user1.age)
# print(user1.name)
# user1.age = 30
# user1.join = f"{user1.name} {user1.age}"
# print(user1.join)
#
#




class User:
    # class attribute
    name = "Kamoliddin"
    salary = 0


    def __init__(self, name: str, age: int):
        # class instance attribute
        self.name = name
        self.age = age

user1 = User("Hoji", 24)
user2 = User("Botirjon", 27)

print(user1.name)
print(user2.name)





