# check for multiple conditions in the same line of code
# How would we be able to check multiple conditions in the same line of code? 
# A and B - both have to be true for the line of code to work.
# C or D - only one needs to be true.

height = int(input("What is your height?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay 7")
    elif age <= 55 and age >= 45:
        bill = 0
    else:
        bill = 12
        print("Please pay $12.")
    
    wants_photo = input("Do you want a photo take? Y or N. ").upper()
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is {bill}")
else:
    print("Sorry you cannot ride the rollercoaster")