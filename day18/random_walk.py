from random import choice
from turtle import Turtle, Screen
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = list(range(0, 360, 90))

mic = Turtle()
mic.width(5)

for _ in range(200):
    mic.color(choice(colors))
    direction = choice(directions)
    mic.setheading(direction)

    mic.forward(30)
    
screen = Screen()
screen.exitonclick()
