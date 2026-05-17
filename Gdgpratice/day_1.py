#largest elements of an array
arr = [2,1,9,8,34,7]
largest = arr[0]
for i in arr:
   if i > largest:
      largest= i
print("largest element of array is ",largest)      

#largest elements of an array
arr = [2,1,9,8,34,7]
largest = max(arr)
print(largest)

#reverse of an array
arr = [2,1,9,8,34,7]
print(arr[::-1])