import os

all_bids = {}
more_bidders = True

while more_bidders:
    name = input("Enter your name: ")
    bid = int(input("Enter your bidding amount: "))

    all_bids[name] = bid

    while True:
        more_bid = input("\nAre there more bidders? Type yes or no: ").lower()
        if more_bid == "yes":
            print("\n" * 100)
            break
        elif more_bid == "no":
            more_bidders = False
            break
        else:
            print("Invalid input. Please type yes or no.")

highest_bidder_name = ""
highest_bidder_bid = 0

for name in all_bids:
    if all_bids[name] > highest_bidder_bid:
        highest_bidder_bid = all_bids[name]
        highest_bidder_name = name

print(f"The highest bidder is {highest_bidder_name} with a bid of {highest_bidder_bid}.")

