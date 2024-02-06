age = input("Enter your current age:")
years = input("How many years would you think, you lived for:")

# the age and years outputs are in string. we have convert it into integer and then do subtraction.
years_left = int(years) - int(age)

# per year we have 52 weeks average.
weeks_left = years_left * 52

# the f-String is used to print the aboave defined variable.
print(f"You have {weeks_left} weeks left in your life")

