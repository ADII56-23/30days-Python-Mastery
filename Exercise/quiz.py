#quiz game
questions = (("Which planet is known as the Red Planet?"),
             ("Who wrote the play Romeo and Juliet?"),
             ("What is the chemical symbol for gold?"),
             ("Which gas do plants absorb from the atmosphere?"),
             ("Which country is the largest by land area?"))

options = (("a) Venus" , "b) Mars ", "c) Jupiter ", "d) Saturn "),
           ("a) Leo Tolstoy ", "b) Mark Twain ", "c) William Shakespeare ", "d) Charles Dickens "),
           ("a) Ag ", "b) Au ", "c) Pb " ,"d) Fe "),
           ("a) Oxygen ", "b) Nitrogen " , "c) Carbon dioxide ", "d) Helium "),
           ("a) Russia ", "b) Canada ", "c) China ", "d) United States "))

answers = ("b)" ,"c)","b)","c)","a)")

guesses = []
score = 0
question_num = 0

for question in questions:
  # for quiz in question: 
  #  print(quiz, end="")
  # print()  
  print("------------") 
  print(question)

  for option in options[question_num]:
   print(option)

  guess = input("Enter the answer ") 
  guesses.append(guess)

  if guess == answers[question_num]:
    score+=1
    print("correct")
  else:
    print("incorrect")
    print(f"{answers[question_num]}is the correct one!!!")
  question_num+=1  

print("-------result--------")

score = int(score / len(questions)*100)
print(f"yooo!! you scored {score}% of total")