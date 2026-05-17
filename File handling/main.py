
# def createfile():

#  print("press 1 for create a file :")
#  print("press 2 for reading a file :")
#  print("press 3 for update a file :")
#  print("press 4 for delete a file :")

# check = int(input("please tell your response:"))

file = open("Function/F1.py","r")
print(file.read())     # read the whole file
print(file.readlines())#read line at a time
file.close()           #used to close the file
