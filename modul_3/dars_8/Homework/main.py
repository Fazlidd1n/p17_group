# import numpy as np
#
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#
# print(arr[0, 1, 2])

# import numpy as np
#
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# import numpy as np
#
# arr = np.array([1, 2, 3, 4], ndmin=5)
#
# print(arr)
# print('number of dimensions :', arr.ndim)

# import numpy as np
#
# arr = np.array([1, 2, 3, 4])
#
# print(arr[1])


# import numpy as np
#
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#
# print('Last element from 2nd dim: ', arr[1, -1])


# import numpy as np
#
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr[0:2, 2])


# import numpy as np
#
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr[0:2, 1:4])


# import numpy as np
#
# arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr)
# print(arr.dtype)


# import numpy as np
#
# arr = np.array([1.1, 2.1, 3.1])
#
# newarr = arr.astype('i')
#
# print(newarr)
# print(newarr.dtype)



# import numpy as np
#
# arr = np.array([1, 0, 0])
#
# newarr = arr.astype(bool)
#
# print(newarr)
# print(newarr.dtype)

# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
#
# print(arr)
# print(x)

# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# newarr = arr.reshape(4, 3)
#
# print(newarr)


# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# newarr = arr.reshape(2, 3, -1)
#
# print(newarr)


# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# print(arr.reshape(2, 4).base)


# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# newarr = arr.reshape(2, 2, 2)
#
# print(newarr)


# import numpy as np
#
# arr = np.array([41, 42, 43, 44])
#
# filter_arr = arr % 2 == 0
#
# newarr = arr[filter_arr]
#
# print(filter_arr)
# print(newarr)


"""PANDAS"""

# import pandas as pn
# print(pn.__version__)


# a = [1, 2, 3, 4, 5]
#
# res = pn.Series(a)
# print(res[0:2])

# a = [1, 2, 3]
#
# res = pn.Series(a, index=['x', 'y', 'z'])
# print(res)

# a = [1, 2, 3]
#
# res = pn.Series(a, index=['x', 'y', 'z'])
# print(res['y')

# calories = {"day1": 567, "day2": 777, "day3": 77}
#
# mayVar = pn.Series(calories)
# print(mayVar)


# calories = {"day1": 567, "day2": 777, "day3": 77}
#
# mayVar = pn.Series(calories, index = ["day1", "day3"])
# print(mayVar)

# re = pn.read_csv('data.csv')
# print(re)
#
# re = pn.read_csv('data.csv')
# print(re.to_string())

# import pandas as pd
#
# print(pd.options.display.max_rows)
#
# import pandas as pd
#
# data = {
#     'Name': ['John', 'Alice', 'Bob'],
#     'Age': [28, 24, 22],
#     'City': ['New York', 'San Francisco', 'Los Angeles']
# }
#
# df = pd.DataFrame(data)

