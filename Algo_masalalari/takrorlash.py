# a, b, h = map(int, input("son kiriting : ").split())
# tmp = 0
# day = 0
# if a > h:
#     print(1)
# if a <= b:
#     print(-1)
# else:
#     while tmp < h:
#         day += 1
#         if tmp + a >= h:
#             break
#         tmp += a - b
#     print(day)

# N31
# x, y = map(float, input().split())
# max_ = max(x, y)
# min_ = min(x, y)
# print(max_, min_)

# N1
# a = int(input())
# print(a ** 3)

# N42
# a, b, c, d = map(float, input().split())
# if a <= b <= c <= d:
#     max_ = max(a, b, c, d)
#     a = max_
#     b = max_
#     c = max_
#     d = max_
#     print(a, b, c, d)
# else:
#     min_ = min(a, b, c, d)
#     a = min_
#     b = min_
#     c = min_
#     d = min_
#     print(a, b, c, d)

# N61
# from math import *
#
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += sin(i) / pow(2, i)
#
# print(f"{s:.2f}")

# N62
# from math import *
#
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     if i % 2 == 1:
#         s += sin(pow(i, i)) / pow(2, i)
#     elif i % 2 == 0:
#         s -= sin(pow(i, i)) / pow(2, i)
#
# print(f"{s:.2f}")

# N63
# from math import *
#
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += pow(-1, i - 1) * 1 / factorial(2 * i - 1)
#
# print(f"{s:.4f}")

# N100
# from math import *
#
# x, y, c, d = map(int, input().split())
#
# S = 0
# for a in range(1, x + 1):
#     S += (a * x + 4) / sqrt(a + log(6, e))
#
# P = 1
# for a in range(1, y + 1):
#     P *= (a * (x ** 2) + 6) / sin(a * x)
#
# SP = 1
# for i in range(1, c + 1):
#     tmp = 1
#     for j in range(1, d + 1):
#         tmp *= (i * j + y * x) / sqrt(pow(j * x + y, i))
#     SP *= tmp
#
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

