import turtle as t

tim = t.Turtle()
screen = t.Screen()

screen.colormode(255)

def forward():
    tim.forward(20)

def backward():
    tim.backward(20)

def counter_clockwise():
    tim.left(30)
    #current_heading = tim.heading()
    #tim.setheading((current_heading + 90) % 360) 

def clockwise():
    tim.right(30)
    #current_heading = tim.heading()
    #tim.setheading((current_heading + 270) % 360)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def test():
    pass
    #print('Test')

key_functions = {
    'w': forward,
    's': backward,
    'a': counter_clockwise,
    'd': clockwise,
    'c': clear,
}

screen.listen()
for i, f in key_functions.items():
    screen.onkey(fun=f, key=i)

screen.onkeypress(key='a', fun=test)

screen.exitonclick()

