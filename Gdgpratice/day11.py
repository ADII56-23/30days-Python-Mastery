#second smallest eleemnt in a array without sorting
arr = [23,44,8,10,67,89]
smallest = arr[0]
for i in range(len(arr)):
  if arr[i] < smallest:
    smallest = arr[i]
print("The smallest element in the array is ",smallest)     
arr.remove(smallest)
print("updated array is ",arr)
small = arr[0]
for i in range(len(arr)):
  if arr[i] < small:
    small = arr[i]
print("The second smallest element in the array is ",small)      


#using inbuilt function
def second_smallest(arr):
  smallest1 = min(arr)
  arr.remove(smallest1)
  small1 = min(arr)
  print("The 2nd smallest in the array is ",small1)
second_smallest([23,44,8,10,67,89])  


#fibonnaci series upto n terms
n = int(input("Enter the n no of terms(for fibonnaci series) :"))
a, b = 0,1
series = []
for _ in range(n+1):
  series.append(a)
  a, b = b, a+b 
print(f"The fibonaci series of  {n} terms is {series}")
