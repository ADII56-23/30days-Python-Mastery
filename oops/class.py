''' class examples'''

class Person:
  ''' inside the class but outside the method is class variable'''
  organisaton = "MNC"


  def __init__(self,name,sex):
    ''' inside the __init__ every class is instance'''
    self.name=name
    self.sex= sex

  def show(self):
    print(f"The name of the employee is {self.name} and sex is {self.sex}")

  def work(self,position):
    self.position = position
    print(f"{self.name} is in the {self.position}")

person1 =   Person("jessa","Female")
person1.show()
person1.work("developer")

person2 = Person("Harry","male")
person2.show()

#we can modify the instance variables with dot notation
person2.name = "john"
person2.sex = "bi"
person2.show()

#we can access and modify the class atributes like shown below using classname.class atribute
print("he is working in",Person.organisaton)


Person.organisaton = "Amazon"
print("He is working in ",Person.organisaton)





class Addition:
  def __init__(self,a,b):
     print(a+b) 
v = Addition(2,3)


class Animal:
   species = "Dog"  #attribute

   def mak_noise(self):  #method
      print("Bark")      # inside the mak_noise is all parameters 

a = Animal()             #inside the object which we passes is argument
a.mak_noise()           #call method
print(a.species)



