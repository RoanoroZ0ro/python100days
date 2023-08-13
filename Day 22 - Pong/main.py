from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)
#
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
