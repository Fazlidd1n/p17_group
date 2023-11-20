# l = ["is2", "this1", "a3", "laptop4"]
# l.sort(key=lambda x: x[-1])
# print(" ".join([i[:-1] for i in l]))

# l = [1, 5, 6, 8, 3, 9]
# l.sort(key=lambda x: -x if x % 2 == 0 else x)
# print(l)
# re1 = []
# re2 = []
# for i in l:
#     if i % 2 == 0:
#         re1.append(i)
#     else:
#         re2.append(i)
#     sorted(re1)
#     re2.sort(reverse=True)
# print(re1 + re2)

# def factorial(num):
#     # s = 1
#     # for i in range(1, num+1):
#     #     s *= i
#     # return s
#     if num == 1:
#         return 1
#     return num * factorial(num-1)
#
# print(factorial(int(input("son kiriting : "))))

# s = [0,1]
# def fibonanchi(n):
#     if len(s) == n:
#         return s
#     return s.append(s[-2]+s[-1])
# print(fibonanchi(int(input("son kiriting : "))))

# def fib(n):
#     if n <= 0:
#         return 0
#     if n <= 2:
#         return 1
#
#     return fib(n-1) + fib(n - 2)
# n: int = int(input(">>>"))
#
# for i in range(0, n):
#     print(fib(i))

