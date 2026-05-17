# #A 2Dimentional list

# fruits =     ["apple" , "banana" , "pineapple" , "pice"]
# vegetables = ["onion" , "garlic" , "potato" "peas"]
# meats =      ["chicken" , "fish" , "pig"]
# Grocories = [fruits,vegetables,meats]
# # fruits[0] = "pineapple"
# # print(fruits)
# print(Grocories[2][2])


Grocories = [["apple" , "banana" , "pineapple" , "pice"],
             ["onion" , "garlic" , "potato" "peas"],
             ["chicken" , "fish" , "pig"] ]

for collection in Grocories:
  for food in collection:
    print(food , end =" ")
