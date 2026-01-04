"""
array[index] # 1D array
array[row,column] # 2D array
"""
import numpy as np

arr = np.array([1,2,3,45,64,2])
print(arr[0])
print(arr[-2])

arr = np.array([[1,2,3,2],
               [1,6,4,3]])
print(arr)
print(arr[1,2])
