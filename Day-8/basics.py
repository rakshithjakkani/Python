####### Function inputs
# simple function
def greet():
    print("Hello Rakshith")
    print("How do you do?")
    print("is't weather nice today?")
greet()

# function with inputs
def greet_with_input(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("is't weather nice today?")
greet_with_input("rakshith")

# positional parameter
def greet_with_input(name, location):
    print(f"Hello {name}") 
    print(f"How do you do {name}?")
    print(f"is't weather nice today in {location}?")
greet_with_input("rakshith", "hyd")

## keyword argument
def greet_with_input(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"is't weather nice today in {location}?")
greet_with_input(name="rakshith", location="hyd")
    
