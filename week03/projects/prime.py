def is_prime(num):
  
  if num <= 1:
     print("not prime")
  count = 0   
  for i in range(1,num+1):
    if num % i == 0:
      count +=1
  return count == 2
  

num = int(input("Enter a digit:"))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print("Not prime")   