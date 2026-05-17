#COMPOUUND  intrest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
   principle = float(input("enter the principal amount :"))
if principle <= 0:
   print("principle can't be 0 or lessthan 0") 
print(principle)

while rate <= 0:
   rate = float(input("enter the rate of intrest"))
if rate <= 0:
   print("Rate of intrest cant be negative") 
rate= rate/100   
print(rate)      

while time <= 0:
   time = int(input("enter the time"))
if time <= 0:
   print("enter a valid time ") 
print(time)  
n = 1
total = principle * pow((1 + rate/n ),n*time)

print(f"total amont after {time} years is {total}")