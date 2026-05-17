#creating a function
def add(a,b):
  return a+b
print(add(2,3))

#function with variable length of argument
def fun1(a,b,c):
  return a,b,c
print(fun1(20,40,60))


#return multiple values from a function
def calculation(a ,b):
  return a+b,a-b
res = calculation(40,10)
print(res) 


#create a function with a default argument
def show_employee(name,salary=9000):
  print("name:",name)
  print("salary:",salary)
show_employee("Ben",12000)
show_employee("jessica")  


#create an inner function
def calculation(a,b):  #4,5
  def sum(a,b):     
    s = a+b        #9
    return s       #9
  add = sum(a,b)    #4,5
  return add +5     #14
print(calculation(4,5))

#recursive function
# def recursive(n):



#assign a diff name to function and call it through the new name
def display_student(name,age):
  print(name,age)
  def show_student(name,age):
    return display_student(name,age)
  return show_student
a= display_student("emma",21)    
a("john",32)

#