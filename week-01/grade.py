#grade calculator
m = int(input("Enter the marks in the maths:"))
p = int(input("Enter the marks in the python:"))
c = int(input("Enter the marks in the C:"))
j = int(input("Enter the marks in the java:"))

sum = m+p+c+j

per = (sum /400)*100

print(f"total mark is {sum} out of 400")
print(f"percentage is {per}")

if per >=90:
  print ("grade O")
elif per <90 and per >=80:
  print("grade E")
elif per <80 and per >=70:
  print("grade A")
elif per <70 and per >=60:
  print("grade B ")
else:
  print("you are failed")          
