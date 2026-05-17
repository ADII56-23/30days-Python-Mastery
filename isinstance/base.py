# these are built in types
num =20
print(isinstance(num,int))

num1= 23.33
print(isinstance(num1,str))

num2 = 4+ 2j
print(isinstance(num2,complex))

word = "he is a good person"
print(isinstance(word,str))

li = [22,3,3,21]
print(isinstance(li,list))

tup = (22,33,"dog",23.89)
print(isinstance(tup,tuple))

dict = {
  "name": "aditya",
  "marks": 22

}
print(dict)
print(isinstance(dict,set))