from art import logo
print(logo)
def find_highest_bidder(bidding_dictionary):
    winner = ''
    highest_bid = 0

    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
condition = True
while condition:
    # Taking inputs
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    # Storing input data in dictionary
    bids[name] = price

    # Checking if further looping is necessary
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == 'no':
        condition = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print("\n" * 20)