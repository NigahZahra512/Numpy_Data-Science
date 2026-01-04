"""
slicing :  array[start:stop:step]
"""
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[3:7])
print(arr[:5])
print(arr[0:7:2])
print(arr[-2:])
print(arr[::-1]) #reverse the array