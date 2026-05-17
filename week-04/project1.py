#Student record manager
Filename = "Student.txt"

def add_student():
  f = open(Filename, "a")
  roll = input("enter student rollno:")
  name = input("enter student name:")
  marks = input("Enter student marks:")

  record = roll + ","+ name + "," + marks + "\n"
  f.write(record)
  f.close()
  print("Student details added successfuly ")



def show_students():
 try:  
   f = open(Filename,"r")
   data = f.read()
   if data:
     print("Student records")
     print(data)
   else:
     print("No record found")
   f.close()
 except FileNotFoundError:
         print("File not found")


def update_marks():
   roll_update = input("enter roll to update:")

   try:
      f = open(Filename,"r+")
      lines = f.readlines()
      f.seek(0)

      for line in lines:
         roll,name,marks = line.strip().split(",")

         if roll_update == roll:
           new_marks = input("enter the new mark")
           line = roll + "," + name + "," + new_marks +  "\n"
           found = True
         f.write(line)
    
      f.close()

      if found:
         print("Marks uodated successfully")
      else:
         print("Not found")

   except FileNotFoundError:
      print("File not found")


while True:
   print("--Student Record manager--")
   print("1. Add student ")
   print("2. Show all student")
   print("3. upadate student marks")
   print("4. Exit")

   choice = input("Enter choice:")

   if choice == "1":
      add_student() 
   elif choice == "2":
      show_students()
   elif choice == "3":
      update_marks()
   elif choice == "4":
      print("existinggggggggg")
      break
   else:
      print("Invalid choice")


