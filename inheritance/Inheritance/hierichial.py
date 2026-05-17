#Company structure
class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary

  def display_basic(self):
    print(f"The name of the employee is {self.name}")
    print(f"The salary is {self.salary}")

class Developer(Employee):
  def __init__(self,name,salary,age):
    super().__init__(name,salary)
    self.age = age

  def display_developer(self):
    super().display_basic()
    print(f"the age of the developer is {self.age}")

class Designer(Employee):
  def __init__(self,name,salary,age,experience):
    super().__init__(name,salary)     
    self.experience= experience
    self.age = age

  def display_Designer(self):
    super().display_basic()
    print(f"The age of the designer is {self.age}")
    print(f"The designer is {self.experience} years")

emp1 = Designer("priya",35000,23,1)
emp1.display_Designer()            
