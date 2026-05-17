#instance with multiple classes
def check_number(num):
  if isinstance(num,(int,float)):
    print("The", num , "is a instance of int and float" )
  else:
    print("The", num , "is not a instance of int and float")

check_number(89)      
check_number(90.88)
