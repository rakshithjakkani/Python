# import turtle
# import rakshith
# print(rakshith.rakshith)

# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(200)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Mumbai Places", ["merin drive", "zoho beach", "colaba stree"])
table.add_column("Mumbai Restaurents", ["Colaba", "Veronika's", "Foodies"])
table.align = 'l'
print(table.sortby)
