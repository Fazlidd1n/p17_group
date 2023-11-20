# import pandas as pd
# file = 'Book2_unit10.xlsx'
# s = pd.read_excel(file)
# print(s)
# data = dict()
# for i in s.items():
#     data[i[0]] = i[1]
# print(data)
# import openpyxl


# ENUM
# from enum import Enum

# class Season(Enum):
#     Spring = 0
#     Summer = 1
#     Autumn = 2
#     Winter = 3
#
# # for i in Season:
# #     print(i.value)
#
# print(Season(0).name)

## task
# class Gender(Enum):
#     MAN = "1"
#     WOMAN = "2"
#
#
# while True:
#     menu = """
# 1) Man
# 2) Woman
# 3) Exit
# >>> """
#     key = input(menu)
#     if key == "3":
#         break
#     print(Gender(key).name)


# DTO

# class User:
#     def __init__(self,id,username,password):
#         self.id = id
#         self.username = username
#         self.password = password

# from collections import namedtuple

#
# UserDto = namedtuple('UserDto',('id','username','password'))
# user = UserDto(1,"botirjon","1234")
# print(user)

# task
# Customers = namedtuple('Customers', ('customersID', 'firstname', 'lastname', 'birthDate', 'moneySpent', 'anniversary'))
# Employees = namedtuple('Employees', ('employeeID', 'firstname', 'lastname', 'birthDate'))
# Products = namedtuple('Products', ('productID', 'category', 'price'))
# Orders = namedtuple('Orders', ('orderID', 'customerID', 'employeeId', 'productID', 'orderTotal', 'orderDate'))


# UserList
from collections import UserString


class MyString(UserString):
    def add(self, s):
        self.data += s
    def upper(self):
        self.data = self.data.upper()

# a = MyString("1")
# print(id(a))
# a.add("2")
# print(id(a))
# print(a)


a = MyString("qondayey !")
a.upper()
print(a)