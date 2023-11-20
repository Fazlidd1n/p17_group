# tuple -> (1,2,3,4,5 , "dsfgg")
# a  = (True  , "Botirjon", "kamol" , "Botirjon" , 1,2,3 )

# count
# print(a.count(1))

# index
# print(a.index("Botirjon"))
# r = []
# for i , v in enumerate(a):
#     if v == "Botirjon":
#         r.append(i)
# print(r[-1])

# print([i for i,v in enumerate(a) if v == "Botirjon"][-1])

# a = {9,True , 0.5,10 , False ,1,7,3,"Botirjon", "Botirjon" , "Kamol"}

a = {1,2,3,"Doniyor"}

# add

print(a.add("Ozodbek"))


# clear
# a.clear()
# print(len(a))
# copy


# discard
# a.discard("Ozodbek")
# a.discard(1)
print(a)

a = {2,"o"}
b = {3, 4 ,2 , "o"}
# difference
print(b.difference(a))

# intersection
print(a.intersection(b))

# isdisjoint
print(a.isdisjoint(b))

# issubset
print(a.issubset(b))

# issuperset
print(a.issuperset(b))

# pop
# print(a.pop())

# remove
a.remove("o")
print(a)

# union
print(a.union(b))
print(a)


# update
print(a.update(b))
print(a)






