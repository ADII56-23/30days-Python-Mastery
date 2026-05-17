#guess the word game 
import random
word = ["python","apple","john","orange","computer","engineering"]
guess_word = random.choice(word)
print(guess_word)
attempt = 5
while attempt > 0:
   guess = input("Guess a word:")
   attempt -=1
   if guess == guess_word:
      print("You gueess the correct !!")
      break
   else:
      print("guess once more")
if attempt == 0:
      print("game over")
      