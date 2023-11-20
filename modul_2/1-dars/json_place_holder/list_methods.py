class List:
    def __init__(self, massiv):
        self.massiv = massiv

    def append(self, item):
        self.massiv = self.massiv + [item]

    def clear(self):
        self.massiv = []

    def count(self, item):
        return sum([True for i in self.massiv if i == item])

    def extend(self, item):
        self.massiv = self.massiv + item

    def index(self, item):
        # return [i for i in range(len(self.massiv)) if self.massiv[i] == item]
        for i in range(len(self.massiv)):
            if self.massiv[i] == item:
                return i

    def pop(self, index: int = -1):
        return_val = self.massiv[index]
        del self.massiv[index]
        return return_val

    def remove(self, item):
        self.massiv = [i for i in self.massiv if i != item]

    def reverse(self):
        self.massiv = self.massiv[::-1]

    def sort(self, reverse=False):
        self.massiv = sorted(self.massiv, reverse=reverse)

    def __str__(self):
        return f"{self.massiv}"


a = List([1, 2, 3, 3, 4])
