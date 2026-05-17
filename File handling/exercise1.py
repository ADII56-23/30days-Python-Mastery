##simple bank account system
File_name = "account.txt"

def account():
  f = open(File_name,"a")
  name = input("enter name:")
  init_bal = input("enter your balance:")

  record = name +"," + init_bal + "\n"
  f.write(record)


def check_balance():
   f = open(File_name,"r")
   line = f.readlines()
   name = input("Enter your name:")

   for name in range():
     if name ==   

# for choices 
while True:
  print("===Simple bank account System===")
  print("1. create account ")
  print("2. check balance")

  choice = input("Enter choice:")
  
  if choice == "1":
    account()
  elif choice == "2":
    check_balance()

  else:  
    print("Exit")
    break

 