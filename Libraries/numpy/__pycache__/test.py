import numpy as np
arr2= np.array([1,2,3,4])
print(arr2)
print(arr2[1:3])

arr = np.array([[1,2,3],
               [4,5,6]])
print(arr[:])
print(arr[0:1])  #[[1 2 3]]
print(arr[0:1,2:])

max_arr = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])
print(max_arr[1:2,2:])
print(max_arr[:,1:3])
print(max_arr[1,:]) # 1st row all column 
print("the dimension is",max_arr.ndim)
