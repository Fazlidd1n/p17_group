# N1
from string import ascii_lowercase

#
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# for i in ascii_lowercase:
#     if not i in sentence:
#         print(False)
#         break
# else:
#     print(True)

# N2
# s = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
#      "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
# words = ["gin", "zen", "gig", "msg"]
# d = {}
# for i in range(len(ascii_lowercase)):
#     d[ascii_lowercase[i]] = s[i]
# # print(d)
# tmp = []
# for i in words:
#     t = ""
#     for j in i:
#         t += d[j]
#     tmp.append(t)
# print(len(set(tmp)))

# N3
# mat = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# s = 0
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if i == j or i + j == len(mat[0]) - 1:
#             s += mat[i][j]
# print(s)

# N4
# mat = [[0, 0], [1, 1], [0, 0]]
# re = [0, float("-inf")]
# for i, v in enumerate(mat):
#     if re[1] < (s := sum(v)):
#         re[1] = s
#         re[0] = i
# print(re)

# N5
# image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
# for i in range(len(image)):
#     image[i].reverse()
#     for j in range(len(image[i])):
#         if image[i][j] == 0:
#             image[i][j] = 1
#         else:
#             image[i][j] = 0
# print(image)


