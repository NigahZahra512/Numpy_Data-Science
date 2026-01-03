#functions for changing array

import numpy as np
arr = np.array([1.2,2.3,3.4])
print(arr)
print(arr.dtype)

int_arr = arr.astype(int)   #changing type of array(decimal to int)
print(int_arr)    
print(int_arr.dtype)