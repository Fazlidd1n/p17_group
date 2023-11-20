# user = {
#         "fullname" : "",
#         "age" : "",
#         "phone_number" : "",
#         "email" : "",
#         "password" : ""
#     }

data = []


def register(user:dict):
    data.append(user)


def login(email , password):
    pass


def check_email(email):
    for i in data:
        if i.get("email") == email:
            return False
    return True


while True:
    menu = """
        1. Register
        2. Login
        3. exit
        4. all data
        >>>"""
    key = input(menu)
    if not key.isdigit() or not 1 <= int(key) <= 4:
        print("Key invalid !")
        continue

    match key:
        case "1":
            user = {
                "fullname": input("fullname: "),
                "age": input("age: "),
                "phone_number": input("phone_number: "),
                "email": input("email: "),
                "password": input("password: ")
            }
            isvalid = check_email(user.get("email"))
            if isvalid:
                register(user)
            else:
                print("Already email exists !")
                continue
        case "2":
            email = input("email : ")
            password = input("password : ")
            login(email , password)
        case "3":
            break
        case "4":
            print(data)




