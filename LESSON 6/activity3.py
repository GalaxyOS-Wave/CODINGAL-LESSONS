height = float(input("enter your height in cm"))
weight = float(input("enter your weight in KG's "))

BMI = weight / (height/100)**2
print("Your BMI is",BMI)

if BMI <= 18.4 :
    print("you are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9 :
    print("You are overweight")