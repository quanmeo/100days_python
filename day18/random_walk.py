from random import choice
from turtle import Turtle, Screen
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

mic = Turtle()
mic.width(5)

for _ in range(200):
    mic.color(choice(colors))
    direction = choice(list(range(4)))
    if direction == 0:
        mic.right(0)
    elif direction == 1:
        mic.right(90)
    elif direction == 2:
        mic.right(180)
    else:
        mic.left(90)

    mic.forward(30)
    
screen = Screen()
screen.exitonclick()
