# Functions with outputs

def format_name(name, lastname):
  name = name.title()
  lastname = lastname.title()
  #str = "jadfj"
  return print(f'{name} {lastname}')
  #return print(f'{str.title()}')

name = input("What is your name? \n")
lastname = input("What is your lastname? \n")

format_name(name, lastname)