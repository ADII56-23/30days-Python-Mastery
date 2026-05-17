#even or odd using bit manipulaton 
def is_even(num):
  if num & 1 == 0:
    return "even"
  else:
    return "odd"
num = int(input("enter a number :"))
print(is_even(num))  


#check if the given number is power of 2 or not
def power(n):
   if n <=0:
     return False

   while n % 2 == 0:   
     n = n // 2
   if n == 1:  
    return True
   else:
     return False
     
n = int(input("enter a num :"))
print(power(n))     



def poweroftwo(n):
  return n > 0 and (n & (n - 1)) == 0
n = int(input("enter a num :"))
print(poweroftwo(n))
