import time
from turtle import Screen
from Day_22.paddle import Paddle
from ball import Ball
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
game_is_on = True


screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_paddle_up)
screen.onkey(key="Down", fun=r_paddle.move_paddle_down)
screen.onkey(key="w", fun=l_paddle.move_paddle_up)
screen.onkey(key="s", fun=l_paddle.move_paddle_down)
while game_is_on:
    time.sleep(.1)
    ball.move()
    screen.update()

    if ball.ycor() > 280:
        ball.topWall = True
        ball.bounce()
    elif ball.ycor() < -270:
        ball.bottomWall = True
        ball.bounce()

    if ball.distance(r_paddle) > 320 and (r_paddle.ycor() - 50 < ball.ycor() < r_paddle.ycor() + 50):
        ball.setheading(225)

    print(r_paddle.xcor() - 50)


screen.exitonclick()