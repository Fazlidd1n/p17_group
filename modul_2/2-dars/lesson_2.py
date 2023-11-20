class Animal:
    def __init__(self, name, gender, habitat):
        self.name = name
        self.gender = gender
        self.habitat = habitat


class Bird(Animal):
    def __init__(self, name, gender, habitat):
        super().__init__(name, gender, habitat)


class Fish(Animal):
    def __init__(self, name, gender, habitat):
        super().__init__(name, gender, habitat)


class Mammal(Animal):
    def __init__(self, name, gender, habitat):
        super().__init__(name, gender, habitat)
