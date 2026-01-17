#simple calculator
a = int(input("Enter the 1st number:"))
b = int(input("enter the second number:"))
ch = input("enter the opearator:")

if ch =='+':
   print(a+b)
elif ch == '-':
   print(a-b)
elif ch == '*':
   print(a*b)
elif ch == '/':
   print(a//b)
else:
   print("invalid operator")             
