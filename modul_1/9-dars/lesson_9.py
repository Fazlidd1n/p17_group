# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# ramka yigindisi
# s = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if i == 0 or i == len(matrix[0]) - 1 or j == 0 or j == len(matrix[0]) - 1:
#             s+=matrix[i][j]
# print(s)

# s = sum(matrix[0]) + sum(matrix[-1])
# for i in matrix[1,-1]:
#     s+= i[0]+i[-1]
# print(s)


# for i in range(len(matrix[0])):
#     for j in matrix:
#         print(j[i], end=" ")
#     print()

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     inner = ["*"] * m
#     matrix.append(inner)
#
# for i in matrix:
#     print(*i)

n, m = map(int, input().split())
matrix = []
s = 1
for i in range(n):
    inner = []
    for j in range(m):
        inner.append(s)
        s += 1
    matrix.append(inner)
for i in matrix:
    print(*i)
