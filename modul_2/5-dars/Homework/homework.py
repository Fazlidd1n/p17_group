# N1
# with open("homework.txt","a") as file:
#     a = int(input("son : "))
#     [file.write(f"{i}\n") for i in range(1, a + 1)]

# N2
# with open("homework.txt","a") as file:
#     a = int(input("son : "))
#     [file.write(f"{i}\n") for i in range(2, a + 1,2)]

# N3
# with open("homework.txt", "a") as file:
#     a = int(input("son : "))
#     s = 1
#     for i in range(a):
#         for j in range(1, a):
#             if j == i and s <= a:
#                 file.write(f"{s} ")
#                 s += 2
#             else:
#                 file.write(f"  ")
#         file.write(f"\n")

# a = int(input("son : "))
# with open("homework.txt", "a") as file:
#     for i in range(1, a + 1, 2):
#         file.write(" "*i + f"{i}\n")

# N4
# with open("homework.txt", "r") as file:
#     a = [int(i) for i in file.read().split()]
#
# c = 0
# result = ""
# for i in a:
#     c += i
#     result += f"{c} "
# print(result)
# with open("homework.txt", "w") as file:
#     file.write(result)


# class File:
#     def __init__(self, filename: str = None) -> None:
#         self.filename = filename
#
#     def read(self):
#         with open(self.filename, "r") as f:
#             return f.read()
#
#     def write(self, data):
#         with open(self.filename, "a") as f:
#             f.write(f"{data}")
#
#     def update(self, data):
#         with open(self.filename, "w") as f:
#             f.write(f"{data}")
#
#     def clear(self):
#         with open(self.filename, "w") as f:
#             f.write("")
#
#
# file = File("homework.txt")
# print(file.read())
# file.write(" Fazliddin ")
# print(file.read())
# file.update("1 2 3 4")
# print(file.read())
# file.clear()
# print(file.read())






