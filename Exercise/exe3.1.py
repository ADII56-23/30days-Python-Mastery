#validate a username 
#the user name not more than 12 character
#not contain any space or digits

username = input("Enter a  username ")

if len(username)>12 :
  print("you are exceeding more than 12 digits")
elif not username.find(" ") == -1:
  print("you can't access ")
elif not username.isalpha():
  print("your name contains digits") 

else :
  print(f"you are welcome {username}")