class Animal:
    def __init__(self, name, gender, habitat):
        self.name = name
        self.gender = gender
        self.habitat = habitat
    def printinfo(self):
        return self.name , self.gender , self.habitat


class Bird(Animal):
    def __init__(self, name , gender , habitat , is_fly : bool = True):
        super().__init__(name, gender, habitat)
        self.is_fly = is_fly


class Fish(Animal):
    def __init__(self, name , gender , habitat , ):
        Animal.__init__(self , name, gender, habitat)


class Mammal(Animal):
    def __init__(self, name , gender , habitat):
        super().__init__(name, gender, habitat)

bird1 = Bird("Burgut" , "M" , "Mount", is_fly="f")
fish = Fish("akula" , "M" , "ocean")
print(bird1.printinfo())
print(fish.habitat)










