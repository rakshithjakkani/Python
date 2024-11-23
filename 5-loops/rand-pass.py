import random
print("Hey welcome to random password generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

user_letters = int(input("Enter the number of letters\n:"))
user_numbers = int(input("Enter the number of numbers\n:"))
user_special_char = int(input("Enter the number of special\n:"))

# collecting the list of letters, numbrs, specials chars into the password and shuffling it 
pass_list = []
for i in range(0, user_letters):
    pass_list.append(random.choice(letters))

for i in range(0, user_numbers):
    pass_list.append(random.choice(numbers))

for i in range(0, user_special_char):
    pass_list.append(random.choice(special_char))
random.shuffle(pass_list)

# rearranging password from list to string
password = ""
for i in pass_list:
    password += i
print(password)



