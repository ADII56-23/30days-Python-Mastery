#length of string without library function
str = "Elephant"
count = 0
for i in str:
  count += 1
print(count)  

#sort an array using bubble sort
arr= [22,33,12,56,67,87,33,121,1]
for i in range(len(arr)):
  for j in range(0,len(arr)-1):
    if arr[j] >arr[j+1]:

      arr[j],arr[j+1]  = arr[j+1],arr[j]

print("sorted array is :",arr)    