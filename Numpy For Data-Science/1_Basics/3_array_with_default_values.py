#with default values (0's function)
import numpy as np
arr_zeros = np.zeros((3))  
print("Array of zeros:\n", arr_zeros)



#with default values (1's function)
import numpy as np
arr_ones = np.ones((2, 3))  #in tuple form
print("Array of ones:\n", arr_ones)



#with default values (full function)
#syntax : np.full(shape, fill_value)
import numpy as np
arr_full = np.full((3, 4), 5)  
print("Array of full values:\n", arr_full)