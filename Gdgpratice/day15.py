#total sum using recursion 
def sum(n):
  if n == 0:
    return 0
  else:
    return n + sum(n-1)
n= int(input())
print(sum(n))  

#enter a string and find ith given character
def char(s,c):
    if c in s:
      return f"{c} found at index {s.index(c)}"
    else:
      return "character not found"
s = input("enter the string:")
c = input("Enter the letter:")
print(char(s,c))     