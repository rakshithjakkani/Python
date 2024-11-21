print("Hi welcome to rollercoaster")
height = int(input("what is your height in cm ?: "))
bill = 0

if height >= 120:
    print("you can ride a rollercoaster")
    age = int(input("what is your age ?: "))
    if age >= 45 and age <= 55:
        print("Everything is gonna be okay. Have a free ride on us!")
    elif age < 12:
        bill = 7
    elif age >= 12 and age < 18:
        bill = 12
    else: 
        bill = 20
    
    photo = input("do you want a picture on rollercoaster ? if yes, type y if not type n: ")
    if photo == "y":
        bill += 3
    print(f"your final bill would be ${bill}")

else:
    print("sorry you need to grow up to ride a rollercoaster")