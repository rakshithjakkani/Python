year = int(input("Enter the year that you wanna check: "))

def leap_year(user_year):
    if user_year % 4 == 0 and user_year % 100 == 0 and user_year % 400 == 0:
        print("True")
    elif user_year % 4 == 0 and user_year % 100 > 0:
        print("False")
    elif user_year % 4 == 0 and user_year % 100 > 0 and user_year % 400 == 0:
        print("True")
    else: 
        print("False")
leap_year(year)