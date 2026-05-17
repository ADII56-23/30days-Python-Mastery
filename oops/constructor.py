'''sample example'''

class Student:

  #initialising the constructor
  def __init__(self,age):
    #instance variable
    self.age=age

  #instance method
  def show(self):
    print(f"The age of the students {self.age}")
    
s = Student(13) #INSIDE this all are arguments
s.show()
  



'''Types of constructor'''
#default constructor

class Employee:
  #here if user forget or has not given any constructor python will help you to take a default constructor
  def show(self):
    print("inside display")

emp = Employee()
emp.show()



#non-parameterized constructor

class Employee:
  def __init__(self):
      self.name ="pynative"

  def show(self):
     print("name is ",self.name)    

emp = Employee()
emp.show()     


#parameterized constructor

class Employee:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def disp(self):
    print(f"name is {self.name} and age is {self.age} ")

emp1 = Employee("alok",22)
emp1.disp()    


'''constructor with default values'''

class Student:
  def __init__(self, name = "kirti", age =12):
    self.name =  name
    self.age = age

  def disp(self):
    print(f" the name of the student is {self.name} and age is {self.age}")

student1 = Student("ayush",23)
student1.disp()      



'''constructor overloading'''
'''in python constructor overloading is nop possible'''
class Animal:
  def __init__(self, name, type ):
    print("one argument constructor")
    self.name =  name 
    self.type = type


  def __init__(self,name):
    print("Two agrument constructor")
    self.name = name 

cat = Animal("cat")   # it will give result caus eit calls last constructor



'''constructor chaining'''
class Vehicle:
  def __init__(self,engine):
    self.engine = engine
    print("this is inside Vehicle class")

class car(Vehicle):
  def __init__(self, engine,model):
    super().__init__(engine)
    print("this is inside car class")
    self.model = model

class electric_car(car):
  def __init__(self, engine, model,price):
    super().__init__(engine, model)    
    print("this is inside the electric car class")
    self.price = price

ev = electric_car('1500cc', "x15", "750k")
print(f'Engine={ev.engine}, Model is={ev.model}, price is={ev.price}')

    
"""count the number of objects"""
class Employee:
  count  = 0
  def __init__(self):
    Employee.count = Employee.count+1 

e1 = Employee()
e2 = Employee()
e3 = Employee()
print("The no of the object is",Employee.count)


''''''
