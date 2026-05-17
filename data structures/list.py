# n= [5, 2, 9, 1, 5, 6,9,9]
# n.append(10)        #adding 10 to the last of the list
# n.insert(1,8)       # adding 8 in index 1 of the list
# n.extend([9,8,7])   #add multiple elements at the last of the list
# n.remove(5)         #removes the 1st 5 of the list
# n.sort()            #sorting in ascending order
# n.reverse()         #in reversing order   
# a= n.count(9)       #count the specific numbers

# n.clear()           #clear all the elemenst of the list
# print(a) 



#--------------pratice--------------------
#print positive and negative elements of the list

# li = [2 ,3, 9, -1, 9, -4, 7 ]
# a = len(li)
# print("positive numbers are:")
# for i in range(0,a):
#   if li[i] > 0:
#     print(li[i],end=" ")

# print("\n nagetive numbers are:")
# for i in range(0,a):    
#   if li[i]<0:
#     print(li[i],end=" ")  



# mean of the list
# li = [2 ,3, 9, -1, 9, -4, 7 ]
# a = len(li)
# total = 0
# for i in range(0,a): 
#   total+=li[i]
# print(total//a)   


#greatest elemenst and print its index
li = [2 ,3, 9, -1, 9, -4, 7 ]
a = len(li)

biggest = li[0]
index = 0

for i in range(a):
  if  li[i] > biggest:
    biggest=li[i]
    index=i
print(f"the biggest element in the list is {biggest} and index is {index}")    

