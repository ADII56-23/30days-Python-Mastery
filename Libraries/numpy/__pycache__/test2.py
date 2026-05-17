import numpy as np
arr = np.array(1)
print("datatype is ",arr.dtype)

arr1 = np.array(["banana","apple","cherry"])
print(arr1.dtype)

arr2 = np.array([1,2,3,4],dtype='S')
print(arr2) 
print(arr2.dtype)


# reshaping of an array 
import numpy as np

arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr = np.array([[1,2,3],
                [4,5,6]])
new_array= arr.reshape(3,2)
print  (new_array)

arr1 = arr2.reshape(2,3,2)
print(arr1)



#copy()
import numpy as np
array = np.array([1,2,3,4,5])

x = array.copy()
x[1] = 10
print("original arr",array)  #original arr [1 2 3 4 5]
print(x)    #[ 1 10  3  4  5]

#view
y =array.view()
y[1] =10
print("original array",array)
print(y)


#sorting
import numpy as np
arr = np.array([3,5,2,1])
#for ascending
print(np.sort(arr))  # np.sort(arr)
#for descending
sorted_des = np.sort(arr)[::-1]
print(sorted_des) 