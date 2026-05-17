#user defined exception/ constumised exception 
class TooYoungExcetion(Exception):
  def __init__(self, arg):
    self.msg = arg
class ToooldException(Exception):
  def __init__(self,arg):
    self.msg = arg

age = int(input("enter your age:"))
if age > 60:
  raise ToooldException("your age is too old")    
elif age < 18:
  raise TooYoungExcetion("your age is too young")
else:
  print("match soon")
       