#create a python programming that manage and analysis student marks using build-in functions

subject = int(input("Enter the number of subjects:"))
li = []
for i in range(0,subject):
  marks=float(input("Enter individual marks:"))  
  li.append(marks)  
if all(0<= marks <= 100  for marks in li):
  print("all marks are valid")
else:
  print(f"{marks} is not valid")  

total = sum(li)  
m = max(li)
n = min(li)
s = sorted(li)
print("your total marks is",total)
print("your minimum marks is:",n )
print("your maximum marks is:",m )
print(s)
