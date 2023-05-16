from turtle import Turtle, Screen
from random import choice

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

terry = Turtle()

for i in range(3, 15):
    terry.color(choice(colors))
    for _ in range(i):
        terry.forward(60)
        terry.right(360 / i)

screen = Screen()
screen.exitonclick()
