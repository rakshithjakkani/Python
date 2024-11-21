print("welcome to treasure finding Game!")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

choice1 = input('This game will be having total of three levels.'
                'Each level gonna be do or die level. And here we gooo..... '
                'Type "Left" or "Right": ').lower()
if choice1 == "left":
    choice2 = input('Greate you crossed first level of the game.'
                    'There is a lake in front of you. Do you wann "swim" or "wait" for the boat ?'
                    'Choose you\'r choice "wait" or "swim": ').lower()
    if choice2 == "wait":
        choice3 = input('Greate! Now you\'re reached to final level of the game.'
                        'There are three doors in front of you "red", "yellow", "green". Which door you wanna open'
                        'Pick it carefully, otherwise you\'ll be lose the game: ').lower()
        if choice3 == "red":
            print("you are cought up with the fire. Game over!")
        elif choice3 == "yellow":
            print("There are bunch of flowers. Game over!")
        elif choice3 == "green":
            print("Woahhhhhhh..... You won the game...!")
        else:
            print("you have entered invalid door")

    else:
        print("Sorry! there are snakes in the lake. You're dead.")


else:
    print("Sorry you're fell into dark hole")