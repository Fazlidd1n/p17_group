# Task1
# try:
#     with open("task1.txt", "r") as f:
#         text = f.read()
#         assert len(text) != 0, Exception("Error !")
#         print(text)
# except Exception as e:
#     print(e)

# Task2

def password():
    try:
        while True:
            password = input("password : ")
            assert not len(password) < 4, Exception("Password invalid !")
            s = 0
            for i in password:
                if i.isupper() or i.islower():
                    s += 1
            if s > 0:
                raise Exception("Password valid !")
                break
            else:
                raise Exception("Password invalid !")


    except Exception as e:
        print(e)


password()
