#ATM pin validation
attempt = 3
pin = "ADMIN"
while attempt >0:
  input_pin = input("Enter your pin :")
  if input_pin == pin:
    print("Welcome back!!")
    break
  else:
    attempt -=1
    print(f"You have entered wrong pin !! {attempt} attempts left") 
  if attempt == 0:
   print("ATM is blocked ") 