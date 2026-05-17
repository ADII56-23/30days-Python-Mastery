class point:
  def __init__(self,x,y):
    self.x  = x
    self.y = y
  def __add__(self,other):
    return self.x + other.x, self.y + other.y
  
p1 = point(1,2) 
p2 = point(3,4)
print(p1+p2) 

  
#comparision operator overloading
class Student:
  def __init__(self,marks):
    self.marks = marks
  def __gt__(self, other):
     return self.marks > other.marks
s1 = Student(90)
s2 = Student(89)
print(s1>s2)    