# for i in range(1,6):
#   for j in range(0,5):
#     print("*",end="")
#   print(" ")  


# for i in range(1,6):
#   print("*" * i )


# for i in range(5,0,-1):
#   print( "*" * i) 


# for i in range(1,6):
#     for j in range(1,i+1):
#       print( j,end=" " )
#     print()

n = int(input("Enter the rows :"))  #5
for i in range(1,n):                  #ranges for row
  for j in range(1,n+1):            #for coloum 
    print(j,end=" ")                # end= " " for colom gap 
  print()                             #for new line of row