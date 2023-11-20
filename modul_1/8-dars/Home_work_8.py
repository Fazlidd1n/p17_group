# N1
# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
# s1 = ""
# s2 = ""
# for i in range(len(word1)):
#     s1 += word1[i]
# for i in range(len(word2)):
#     s2 += word2[i]
# if s1 == s2:
#     print(True)
# else:
#     print(False)

# N2
# s = "Hello how are you Contestant"
# k = 4
# a = s.split()
# s = ""
# for i in a[:k - 1]:
#     s += i + " "
# s += a[k - 1]
# print(s)

# N3
# s = "is2 sentence4 This1 a3"
# a = s.split()
# dic = {}
# for i in a:
#     j = i[-1]
#     dic[j] = i[:-1]
#
# print(" ".join([dic[i] for i in sorted(dic.keys())]))

# N4
# s = "codeleet"
# indices = [4, 5, 6, 7, 0, 2, 1, 3]
# satr = ""
# a = 0
# p = 0
# di = {}
# for i in s:
#     di.update({indices[a]: i})
#     a += 1
# for j in di:
#     satr += di[p]
#     p += 1
# print(satr)

# N5
# nums = [1, 2, 3, 4, 5]
# k = 3
# print((max(nums)) * k + (k - 1) * k // 2)

# N6
# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
# s1 = ""
# s2 = ""
# for i in range(len(word1)):
#     s1 += word1[i]
# for i in range(len(word2)):
#     s2 += word2[i]
# if s1 == s2:
#     print(True)
# else:
#     print(False)

# N7
# operations = ["--X", "X++", "X++"]
# x = 0
# for i in range(len(operations)):
#     if operations[i] == "X++" or operations[i] == "++X":
#         x += 1
#     if operations[i] == "X--" or operations[i] == "--X":
#         x -= 1
# print(x)

# N8
# jewels = "aA"
# stones = "aAAbbbb"
# s = 0
# for i in jewels:
#     for j in stones:
#         if j == i:
#             s += 1
# print(s)

# N9
# command = "G()(al)"
# print(command.replace("()","o").replace("(al)","al"))

# N10
# s = "codeleet"
# indices = [4, 5, 6, 7, 0, 2, 1, 3]
# satr = ""
# a = 0
# p = 0
# di = {}
# for i in s:
#     di.update({indices[a]: i})
#     a += 1
# for j in di:
#     satr += di[p]
#     p += 1
# print(satr)

# N11
# items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
# ruleKey = "color"
# ruleValue = "silver"
# a = 0
# for i in items:
#     if ruleKey == "type":
#         if ruleValue == i[0]:
#             a += 1
#     elif ruleKey == "color":
#         if ruleValue == i[1]:
#             a += 1
#     elif ruleKey == "name":
#         if ruleValue == i[2]:
#             a += 1
# print(a)

# N12
# a = "the quick brown fox jumps over the lazy dog"
# message = "vkbs bs t suepuv"
# key = ""
# for i in a.replace(" ", ""):
#     if not i in key:
#         key += i
# key = key
# alfabit = "abcdefghijklmnopqrstuvwxyz"
# d = {}
# for i in range(len(key)):
#     d[key[i]] = alfabit[i]
# re = ""
# for i in message:
#     if not " " == i:
#         re += d.get(i)
#     else:
#         re += " "
# print(re)

#N13

