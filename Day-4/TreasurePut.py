# Line1 = ["  "," "," "]
# Line2 = ["  "," "," "]
# Line3 = ["  "," "," "]
# map = [Line1,Line2,Line3]
# print("Hiding your treasure! X marks the spot.")
# Position = input() # where do you want to put the treasure
# letter = Position[0].lower()
# abc = ["a","b","c"]
# letter_index = abc.index(letter)
# number_index = int(Position[1]) - 1
# map[number_index][letter_index] = "X"

# print(f"{Line1}\n{Line2}\n{Line3}")


line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]

print("Here we go, X marks your treasure position")
position = input("where you want to put in metrics like A1, B2 and C3\n:")
letter = position[0].lower()
number = int(position[1]) - 1
abc = ["a","b","c"]
letter_position = abc.index(letter)
map = [line1,line2,line3]
map[letter_position][number] = "X"

print(f"{line1}\n{line2}\n{line3}")