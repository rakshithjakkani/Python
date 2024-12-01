import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

properties = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide,
    }
def calculator():
    print(art.logo)
    should_continue = True
    numb_1 = float(input("Enter the number: "))
    while should_continue:
        for i in properties:
            print(i)

        property = input("Enter the operation to perform: ")
        numb_2 = float(input("Enter the next number: "))
        answer = properties[property](numb_1, numb_2)
        print(f"{numb_1} {property} {numb_2} = {answer}")
        choice = input(f"This is your answer {answer}. Do you want to continue ? if yes type 'y' if no type 'n': ")
        if choice == "y":
            numb_1 = answer
        else:
            should_continue = False
            print("\n" * 1000)
            calculator()
calculator()