# n = int(input())
#
# massiv = list(map(int , input().split()))
#
#
# m = max(massiv)
# for i in massiv:
#     print(f"{i / m + 0.00001 :.2f}", end=" ")


# n = int(input())
# massiv = list(map(int , input().split()))
# k_index = int(input()) - 1
# m = max(massiv)
# m_index = massiv.index(max(massiv))
# for i , v in enumerate(massiv):
#     if v == m:
#         massiv[i] = massiv[k_index]
#
# massiv[k_index] = m
# print(*massiv)





# def groupby(str_ : str):
#     group = []
#     for i in str_:
#         if group and i == group[-1][0]:
#             group[-1][1] += i
#         else:
#             group.append([i , i])
#     return group
#
# for k , g in groupby("AAAABBBCCDAABBB"):
#     print(k , g)
# import collections

# def tee(iterable, n=2):
#     it = iter(iterable)
#     deques = [collections.deque() for i in range(n)]
#     def gen(mydeque):
#         while True:
#             if not mydeque:             # when the local deque is empty
#                 try:
#                     newval = next(it)   # fetch a new value and
#                 except StopIteration:
#                     return
#                 for d in deques:        # load it to all the deques
#                     d.append(newval)
#             yield mydeque.popleft()
#     return tuple(gen(d) for d in deques)
#
# for i in tee([1,2,3,4] , 4):
#     print(list(i))

# decorator
# datetime , time - format
# calendar

# datetime
from datetime import date ,datetime
import time
# Bular bizga hozirgi vaqt va sana format lani yasashga yordam beradi

# 2023-09-19
print(date.today())

# date_input = input("date : ")
# date.fromisoformat(date_input)

# datetime_input = input("datetime : ")
# d = datetime.fromisoformat(datetime_input)
# print(d.month)
# print(d.year)
# print(d.day)
# print(d.hour)
# print(d.minute)

# 2023-09-19 16:46:38.283768
# print(datetime.now())

# format
# print(datetime.now().strftime("%Y-%m %H:%M:%S"))
# print(date.today().strftime("%m-%d"))


# import time
# t = time.time_ns()
# t = time.time()
# t = time.sleep(10)


# print(datetime.fromtimestamp(t))


# def a():
#     time.sleep(10)
#
#
# start = time.time()
# a()
# print(f"{time.time() - start:.2f}" , "sekund")

# print(date.today() - date.fromisoformat("2000-02-19"))
def user_valid(function):
    def wrapper(data: dict):
        if len(data.get("fullname").split()) < 2:
            raise Exception("Invalid fullname")
        if data.get("age") < 1:
            raise Exception("Invalid age !")
        if len(data.get("password")) < 4:
            raise Exception("Must password 4 chars")
        result = function(data)
        return result
    return wrapper



































