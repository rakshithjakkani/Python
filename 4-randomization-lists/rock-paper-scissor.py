import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
icon = [rock, paper, scissors]
user_choice = int(input("Enter a number according to rock=0, paper=1, and scissors=2\n:"))
print(icon[user_choice])
computer_choice = random.randint(0, 2)
print("computer choosed:")
print(icon[computer_choice])

if user_choice > 2 or user_choice < 0:
    print("You entered an invalid number. You lose!")
elif user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 2:
    print("You won!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You won!")