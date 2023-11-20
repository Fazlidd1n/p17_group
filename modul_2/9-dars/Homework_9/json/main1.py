import json


class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def write(self, data: list[dict]):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=3)

    def clear(self):
        with open(self.filename, "w") as f:
            json.dump([], f)


def main():
    menu = """
    1) read
    2) write
    3) clear
    4) exit
    >>>"""
    key = input(menu)
    match key:
        case "1":
            f = File("films.json")
            for i in f.read():
                print(i)
            main()
        case "2":
            f = File("films.json")
            data = {
                "name": input("nomi : "),
                "category": input("janri : ")
            }
            all_data = f.read()
            all_data.append(data)
            f.write(all_data)
            main()
        case "3":
            f = File("films.json")
            f.clear()
            main()
        case "4":
            return


main()

# f = File("films.json")
# f.write({"name": "Forsaj7"})
# print(f.read())
