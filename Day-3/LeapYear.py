year = int(input("which year do you want to check ? :-"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a Leap year")
        else:
            print("It is not a Leap year")   
    else:
        print("It is a Leap Year")
else:
    print("Not a Leap Year")