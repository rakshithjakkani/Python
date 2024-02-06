# This is calculator which calculates the human BMI  
# The formula for calculating the BMI is weight/height ** 2
weight = int(input("What is your current Weight:"))
height = float(input("What is your current height:"))
# make the mathematical operation's result as a integer
result = int(weight / height ** 2)

# bmi = int(result)
# print(bmi)

# print the bmi result.
print(result)