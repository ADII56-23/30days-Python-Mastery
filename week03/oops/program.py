#create class student and display
class Student:
  def __init__(self,name,grade,age,percentage,term):
    self.name = name
    self.grade = grade
    self.age = age
    self.percentage = percentage
    self.term = term

  def display(self):
    print(f"{self.name} is in {self.grade} with {self.percentage}%, from team {self.term}")

Student1 = Student("aditya","O",21,85,"coder")
Student2 = Student("alok","A",19,67,"survivor")
Student1.display()     
Student2.display()

