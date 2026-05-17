#isinstance with inheritance

class Developer:
  def __int__(self,name):
    self.name = name

  def disp(self):
    print(f"The auuthor is {self.name}")


class python_developer(Developer):
  def __init__(self,name,book):
    self.name = name
    self.book = book

  def disp(self):
     print(f"The author of {self.book} is {self.name}")    
  
dev = python_developer("Eric", "python")

print(isinstance(dev,python_developer))

print(isinstance(dev,Developer)) #true because the chile class is the subclass of parent Developer

dev.disp()