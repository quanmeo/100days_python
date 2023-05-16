from turtle import Turtle, Screen

tim = Turtle()

for _ in range(4):
    tim.forward(50)
    tim.right(90)

screen = Screen()
screen.exitonclick()
