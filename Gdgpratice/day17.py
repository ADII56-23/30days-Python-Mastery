#prime number exist in betweeen a range

def is_Prime(n):
  primes=[]

  for num in range(2,n+1):
     count = 0
     for i in range(1,n+1):
         
       if num % i == 0:
         count += 1
        
     if count == 2:
        primes.append(num)
          
  print(primes)

n = int(input("enter range:"))
is_Prime(n)

#reverse of  a string
string = "Ram is a Good boy"
word = string.split()
print(word)
for i in range(0,len(word)):
 word.reverse()

print(word)  
rev_string = " ".join(word)

print(rev_string)
