#largest of three numbers
a = int(input("Enter the 1st number:"))
b = int(input("enter the second number:"))
c = int(input("Enter the 3rd number:"))

if a > b and a> c:
  print("a is largest")
elif b > c and b > a:
  print("b is largest")
else:
  print("c is largest ")    
