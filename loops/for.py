n = int(input("Enter a number:"))

for i in range(n):
  print("Hello",end=" ")


#  print 1 to n
n = int(input("Enter a number:"))
for i in range(1,n):
  print(i)


  # reverse of n to 1
n = int(input("Enter a number:"))
for i in range(n,0,-1):
  print(i) 


#table 
n = int(input("Enter a number:"))
for i in range(1,n):
  print(n *i) 

#sum upto n number
n = int(input("Enter a number:"))
total =0
for i in range(1,n+1):
      total+=i
print(total)  

# factorial of a number
n = int(input("Enter a number:"))
fact =1 
for i in range(1,n+1):
  fact=fact*i
print(fact)  


#sum of odd and even in a range separately
n = int(input("Enter a number:"))
even= 0
odd = 0
for i in range(1,n+1):
  if (i//2)*2 == i:
    even+=i
  else:
    odd+=i
print(f"Even no are totally {even}")
print(f"Odd no are totally {odd}")      
