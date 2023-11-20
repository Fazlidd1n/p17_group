#N1
# nums = list(input("4 xonali son kiriting :"))
# nums = sorted(nums)
# a = int(nums[0]+nums[-1])
# b = int(nums[1]+nums[-2])
# print(a+b)]

#N2
# user_names = {
#                 1: "Alisher" ,
#                 2: "Kamol" ,
#                 3: "Botirjon",
#                 4: "Hamidillo",
#                 5: "John"
#             }
# s = list(sorted(user_names.values()))
# for i in range(len(s)):
#     user_names[i+1]=s[i]
# print(user_names)

#N3
# s = "is2 This1 sentence4 a3"
# arr = s.split()
# dic = {}
# for i in arr:
#     j = int(i[-1])
#     dic[j] = i[:-1]
# print(" ".join([dic[i] for i in sorted(dic.keys())]))

#N4
# s = "2is 4sentence 1This 3a"
# arr = s.split()
# dic = {}
# for i in arr:
#     j = int(i[0])
#     dic[j] = i[1:]
# print(" ".join([dic[i] for i in sorted(dic.keys())]))

#N5
# number: str = input("phone number : ")
# dic = {
#     90: "Beeline",
#     91: "Beeline",
#     99: "Uzmobile",
#     95: "Uzmobile",
#     97: "MobiUz",
#     88: "MobiUz",
#     94: "Usell",
#     93: "Usell",
#     99890: "Beeline",
#     99891: "Beeline",
#     99899: "Uzmobile",
#     99895: "Uzmobile",
#     99897: "MobiUz",
#     99888: "MobiUz",
#     99894: "Usell",
#     99893: "Usell"
# }
# if len(number) == 9:
#     s: str = int(number[:2])
#     for k, v in dic.items():
#         if k == s:
#             print(v)
# elif len(number) == 12:
#     s: str = int(number[:5])
#     for k, v in dic.items():
#         if k == s:
#             print(v)
# else :
#     print("Bunday kompaniya yoq !")

# input : "2000-1-12"
# output : "2000-01-12"
#N6
date: str = input("Yil-oy-kun : ")
year: str = date[:len(date)-6]
month: str = date[len(date)-5:len(date)-3]
day: str = date[len(date)-2:]
print(year, month, day)


