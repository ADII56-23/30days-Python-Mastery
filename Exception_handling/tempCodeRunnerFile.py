'''ATM PIN probblem'''
try:
  pin = int(input("Enter your pin  :"))
  print("PIN Accepted")
except ValueError as e:
  print("Please enter only numbers",e)

finally:
  print("Transation begins")
