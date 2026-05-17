#binary search 
arr = [2,4,7,8,10,89,98]
def binarysearch(n):
  low = 0
  high = len(arr)-1
  while low <= high:
   mid = (low +high) //2
   if arr[mid] == n:
    return mid 
   elif arr[mid] > n:
    high = mid -1 
   else:
    low = mid+1    
     
n =int(input("enter the digit :"))
print(binarysearch(n))


#string is pallindrome or not
def pal(str):
  low =0
  high = len(str) -1
  while low < high:
     if str[low] != str[high]:
      return False
     low +=1
     high-=1
  return True    

str = input("enter a word")
print(pal(str))

#another
str = input()
if str == str[::-1]:
  print("palindrome")
else:
  print("Not pallindrome")  