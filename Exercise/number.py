#number guessing game
import random
print("Python number guessing game")

lowest = 1
highest = 100

gusses = 0

is_correct = True
number = random.randint(lowest,highest)

print(number)


while is_correct:
  
  num = int(input(f"Guess a number in between {lowest} and {highest} : ")) 
  if num == number:
    print("Correct")
  elif num > number:
    print("the number is too high")
  elif num < number:
    print("the number is too low")
  else:
    print("invalid")         


