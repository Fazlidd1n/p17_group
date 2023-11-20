# simple example
class A:
    a = "A class"


class B(A):
    b = "B class"


obj = B()
print(obj.a)


# example
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

