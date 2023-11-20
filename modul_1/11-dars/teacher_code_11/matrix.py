# termin -> col , row , list , dioganal , size

matrix = []



n , m = map(int , input().split())
for i in range(n):
    matrix.append(["*"]*m)

print("==================T====================")
print(*matrix[0])
for i in matrix[1:]:
    print("  "*(m//2) + "*")

print("==================H=====================")


for i , v in enumerate(matrix):
    if i == n // 2:
        print(*v)
    else:
        print(v[0] + "  "*(m-2)+ " " + v[-1])







# H
# L
# E
# Z
# N


# * * * * *
#     *
#     *
#     *
#     *



