# massiv = ["1", "10", "190", "300000"]
# target = 5
#
# re = []
#
# for i in massiv:
#     re.append("0"*(target-len(i)) + i)
# print(re)


# massiv = input().split()
# print(massiv)

# 1. Dictionary functions, methods

# d = {
#     1 : "value1",
#     1.0 : "value2",
#     (1,0,1) : "value3",
#     True : "value4",
#     "True" : "value5",
# }
#
# print(d)

# user = {
#     "fullname" : "Botirjon Qodirov",
#     "age" : 23,
#     "phone_number" : "+998993456789",
#     "email" : "botirjon@gmail.com",
#     "city" : "London",
#     "birthday" : "2000-01-01"
# }
# print(user["wqert"])
# print(user.get("age", -1))

# user = {
#     "fullname" : "Botirjon Qodirov",
#     "age" : 23,
#     "phone_number" : "+998993456789",
#     "email" : "botirjon@gmail.com",
#     "city" : "London",
#     "birthday" : "2000-01-01"
# }
# user.keys()
# user.values()
# user.items()
#
# for k , v in user.items():
#     print(k ,":", v)


# nums = {
#     2 : 10,
#     20 : 20,
#     31 : 30,
#     38 : 40,
#     58 : 50,
#     48 : 60
# }

# print(sum(list(nums.values())[1::2]))

# for k , v in nums.items():
#     if k > v:
#         print(f"{k} > {v}")
#     elif k < v:
#         print(f"{k} < {v}")
#     else:
#         print(f"{k} = {v}")


"""
output:
    2 < 10
    19 < 20
    31 > 30
    .
    .
    .
    48 < 60
"""
# users = []
# user = {}
#
# for _ in range(2):
#     fullname = input("Fullname: ")
#     age = input("age: ")
#     user["fullname"] = fullname
#     user["age"] = age
#     users.append(user)


# print(users[1].get("fullname"))
# print(users[1].get("fullname" , -1))


# user["email"] = input("birthday")
# print(user)


# a = [0,1,2,3,4]
# a[1]


# user = {
#     "fullname" : "Botirjon Qodirov",
#     "age" : 23,
#     "phone_number" : "+998993456789",
#     "email" : "botirjon@gmail.com",
#     "city" : "London",
#     "birthday" : "2000-01-01"
# }

# print(len(user))

"""
items
values
keys
get
"""

# d = {
#     "age": 23, "phone_number": 998993583235
# }
# pop
# d.pop("age")
# print(d)

# update
# d = {
#     "age": 23, "phone_number": 998993583235
# }
# c = {"age":2 , 2:3}
# d.update(c)
# print(d)



# popitem
# print(d.popitem())
# print(d.popitem())
# print(d)

# clear
# d.clear()
# print(d)

# copy
# a = d.copy()
# a["fullname"] = "botir"
# print(d)

# setdefault
# print(d.setdefault("sdaf" , 0))
# print(d)


# a  = "saddgfhgwert"
# d = {}.fromkeys(a , 0)
#
# for i in a:
#     d[i] += 1
# print(d)
# re = {}
# for i in a:
#     c = a.count(i)
#     re[i] = c
# print(re)

# u = {}
# for i in a:
#     u[i] = u.get(i , 0)
# print(u)








# fromkeys
# d = {
#     "age": 23, "phone_number": 998993583235
# }

# print(d.fromkeys((1, 2, 3, 5) , 0))




# iterable -> for bilan aylanib buladigan hamma type ga aytiladi

# remove
d = {
    "age": 23, "phone_number": 998993583235
}

# def remove(map: dict , key:int | str | float):
#     del map[key]
#     return map
#
# # del d[key]
# print(remove(d, "age"))


# d = dict([("fullname", "botirjon"), ("age" , 23)])











