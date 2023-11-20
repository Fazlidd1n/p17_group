# 1. Arithmetic operators
"""
+ , - , * , ** , % , / , //
"""

print("8 + 7 = ", 8 + 7)
print("8 - 7 = ", 8 - 7)
print("8 * 7 = ", 8 * 7)
print("8 ** 2 = ", 8 ** 2)
print("9 % 2 = ", 9 % 2)
print("9 / 2 = ", 9 / 2)
print("9 // 2 = ", 9 // 2)

# 2. Taqoslash operatorlari
"""
== , <= , >= , < , > , !=
"""
print(1 == 2)
print(1 <= 2)
print(2 >= 2)
print(2 > 2)
print(2 < 2.000000000001)
print(2 != 2.0)

# 3. mantiqiy operatorlar
"""and , or , in , is"""
print(True and True) # True
print(True and False) # False
print(False and False) # False
print(True or False) # True
print(False or False) # False
print(True or True) # True
print("13" in "123") # True
print("1" in [1,2,3]) # True
print([1,2,3] is [1,2,3]) # True

# -----------id------------------------
a = [1,2,3]
print(id(a))
b = a
print(id(b))
print(a is b)

# -----------------------------------------
# 4. Bitwise operators
"""& - and , | - or , >> , <<"""
print(True & False)
print(True | False)
print(10 >> 2)

# print(bin(12))
# print(int("1100", 2))



# 5. Assigning operators
"""
+= , -= , *= , **= , %= , /= , //=
"""



"""
hashable | unhashable
inf         list
float       set
str         dict
tuple
bool
"""

a = "78"
b = 89
c = 8.0
u = [1,2]
u = {1,2}
u = (1,2)
u = {1:2}
print(hash(u))


# ------------------------------------
"""
mutable  |   immutable

list        str     
set         int
dict        float
            tuple
            bool
"""









