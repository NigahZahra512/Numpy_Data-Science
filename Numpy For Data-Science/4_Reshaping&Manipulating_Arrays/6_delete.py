"""
.delete(array ,index,axis=None)
Removes elements from an array at specified indices.
"""

import numpy as np
arr = np.array([[1, 2, 3, 4]])
new_arr = np.delete(arr, 0)
print(new_arr)

arr_1 = np.array([[1, 2, 3],[4,5,6]])
new_array = np.delete(arr_1, 0, axis=1)
print(new_array)