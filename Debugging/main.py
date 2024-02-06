# # Describe the problem 
# def my_function():
#     for i in range(1, 21):
# # in range function bothe the ends could not be counted
#         if i == 20:
#             print("you go it")
# my_function()

# Reproduce the bug
# from random import randint
# dice_list = ["rakshith", "jakkai", "dev", "ops", "python", "minfy"]
# # note that in randint both the ends to be counted 
# # the list count will be 0, 1, 2, 3.....
# dice_num = randint(0, 5)
# print(dice_list[dice_num])

# # Play computer
# year = int(input("What is your birth year: "))
# if year > 1940 and year < 1980:
#     print("your a millenial")
# elif year > 1980:
#     print("your a gen z")

# # fix the error
# age = input("what is your age? ")
# if age > 18:
#     print("your age is {age} allowed to get the driving license")

# use a debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_list = item * 2
#         b_list.append(new_list)
#     print(b_list)
# mutate([1,2,2,3,4])

number = int(input())

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

