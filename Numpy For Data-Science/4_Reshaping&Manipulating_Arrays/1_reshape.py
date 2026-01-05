""" reshape(rows,columns)  specify new shape
if dimensions match, return reshaped array.
reshaping doesnot create copy of original array, returns view of it.
"""



import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
reshape_arr = arr.reshape(3, 2)
print(reshape_arr)
