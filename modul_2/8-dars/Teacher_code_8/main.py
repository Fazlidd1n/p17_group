# 1a = 0
# (p=9
#
# u=10
# python_ = 7


# nums = [1,1,2,2,3]
#
# for i in set(nums):
#     if (c:= nums.count(i)) > 2:
#         for _ in range(c - 2):
#             nums.remove(i)
# return len(nums)

# In-built python Exception


# a = """ArithmeticError
# AssertionError
# AttributeError
# OSError
# BlockingIOError
# ConnectionError
# BrokenPipeError
# BufferError
# ChildProcessError
# ConnectionAbortedError
# ConnectionRefusedError
# ConnectionResetError
# EOFError
# FileExistsError
# FileNotFoundError
# FloatingPointError
# ImportError
# SyntaxError
# IndentationError
# LookupError
# IndexError
# InterruptedError
# IsADirectoryError
# KeyError
# MemoryError
# ModuleNotFoundError
# NameError
# NotADirectoryError
# RuntimeError
# NotImplementedError
# OverflowError
# PermissionError
# ProcessLookupError
# RecursionError
# ReferenceError
# SystemError
# TabError
# TimeoutError
# TypeError
# UnboundLocalError
# ValueError
# UnicodeError
# UnicodeDecodeError
# UnicodeEncodeError
# UnicodeTranslateError
# ZeroDivisionError"""
# try:
#     print(b)
# except Exception as e:
#     print()



# while True:
#     try:
#         fullname = input("Fullname : ")
#         if len(fullname.split()) < 2:
#             raise Exception("Fullname invalid !")
#
#     except Exception as e:
#         print(e)
#     finally:
#         break
    # else:
    #     break



# while True:
#     break
# else:
#     print("Finish while")
# print("hello")



# class MyException(Exception):
#     pass
#
# try:
#     a = 9
#     b = 0
#     if b == 0:
#         raise MyException("MyException")
# except MyException as e:
#     print(e)

# a = 9
# b = 0
#
# try:
#     assert b != 0 , "Assertion failed"
#     print(a / b)
# except AssertionError as e:
#     print(e)



# library

def add_book(id , name , author):
    with open("book.txt" , "a") as f:
        data = f"""{id}|{name}|{author}\n"""
        f.write(data)

def search_book(id):
    with open("book.txt" , "r") as f:
        for i in f.read().split('\n'):
            if  i.split('|')[0] == id :
                return i.split('|')

        else:
            raise Exception("Not Found")


while True:
    try:
        menu = """
    1) add book
    2) search book
    3) stop
    >>>"""
        key = input(menu)
        match key:
            case "1":
                id = input("id:")
                name = input("name:")
                author = input("author:")
                add_book(id, name, author)

            case "2":
                id = input("id:")
                print(search_book(id))
            case "3":
                break
    except Exception as e:
        print(e)












