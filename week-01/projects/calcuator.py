a = int(input("Enter  first integer:"))
b = int(input("Enter second integers")) 
ch = input("enter the operator(+,-,*,/)")
if ch == '+':
  print(a+b)
elif ch == '-':
  print(a-b)
elif ch =='*':
  print(a*b)
elif ch =='/':
  print(a/b)
elif ch =='//':
  print(a//b)  
else:
  print("invalid opeerator")     