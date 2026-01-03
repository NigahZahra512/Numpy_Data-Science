#Functions for checking arrays

import numpy as np
arr_1 = np.array([[1,2,3],
                 [5,4,6]])
print(arr_1.shape)    #shape fun :Calc total number of rows and column

print(arr_1.size)    #size fun :Calc total number of elements

print(arr_1.dtype)    #dtype fun :tells about data type


arr_1D = np.array([1,4,3,2])
arr_2D = np.array([[1,4,3],[2,34,5]])
arr_3D = np.array([[[1,3],[2,5],[2,2],[2,5]]])
print(arr_1D.ndim)    #dtype fun :tells about data type
print(arr_2D.ndim)  
print(arr_3D.ndim)