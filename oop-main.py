from art import logo
import os
from oopcheckbid import CheckBid

clear = lambda: os.system('cls')

print(logo)
print("Welcome to the secret auction program.")

bidding = True
bidders = {}
check_bid = CheckBid()

while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    other_bids = input("Are there other bidders? Type 'ye's or 'no': ").lower()
    if other_bids == "no":
        winner = check_bid.check(bidders)
        print(winner)
        bidding = False
    elif other_bids == "yes":
        clear()