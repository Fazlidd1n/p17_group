n = int(input("n = "))
m = int(input("m = "))
mat = []

for i in range(n):
    mat.append(["*"] * m)

# for i in mat:
#     print(*i)

# l = list(range(1, n * m + 1))
# for i in range(m):
#     mat.append(l[i*m:i*m+m])
# for i in range(0,mat):
#     mat[i] = list(zip(*mat[i]))


# s = 1
# for i in range(n):
#     l = []
#     for j in range(m):
#         l.append(s)
#         s += 1
#     mat.append(l)

# for i in mat:
#     print(i)

# T
# print(*mat[0])
# for i in mat[1:]:
#     print("  " * (m // 2) + "*")
#
# print()
#
# # I
# print(*mat[0])
# for i in mat[1:-1]:
#     print("  " * (m // 2) + "*")
# print(*mat[-1])
#
# print()
#
# # H
# for i in range(n):
#     for j in range(m):
#         if j == 0 or j == m-1 - 1 or i == n // 2:
#             print(mat[i][j] , end=" ")
#         else:
#             print("  ", end=" ")
#     print()

# L
# for i in mat[1:]:
#     print("*")
# print(*mat[-1])

# E
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if j == 0 or i == 0 or i == len(mat) - 1 or i == len(mat) // 2:
#             print(mat[i][j], end=" ")
#     print()

# Z
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if i == 0 or i == len(mat) - 1 or i + j == len(mat[0]) - 1:
#             print(mat[i][j], end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# N
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if j == 0 or j == len(mat) - 1 or i == j:
#             print(mat[i][j], end=" ")
#         else:
#             print(" ", end=" ")
#     print()
