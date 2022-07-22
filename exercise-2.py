height = float(input("What is your height?"))
weight = float(input("What is your weight"))

bmi = round(weight / (height * height))


if bmi < 18.5:
    print("You are underwieght")
elif bmi > 18.5: 
    print("Normal weight")
elif bmi > 25:
    print("Overweight")
elif bmi > 29:
    print("Obese")
else:
    print("Clinically obese.")





