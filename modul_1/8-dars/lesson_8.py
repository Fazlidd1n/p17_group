# N1
# nums = [0,2,1,5,3,4]
# q = len(nums)
#
# for i in range(len(nums)):
#     r = nums[i]
#     b = nums[nums[i]] % q
#     nums[i] = q * b + r
#
# for i in range(len(nums)):
#     nums[i] = nums[i]
#
# print(nums)

# N2
key = "thequickbrownfxjmpsvlazydg"
alfabit = "abcdefghijklmnopqrstuvwxyz"
message = "vkbs bs t suepuv"
result = ""
d = {

}
for i in range(len(key)):
    d[key[i]] = alfabit[i]
for i in message:
    if i != " ":
        for k, v in d.items():
            if i == k:
                result += v
    else:
        result += " "
print(result)
