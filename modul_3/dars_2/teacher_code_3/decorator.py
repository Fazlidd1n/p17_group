# import calendar

# print(calendar.month(2023, 9))
# print(calendar.calendar(2024))

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
# import time
# import os
#
# print(os.cpu_count())
#
# def uppercase_decarator(function):
#     def wrapper(name):
#         name = name.title()
#         func = function(name)
#         return func
#     return wrapper
#
#
# def time_decorator(function):
#     def wrapper(*args , **kwargs):
#         start = time.time()
#         result = function(*args, **kwargs)
#         print(time.time() - start)
#         return result
#     return wrapper
#
#
# @time_decorator
# def say_hi(name):
#     # time.sleep(5)
#     return f"Hello {name}"
#
# @time_decorator
# def send_message():
#     time.sleep(3)
#     return "nimadir"

# print(say_hi(name = "botirjon"))
# print(send_message())

from datetime_ import user_valid
user = {
    "fullname": "Botirjon Qodirov",
    "age": 15,
    "username": "botir",
    "password": "12345"
}

@user_valid
def register(data: dict):
    return "Success save!"

try:
    print(register(user))
except Exception as e:
    print(e)
