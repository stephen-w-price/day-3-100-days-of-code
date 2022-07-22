if condition:
    do this 
else: 
    do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry!")

# Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to 
# <= Lesser than or equal to 
# == Checking to see if it is equal 
# = Assignment
# !=


# Nested if statements and elif statements
# elif - you can add as many as you want
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
    else:
        bill = 12
        print("Please pay $12.")
    
    wants_photo = input("Do you want a photo take? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is {bill}")
else:
    print("Sorry you cannot ride the rollercoaster")



# Multiple if statements in succession 

# MULTIPLE IF - With multiple if conditions can be executed as long as they are true. 
# if condition1:
#   do A
# if condition2: 
#   do B
# if condition3:
#   do C



# IF / ELIF / ELSE - With If, elif and else only one condition can be true. Or the first condition true will complete the code. 

# if condition1:
#   do A
# elif condition2:
#   do B
# else condition3:
#   do C
# How would we be able to check multiple conditions in the same line of code? 
# A and B - both have to be true for the line of code