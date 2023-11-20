"130"

# n , m = map(int , input().split())
#
# matrix = []
# for i in range(n):
#     l = list(map(int , input().split()))
#     matrix.append(l)
#
# maxx = float("-inf")
# minn = float("inf")
#
# result = []
# for i in matrix:
#     if (a:=max(i)) > maxx:
#         maxx = a
#     if (a:=min(i)) < minn:
#         minn = a
#     result.append(sum(i))
#
# print(*result)
# print(maxx , minn)


"172"
# def fibonacci(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     elif n % 2 == 0:
#         m = n // 2
#         return fibonacci(m)
#     else:
#         m = n // 2
#         return fibonacci(m) + fibonacci(m + 1)
#
# n = int(input())
# result = fibonacci(n)
# print(result)

