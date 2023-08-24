from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

# creating the empty dictionary
bidder_dictionary = {}


# To determine who's the highest bidder
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bidding_record:
        bid_price = bidding_record[key]
        if bid_price > highest_bid:
            bid_price = highest_bid
            winner = key
            print(f"The winner is {winner} with a bid of {highest_bid}")


print(logo)

is_on = True

while is_on:
    name = input("What is your name?: ").title()

    bid_amount = int(input("What's your bid?: "))
    bidder_dictionary[name] = bid_amount

    bidder = input("Are there anyother bidders? Type 'yes' or 'no': ").lower()

    if bidder == "yes":
        clear()
    elif bidder == "no":
        highest_bidder(bidder_dictionary)
        is_on = False
