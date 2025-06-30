print("welcome to amusement park")
name = input("Enter your name:")
age = int(input("Enter your age to check if you are eligible to enter the roller coaster:"))
height = float(input("Enter your height in cm to check if you are eligible to enter the roller coaster:"))
heart = input("Are you a heart patient(yes/no):")
if age>18 and age<60:
    if height>158 and height<200:
        if heart=="no":
            print(f"name:{name}")
            print(f"age:{age}")
            print(f"height:{height}")
            print(f"heart patient:{heart}")
            print("Congratulation you are eligible")
        else:  
            print("not eligible cause you are a heart patient")
    else:  
        print("not eligible cause(you are potato) your height is not within 158 and 200cm")
else:  
    print("not eligible cause your age is not within 18 and 60 yrs")




            


    



