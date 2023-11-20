
# slicing -> qirqib olish


# a : str = "botirjonadsdhfjghkluiykjgdhf"
# print(a[-1])
# print(a[0])
# print(a[7])
#
# # a[start ,end , step ]  -> slicing
# print(a[0:8])
# print(a[-5:])
# print(a[-5:-1])
# print(a[::])
#
# a = "123456789"
# len_ = len(a)
# print(a[:len_//2])


# type casting

# a = "12"
# a = int(a)
# a = float(a)
# a = str(a)
# print(type(a), len(a))
# a = "2.9"
# print(int(float(a)))


# type heading

# a : int = 1.9
# print(type(a))
# b: str
# b : list



# for , while

# loop
# a = "1234567"
# for var in a:
#     print(var , end =" ")


# a = "1234"
# c = 1
# sum_ = 0
# for i in a:
#     if c % 2 == 1:
#         sum_ += int(i)
#     c += 1
#
# print(sum_)


# a = input(">>>")
# s = 0
# for i in a[::2]:
#     s += int(i)
# print(s)

# a = input(">>>")
# c = 0
# for i in a:
#     c += i
# print(c)
# print("1" + "1")


# l = [1,2,3,4,5,6]
# s = 1
# for i in l:
#     if s == 5:
#         break
#     print(i, end="")
#     s += 1

# l = [1,2,3,4,5,6]
# s = 0
# for i in l:
#     s += 1
#     if s == 5:
#         continue
#     print(i, end="")

# num = "156567755554"
# start = 0
# sum_ = 0
# while start < len(num):
#     sum_ += int(num[start])
#     start += 2
# print(sum_)


# 166774
# a=input()
# start=0
# while start<len(a):
#     if a[start]!='5':
#         print(a[start],end='')
#     start+=1

str="code cope cose"
s = 0
i = 0
while i < len(str):
    if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
        s += 1

    i += 1
print(s)





















