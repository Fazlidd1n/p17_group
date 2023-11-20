# sorting -> tartiblash

# list -> sort
# sorted -> all types

# l = [[1, 23], [1, 5, 6, 8], [1, 50, 2]]
# l.sort(key=lambda x: x[-1])
# print(l)

# l = ["is2", "this1", "a3", "laptop4"]
# l.sort(key=lambda x: x[-1])
# r = []
# for i in l:
#     r.append(i[:-1])
# print(" ".join([i[:-1] for i in l]))

# l = [1,5,6,8,3,9]
# l.sort(key= lambda x : -x if x % 2 == 0 else x)
# print(l)

# output: this is a laptop

# seats = [3,1,5]
# students = [2,7,4]
#
# seats.sort()
# students.sort()
#
# print(sum([abs(seats[i] - students[i]) for i in range(len(seats))]))
# c = 0
# for i in range(len(seats)):
#     c += abs(seats[i] - students[i])
# print(c)


# def f(*args, **kwargs):
#     print(kwargs)
#     print(args)
#
# f(1,2,3,456,3456,345 ,bir=1 , ikki=2 , uch=3)


# names = ["Mary","John","Emma"]
# heights = [180,165,170]
#
# l = list(zip(names, heights))
#
# l.sort(key=lambda x : x[-1] , reverse=True)
# print([i[0] for i in l])

