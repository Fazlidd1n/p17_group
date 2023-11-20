# from collections import UserString
#
#
# # Creating a Mutable String
# class Mystring(UserString):
#
#     # Function to append to
#     # string
#     def append(self, s):
#         self.data += s
#
#     # Function to remove from
#     # string
#     def remove(self, s):
#         self.data = self.data.replace(s, "")
#
#     def upper(self):
#         self.data = self.data.upper()
#
#
# s1 = Mystring("Geeks")
# print("Original String:", s1.data)
# print(id(s1))
# s1.upper()
# print("String After Appending:", s1.data)
# print(id(s1))
#
# s1.remove("E")
# print("String after Removing:", s1.data)
# print(id(s1))

from collections import UserString , UserList
# a = "1"
# print(id(a))
# a += "2"
# print(id(a))
# print(a)


# class MyString(UserString):
#     def __iadd__(self, other):
#         print("nimadir")
#         self.data += other
#     def append(self, s):
#         self.data += s
#
#     def upper(self):
#         self.data = self.data.upper()
#
# a  = MyString("ab")
# print(id(a))
# a.upper()
# print(id(a))
# print(a)


# class MyList(UserList):
#     def to_str(self):
#         self.data = list(map(str , self.data))



# mylist = MyList([1,2,3,45])
# print(mylist, id(mylist))
# mylist.to_str()
# print(mylist , id(mylist))
