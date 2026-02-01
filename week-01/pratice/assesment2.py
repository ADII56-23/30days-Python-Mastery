##Write a program to check whether a number is positive, negative or zero
i = 1
while i < 4:
  n = int(input())
  i+=1  
  if n > 0:
   print("positive")
  elif n<0:
   print("negative")
  else:
   print("zero")    

##Write a program to reverse a string without using built-in functions

s = input("Input a string:")
for i in s[::-1]:
   print(i)

##Write a program to count vowels in a string
s = input("Input a string:")
count = 0
for i in s:
  if i in "aeiouAEIOU":
    count+=1  
print(count)    

##Print numbers from 1 to 50 except multiples of 5 using continue

for i in range(1,51):
  if i % 5 == 0:
    continue
  print(i)
 
##Write a program to check whether a number is prime or not
n =int(input())
count = 0
for i in range(1,n+1):
  if n % i == 0:
    count +=1
if count ==2:
    print("prime")
else:
    print("not prime")     

##Write a program to find factorial of a number using loop
n = int(input())
fact = 1
for i in range(1,n+1):
  fact*=i
print(fact)  

##1
22
333
4444

for i in range(1,5):
  for j in range(1,i+1):
    print(i,end=" ")
  print( )  

##Write a program to find sum of digits of a number
n = int(input())
sum = 0 
for i in range(1,n+1):
  sum+=i
print(sum)

# #Write a program to check if a string is palindrome
n = input()
if n == n[::-1]:
  print("pallindrome")
else:
  print("not pallindrome")  

##Write a program to print first 10 even numbers using while loop
for i in range(1,20):
  if i% 2==0:
    print(i)

##Explain with code difference between break and continue
for i in range(1,21):
  if i ==3:
    break
  print(i)

##Write a program to count uppercase and lowercase letters in a string
s = input()
upper =0
lower =0
for i in s:
  if i.isupper():
    upper+=1
  elif i.islower():
    lower+=1
print(upper)
print(lower)      


##Write a program to print pattern: 
# A
# BB
# CCC
# DDDD
for i in range(4):
   for j in range(i+1):
      print(chr(ord("A")+i),end="")
   print()    


