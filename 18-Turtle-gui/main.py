# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy_the_turtle.color(c)
#         timmy_the_turtle.forward(steps)
#         timmy_the_turtle.right(30)

# from turtle import *
# from turtle import Screen 

# t = Screen()
# t.title('Object-oriented turtle demo')

# steps = 20
# while True:
#     step = 0
#     while step < steps:
#         for c in ('orange', 'white'):
#             color(c)
#             forward(step)
#         print(step)
#         step += 1

#     steps += 1

# t.exitonclick()


import turtle as t
import random

tim = t.Turtle()
scr = t.Screen()

colours = ["black", "navy", "green", "magenta", "red", "yellow"]
def sketch(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape in range(3, 10):
    tim.color(random.choice(colours))
    sketch(shape)
scr.exitonclick()