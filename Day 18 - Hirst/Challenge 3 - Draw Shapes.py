import turtle as t
import random

tim = t.Turtle()

colours = ["Red", "Green", "Blue", "Orange", "Brown", "Violet", "Yellow", "Gold"]

for i in range(3, 10):
    tim.color(random.choice(colours))
    angle = 360/i
    for j in range(i):
        tim.forward(100)
        tim.right(angle)

screen = t.Screen()
screen.exitonclick()
