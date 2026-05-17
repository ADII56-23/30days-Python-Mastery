#pallidrome
n = int(input())
original = n 
reverse  = 0
while n > 0:
  digit = n % 10
  reverse = reverse*10 +digit
  n = n//10

if reverse == original:
  print("pallindrome")
else:
  print("not pallindrome")       

#Linear Search of an array
arr = [12,22,1,11,45,67]
n = int(input("Enter the target element:"))
for i in range(len(arr)):
  if arr[i] == n:
    print(f"The element is found in the index of {i}")
    break
else:
  print("Element is not found")   



#liner search in array (approach 1)
arr = [12,22,1,11,45,67]
n = int(input("Enter the target element:"))
for i in arr:
  if  n == i:
    print("element is found")
    break
else:    
  print("element is not found")   