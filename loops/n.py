num = int(input("enter a number:"))
if num % 2 == 0:
  if num % 4 == 0:
    print("number is divisible by both 2 and 4")
  else:
    print("num  is not divisible by 4 but even")
else:
  print("odd!!")      