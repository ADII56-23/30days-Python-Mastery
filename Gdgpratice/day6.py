# #remove duplicates from a sorted array
arr = [2,55,2,67,89,89,90,96]
b = arr[0]

for i in range(0,len(arr)):
    if arr[i] != b:
        print(arr[i])
        b = arr[i]

#second largest element in the array
a =[23,90,12,112,22,33] 
largest = a[0]
for i in a:
  if i > largest:
    largest = i
print(largest)    
a.remove(largest)
print(a)
largest1 = a[0]
for i in a:
  if i > largest1:
    largest1 = i
print(largest1)  


#another
a =[23,90,12,112,22,33] 
largest11 = max(a)
a.remove(largest11)
largest2 = max(a)
print("The second Largest number is ",largest2) 