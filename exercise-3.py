# Leap Year Challenge 
# on every year that is evenly divisble by 4
# except every year that is evenly divisible by 100
# unless that year is also divisible by 400


leap_Year = int(input("Pick a year \n"))

if (leap_Year % 100 == 0) and (leap_Year % 400 == 0):
    print("This is a leap year because it's evenely divisible by 100 and 400.")
elif leap_Year % 4 == 0:
    if leap_Year % 100 == 0:
        print("This is not a leap year because it's evenely divisible by 100.")
    else:
        print("Evenely divisible by just 4 - it is a leap year.")
else: 
    print("Not a leap year.")