MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffe": 18,
        }, 
        "cost": 1.5,
    }, 
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.8,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_off = True

def process_coins():
    """This function is using to process the coins"""
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes ?: ")) * 0.1
    total += int(input("How many nickles ?: ")) * 0.05
    total += int(input("How many pennies ?: ")) * 0.01
    return total

def is_resources_sufficient(drink_resources):
    """This function will check whether enough resources available in the machine or not"""
    for item in drink_resources:
        if resources[item] >= drink_resources[item]:
            print(f"Hey Congratulations! Resources available for the {choice}")
            return True
        else:
            print(f"Sorry! {choice} resources not available at the movement. ")
            return True


def is_transaction_succeful(payment, drink_price):
    """Function to check the money that user has given and change to be given back to user"""
    if payment >= drink_price:
        global change
        global profit
        change = payment - drink_price
        profit += drink_price
        print(f"payment succesful here is your change ${change}")
        return True
    else:
        print(f"Please insert enough money. Your money ${payment} has refunded")
        return False

def make_coffee(order_ingredience):
    """Function to substract the values from the available resources"""
    for item in order_ingredience:
        resources[item] -= order_ingredience[item]
    print(f"here is your drink {choice} ☕")

    


while is_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_off = False
    
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succeful(payment, drink["cost"]):
                make_coffee(drink["ingredients"])
                