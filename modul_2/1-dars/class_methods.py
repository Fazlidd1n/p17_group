# class Calculator:
#     def __init__(self, num1: int, num2: int):
#         self.num1 = num1
#         self.num2 = num2
#
#     def multiply(self):
#         return self.num1 * self.num2
#
#     def devision(self):
#         return self.num1 // self.num2
#
#     def plus(self):
#         return self.num1 + self.num2
#
#     def minus(self):
#         return self.num1 - self.num2
#
#
# obj = Calculator(10, 20)
# print(obj.multiply())
# print(obj.devision())
# print(obj.plus())
# print(obj.minus())


# from math import pi as PI
#
# class Circle:
#     PI = PI
#     def __init__(self, radius):
#         self.radius = radius
#         self.diometr = radius * 2
#     def yuza(self):
#         return self.PI * (self.radius **2)
#
#
# obj = Circle(10)
# print(obj.yuza())
# print(obj.diometr)


class Mylist:
    def __init__(self, massiv):
        self.massiv = massiv

    def append(self, item):
        self.massiv = self.massiv + [item]

    def remove(self, item):
        return [i for i in self.massiv if i != item]

    def pop(self, index: int = -1):
        return_val = self.massiv[index]
        del self.massiv[index]
        return return_val
    

    def __str__(self):
        return f"{self.massiv}"


a = Mylist([1, 2, 3, 4])
print(a.pop(1))
