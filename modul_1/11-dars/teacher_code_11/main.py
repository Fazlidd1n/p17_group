# nums = [0,1,2,3,4]
# index = [0,1,2,2,1]
#
# l = []
# for i in range(len(nums)):
#     # print(nums[i] , index[i])
#     l.insert(index[i], nums[i])
# print(l)

# ==================================

#
# nums = [1,1,2,3]
# l = []
# for i in range(0 , len(nums) , 2):
#     # print(nums[i] , nums[i + 1])
#     # print([nums[i + 1]] * nums[i])
#     l.extend([nums[i + 1]] * nums[i])
# print(l)


# print(int("0b101111", 2))
# print(bin(47))

# encoded = [1,2,3]
# first = 1
# re = [first]
# for i in encoded:
#     re.append(re[-1]^i)
# [re.append(re[-1]^i) for i in encoded]
# print(re)


# l = [5,3,7,9,5,6]

# def a(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# print(list(map(a, l)))
# print([True if i % 2 == 0 else False for i in l])

# output: [6]

# [1,2,3]
# [4,5,6]
# [7,8,9]

# n ,m = map(int , input().split())
# matrix = []
# c = 1
# for i in range(n):
#     tmp = []
#     for j in range(m):
#         tmp.append(c)
#         c += 1
#     matrix.append(tmp)
#
# for i in matrix:
#     print(i)

#
# n ,m = map(int , input().split())
#
# l = list(range(1 ,n*m+1))
# matrix = []
# for i in range(n):
#     matrix.append(l[i*m:i*m+m])
#
# re = []
# for i in list(zip(*matrix)):
#     re.append(i)
# print(re)























