#Email validation
import re

text = "adi@gmail.com"
patten = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(patten,text):
  print("valid email")
else:
  print("invalid email")  


#email extraction
import re

email = input("Enter your Email:")
pattern = r"[\w\.-]+@[\w\.-]+\.\w+"

emails = re.findall(pattern,email)

print("Extracted Emails",emails)


#number extraction 
import re

number = input()
search = re.search(r"\d+",number)
print("number is:",search)


#password strength checker
import re
password = input("Enter your password:")

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

if re.match(pattern,password):
  print("Strong password")
else:
  print("Weak password")  

  