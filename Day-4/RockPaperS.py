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
game_images = [rock, paper, scissors]
print("Let's paly Rock Paper Scissor")
user_choice = int(input("Enter your choice between 0 to till 2\n:"))
if user_choice >= 3 or user_choice < 0:
    print("You have choosesn invalid number. You lost")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer chooses:")
    print(game_images[computer_choice])
    if user_choice == 0  and computer_choice == 2:
        print("You won!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Wins!")
    elif computer_choice > user_choice:
        print("Computer Won!")
    elif user_choice > computer_choice:
        print("You Wins!")
    elif computer_choice == user_choice:
        print("it's draw")

    

