#find factorial of a number 
def Factorial(num):
  fact = 1
  for i in range(1,num+1):
    fact *= i
  return fact
  
num = int(input("enter the number :"))
print(Factorial(num))


#array is sorted or not
def is_sorted(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      return "not sorted"
  return "sorted"

print(is_sorted([2,22,56,77,89]))
print(is_sorted([2,56,89,22,11]))    
