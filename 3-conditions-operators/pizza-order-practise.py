print("welcome to pizza Delieveries!")
size = input("which size pizza you want? S, M or L ?: ")
pepporoni = input("Do you want pepperoni on your pizza ? y or n: ")
extra_cheese = input("Do you want extra cheese on your pizza ? y or n: ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you entered incorrect inpute. Please check your inpute")

if pepporoni == "y":
    if size == "M":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Please pay ${bill} to deliver your pizza")
    

