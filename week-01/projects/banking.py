#Mini banking project

print("Welcome to Your bank!!")

li = []
total = 0
i = 2
while i<=2:
 i+=1 
 operation= input("Enter the operation : Deposit,Withdraw,check,history(enter E for EXIT) ")
 if  operation == 'd':
      a=int(input("Enter the amount you want to deposit:"))
      for i in range(0,1):
       li.append(a)
 
      print(f"The amount {a} is deposited")
      total +=a
 elif operation == 'b':
    pin=int(input("Enter your pin:"))
    pin =123
    for i in range(3):
       i=input("enter your pin again:")
       if i == pin:
        print("Your account balance is",total)
       else:
        print("You have entered wrong PIN")       
      
 elif operation == "e":
  print("Your transaction successfully")  
  break
else:
  print("Thank you")