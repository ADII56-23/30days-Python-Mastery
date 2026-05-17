#product of element of array
n = [2,3,3,5]
product = 1
for i in range(len(n)):
   product *= n[i]
print("The product of the array is",product)   

#mid element amoung 3 number
i = int(input())
j = int(input())
mid = (i+j)//2
if mid == i and j:
   print("select 2 elements with a gap of number")
else:
   print(round(mid))

#another approach
li = []
for i in range(3):
  a = int(input())
  li.append(a)
# result  = a if a > b and a > c else b if b>c else c 
print(li)
min = li[0]
max = li[0] 
for j in range(len(li)):
  if li[j] < min:
    min = li[j]
  elif li[j] > max:
    max = li[j]
print(min)
print(max)   

mid = li.sort()
print(li[1])