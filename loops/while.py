food = input("Enter the food you like (q to quit): ")
while not food ==  "q":
  print(f"ohh!! you like {food}")
  food = input("Enter another food you like (q to quit): ")
print("okay Bye")

n =1 
while n <=100:
  print(n)
  n+=1

i = 100
while i>=1:
  print(i)
  i-=1

n = int(input())
i=1
while i <=10:
  print( n,"X", i,"=",n*i)
  i+=1

i = 1
while i<=10:
  print(i*i)
  i+=1

t = (2,3,4,233,1,77)
print("Enter the number you want to print:")
n = int(input())
for i in t:
  if i == n:
    print(f"{n}is found")
    break
else:
    print("not found")  
