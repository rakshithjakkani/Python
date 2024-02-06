print("Welcome to PizzaHut")
pizza_size = input("which pizza you want s=small m=medium and l=larger\n:")
add_pepporine = input("Add pepporine ? please selete Y or N\n:")
extra_cheese = input("Add extra cheese ? Please select Y or N\n:")

bill = 0 
if pizza_size == "s":
    bill += 15
elif pizza_size == "m":
    bill += 20
else:
    bill += 25

if add_pepporine == "Y":
    if pizza_size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: Rs.{bill}")





