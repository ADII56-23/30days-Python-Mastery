#reverse of a string 
str = "ADITYA"
print(str[::-1])

#count vowels and consonets
str = "ADITYA"
v_count = 0
c_count = 0
for i in str:
  if i in "aeiouAEIOU":
    v_count+=1
  else:  
    c_count+=1
print(f"Total vowel is {v_count} and total consonants is {c_count}")    