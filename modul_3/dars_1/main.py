# """
# iterator
# generator
# itertools
# """


# iterator
a = [1, "hello", 0.9, True]
a = iter(a)
print(next(a))
print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# a = [-3,-4,-7,-9]
# a = iter(a)
# s = float("-inf")
# while True:
#     try:
#         b = next(a)
#         if b > s:
#             s = b
#
#     except:
#         break
#
# print(s)


# generator
# map()
# range()
# print(map())

# def range(start,end,step):

# def rangee(*args):
#     l = len(args)
#     start = 0
#     step = 1
#     if l == 1:
#         end = args[0]
#         while start < end:
#             yield start
#             start += step
#     elif l == 2:
#         start = args[0]
#         end = args[1]
#         while start < end:
#             yield start
#             start += step
#     elif l == 3:
#         start = args[0]
#         end = args[1]
#         step = args[2]
#         while start < end:
#             yield start
#             start += step
#
#
#
# for i in rangee(100):
#     print(i)

# def mapp(function, iterable):
#     for i in iterable:
#         yield function(i)
#
#
# def filterr(function, iterable):
#     for i in iterable:
#         if function(i):
#             yield i
#
#
# def fibonaci(iterable):
#     a, b, c = 0, 1, 0
#     while c < iterable:
#         yield a
#         a, b = b, a + b
#         c += 1
#
#
# for i in mapp(lambda a: a + 10, [0, 9, 8, 8]):
#     print(i, end=" ")
# print("")
# for i in filterr(lambda a: a, [0, 9, 8, 8]):
#     print(i, end=" ")
# print("")
# for i in fibonaci(10):
#     print(i, end=" ")


# itertools
# import itertools
#
# for i in itertools.tee([1, 2, 3, 4, 5, 6, 7, 8, 9], 2):
#     for j in i:
#         print(j)
