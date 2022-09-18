'''
Instructions
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
https://en.wikipedia.org/wiki/Prime_number
You need to write a function that checks whether if the number passed into it is a prime number or not.
e.g. 2 is a prime number because it's only divisible by 1 and 2.
But 4 is not a prime number because you can divide it by 1, 2 or 4.
'''

#Write your code below this line 👇
def prime_checker(number):
    prime = 0
    for num in range(1, 100): 
        if number % num == 0:
            prime += 1
    if prime > 2:
        print("It's not a prime number")
    else:
        print("It's a prime number")
