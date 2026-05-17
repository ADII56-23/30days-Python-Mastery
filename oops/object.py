class Fruit:
  def __init__(self,name,color):
    self.name= name
    self.color= color

  def disp(self):
    print(f"The fruit is {self.name} and colour is {self.color}")

# creating object of the class
obj = Fruit("Apple", "red")

#modifyig object prop
obj.name = "Strawberry"

#deleting obj prop
del obj.color
print(obj.color)

#deleting object
del obj
obj.disp()