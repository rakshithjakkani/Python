# This is a code example for nested if else coditions
# print("Hi! Welcome to Roller Coaster")
# height = int(input("What is your height?:-"))

# if height >= 120:
#     print('"Hey hi buddy! Welcome to Roller Coaster have a greate ride"')
#     age = int(input("what is your age?:"))
#     if age > 18:
#         print("You have to pay Rs. 25")
#     else:
#         print("You have to pay Rs. 15")
# else:
#     print("Sorry, You have to grow taller before you can ride.")


# This is a code example for if elif else
print("Hi! Welcome to Roller Coaster")
height = int(input("What is your height?:-"))

if height >= 120:
    print('"Hey hi buddy! Welcome to Roller Coaster have a greate ride"')
    age = int(input("what is your age?:"))
    if age < 12:
        bill = 7
        print("Child tickets Rupees 7")
    elif age < 18:
        bill = 15
        print("Young tickets Rupees 15")
    elif age >= 40 and age <= 55:
        bill = 0
        print("Your free to ride without any ticket. Please go and ride have a great fun.")

    else:
        bill = 25
        print("Adult tickets Rupees 25")
    print("Photo costs 3 Rupees")
    photo = input("Do you want a photo ? Type yes or no :-")
    if photo == "yes":
        # by using += we can add a increment value to the variable.
        bill += 3
    print(f"You need to pay {bill} Rupees")
else:
    print("Sorry, You have to grow taller before you can ride.")






