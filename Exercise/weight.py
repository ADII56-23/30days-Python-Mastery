#weight convertor program

weight = float(input("Enter your weight "))
unit = input(" kilogram or pounds (K or P):")

if unit == "K":
  weight = weight * 2.205
  unit ="Lbs"
print(f"your weight is {weight} {unit} ")