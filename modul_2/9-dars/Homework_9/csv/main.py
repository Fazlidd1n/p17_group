import csv
import json


class File:
    def __init__(self, filename, fieldname):
        self.filename = filename
        self.fieldname = fieldname

    def read(self):
        with open(self.filename, "r") as f:
            data = csv.DictReader(f)
            result = []
            for i in data:
                result.append(i)
            return result

    def write(self, data: dict):
        with open(self.filename, "a") as f:
            writer = csv.DictWriter(f, self.fieldname)
            writer.writerow(data)

    def clear(self):
        with open(self.filename, "w") as f:
            writer = csv.DictWriter(f,self.fieldname)
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
            f = File("books.csv", ["id", "name", "author"])
            for i in f.read():
                print(i)
            main()
        case "2":
            f = File("books.csv", ["id", "name", "author"])
            book = {
                "id": input("id : "),
                "name": input("name : "),
                "author": input("author : ")
            }
            f.write(book)
            main()
        case "3":
            f = File("books.csv", ["id", "name", "author"])
            field = """
            1) name
            2) author
            >>>"""
            key = input(field)
            match key:
                case "1":
                    id = input("id : ")
                    new_val = input("name : ")
                    books = f.read()
                    for i, book in enumerate(books):
                        if book.get("id") == id:
                            books[i]["name"] = new_val
                            break
                    f.clear()
                    for i in books:
                        f.write(i)
                    main()
                case "2":
                    id = input("id : ")
                    new_val = input("author : ")
                    books = f.read()
                    for i, book in enumerate(books):
                        if book.get("id") == id:
                            books[i]["author"] = new_val
                            break
                    f.clear()
                    for i in books:
                        f.write(i)
                    main()
        case "4":
            return

main()