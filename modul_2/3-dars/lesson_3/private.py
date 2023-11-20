class A:
    def __init__(self , a, b):
        self.a = a
        self.__b = b

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self , v):
        self.__b = v

obj = A(2, 8)
print(obj.b)
obj.b = 20
print(obj.b)

