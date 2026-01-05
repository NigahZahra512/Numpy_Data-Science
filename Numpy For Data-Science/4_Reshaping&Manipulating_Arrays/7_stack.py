"""
vertically and horizontally stack arrays using NumPy.
vstack()  ->row wise stacking
hstack()  ->column wise stacking

"""
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
new_arr = np.vstack((arr1, arr2))
print(new_arr)
new_array = np.hstack((arr1, arr2))
print(new_array)