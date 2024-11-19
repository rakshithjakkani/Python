print("Welcome to JAKKANI's restuarent")


bill = float(input("what was the bill ?: $"))
tip = int(input("how much percentage you want to give tip ?: "))

total_bill = tip / 100 * bill + bill
actual_bill = round(total_bill, 2)
print(f"this is your total bill sir ${actual_bill}")

spplit_bool = input("do you want to split it sir ?: ")

if spplit_bool == "yes":
    split_number = int(input("among how many members sir ?"))
    final_bill = actual_bill / split_number
    print(f"this is your splitted amount: ${final_bill}")

else:
    print(f"please play amount ${actual_bill}")