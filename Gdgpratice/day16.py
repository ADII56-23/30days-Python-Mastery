#convert decimal to binary
def con_bin(num):
  return bin(num)

num = int(input("Enter a digit:"))
print(con_bin(num))

num = int(input())
binary = " "
while num > 0:
  rem = num % 2 
  binary = str(rem) + binary 
  num = num //2
print(binary)

#addition of two matrix
a = [[1,2,4],
     [2,3,4]]

b = [[1,2,4],
     [2,3,4]]

result = [[0,0,0],
          [0,0,0]]

for i in range(len(a)):
  for j in range(len(b[0])):
    result[i][j] = a[i][j] + b[i][j]
print(result)       