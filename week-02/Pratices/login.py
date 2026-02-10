#Write a program to simulate a simple login system.
print("Welcome to python pratice ")

set_pin = input("Enter a pin to signup :")  
print("Welcome back!! please login")

pin = input("Enter your pin to log in:")

if pin == set_pin:
  print("Log in Success")
else:
  print("invalid pin try again")
  attemmpt =3
  for i in range(attemmpt):
    pin = input("Enter your pin")
    if pin == set_pin:
       print("Login Success")
       break   
    else:
      remaining = attemmpt-(i+1)
      if remaining >0:
       print(f"invalid pin,{remaining} attempts left")    
      else:
       print("maximum attempted,Access denied")