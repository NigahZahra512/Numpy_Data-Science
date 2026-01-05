import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
new_arr = np.append(arr, [[7, 8, 9]])
print(new_arr)

new_arr_axis0 = np.append(arr, [[10, 11, 12]], axis=0)
print(new_arr_axis0)

