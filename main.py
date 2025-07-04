height = (input("Please enter your height (M): "))
while not(height.isnumeric()):
    print("wrong input! please enter a number")
    height = (input("Please enter your height (M): "))
else:
    weight = (input("Please enter your weight (Kg): "))
    while not(weight.isnumeric()):
        print("wrong input! please enter a number")
        weight = (input("Please enter your weight (Kg): "))

weight = float(weight)
height = float(height)

if height > 3:
    height = height / 100

bmi = round(weight / height ** 2, 1)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("under weight")
elif bmi < 25:
    print("normal weight")
elif bmi < 30:
    print("over weight")
elif bmi < 35:
    print("obese weight")
else:
    print("clinically obese")
