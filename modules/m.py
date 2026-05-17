import random
def roll_dice(times = 5):
  rolls = []
  for _ in range(times):
    rolls.append(random.randint(1,6))
  return rolls

def play_round(round_numbers):
  print(f"--{round_numbers}--")

  player1_rolls = roll_dice()
  player2_rolls = roll_dice()

  p1_total = sum(player1_rolls)
  p2_total = sum(player2_rolls)

  print(f"player1 rolls : {player1_rolls} total  is {p1_total}")
  print(f"player2 rolls : {player2_rolls} total  is {p2_total}")

  if p1_total > p2_total:
    print("player 1 wins")
  else:
    print("player 2 wins")  
    
play_round(5)
