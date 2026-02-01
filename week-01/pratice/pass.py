password = input("enter password")
while password != "admin":
  print("access denied")
  password= input("enter password")   
else:
  print("password success")