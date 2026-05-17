#shopping cart calc

item = input("What you want to buy ")
price = float(input("What is the price "))
quantity = int(input("how much quantity ")) 

total = price * quantity
print(f"you have brought {quantity} {item}")
print(total)