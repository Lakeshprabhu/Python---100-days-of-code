# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

new_bid = True

import art

print(art.logo)

auction = {}


def online_bid(name,bid):
    auction[name]=bid
    continue_auction = (input("Do you wish to continue (yes or no) :")).lower()
    if continue_auction =="yes":
        print("\n"*20)
        bid_placer()
    if continue_auction =="no":
        return 0











def bid_placer():

    bidder_name = input("Please enter your name :")
    bid = int(input("Place your bid :"))
    online_bid(bidder_name,bid)

bid_placer()
count = 0
for bidder in auction:


    if auction[bidder] > count:
        highest_bidder = bidder
        count = auction[bidder]
    else:
        pass





print(f"The winner is {highest_bidder} with ${auction[highest_bidder]}")