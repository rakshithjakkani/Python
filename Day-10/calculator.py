# Import the art module which we defined in anther file called art.py
from art import logo
# addition
def addition(n1, n2):
    return (n1 + n2)
# print(addition(2, 3))

# subtraction
def subtraction(n1, n2):
    return (n1 - n2)
# print(subtraction(2, 3))

# multiplication
def multiplication(n1, n2):
    return (n1 * n2)
# print(multiplication(2, 3))

# division
def division(n1, n2):
    return (n1 / n2)
# print(division(2, 3))

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
def calculator():
    print(logo)
    num1 = int(input("what's the first number ?: "))
    for symbol in operations:
        print(symbol)
    should_ccontinue = True
    while should_ccontinue:
        pick_operation = input("pick the operation from the above list: ")
        num2 = int(input("what's the next number ?: "))
        calculation_function = operations[pick_operation]
        answer = calculation_function(num1, num2)
        print(f"{num1} {pick_operation} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, Type 'n'to start new calculation: ") == "y":
            num1 = answer
        else:
            should_ccontinue = False
            calculator()
calculator()


# pick_operation = input("pick another operation: ")
# num3 = int(input("what's the number ?: "))
# calculation_function = operations[pick_operation]
# second_answer = calculation_function(calculation_function(num1, num2), num3)
# print(f"{answer} {pick_operation} {num3} = {second_answer}")

