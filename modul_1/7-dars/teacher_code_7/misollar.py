jewels = "aA"
stones = "aAAbbbb"

# 1 version
# d = {}.fromkeys(jewels , 0)
# for i in stones:
#     if i in d.keys():
#         d[i] += 1
#
# print(sum(d.values()))

# 2 version
# d = {}
# for i in stones:
#     if i in jewels:
#         d[i] = d.get(i , -1) + 1
# print(sum(d.values()))



# ================================================

# nums = [1,2,3,1,1,3]
# Output: 4
# c = 0
# for i in range(len(nums)):
#     c += nums[i+1:].count(nums[i])
# print(c)













