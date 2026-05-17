#changing a float data type to integer by using 'i' and astype() method
import numpy as np 
arr = np.array([1.2,2.3,3.3])
new_array = arr.astype('i')
print(arr)
print(new_array)

import numpy as np
arr1 = np.array([3,0,9])
new = arr1.astype(bool)
print(arr1)
print(arr1.dtype)
print(new)
print(new.dtype)

'''array creation functions '''
#zeros()
import numpy as np
print(np.zeros((2,3)))

#empty()
print(np.empty((2,2)))  #empty will generate different values every execution 

#ones()
print(np.ones((2,3)))