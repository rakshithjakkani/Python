print("Welcome to JAKKANI's restuarent. here is your bill $128.50")

bill = 128.50
tip = int(input("how much percentage you want to give tip ?: "))

tip /= 100
total_tip = tip * bill
total_bill = bill + total_tip
actual_bill = round(total_bill, 2)
print(f"this is your total bill sir {actual_bill}")

spplit_bool = input("do you want to split it sir ?")

if spplit_bool == "yes":
    split_number = int(input("among how many members sir ?"))
    final_bill = actual_bill / split_number
    print(f"this is your split amount: {final_bill}")

else:
    print(f"please play amount {actual_bill}")