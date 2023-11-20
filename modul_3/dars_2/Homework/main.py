# import json
#
#
# def main():
#     menu = """
#     1) register
#     2) login
#     3) exit
#     >>>"""
#     try:
#         key = input(menu)
#         key = key1(key, "1", "3")
#     except Exception as e:
#         print(e)
#         main()
#
#     match key:
#         case "1":
#             user = {
#                 "id": create_id(),
#                 "fullname": input("fullname : "),
#                 "username": input("username : "),
#                 "password": input("password : ")
#             }
#             try:
#                 register(user)
#             except Exception as e:
#                 print(e)
#                 main()
#         case "2":
#             user = {
#                 "username": input("username : "),
#                 "password": input("password : ")
#             }
#             try:
#                 login(user)
#             except Exception as e:
#                 print(e)
#
#         case "3":
#             print("Exit ☑️")
#             return
#     return
#
#
# file = "users.json"
#
#
# def read():
#     with open(file, "r") as f:
#         return json.load(f)
#
#
# def write(data: list[dict]):
#     with open(file, "w") as f:
#         json.dump(data, f, indent=3)
#
#
# def clear():
#     with open(file, "w") as f:
#         json.dump([], f)
#         print("Succesfully clear ✔️")
#
#
# def create_id():
#     users = read()
#     if not users:
#         id = 1
#     else:
#         id = users[-1]["id"] + 1
#
#     return id
#
#
# def save(data: dict):
#     users = read()
#     users.append(data)
#     write(users)
#
#
# def check_register(function):
#     def wrapper(user: dict):
#         if len(user.get("fullname").split()) < 2:
#             raise Exception("Invalid fullname ❗")
#         for i in read():
#             if user.get("username") == i.get("username"):
#                 raise Exception("Invalid username ❗️")
#         if len(user.get("password")) < 4:
#             raise Exception("Must password 4 chars ❗️")
#         result = function(user)
#         return result
#
#     return wrapper
#
#
# @check_register
# def register(data: dict):
#     save(data)
#     print("Succesfully save ☑️")
#     main()
#
#
# def check_login(function):
#     def wrapper(user: dict):
#         s = 0
#         for i in read():
#             if i.get("username") == user.get("username") and i.get("password") == user.get("password"):
#                 s = 1
#         if s == 1:
#             result = function(user)
#             return result
#         else:
#             raise Exception("Not found this username and password ❗️")
#
#     return wrapper
#
# @check_login
# def login(data: dict):
#     print("Welcome to your account ☑️️")
#     main()
#
# def key_valid(function):
#     def wrapper(key:str, start:str, end:str):
#         if not start <= key <= end:
#             raise Exception("Invalid key ❌")
#         return key
#     return wrapper
#
#
# @key_valid
# def key1(key, start, end) :
#     return key
#
# main()


# strp_case()

# print("input: |      Botir Qodirov       |")
# print("output: |Botir Qodirov|")
# l = input("nmadr: ")
#
#
# def check(function):
#     def wrapper(l: str):
#         return l.strip()
#
#     return wrapper
#
#
# @check
# def strip_case(l: str):
#     return l
#
#
# print(strip_case(l))


# datetime_valid
# def check_datetime(function):
#     def wrapper(data: str, hour: str):
#         s = 0
#         c = 0
#         for i in data:
#             if i == "-":
#                 s += 1
#         for i in hour:
#             if i == ":":
#                 c += 1
#         if s == 2 and c == 2:
#             result = function(d, h)
#             return result
#         else:
#             raise Exception("Date or time invalid ❌")
#
#     return wrapper
#
#
# @check_datetime
# def check_time(d: str, h: str):
#     return "Datetime valid ✅"
#
#
# try:
#     l = input("datetime: ")
#     d, h = l.split()
#     print(check_time(d, h))
#
# except Exception as e:
#     print(e)
