print("Welcome to even odd number teller!")
input_number = int(input("what number do you want to check ? :"))
second_number = int(input("what number do you want to check ? :"))

devided = input_number % second_number 
print(devided)


if devided % 2 == 0:
    print("the remainder is even number")
else:
    print("the remainder is odd number")
    