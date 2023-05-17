from random import choice, randint
import turtle as t

def generate_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)

directions = list(range(0, 360, 90))

screen = t.Screen()
mic = t.Turtle()
mic.width(5)

t.colormode(255)

for _ in range(200):
    mic.color(generate_rgb())

    direction = choice(directions)
    mic.setheading(direction)

    mic.forward(30)

screen.exitonclick()
