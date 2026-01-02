import numpy as np
arr_1D= np.array([10,20,30,40,50])   # Create a 1D NumPy array
print(arr_1D)


arr_2D= np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])   # Create a 2D NumPy array
print(arr_2D)
print("Shape of 1D array:", arr_1D.shape)   # Print shape of 1D array
print("Shape of 2D array:", arr_2D.shape)   # Print shape of 2D array


arr_3D= np.array([[[1,2],
                   [3,4]],
                   [[5,6],
                   [7,8]]])   # Create a 3D NumPy array
print(arr_3D)
print("Shape of 3D array:", arr_3D.shape)   # Print shape of 3D array

# Accessing elements in 2D array
print("Element at row 1, column 2:", arr_2D[1, 2])   # Access element at row 1, column 2
print("First row:", arr_2D[0, :])   # Access first row
print("Second column:", arr_2D[:, 1])   # Access second column