print("Hey I am here to calculate your BMI")
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in m:"))
BMI = weight/height**2
if BMI <= 18.4:
    print("You are underweight")
elif BMI>18.5 and BMI<24.9:
    print("Congratution you are normal")
elif BMI>25.0 and BMI<39.9:
    print(" you are overweight")
else:
    print("you need to consult dr")





