class A:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b

    @a.setter
    def a(self , v):
        self._a = v



obj = A(2 , 5)

print(obj.a)
obj.a = 10
print(obj.a)





