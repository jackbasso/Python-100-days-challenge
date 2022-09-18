'''
## Tip Calculator

# Instructions
If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Example Input
```
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
```
# Example Output
```
Each person should pay: $19.93
```
'''

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

bill_split = total / people
pay_by_person = bill_split + round(total * (tip / 100) / people, 2)
pay_by_person = "{:.2f}".format(pay_by_person) # cero at the end
print(f"Each person should pay: ${pay_by_person}")