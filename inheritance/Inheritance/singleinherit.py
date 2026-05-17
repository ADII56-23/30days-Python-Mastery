#bank-account system(single inheritance system) 
class Account:
  def __init__(self,account_holder,balance):
    self.account_holder = account_holder
    self.balance = balance 

  def show_balance(self):
    print(f"Name of the account holder is {self.account_holder}")
    print(f"balance is {self.balance}")

class SavingAccount(Account):
  def __init__(self, account_holder, balance,intrtest_rate):
    super().__init__(account_holder, balance)   
    self.intrtest_rate = intrtest_rate

  def calculate_intrest(self):
    super().show_balance()
    print(f"intrest rate is{self.intrtest_rate}")

save = SavingAccount("aditya",10000,8)
save.show_balance()
save.calculate_intrest()



#person employee
class person:       #parent
  def __init__(self,name,age):
    self.name = name
    self.age = age 

  def display_person(self):
     print(f"name of the persom is {self.name}")
     print(f"age of the person is {self.age}")

class Employee(person):     #child
  def __init__(self, name, age,employee_id,salary):
    super().__init__(name, age)
    self.emloyee_id =employee_id 
    self.salary = salary 

  def display_employee(self):
    super().display_person()
    print(f"salary is {self.salary}")
    print(f"employee id is {self.emloyee_id}")

emp1 = Employee("raj",28,1002,12000)
emp1.display_employee()
