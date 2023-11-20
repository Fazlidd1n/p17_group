# N1
# print("oop prinseplari : class , encapsulatsiya, polimarfizm , obyekt , abstraktsiya , !")

# N2
# # 4
# # 7 97 -58 90
# l = int(input())
# arr = map(int,input().split())
# s=[]
# for i,val in enumerate(arr):
#     if val%2==0:
#         s.append(val)
# print(f"{sum(s)/len(s):.2f}")

# N3
# import json
#
#
# class File:
#     def __init__(self, filename: str):
#         self.filename = filename
#
#     def read(self):
#         with open(self.filename, "r") as f:
#             return json.load(f)
#
#     def write(self, datas: list[dict]):
#         with open(self.filename, "w") as f:
#             json.dump(datas, f, indent=3)
#
#     def clear(self):
#         with open(self.filename, "w") as f:
#             json.dump([], f)
#
#
# user = File("N3.json")
# s = user.read()
# user1 = {"name": "Fazliddin"}
# user2 = {"name": "suxrop"}
# s.append(user1)
# s.append(user2)
#
# user.write(s)
# for i in user.read():
#     print(i)
#
# user.clear()
# print(user.read())


# N4
# import json
#
#
# class File:
#     def __init__(self, filename: str, field: str):
#         self.filename = filename
#         self.field = field
#
#     def read(self):
#         with open(self.filename, "r") as f:
#             for i in json.load(f):
#                 if not i.get(self.field) or i == None:
#                     break
#                 print(i.get(self.field))
#
#
# print("user_id , id , title , completed")
# field = input("field name : ")
# user = File("todos.json", field)
# user.read()
