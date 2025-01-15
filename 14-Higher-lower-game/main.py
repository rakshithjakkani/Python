# Display the logo
from art import logo, vs
from game_data import data
import random



# Generate a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)
# format account data into printable format.
def format_data(account):
    """format account data into printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_city = account['city']
    return f'{account_name}, a {account_descr}, from {account_city}'
# Ask user for a guess.
print(f"Compare A = {format_data(account_a)}")
print(vs)
print(f"Against B = {format_data(account_b)}")
# Check if user is correct.
user_guess = input("who has the more followers? Type 'A' or 'B':").lower()

# - get the followers of each account
# - use if statement to check if user is correct.

# Give user feedback on their guess.

# Score keeping.

# Make game repeatable.

# Making account position at B become the next account position at A.
