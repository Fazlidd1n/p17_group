# user = {
#     "fulname" : "Fazliddin Ismoilov",
#     "age" : 16,
#     "phone number" : "+998950107818",
#     "email" : "fazliddinismoilov234@gmail.com",
#     "city" : "Tashkent",
#     "birthday" : "2007-02-20"
# }
# user.keys()
# user.values()
# user.items()
# for k , v in user.items():
#     print(k , ":" , v)

# N1
# nums = {
#     2 : 10,
#     19 : 20,
#     31 : 30,
#     38 : 40,
#     58 : 50,
#     48 : 60
# }
# for k , v in nums.items():
#     if k > v:
#         print(f"{k} > {v}")
#     elif k < v:
#         print(f"{k} < {v}")
#     else:
#         print(f"{k} = {v}")

# N2
# users = []
# user = {
#     "fullname" : "",
#     "age" : 0,
# }
# for i in range(5):
#     user["fullname"] = input("fullname : ")
#     user["age"] = int(input("age : "))
#     users.append(user)
# print(users)

# N3
# nums = {
#     2 : 10,
#     19 : 20,
#     31 : 30,
#     38 : 40,
#     58 : 50,
#     48 : 60
# }
# print(sum(list(nums.values())[1::2]))

# N4
# def remove(map:dict,key:str|int|float):
#     del map[key]
#     return map
# d = {
#     "age" : 23,
#     "phone_number" : 19993992
# }
# print(remove(d,"age"))


# Input: jewels = "aA", stones = "aAAbbbb"
#        Output: 3

# jewels:str = "aA"
# stones:str = "aAAbbb"
# d = {}
# for i in stones:
#     if i in jewels:
#         d[i]=d.get(i,0)+1
# print(sum(d.values()))


# nums = [1,2,3,1,1,3]
# d = {}
# s=0
# for i in range(len(nums)):
#     s += nums[i+1:].count(nums[i])
# print(s)



