import json


class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def write(self, data):
        with open("car.json", "w") as f:
            json.dump(data, f, indent=3)



def main():
    menu = """
    1) read
    2) write
    3) exit
    >>>"""
    key = input(menu)
    match key:
        case "1":
            f = File("car.json")
            for i in f.read():
                print(i)
            main()

        case "2":
            f = File("car.json")
            data = {
                "name": input("name: "),
                "price": input("price: ")
            }
            f.write(data)
            main()

main()