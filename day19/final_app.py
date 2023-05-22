import turtle as t
from random import shuffle, randint

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

shuffle(colors)

rang = (i for i in range(7))

screen = t.Screen()
screen.setup(width=600, height=400)

turtles = []

def create_turtle():
    turtle = t.Turtle('turtle')
    turtle.speed('slowest')
    turtle.color(colors[next(rang)])
    turtle.penup()
    return turtle

turtles.append(create_turtle())
turtles[-1].goto(x=-280, y=0)

for i in range(1, 4):
    turtles.append(create_turtle())
    y_ = i * 30
    turtles[-1].goto(x=-280, y=y_)

    turtles.append(create_turtle())
    y_ = 0 - i * 30
    turtles[-1].goto(x=-280, y=y_)
exit_game = False
winner = None

while True:
    if exit_game:
        break
    for turtle in turtles:
        distance = randint(0, 10)
        turtle.forward(distance)
        if turtle.position()[0] > 270:
            print('Done')
            winner = turtle
            exit_game = True
            break

print(winner.color())

screen.exitonclick()
