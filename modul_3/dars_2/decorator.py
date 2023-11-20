# def plus_one(num: int):
#     return num + 1
#
# add_one = plus_one
# print(add_one(5))


# def plus_one(num: int):
#     def add_one(num:int):
#         return num+1
#     result = add_one(5)
#     return result
#
# print(plus_one(5))


# def plus_one(num: int):
#     return num + 1
#
#
# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)
#
#
# print(function_call(plus_one))


# def hell_function():
#     def say_hi():
#         return "Hi"
#
#     return say_hi
#
#
# hello = hell_function()
# print(hello())


# DECARATOR
# def uppercase_decarator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
#
# def say_hi():
#     return "Hello world !"
# decorate = uppercase_decarator(say_hi)
# print(decorate())
import time
import os

# print(os.cpu_count())


# def uppercase_decarator(function):
#     def wrapper(name:str):
#         name = name.title()
#         func = function(name)
#         # make_uppercase = func.upper()
#         return func
#
#     return wrapper
#
# def time_decorater(function):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = function(*args,**kwargs)
#         print(time.time() - start)
#         return result
#     return wrapper
#
# # @uppercase_decarator
# @time_decorater
# def say_hi(name:str):
#     time.sleep(2)
#     result = "mwncjncfjvehvhfvhrvnnvnfvbvd"
#     return f"Hello {name} !" , result
#
#
# print(say_hi("fazliddin"))

user = {
    "fullname": "Botirjon",
    "age": 25,
    "username": "botir",
    "password": 7818
}


def user_valid(function):
    def wrapper(*ags, **kwargs):
        if not len(kwargs.get("fullname").split())<2:
            raise Exception("Invalid ullname !")


def register(data: dict):
    return "Succesfully save !"
