import os
#clear the output in the console.

bids_list = []

more_bidders = True
while more_bidders:
  name = input("What is your name?  ")
  bid_amount = float(input("What's your bid?  "))
  new_user = input("Are there any other bidder? Type 'yes' or 'no'  ")
  # Create a dictionary
  bid_per_user = {}
  bid_per_user["user_name"] = name
  bid_per_user["bid"] = bid_amount

  # Add dictionary to list
  bids_list.append(bid_per_user)
  
  if new_user == "no":
    more_bidders = False

print(bids_list)

