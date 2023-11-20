# N1
# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
# if "".join(word1) == "".join(word2):
#     print(True)
# else:
#     print(False)

# N2
# a = "Hello"
# b = "Hello Python !!!"
# s1 = 0
# s2=0
# for i in range(len(b) - len(a)):
#     x = b[i:i + len(a)]
#     if x == a:
#         s1 = i
#         s2 = i + len(a)
#
# b[s1:s2]=a[::-1]
#
# print(b)

# N3
nums = input("nums :").split()
target = int(input("target = "))
s = []
for i in range(len(nums) - 1):
    if int(nums[i]) + int(nums[i + 1]) == target:
        s.append(i)
        s.append(i + 1)
        break
print(s)

# N4
# names = ["Mary", "John", "Emma"]
# heights = [180, 165, 170]
# s = []
# s2 = []
# for i in range(len(names)):
#     s.append([names[i], heights[i]])
# s = sorted(s, key=lambda x: x[-1], reverse=True)
# for i in s:
#     s2.append(i[0])
# print(s2)

# N5
# mat = []
# n, m = map(int, input("massiv uzunligi = ").split())
# s = 1
# for i in range(n):
#     l = []
#     for i in range(m):
#         l.append(s)
#         s += 1
#     mat.append(l)
# matrix = []
# for i in list(zip(*mat)):
#     matrix.append(i)
# for i in matrix:
#     print(*i)
