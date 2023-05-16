from turtle import Turtle, Screen

tom = Turtle()

for _ in range(10):
    for i in range(2):
        tom.pendown() if i % 2 == 0 else tom.penup()
        tom.forward(10)

screen = Screen()
screen.exitonclick()
