#vehicle hierachy(multilevel inheritance)
class vehicle:                 #parent class
  def __init__(self,brand):
    self.brand = brand

  def start(self):
    print(f"The vehicle is from {self.brand} brand")

class Car(vehicle):            #child class 1 
  def __init__(self, brand,model):
    super().__init__(brand)
    self.model = model
    print(f"The car is of {self.model} model")

  def car_info(self):
    super().start()
 
class ElectricCar(Car):          #child class 2
  def __init__(self, brand, model,battery_capacity):
    super().__init__(brand, model)
    self.battery_capacity = battery_capacity
    print(f"The battery capacity of this car is {battery_capacity} hours")
   
  def disp(self):
    super().car_info()  

car1 = Car("Audi","M6")
car1.car_info()            

car2 = ElectricCar("BMW","X7",36)
car2.disp()