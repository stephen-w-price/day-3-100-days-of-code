# small pizza - 2
# m or l - 3
# extra cheese + 1
# pep for small = 2
# pep for medium/l = 3


print("Welcome to Python build your pizza")
size = input("What size pizza would you like? S, M, L?").upper()
add_pepperoni = input("Do you want pepperoni? Y or N").upper()
extra_cheese = input("Do you want extra cheese? Y or N").upper()
if size == "S":
  bill = 20
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y": 
    bill += 
  
  print(bill)

if size == "M" and "L":
  bill = 30
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y": 
    bill += 1

  print(bill)
ß