#
# import csv
#
#
# with open("cars.csv" , "w") as f:
#     writer = csv.writer(f)
#
#     writer.writerow(["GM","chevrolet","gentra"])

# import csv
#
# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


# import csv
#
#
# # with open("names.csv" , "x") as f:
# #     data = csv.DictReader(f)
# #     for i in data:
# #         print(i)
# import csv
#
# with open("cars.csv" , 'a') as f:
#     fieldnames = ["id" , "company", 'model', 'name']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     # while True:
#     company = input("Company : ")
#     model = input("Model : ")
#     name = input("Name : ")
#     writer.writerow({"id" : 1, "company": company, "model": model, "name": name})

# json , txt , csv
# import csv
#
# with open("cars.csv" , "r") as f:
#     datas = csv.DictReader(f)
#     for data in datas:
#         print(data)

import csv
class File:
    def __init__(self , filename : str , fieldname: list = None):
        self.filename = filename
        self.fieldname = fieldname

    def read(self):
        with open(self.filename , "r") as f:
            result = []
            datas = csv.DictReader(f)
            for data in datas:
                result.append(data)
            return result

    def write(self, data : dict):

        with open(self.filename, "a") as f:
            writer = csv.DictWriter(f, self.fieldname)
            writer.writerow(data)
    def clear(self):
        with open(self.filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.fieldname)

def main():

    menu = """
    1) read
    2) write
    3) edit
    4) exit
    >>>"""
    key = input(menu)
    match key:
        case "1":
            f = File("users.csv", ["id", "name" , "age" , "phone"])
            for i in f.read():
                print(i)
            main()

        case "2":
            f = File("users.csv", ["id", "name", "age", "phone"])
            user = {"id" : input("Id : "),
            "name" : input("Name : "),
            "age" : input("age : "),
            "phone" : input("phone : ")}
            f.write(user)
            main()
        case "3":
            fields = """
            1) name
            2) age
            3) phone
            >>>"""
            key = input(fields)
            match key:
                case "1":
                    id = input("Id : ")
                    new_val = input("new_value : ")
                    f = File("users.csv" , ["id" , "name" , "age" , "phone"])
                    users = f.read()
                    for i,user in enumerate(users):
                        if user.get("id") == id:
                            users[i]["name"] = new_val
                            break

                    f.clear()
                    for i in users:
                        f.write(i)
                    main()


                case "2":
                    pass
                case "3":
                    pass
main()

"""
books.csv

""" # TODO
