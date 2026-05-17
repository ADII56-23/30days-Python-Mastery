# name = "Danny"
# age = 32

# # print(type(name))

# print(type(age))


class Dog:
  def __init__(self,name):
    self.name = name
    print(name)
    
  def add_one(self,x):
    return x+1
  
  def bark(self):
    print("bark")

d=Dog("tim") 
print(d.bark())
print(d.add_one(6))

