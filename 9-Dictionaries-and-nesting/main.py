import art
print(art.logo)
def winner_fun(highest_bid):
    winner = ""
    highest_bid_amount = 0
    for bidder in highest_bid:
        bid_amount = highest_bid[bidder]
        if bid_amount > highest_bid_amount:
            highest_bid_amount = bid_amount
            winner = bidder
    print(f"winner is {bidder} with bidding amount ${highest_bid_amount} 🏆 👑 💥")

bid = {}
condition = True
while condition:
    name = input("what is your name?: ")
    amount = int(input("what is your bid amount?: $"))
    bid[name] = amount
    should_continue = input("any other to bid? type 'yes' otherwise type 'no': ").lower()
    if should_continue == "yes":
        print("\n" * 100)
    elif should_continue == "no":
        winner_fun(bid)
        print(art.winner)
        condition = False
    else:
        print("you entered invalid answer. Please enter yes or no")


    

