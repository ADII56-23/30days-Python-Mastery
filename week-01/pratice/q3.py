s = "I love CodeChef"
for i in s.split():
  print(i) 

fruit = "Coding, world"
print(fruit[6])

n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
elif n %3 == 0 or n % 5 == 0:
    print("Not Divisible by both 3 and 5")

# # Complete the code
tup = (1, 2, 3, 4, 5)
print(tup[::-1])    

arr =[9,4,5,3]
print(arr[4])

#fibonnaci series
n = int(input())
a= 0
b=1 
for i in range(n):
    print(a,end=" ")
    a,b = b ,a+b


t= int(input()) #testcase
for _ in range(t):
  N=int(input())
  print(N+1) 