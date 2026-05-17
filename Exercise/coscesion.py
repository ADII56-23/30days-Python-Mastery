#consseion stand program

menu = { "pizza": 5.00,
          "chocolate": 2.00,
          "coke": 9.99,
          "chips":2.89  
          }
cart = []
total = 0

print("--------------------")
for key,value in menu.items():
  print(f"{key:10}: ${value:.3f}") 

while True:
   food  = input("Enter the food name (press q to quit) ").lower()
   if food == "q":
    break
   elif menu.get(food) is not None:
    cart.append(food)

for food in cart:
  total+=menu.get(food)
  
  print(food)

print(f"your total bill ${total:.2f}") 

  
