import turtle as t
from random import choice, randint

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)

for i in range(5, 361, 5):
    tim.color(random_color())
    tim.circle(60)
    tim.setheading(i)

screen = t.Screen()
screen.exitonclick()
