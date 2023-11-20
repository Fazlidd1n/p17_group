# N1
# a = int(input())
# print(a ** 3)

# N2
# from math import *
#
# r1, r2, r3 = map(int, input().split())
# s1 = pi * pow(r1, 2)
# s2 = pi * pow(r2, 2)
# s3 = pi * pow(r3, 2)
# print(f"{s1:.2f} {s2:.2f} {s3:.2f}")

# N3
# s, h = map(int, input().split())
# c = 2 * s / h
# print(f"{c:.2f}")

# N4
# from math import *
# r = int(input())
# s = 4*pi * pow(r, 2)
# print(f"{s:.2f}")

# N5
# a, b, c = map(int, input().split())
# p = (a + b + c) / 2
# print(f"{p:.2f}")

# N7
# from math import *
# h, r = map(int,input().split())
# v = (pi * pow(r,2) * h)/3
# print(f"{v:.2f}")

# N8
# v, s = map(int, input().split())
# t = s / v
# print(f"{t:.2f}")

# N9
# from math import *
#
# h = int(input())
# g = 9.8
# T = sqrt(2 * h / g)
# print(f"{T:.2f}")

# N10
# x = int(input())
# x = (x*365*24*60*60)//1000
# print(x)

# N11
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += i
# print(s)

# N12
# m = int(input())
# g = 9.8
# P = m * g
# print(f"{P:.2f}")

# N13
# m, a = map(int, input().split())
# p = m * a
# print(p)

# N14
# u, r = map(int,input().split())
# print(f"{u/r:.3f}")

# N15
# r1, r2, r3 = map(int, input().split())
# p = 1 / r1 + 1 / r2 + 1 / r3
# q = 1 / p
# print(f"{q:.2f}")

# N16
# from math import *
#
# x, y = map(float, input().split())
# c1 = ((x + y) / (pow(y, 2) + ((pow(y, 2) + 2) / (x + (pow(x, 3) / 5))))) + (pow(e, y + 2))
# print(f"{c1:.2f}")

# 17
# from math import *
#
# x, y = map(float,input().split())
# f1 = ((2*(tan(x+(pi/6)))) / ((1/3) + pow(cos(y+pow(x,2)),2))) + log2(pow(x,2)+2)
# print(f"{f1:.2f}")

# N18
# from math import *
#
# x, y = map(float,input().split())
# a = (1/(x+(2/pow(x,2)+(3/pow(x,3))))) + (pow(e,pow(x,2)+(3*x)))
# b = atan(x+y) + pow((5+x),2)
# f2 = (a/b) - pow(cos(pow(y,2)+(pow(x,2)/2)),2)
# print(f"{f2:.2f}")

# N19
# from math import *
#
# x, y = map(int, input().split())
# z = log(abs((x + y) ** 2 + sqrt(abs(y) + 2) - (x - (x * y) / (x * x / 2 - 5)))) + cos(x + y) ** 2 / (
#         x + y) ** (1 / 3)
# print("%.2f" % z)

# N20
# from math import *
#
# x, y = map(float, input().split())
# l = ((x**2+1)/(x**2+(x*y + y**2)/(y**2+(y+x*y)/(abs(x*y)+5)))) + (1/(1+cos(x)+(1/sin(abs(x)))))
# print(f"{l:.2f}")

# N21

# a, b = map(float, input().split())
# t = a ** (1/5) + ((b * ((a+b)/(2*b+a*b))) ** (1/4)) * (a**2 + b**2 + 2)
# print(f"{t:.2f}")

# N22
# from math import *
#
# x1, x2, c, d = map(float, input().split())
# a = pow(sin(abs((c * pow(x2, 3)) + (d * pow(x1, 3)) - (c * d))), 2)
# b = sqrt((c * pow(x1, 2)) + (d * pow(x2, 2)) + 7)
# c = tan(x1 * pow(x2, 2) + pow(d, 3))
# f = abs(a / b) + c
# print(f"{f:.2f}")

# N23
# from math import *
#
# a, b, c, d, x = map(float, input().split())
# try:
#     y = (((a * pow(x, 2)) + (b * x) + c) / ((x * pow(a, 3) + pow(a, 2) + pow(a, (b - c))))) + cos(
#         abs((a * x + b) / (c * x + d + pow(2, c))))
#     print(f"{y:.2f}")
# except:
#     print(f"{1:.2f}")

# N24
# from math import *
# a, b, c, x = map(float, input().split())
# try:
#     w = 0.75 + ((8.2 * pow(x, 2) + sqrt(abs(pow(x, 3) + 3 * x) + cos(x - 2))) / (a / 4 + b / 3 + c / 2 + 1))
#     print(f"{w:.2f}")
# except:
#     print(f"{1:.2f}")

# N31
# x, y = map(float, input().split())
# max_ = max(x, y)
# min_ = min(x, y)
# print(max_, min_)

# N32
# x, y, z = map(float, input().split())
# print(max(x, y, z), min(x, y, z))

# N33
# x, y, z = map(float, input().split())
# print(f"{max(x + y + z, x, y, z):.2f} {min(x + y / 2, x, y, z) ** 2:.2f}")

# N34
# a, b, c = map(int, input().split())
# if a < b < c:
#     print("YES")
# else:
#     print("NO")

# N35
# a, b, c = map(int, input().split())
# if c <= b <= a:
#     print(a * 2, b * 2, c * 2)
# else:
#     print(abs(a),abs(b),abs(c))

# N36
# a,b = map(int,input().split())
# if a>b:
#     print(a)
# else:
#     print(a,b)

# N37
# a,b = map(int,input().split())
# if a<=b:
#     a=0
#     print(a,b)
# else:
#     print(a,b)

# N38
# a, b, c = map(float, input().split())
# s = [a, b, c]
# print(*[i for i in s if 1 < i < 3])

# 39
# x, y = map(int, input().split())
# if x < y:
#     print(f"{(x + y) / 2:.1f} {x * y * 4 :.1f}")
# else:
#     print(f"{x * y * 4 :.1f} {(x + y) / 2 :.1f}")

# N40
# a, b, c = map(int, input().split())
# s = [a, b, c]
# for i in range(len(s)):
#     if s[i] > 0:
#         s[i] = pow(s[i],2)
# print(*s)

# N41
# x, y, z = map(float, input().split())
# if x < 1 and y < 1 and z < 1:
#     if x > y < z:
#         print(x, (x + z) / 2, z)
#     elif x > z < y:
#         print(x, y, (x + y) / 2)
#     else:
#         print((y + z) / 2, y, z)
#
# else:
#     print(x, y, z)

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

# N43
# x, y = map(float, input().split())
# if x < 0 and y < 0:
#     print(abs(x), abs(y))
# elif x < 0 and y > 0 or x > 0 and y < 0:
#     print(x + 0.5, y + 0.5)
# else:
#     print(x, y)

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

# N66
# from math import *
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s = s + (-1) ** (i - 1) / i * sin(i * x)
# print(f"{s:.3f}")

# N67
# from math import *
# n , x = map(int, input().split())
# s = 0
#
# for i in range(1, n + 1):
#     s += (x ** i) / sqrt(i)
# print(f"{s:.3f}")


# 70
# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += pow(-1, i - 1) * pow(x, 2 * i - 1) / factorial(2 * i - 1)
# print(f"{s:.3f}")

# N75
# n, k = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     p = 1
#     for j in range(1, i + 1):
#         p = p * j
#     s = s + (i-1) ** i * k ** i/p
# print(f"{s:.3f}")

# N76
# from math import *
#
# a, b, c = map(int, input().split())
# s = 0
# for i in range(a, c + 1, 3):
#     # s = s + ((a * i + b) / (b ** 2 + cos(i) ** 2)) / (1 / 3) - (sin((i) ** 2) / (a * b))
#     s = s + ((a * i + b) / (b ** 2 + cos(i) ** 2)) / (1 / 3) - (sin(i * i) / (a * b))
# print(f"{s:.2f}")

# N88
# from math import *
#
# a, b, c, d = map(int, input().split())
# y = 0
# x = d
# while x <= c:
#     y += pow((a * x + b) / (b ** 2 + cos(x) ** 2), 1 / 5) - sin(x ** 2) / (a * b)
#     x += 1.5
# print(f"{y:.2f}")

# N89
# from math import *
#
# a, b, c = map(int, input().split())
# s = 0
# x = 0
# while x <= 1:
#     s += sqrt((sin(a * x) + b ** c) / (b ** 2 + cos(x) ** 2)) - ((sin(x ** 2) / (a * b)))
#     # s += sqrt((sin(a * x) + b ** c) / (b ** 2 + cos(x) ** 2)) - sin(x ** 2) / (a * b)
#     x += 0.25
# print(f"{s:.2f}")

# N93
# n1, m1 = map(int, input().split())
# matrix1 = []
# for i in range(n1):
#     matrix1.append(list(map(int, input().split())))
#
# n2, m2 = map(int, input().split())
# matrix2 = []
# for i in range(n2):
#     matrix2.append(list(map(int, input().split())))
#
# zip2 = list(zip(*matrix2))
#
# result = []
# for i in matrix1:
#     l = []
#     for j in zip2:
#         tmp = 0
#         for k in range(len(i)):
#             tmp += i[k] * j[k]
#         l.append(tmp)
#     print(*l)
#
# for i in result:
#     print(i)


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

# N101
# l = int(input())
# n = list(map(int, input().split()))
#
# o = sum(n) / l
# s = []
# for i in n:
#     if i < o:
#         s.append(i)
# print(f"{sum(s) / len(s):.2f}")

# N102
# l = int(input())
# n = list(map(int, input().split()))
# x, y = map(int, input().split())
# min_ = min(n)
# s = []
# for i in range(x - 1, y):
#     n[i] = (n[i] / min_) + 0.01
# for i in n:
#     print(f"{i:.1f}", end=" ")

# N105
# s = 0
# n = int(input())
# aa = list(map(int, input().split()))
# a, b = map(int, input().split())
# for i in range(n):
#     if not (i >= a - 1 and i <= b - 1):
#         s += aa[i]
# print("%.2f" % (s / (n - (b - a + 1))))

# N108
# n = int(input())
# massiv = list(map(int, input().split()))
# min_ = min(massiv)
# for i in massiv:
#     print(f"{i / min_:.2f}",end=" ")

# N116
# n = input()
# massiv = list(map(int, input().split()))
# m = max(massiv)
#
# for i in massiv:
#     print(f"{i / m + 0.00001:.2f}", end=" ")

# N120
# n = int(input())
# massiv = list(map(int,input().split()))
# a, b = map(int,input().split())
# print(len([i for i in massiv if not a<i<b]))

# 123
# s = 0
# n = int(input())
# aa = list(map(int,input().split()))
# for i in range(n):
#     if i % 2 == 1:
#         s += aa[i]
# for i in range(n):
#     if aa[i] % 2 == 1 and aa[i] > 0:
#         print("%.2f" % (aa[i] / s),end=" ")
#     else:
#         print("%.2f" % aa[i],end=" ")

# N124
# n = int(input())
# massiv = list(map(int, input().split()))
# k_index = int(input()) - 1
# m = max(massiv)
# m_index = massiv.index(max(massiv))
# for i,v in enumerate(massiv):
#     if v == m:
#         massiv[i] = massiv[k_index]
#
# massiv[k_index] = m
#
# print(*massiv)

# N128
# n = int(input())
# massiv = map(int, input().split())
# s = []
# for i in massiv:
#     if i % 2 == 0:
#         s.append(i)
# print(f"{sum(s)/len(s):.2f}")

# N130
# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# max_, min_ = float("-inf"), float("inf")
# for i in matrix:
#     if max(i) > max_:
#         max_ = max(i)
#     if min(i) < min_:
#         min_ = min(i)
#     print(sum(i),end=" ")
#
# print(f"\n{max_}{min_}")


# N132
# n = int(input())
# massiv = list(map(int, input().split()))
# a, b = map(int, input().split())
# o = 0
# [massiv.append(0) for i in range(a * b - n)]
# for i in range(a):
#     for j in range(b):
#         print(massiv[o],end=" ")
#         o += 1
#     print()

# N133
# n = int(input())
# a = []
# b = []
# x = n
# [a.append(list(map(int, input().split()))) for i in range(n)]
# [b.append(list(map(int, input().split()))) for j in range(n)]
# for i in range(n):
#     for j in range(n * 2):
#         if x > j:
#             print(a[i][j], end=" ")
#         else:
#             print(b[i][j-x], end=" ")
#     print()

# N135
# from math import *
#
# x, y = map(int, input().split())
# z = log(abs((x + y) ** 2 + sqrt(abs(y) + 2) - (x - (x * y) / (x * x / 2 - 5)))) + cos(x + y) ** 2 / (
#         x + y) ** (1 / 3)
# print("%.2f" % z)
#
# n, m = map(int, input().split())
# d = []
# for i in range(n):
#     d.append(list(map(int, input().split())))
# k = int(input())
# for i in range(n):
#     for j in range(m):
#         if k - 1 != i:
#             print(d[i][j], end=" ")
#     print()

# N140

# n1,m1 = int(input())
# massiv1 = list(map(int,input().split()))
# n2,m2 = int(input())
# massiv2 = list(map(int,input().split()))
# s = []
# massiv2 = zip(massiv2)
# for i in range(n2):
#     d = []
#     for j in range(m2):
#         d.append(massiv2[i][j])
#     s.append(d)
#     print()

# N167
# from math import *
# y = float(input())
# def t(x):
#     k = 0
#     surat = 0
#     mahraj = 0
#     while k <= 10:
#         surat += pow(x, 2 * k + 1) / factorial(2 * k + 1)
#         mahraj += pow(x, 2 * k) / factorial(2 * k)
#         k += 1
#     return surat / mahraj
#
#
# result = (1.7 * t(0.25) + 2 * t(y + 1)) / (6 - t(y ** 2 - 1))
# print(f"{result:.2f}")

# N172
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        m = n // 2
        return fibonacci(m)
    else:
        m = n // 2
        return fibonacci(m)+fibonacci(m+1)



n = int(input())
result = fibonacci(n)
print(result)
