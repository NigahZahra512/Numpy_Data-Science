"""
np.insert(array,index,values,axis=None)
axis=None -> 1 row array
axis=0 -> insert rows
axis=1 -> insert columns
"""
import numpy as np
arr = np.array([[1, 2], [3,4]])
new_arr = np.insert(arr, 1, 10)
print(new_arr)

new_arr_axis0 = np.insert(arr, 1, [5,6], axis=0)
print(new_arr_axis0)

new_arr_axis1 = np.insert(arr, 1, [1000, 2000], axis=1)
print(new_arr_axis1)