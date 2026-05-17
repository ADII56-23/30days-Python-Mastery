#remove the given element from an array
arr = [2,4,5,77,88,34,67]
num = int(input("Enter the target value:"))

if num in arr:
  arr.remove(num)
else:
  print("Value not found")   
print(f"The new array is {arr}")    


#second largest
a =[3,30,1,12,22,3] 
largest = max(a)
a.remove(largest)
largests = max(a)
print("The second Largest number is ",largests) 