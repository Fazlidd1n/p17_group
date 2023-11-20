# dict , function


# d = {}

# d.update({"name": "Botirjon"})
# d["name"] = "Botirjon"
# print(d)
# print(d.pop("name"))
# del d["name"]

# print(d)

d = {
    "name": "Botirjon",
    "age": 23
}


# d.update({"name": "Javohir"})

# d["name1"] = d.pop("name")

# print(list(d.items()))
# k , v = ('name', 'Botirjon')
# print(i)
# for k , v in d.items():
#     print(k , v)

# print(*list(d.items())[0])
# a = 1,2,3
#
# def function_name(arg1 , arg2 , arg3):
#     return arg1 , arg2 , arg3
#
# print(function_name(1,2,3))


# def f(a, b = 8,*,c = 9 ):
#     print(a, b, c)
#
#
# f(a=1, c=3)


users = []


# 1 version
# def add(username , password):
#     d = {"username": username, "password": password}
#     user.append(d)
#
#
# while True:
#     username = input("Username: ")
#     password = input("Password: ")
#     add(username , password)
#     print(user)
#     is_cont = input("Yes/no :")
#     if is_cont == "no":
#         break


# 2 version
# def add(**user):
#     users.append(user)
#
#
# while True:
#     username = input("Username: ")
#     password = input("Password: ")
#     add(username=username , password=password)
#     print(users)
#     is_cont = input("Yes/no :")
#     if is_cont == "no":
#         break

# 3 version
# def add(fullname , username , password , age ):
#     users.append(f"{username}:{password}")
#
#
# while True:
#     d = {
#         "fullname" : input("Fullname: "),
#         "username" : input("Username: "),
#         "password2" : input("Password: "),
#         "age" : input("Age: ")
#     }
#     add(**d)
#     print(users)
#     is_cont = input("Yes/no :")
#     if is_cont == "no":
#         break


# def factorial(n):
#     re = 1
#     for i in range(1 , n+1):
#         re *= i
#     return re
#
#
# print(factorial(5))


# # recursive function
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(5))


# recursive function


# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return (recur_fibo(n-1) + recur_fibo(n-2))
#
# nterms = 5
#
# for i in range(nterms):
#    print(recur_fibo(i))

n = 7

l = [0,1]

for _ in range(n-2):
    l.append(sum(l[-2:]))
print(l)












# [0,1,1,2,3,5,8...]