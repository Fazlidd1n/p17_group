# a = "hello3world534"
# c = 0
# for i in a:
#     if i.isdecimal():
#         c += int(i)
# print(c)

# a = [1,2,4]
# # b = a.copy()
# b = a[:]
#
#
# print(id(a))
# print(id(b))


# ord()
a = "a"
print(ord(a))

# chr()
print(chr(66))

a = "sdGVHGasdauUNinas7664865)(*"
# 1 version
# c = 0
# for i in a:
#     if 65 <= ord(i) <= 90:
#         c += 1
# print(c)

c = 0
for i in a:
    if i.isupper():
        c += 1
print(a)
# print(c)
# print(sum([True , True , False]))
# a = "ArtE"
# print(sum([True if i.isupper() else False for i in a ]))
# def b():
#     return sum([True for i in a if 65 <= ord(i) <= 90])
#
# print(b())

# a = "botirjon"
# b = "botirjon"
# print(hash(a))
# print(hash(b))
# print(hash(a) == hash(b))

# "botirjon" # TODO : create shifr
# 98-114-123-111-124

