import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
extra_char = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

no_of_letters = int(input("enter the no. of letters in password\n"))
no_of_numbers = int(input("Enter the no. of numbers in password\n"))
no_of_extra = int(input("Enter the no. of numbers in password\n"))

# password = ""

# for char in range(1, no_of_letters + 1):
#     password += random.choice(letters)

# for symbols in range(1, no_of_extra + 1):
#     password += random.choice(extra_char)

# for number in range(1, no_of_numbers + 1):
#     password += random.choice(numbers)

# print(password)


####---complicated---########

password_list = []

for char in range(1, no_of_letters + 1):
    password_list += random.choice(letters)

for symbols in range(1, no_of_extra + 1):
    password_list += random.choice(extra_char)

for number in range(1, no_of_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"This is your password: {password}")




