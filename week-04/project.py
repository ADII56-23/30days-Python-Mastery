#sales ledger evaluater 
File = "sales.txt"

while True:
  print("welcome to Sales automation")
  print("Press 1: add product sale")
  print("press 2: view sale records")
  print("press 3: total sales amount")
  print("press 4: Exit..") 

  choice = input("Enter your choice:")
  if choice == "1":
    f = open(File,"a")
    product = input("Enter product name:")
    amount = input("enter product amount:")
    
    details = product + "," + amount +"\n"   
    f.write(details)
    f.close()
    print("Record saved")

  elif choice == "2":
    f  = open(File, "r")
    data = f.read()
    print("Sales details:")
    print(data)

  elif choice == "3":
    f = open(File, "r")
    total = 0
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 2:
            try:
                amount = float(parts[1])  
                total += amount
            except ValueError:
                print(f"Invalid amount found in record: {line.strip()}")
    f.close()
    print("Total Sales Amount:", total)


  elif choice == "4":
    print("Thanks for using our automation")  
    break  
  else:
    print("invalid Responses.....")