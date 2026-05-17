#calculate sqrt of a number without using inbuilt function
n = int(input("enter a  number:"))
num = n **(1/2)
print(num)

#given an array range(1-n), find the number which is not present in the array

def array(n): 
  li = []
  li1 = [1,2,4,5,6,7,8,9]
  for num in range(1,n+1):
      li.append(num)
      if li == li1:
        return True
      else:
          
        print(num)
print(array(9))