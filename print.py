print(12)
print(13,end="")
print(34)

for i in range(1,6):
    print(i, "-", i*i)

for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()    

print(15 // 4)

time1 = 1650
time2= 1415
print(time2-time1)

name = input()
verb =input()
place =input()
print(f"{name} is {verb} in the {place}")

num = 12

if num % 3 == 0:
    print("Divisible by 3")
elif num % 4 == 0:
    print("Divisible by 4")  

list=[4]
N = list.append()
a= list[0]*list[2]
print(a)


l = []
print("enter 5 fruits name:")
for i in range(0,5):
  l.append(input())
  print("the 5 fruits are :")
for i in range(0,5):
  print(i)
 

print(ord("0")) 

a= -1
a=bool(a)
print(a)
print(type(a))

print(True and bool(0))