print("Welcome to the auction bidder program!")

# Import logo from art.py and clear() function from replit
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

# To need to know who is the highest bidder create new function 
def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]

    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f'The winner is {winner} and the bid is {highest_bid}$')

# Create the function that name and price are inputs
while not bidding_finished:
  name = input("What is your name? \n").upper()
  price = int(input(f"What is the {name}'s bid?\n"))

  bids[name] = price
  should_continue = input("Are there any other bidder? Type 'yes' or 'no'.\n")
  if should_continue == 'no':
    highest_bidder(bids)
    bidding_finished = True
   
  elif should_continue == 'yes':
    clear()
