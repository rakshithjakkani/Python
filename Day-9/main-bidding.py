from replit import clear
ask_for_continue = False
should_continue = ""
bid_dict = {}
def find_highest_bidder(bidding_record):
    highest_bid = 0 
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {bidder} with the bid of Rs.{highest_bid}")
while not ask_for_continue:
    from art import logo
    print("..............WELCOME TO SECRET BIDDING................")
    print(logo)
    name = input("What is your name.?: ")
    price = int(input("What is your bid amount.?: "))
    bid_dict[name] = price
    should_continue = input("want to continue to bidding.? type yes or no: ")
    if should_continue == "no":
        ask_for_continue = True
        find_highest_bidder(bid_dict)
    elif should_continue == "yes":
        clear()





