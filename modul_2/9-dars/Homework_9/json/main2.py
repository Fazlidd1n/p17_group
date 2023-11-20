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
    1) add
    2) delete
    3) actors_list
    4) clear
    5) exit
    >>>"""
    key = input(menu)
    match key:
        case "1":
            f = File("actors.json")
            actor = {
                "name": input("Ismi: "),
                "age": input("Yoshi: "),
                "popular_movie": input("Mashxur kinosi: ")
            }
            data = f.read()
            data.append(actor)
            f.write(data)
            print("Succesfully add !")
            main()
        case "2":
            f = File("actors.json")
            for i, v in enumerate(f.read()):
                print(f"{i} {v}")
            s = int(input("index : "))
            data = list(f.read())
            data.remove(data[s])
            f.write(data)
            print("Succesfully delete !")
            main()
        case "3":
            f = File("actors.json")
            for i in f.read():
                print(i)
            main()

        case "4":
            f = File("actors.json")
            f.clear()
            print("Succesfully clear !")
            main()
        case "5":
            return


main()
