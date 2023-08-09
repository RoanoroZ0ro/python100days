import turtle as t

tim = t.Turtle()

for i in range(30):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = t.Screen()
screen.exitonclick()