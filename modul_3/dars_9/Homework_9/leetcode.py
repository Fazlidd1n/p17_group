# N1 - matrix

# grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
# print(sum([True for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] < 0]))

# mat = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 1, 1]
# ]
# k = 3
# print(sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k])

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# l = [10,9]
# print(*[matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))
#        if min(matrix[i]) == matrix[i][j] and max(l) < matrix[i][j] and max(l) < matrix[i][j]])

s = [0]
l = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if min(matrix[i]) == matrix[i][j] and max(s) < matrix[i][j]:
            l.append(matrix[i][j])
    s.append(max(matrix[i]))
print(l[-1])
