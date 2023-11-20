# N1
# nums = [2,2,4,4,4,3]
# s = 0
# n = 0
#
# for i in nums:
#     x = 0
#     for j in nums:
#         if i == j:
#             x += 1
#     if s < x:
#         s = x
#         n = i
# print(n)

# N3
# nums = [1, 2, 2, 5]
# s = []
# for i in range(len(nums)-1):
#     if nums[i + 1] - nums[i] != 1:
#         s.append([nums[i+1],nums[i] + 1])
#         nums[i + 1] = nums[i] + 1
# print(nums)
# print(s)

# N4
# word = ["cat", "bt", "hat", "tree"]
# chars = "atach"
# s1 = 0
# for i in word:
#     l = 0
#     s = []
#     for j in i:
#         s.append(j)
#     for a in s:
#         if chars.count(a):
#             l += 1
#     if len(s) == l:
#         s1 += len(s)
# print(s1)
