# N1
# a: str = input("matn kiriting : ")
# s: int = 0
# for i in a:
#     if i.isalpha():
#         s += 1
# print(s)

# N2
# a: str = input("matn kiriting : ")
# s: int = 0
# for i in a:
#     if i.isdecimal():
#         s += int(i)
# print(s)

# N3
# a: str = input("matn kiriting : ")
# s: int = 0
# print(sum([True if i.isupper() else False for i in a]))
# for i in a:
#     i=ord(i)
#     if i>=65 and i<=90:
#         s+=1
# for i in a:
#     if i.isupper():
#         s += 1
# print(s)

# a = (True, 1, 2, 3, "Botirjon", "Kamol", "Botirjon", 1, 2, 3)
# start = len(a) - 1
# while start >= 0:
#     if a[start] == "Botirjon":
#         print(start)
#         break
#     start -= 1
# print([i for i , v in enumerate(a) if v=="Botirjon"][-1])

# a: str = "abcddeffgtt"
# print(len(set(a)))

