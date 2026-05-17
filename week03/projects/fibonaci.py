def Fibonnaci(num):
  a = 0 
  b = 1
  series = []
  for _ in range(num):
    series.append(a)
    a ,b  = b , a+b
  return series

print(Fibonnaci(10))
