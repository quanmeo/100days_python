#import colorgram
import turtle as t
from random import choice

#colors = colorgram.extract('image.jpg', 30)

color_used = [(226, 229, 235), (244, 237, 222), (243, 234, 240), (232, 242, 237), (192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165), (25, 91, 65), (172, 205, 180)]
t.colormode(255)
screen = t.Screen()
t.speed('fastest')

t.penup()
t.setx(-280)
t.sety(-260)
for _ in range(10):
    for i in range(10):
        t.color(choice(color_used))
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()
        t.forward(60)
    t.penup()
    t.setx(-280)
    t.sety(t.pos()[1] + 55)

screen.exitonclick()
