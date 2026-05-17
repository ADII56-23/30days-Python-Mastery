#check if a number prime
n = int(input())
count = 0
for i in range(1,n+1):
  if n % i ==0:
    count +=1
if count == 2:
  print("prime")
else:
  print("not prime")  

#sum of digits of number 
n = int(input())
total = 0

while n > 0:
  digit= n% 10 
  total+=digit
  n = n//10 
print(total)  