#count the each element of a array
arr = [2,2,4,22,11,4,11]
freq = {}
for i in arr:
  if i in freq:
    freq[i] += 1
  else:
    freq[i] = 1
print(freq)       

#find the largest element in a array
arr = [22,33,15,4,43,90,89]
largest = arr[0]
for i in range(len(arr)):
  if arr[i] > largest:
    largest = arr[i]
print(f"largest element of the array is {largest}")    

