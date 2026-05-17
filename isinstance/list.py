#isinstance() with nested list

sampleList = ['Emma', 'Stevan', ['Jordan', 'Donald', 'Sam']]
for item  in sampleList:
  if isinstance(item,list):
    print(F"yes {item} contains nestedlist ")
  else:
    print("No")


#check elements of the lists are string or numbers     

sample_list = ['Emma', 'Stevan', 12, 45.6, 1 + 2j, "Eric", ]
number_list =[]
String_list =[]

for item in sample_list:
  if isinstance(item,(int,float,complex)):
    number_list.append(item)
  elif isinstance(item,str):
    String_list.append(item)

print(number_list)
print(String_list)    