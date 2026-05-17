#instance with python class  syntax: isinstance(object, class info)
#here we will check the object is belongs to which class

class Employee:
  def  __init__(self,name,age):
    self.name= name
    self.age = age
  
class Person:
  def __init__(self,name,sex):
    self.name = name
    self.sex = sex

emp = Employee("aditya", 22)
person1 = Person("asish","Male") 

print(isinstance(emp,Employee))
print(isinstance(person1,Employee))
