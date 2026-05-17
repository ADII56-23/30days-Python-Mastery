#smallest element in array
arr = [22,12,11,6,3,67]
smallest = arr[0]
for i in range(len(arr)):
   if arr[i] < smallest:
      smallest = arr[i]
print("The smallest element is ",smallest)    


#count even and odd numbers in an array
arr = [22,12,12,6,3,67,23,11,90]
is_even = 0
is_odd = 0
for i in range(len(arr)):
   if arr[i] % 2 == 0:
      is_even +=1
   else:
      is_odd +=1    
print(f"Their is {is_even} even no. present in the array")
print(f"Their is {is_odd} odd no. present in the array")      