def greet(name):
  print(f"Hello !! welcome {name}")

greet("adii")
greet("alok")  


def add(a,b):
  return a+b
s=add(2,3)
print(s)

class Person:
 def __init__(self,name):
    pass          #pass is used if there is some errors in the code it will also pass them 
    self.name = name

p = Person("adiii")
print(p.name)