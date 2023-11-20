# class Animal:
#     def speak(self):
#         pass
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof !"
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow !"
#
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
# data = [animal, dog, cat]
# print(animal.speak())
# print(dog.speak())
# print(cat.speak())


# class Shape:
#     def area(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         self.pi = 3.14
#
#     def area(self):
#         return "Area - Circle :", self.pi * (self.radius ** 2)
#
#
# class Square(Shape):
#     def __init__(self, x):
#         self.x = x
#
#     def area(self):
#         return "Area - Square :", self.x * self.x
#
#
# class Triangle(Shape):
#     def __init__(self, base, hight):
#         self.base = base
#         self.hight = hight
#
#     def area(self):
#         return "Area - Triangle :", (self.base * self.hight) // 2
#
#
# circle = Circle(5)
# square = Square(4)
# triangle = Triangle(3, 4)
# data = [circle, square, triangle]
# for i in data:
#     print(*i.area())


# class Crud:
#     def create(self):
#         pass
#
#     def get(self):
#         return self
#
#     def update(self, value):
#         pass
#
#     def delete(self):
#         pass
#
#
# class User(Crud):
#     def __init__(self, fullname: str, age: int):
#         self.fullname = fullname
#         self.age = age
#
#     def create(self):
#         users.append(self)
#         print("Succesfuly created")
#
#     def update(self, new_fullname):
#         index = users.index(self)
#         users[index].fullname = new_fullname
#
#     def delete(self):
#         index = users.index(self)
#         del users[index]
#
#     def __str__(self):
#         return f"{self.fullname} {self.age}"
#
#     def __repr__(self):
#         return f"{self.fullname} {self.age}"
#
#
# users: list[User] = []
#
#
# class Todos:
#     def __init__(self, title: str, time: str):
#         self.title = title
#         self.time = time
#
#     def create(self):
#         todos.append(self)
#         print("Succesfuly created")
#
#     def update(self, new_title):
#         index = todos.index(self)
#         todos[index].title = new_title
#
#     def delete(self):
#         index = todos.index(self)
#         del todos[index]
#
#     def __str__(self):
#         return f"{self.title} {self.time}"
#
#     def __repr__(self):
#         return f"{self.title} {self.time}"
#
#
# todos: list[Todos] = []
# todo1 = Todos("pdp", "13:00")
# todo2 = Todos("pdp", "15:00")
# todo1.create()
# todo2.create()
# print(todos)


#
# user1 = User("Fazliddin", 16)
# user1.create()
# user2 = User("Botir", 14)
# user2.create()
# print(users)
# user2.update("Suxrop")
# print(users)
# user2.delete()
# print(users)
# print(user2.get())


# class Mathoperations:
#     def add(self, a, b):
#         return a + b
#
#     def add(self, a):
#         return a
#
#
# a = Mathoperations()
# print(a.add(5,5))




