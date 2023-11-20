# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix[len(matrix) // 2][len(matrix[0]) // 2])

# print(matrix[0][0])
# print(matrix[1][1])
# print(matrix[2][2])

# ==============================================
# c = 0
# for row in range(len(matrix)):
#     for col in range(len(matrix[0])):
#         if row + col == len(matrix[0]) - 1 or row == col:
#             c += matrix[row][col]
# print(c)

# ==============================================

# ramkadagi sonlar yig'indisi
# c = sum(matrix[0]) + sum(matrix[-1])
# for row in matrix[1:-1]:
#     c += row[0] + row[-1]
# print(c)
#
# print(sum(matrix[0]) + sum(matrix[-1]) + sum([row[0] + row[-1] for row in matrix[1:-1]]))


# 1 4 7
# 2 5 8
# 3 6 9

# for i in range(len(matrix[0])):
#     for j in matrix:
#         print(j[i] , end = " ")
#     print()


# nxm = input
# 2   3
# n , m = list(map(lambda x : int(x),input().split()))

#
# matrix = []
# for i in range(n):
#     inner = ['*'] * m
#     matrix.append(inner)
#
# for i in matrix:
#     print(*i)


# matrix = []
# c = 1
# for i in range(n):
#     inner = []
#     for j in range(m):
#         inner.append(c)
#         c += 1
#     matrix.append(inner)
# print(matrix)
#
# for i in matrix:
#     print(*i)

# https://leetcode.com/problems/number-of-good-pairs/
# nums = [1, 2, 3, 1, 1, 3]
# c = 0
# for i in range(len(nums)):
#     print(i)
#     c += nums[i+1:].count(nums[i])
# print(c)

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# nums = [8,1,2,2,3]
# re = []
# for i in nums:
#     c = 0
#     for j in nums:
#         if i > j:
#             c += 1
#     re.append(c)
# print(re)


# from string import ascii_lowercase
#
# sentence = "thequickbrownfoxjumpsoverthelazydog"
#
# for i in ascii_lowercase:
#     if not i in sentence:
#         return False
#
# return True


# d = {
#
# }
#
# d["a"] = "--__.."
#
# d.update({"a":"--__.."})

from string import ascii_lowercase

belgilar = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
            ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
words = ["gin", "zen", "gig", "msg"]

# d = {}
# for i in range(len(ascii_lowercase)):
#     d[ascii_lowercase[i]] = belgilar[i]
#
# tmp = []
# for i in words:
#     t = ""
#     for j in i:
#         t += d[j]
#     tmp.append(t)
# print(len(set(tmp)))


# mat = [[0,0,0],[0,1,1]]
#
#
# re = [0 , float("-inf")]
# for i , v in enumerate(mat):
#
#     if re[1] < (s:=sum(v)):
#         re[1] = s
#         re[0] = i
# print(re)

# image = [
#     [1, 1, 0, 0],
#     [1, 0, 0, 1],
#     [0, 1, 1, 1],
#     [1, 0, 1, 0]
# ]
#
# for i in range(len(image)):
#     image[i].reverse()
#     for j in range(len(image[0])):
#         if image[i][j] == 0:
#             image[i][j] = 1
#         else:
#             image[i][j] = 0
# print(image)


l = [
    [1,2,3]
]

# del l[0][2]
# print(l)
grid = [
    [1,2],
    [3,4],
    [5,6]
]

print(list(zip(*grid)))



