class Student:

  #class attribute
  school_name = "ABC School"  

  #methods
  def __init__(self,name,age):
    #instace variables
    self.name = name
    self.age  = age
  
  def show(self):
    print("name is ",self.name,"age is",self.age, "school is ",Student.school_name)

  #instance method
  def modify_age(self,age):
      #modify instance variables
    self.age = age


  #class method
  @classmethod
  def modify_school(self,school_name):
   #modify class variables    
   self.school_name = school_name


s1 = Student("Harry", 12)
s1.show()   

s1.modify_age(17)
s1.show()

Student.modify_school("xyzz")
s1.show()