# N1
# accumalate()
# def acumalate(l: list):
#     s = 0
#     for i in l:
#         s += i
#         yield s
#
#
# for i in acumalate([1, 2, 3, 4, 5]):
#     print(i, end=" ")

# N2
# chain()
# def chainn(*args):
#     s = []
#     for i in range(len(args)):
#         s += list(args[i])
#     yield s
# for i in chainn("ABCD","EFG"):
#     print(*i)

# N3
# chain.from_iterable()
# def chain_from_iterable(l: list):
#     s = []
#     for i in l:
#         s += list(i)
#     yield s
#
# for i in chain_from_iterable(["ABCD","EFG"]):
#     print(*i)

# N4
# compress()
# def compress(a: str, b: list):
#     s = []
#     for i in range(len(b)):
#         if b[i] == 1:
#             s.append(a[i])
#     yield s
#
# for i in compress("ABCDEF", [1, 0, 1, 0, 1, 1]):
#     print(*i)

# N5
# dropwhile()
# def dropwhile(func, iter: list):
#     s = []
#     for i in range(len(iter)):
#         if not func(iter[i]):
#             s.append(iter[i:])
#             break
#     yield s
#
#
# for i in dropwhile(lambda x: x < 5, [9, 1, 9, 8, 8]):
#     print(*i)

# N6
# filterfalse()
# def filterfalse(func, iter):
#     for i in iter:
#         if not func(i):
#             yield i
#
#
# for i in filterfalse(lambda x: x % 2, range(10)):
#     print(i, end=" ")

# N7
# gruopby()
# def groupby(l: list):
#     for i in l:
#         a = YIELD(i)
#         yield (i, a)
#
#
# def YIELD(l):
#     yield l
#
#
# for i in groupby(list("AAABBCCD")):
#     print(i)

# N8
# islice()
# def islice(*args):
#     if len(args) == 2:
#         yield args[0][args[1]:]
#     elif len(args) == 3:
#         a = args[1]
#         b = args[2]
#         c = list(args[0])
#         for i in range(a,len(c),b):
#             yield c[i]
# for i in islice("ABCDEFG",2,2):
#     print(i,end=" ")

# N9
# pairwase()
# def pairwase(l:str):
#     for i in range(1,len(l)):
#         yield l[i-1]+l[i]
# for i in pairwase("ABCDEFG"):
#     print(i,end=" ")

# N10
# startmap()
# def startmap(func,iter:list[tuple]):
#     for i in iter:
#         yield pow(i[0],i[1])
#
# for i in startmap(pow,[(2,5),(3,2),(10,3)]):
#     print(i)

# N11
# takewhile()
# def dropwhile(func, iter: list):
#     s = []
#     for i in range(len(iter)):
#         if not func(iter[i]):
#             s.append(iter[:i])
#             break
#     yield s
#
#
# for i in dropwhile(lambda x: x < 5, [0, 1, 9, 8, 8]):
#     print(*i)

# N12
# tee()
# def tee(l:list,n:int):
#     for i in range(n):
#         yield te2(l)
#
# def te2(l):
#     yield l
#
# for i in tee([1,2,3],2):
#     for j in i:
#         print(j)

# N13
# zip_longest()
# def zip_longest(p,q,fillvalue:str = "-"):
#     s = list(q)
#     if len(q) < len(p):
#         n = len(p) - len(q)
#         for i in range(n):
#             s.append(fillvalue)
#     for i in range(len(p)):
#         yield p[i]+s[i]
# for i in zip_longest("ABCDEFG","xy","*"):
#     print(i)