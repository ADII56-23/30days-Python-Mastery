#default argument
def sum(a=8,b=9):
  return a+b

print(sum())

#keyword arguments
def greet(age,name="adii"):
  print(name,age)

greet(age= 21 , name="rahul")

