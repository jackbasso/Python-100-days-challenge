'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

Warning you should round the result to the nearest whole number. 
'''

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))
verb = "are"
if bmi < 18.5:
    interpretation = "underweight"
elif bmi < 25:
    verb = "have a"
    interpretation = "normal weight"
elif bmi < 30:
    interpretation = "slightly overweight"
elif bmi < 35:
    interpretation = "obese"
else:
    interpretation = "clinically obese"

print(f"Your BMI is {bmi}, you {verb} {interpretation}.")
