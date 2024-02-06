print("Welcome to the tip calculator!")
# Take the input from user and convert it into float or int using flaot or int functions
bill = float(input("what was the total bill?: Rs."))
# Take the input from user and convert it into float or int using flaot or int functions
tip = int(input("How much tip you wanna give? 10 12 14 15 ?:"))
# Take the input from user and convert it into float or int using flaot or int functions
people = int(input("How many people are going to share the bill?:")) 

# calculate the tip amount out of percentage
tip_per = tip / 100

# multiply the tip and bill, so that we will get total tip that has to add to actual bill
total_tip_amount = tip_per * bill 

# add the tip amount and the bill to get total bill 
total_bill = bill + total_tip_amount

# Print the total bill
print(f"this is your {total_bill} total_bill")

# devide the total bill among the number of people 
per_head_bill = total_bill // people

# round function limits the decimal numbers. lets say we have 2.3456 and this round("2.3456",1) then it limits to 2.3 if ("2.34199",2) = 2.35
# final_amount = round(per_head_bill, 1)

# this is to print the zero after decimal number.
# final_amount = "{:.2f}"format(per_head_bill, 1)

# print the per head bill 
print(f"Each person has to pay {per_head_bill} rupees")
