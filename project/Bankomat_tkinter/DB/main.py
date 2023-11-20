import json


class File:
    def __init__(self, filename: str = None):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def write(self, datas: list[dict]):
        with open(self.filename, "w") as f:
            json.dump(datas, f, indent=3)
