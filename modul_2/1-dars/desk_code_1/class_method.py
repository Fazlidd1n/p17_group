# class Calculator:
#     def __init__(self, num1, num2: int | str = None):
#         self.num1 = num1
#         self.num2 = num2
#
#     def multiply(self):
#         return self.num1 * self.num2
#
#
# obj = Calculator(num2 = 10, num1 = 2)
# print(obj.num1)
# print(obj.num2)
# print(obj.multiply())


# class Circle:
#     PI = PI
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def yuza(self):
#         return self.PI * self.diametr * (self.radius ** 2)
#
#
# obj = Circle(10)
# obj.diametr = obj.radius * 2
# obj.yuza()
# print(obj.diametr)


class MyList:
    def __init__(self, massiv):
        self.massiv = massiv

    def append(self, item):
        self.massiv = self.massiv + [item]
    def pop(self , index:int = -1):
        return_val = self.massiv[index]
        del self.massiv[index]
        return return_val

    def sort(self, reverse=False):
        self.massiv = sorted(self.massiv , reverse=reverse)

    def __str__(self):
        return f"{self.massiv}"

# o = [1,2,3]
# o.pop()
a = MyList([1,10,20,4])

a.append(5)
a.append(6)
print(a.pop())
print(a.sort(reverse=True))
print(a)
