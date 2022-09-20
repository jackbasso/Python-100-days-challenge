import os
#clear the output in the console.

more_bidders = True
# Create a dictionary
bid_per_user = {'Test': 0}

while more_bidders:
  name = input("What is your name?  ")
  bid_amount = float(input("What's your bid?  "))
  new_user = input("Are there any other bidder? Type 'yes' or 'no'  ")
  # clear console 
  if new_user == "yes":
    os.system("cls")
  # add inputs to dict where name is the key of each bid
  bid_per_user[name] = bid_amount
  
  # highest bidder manually, there are some methods like max and min
  def highest_bidder():
    '''
    high_bid = "Test"
    for key in bid_per_user:
      if bid_per_user[key] > bid_per_user[high_bid]:
        high_bid = key
    print(bid_per_user[high_bid])
    '''
    bid = 0
    high_bidder = ""
    for key, value in bid_per_user.items():
      if value > bid:
        bid = value
        high_bidder = key
    print(f"The highest bid was made by: {high_bidder} for ${bid}") 
  
  if new_user == "no":
    more_bidders = False
    highest_bidder()


