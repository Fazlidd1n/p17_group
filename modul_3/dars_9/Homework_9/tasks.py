# DTO_tasks
# N1
# from collections import namedtuple
# users = namedtuple("users", ('user_id', 'first_name', 'last_name', 'address', 'email'))
# orders = namedtuple("orders", ('order_id', 'user', 'product_ordered', 'total_paid'))
# products = namedtuple("products", ('product_id', 'product_name', 'description', 'price'))

# N2
# orders = namedtuple("orders", ('order_id', 'order_date', 'customer_id'))
# customers = namedtuple("customers", ('customer_id', 'customer_phone', 'customer_email'))
# orders_items = namedtuple("orders_items", ('order_id', 'item_date'))
# items = namedtuple("items", ('item_id', 'item_name', 'item_price'))


# Enum_tasks
from enum import Enum


# N1
# class DayOfWeek(Enum):
#     MONDAY = '1'
#     TUESDAY = '2'
#     WEDNESDAY = '3'
#     THURSDAY = '4'
#     FRIDAY = '5'
#     SATURDAY = '6'
#     SUNDAY = '7'
#
# days = """
# 1) Monday
# 2) Tuesday
# 3) Wednesday
# 4) Thursday
# 5) Friday
# 6) Saturday
# 7) Sunday
# >>> """
# key = input(days)
# print(DayOfWeek(key).name)

# N2
# class Color(Enum):
#     RED = '1'
#     BlUE = '2'
#     YELLOW = '3'
#
# colors = """
# 1) red
# 2) blue
# 3) yellow
# >>> """
# key = input(colors)
# print(Color(key).value)

# N3
# class PizzaSizes(Enum):
#     LARGE = "Large - 12-slices , price - 8$"
#     MEDIUM = "Medium - 8-slices , price - 5$"
#     SMALL = "Small - 6-slices , price - 3$"
#
# pizzas = """
# LARGE
# MEDIUM
# SMALL
# >>> """
# key = input(pizzas)
# print(PizzaSizes[key].value)

# N4
# class HTTP_STATUS(Enum):
#     CONTINUE = "100"
#     SWITCHING_PROTOCOLS = "101"
#     OK = "200"
#     CREATED = "201"
#     ACCEPTED = "202"
#     NO_CONTENT = "204"
#     MOVED_PERMANENTLY = "301"
#     FOUND = "302"
#     SEE_OTHER = "303"
#     NOT_MODIIED = "304"
#     TEMPORARY_REDIRECT = "307"
#     BAD_REQUST = "400"
#     UNAUTHORIZED = "401"
#     FORIDDEN = "403"
#     NOT_FOUND = "404"
#     NOT_ACCEPTABLE = "406"
#     GONE = "410"
#     TOO_MANY_REQUESTS = "429"
#     INTERNAL_SERVER_ERROR  = "500"
#     BAD_GATEWAY = "502"
#     SERVICE_UNAVALABLE = "503"
#     GATEWAY_TIMEOUT = "504"
#
# http_status = """
# Informational (1xx):
#     100) Davom eting
#     101) Protokollarni o'zgartirish
# Successful (2xx):
#     200) Yaxshi
#     201) Yaratildi
#     202) Qabul qilindi
#     204) Tarkib yo'q
# Redirection (3xx):
#     301) O'zgarmas ko'chirildi
#     302) Topildi
#     303) Boshqa joyga o'ting
#     304) O'zgartirilmagan
#     307) Vaqtinchalik yo'nlash
# Client Errors (4xx):
#     400) Yomon so'rov
#     401) Ruxsat yo'q
#     403) Munoqash etilgan
#     404) Topilmadi
#     406) Qabul qilinmadi
#     410) Yo'q
#     429) Juda ko'p so'rov
# Server Errors (5xx):
#     500) Ichki server xatosi
#     503) Xizmat mavjud emas
#     504) G'aytnoma vaqt tugadi
# >>> """
#
# key = input(http_status)
# print(HTTP_STATUS(key).name)

# N5
# class Gender(Enum):
#     MALE = "1"
#     WOMAN = "2"
#
# gender = """
# 1) MALE
# 2) WOMAN
# >>"""
# key = input(gender)
# print(Gender(key).name)

# N6
# class FileType(Enum):
#     TEXT_FILE = '1'
#     CSV_FILE = '2'
#     JSON_FILE = '3'
#     SQLITE = '4'
#
#
# files = """
# 1) datas.txt
# 2) users.csv
# 3) user_datas.json
# 4) all_datas.sqlite
# >>> """
# key = input(files)
# print(FileType(key).name)

# N7
# class Languages(Enum):
#     ENGLISH = "1"
#     RUSSIAN = "2"
#     UZBEK = "3"
#
#
# languages = """
# 1) Eng
# 2) Ru
# 3) Uz
# >>> """
# key = input(languages)
# print(Languages(key).name)

# N8
# class MusicGenre(Enum):
#     ROCK = '1'
#     POP = '2'
#     HIP_HOP = '3'
#     JAZZ = '4'
#     CLASSIC = '5'
#
# genres = """
# 1) Rock
# 2) Pop
# 3) Hip Hop
# 4) Jazz
# 5) Classic
# >>> """
# key = input(genres)
# print(MusicGenre(key).name)

