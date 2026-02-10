#mini calculater for a shop
def purchase_amount(amount):         
   if amount >= 1000:
    return amount* 0.10   
   return 0
  
def costumer_discount(costumer_type,amount):   
   if costumer_type == "p" and amount >=2000:
      return amount * 0.05
   return 0

def final_amount(amount,costumer_type):
  d1 = purchase_amount(amount)
  d2 = costumer_discount(costumer_type,amount)

  discount = max(d1,d2)

  if discount > amount:
    discount = amount

  payable = amount - discount
  if  payable < 0:
    payable = 0

  print("Your total amount is",amount)
  print("your discount amount is ",discount)
  print("Your payable amount is ",payable)


final_amount(5600,"p")
