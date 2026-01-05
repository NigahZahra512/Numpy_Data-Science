import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([7,8,9],)
concat= np.concatenate((arr1,arr2))
print(concat)


arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[7,8,9],[10,11,12]])
concatenated = np.concatenate((arr3,arr4), axis=1)
print(concatenated)