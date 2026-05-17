#sleep()

import time

x = int(input("Enter the time in seconds :"))

for x in reversed(range(1,4)):
   
  print(x)
  time.sleep(2)

print("TIME'S UP!!")