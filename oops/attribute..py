class Student:
  name = "Riya"               #class attributr

  def __init__(self,age):
    self.age= age             #instance attribute
    print(age) 
    
a = Student(18)
print(a.name)
