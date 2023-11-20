import json
import logging

logging.basicConfig(filename="TEST.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def main():
    menu = """
    1) REGISTER
    2) LOGIN
    3) EXIT
    ------> """
    try:
        key = input(menu)
        key = key1(key, "1", "3")
    except Exception as e:
        print(e)
        main()

    match key:
        case "1":
            user = {
                "id": create_id(),
                "fullname": input("fullname : "),
                "username": input("username : "),
                "password": input("password : ")
            }
            try:
                register(user)
            except Exception as e:
                print(e)
                main()
        case "2":
            user = {
                "username": input("username : "),
                "password": input("password : ")
            }
            try:
                logger.info("User is registered ✅")
                login(user)
            except Exception as e:
                print(e)
        case "3":
            logger.info("Exit ✅")
            print("Exit ✅")
            return

file = "users.json"

def read():
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write(data: list[dict]):
    with open(file, "w") as f:
        json.dump(data, f, indent=3)
    logger.info("Data  written to (users.json) file ✅")

def clear():
    with open(file, "w") as f:
        json.dump([], f)
        logger.info("Successfully cleared ✔️")

def create_id():
    users = read()
    if not users:
        id = 1
    else:
        id = users[-1]["id"] + 1
    return id

def save(data: dict):
    users = read()
    users.append(data)
    write(users)

def check_register(function):
    def wrapper(user: dict):
        if len(user.get("fullname").split()) < 2:
            error_message = "Invalid fullname ❗"
            logger.error(error_message)
            raise Exception(error_message)
        for i in read():
            if user.get("username") == i.get("username"):
                error_message = "This username exists! Choose another ❗️"
                logger.error(error_message)
                raise Exception(error_message)
        if len(user.get("password")) < 4:
            error_message = "Password must be at least 4 characters ❗️"
            logger.error(error_message)
            raise Exception(error_message)
        result = function(user)
        return result

    return wrapper

@check_register
def register(data: dict):
    save(data)
    print("Successfully saved ✅")
    main()

def check_login(function):
    def wrapper(user: dict):
        s = 0
        for i in read():
            if i.get("username") == user.get("username") and i.get("password") == user.get("password"):
                s = 1
        if s == 1:
            result = function(user)
            return result
        else:
            error_message = "Username or password not found ❗️"
            logger.error(error_message)
            raise Exception(error_message)

    return wrapper

@check_login
def login(data: dict):
    print("Welcome to your account ✅")
    main()

def key_valid(function):
    def wrapper(key: str, start: str, end: str):
        if not start <= key <= end:
            error_message = "Invalid key ❌"
            logger.error(error_message)
            raise Exception(error_message)
        return key

    return wrapper

@key_valid
def key1(key, start, end):
    return key

main()