#Shopping cart programm

foods = []
prices = []
total = 0

while True : 
  food = input("Enter the food you want to buy(q to QUIT)  ")

  if food.lower() == "q":
    break 
  else:
    price = float(input(f"Enter the price of the {food} :"))    
    foods.append(food)
    prices.append(price) 
print(" ___Your Cart ____")

for food in foods:
   print(food,end=" ")

for price in prices:
  total += price
print(f"the total price is {total}")   
