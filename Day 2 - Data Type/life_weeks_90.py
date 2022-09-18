'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
'''

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remain_years = 90 - int(age)
days = remain_years * 365
weeks = remain_years * 52
months = remain_years * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
