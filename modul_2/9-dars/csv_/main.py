import csv


class File:
    def __init__(self, filename: str, fieldname: list = None):
        self.filename = filename
        self.fieldname = fieldname

    def read(self):
        with open(self.filename, "r") as f:
            result = []
            datas = csv.DictReader(f)
            for data in datas:
                result.append(data)
            return result

    def write(self, data: dict):
        if not self.read():
            with open(self.filename, "a") as f:
                writer = csv.DictWriter(f, self.fieldname)
                writer.writeheader()
                writer.writerow(data)
        else:
            with open(self.filename, "a") as f:
                writer = csv.DictWriter(f, self.fieldname)
                writer.writerow(data)

    def clear(self):
        with open(self.filename,"w") as f:
            writer = csv.writer(f)
            writer.writerow("")


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
            f = File("users.csv", ["id", "name", "age", "phone_number"])
            for i in f.read():
                print(i)
            main()
        case "2":
            f = File("users.csv", ["id", "name", "age", "phone_number"])
            data = {
                "id": input("Id: "),
                "name": input("Name: "),
                "age": input("Age: "),
                "phone_number": input("Phone Number: ")
            }
            f.write(data)
            main()
        case "3":
            return



main()
