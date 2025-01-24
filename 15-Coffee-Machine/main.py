data = {
     "espresso": {
          'water': 10,
          'milk': 25,
          'coffe': 10
     },
     "latte": {
          'water': 10,
          'milk': 25,
          'coffe': 10
     },
     "cappuccino": {
          'water': 5,
          'milk': 25,
          'coffe': 10
     }
}
resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}
def type_of_drink(test):
     
     print

def drink(type, resources):
     print("hello rakshith")


     
profit = 0
turn_on = True
while turn_on:
    choice = input("Please enter what do you want to have (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        turn_on = False
    elif choice == "report":
            print(f'water: {resources["water"]}')
            print(f'milk: {resources["milk"]}')
            print(f'coffee: {resources["coffee"]}')
            print(f'money: {resources["money"]}')