import time
from turtle import Screen
from Day_22.paddle import Paddle
from Day_22.scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_paddle_up)
screen.onkeypress(key="Down", fun=r_paddle.move_paddle_down)
screen.onkeypress(key="w", fun=l_paddle.move_paddle_up)
screen.onkeypress(key="s", fun=l_paddle.move_paddle_down)
while game_is_on:
    scoreboard.write_score()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_pos()
        scoreboard.increase_l_score()
    elif ball.xcor() < -400:
        ball.reset_pos()
        scoreboard.increase_r_score()


    # if ((ball.distance(r_paddle) <= 20 or
    #      ball.distance(x=r_paddle.xcor(), y=r_paddle.ycor() - 50) < 30 or
    #      ball.distance(x=r_paddle.xcor(), y=r_paddle.ycor() + 50)) < 30 and
    #         (r_paddle.ycor() - 50 < ball.ycor() < r_paddle.ycor() + 50)):
    #
    #     if r_paddle.ycor() - 50 < ball.ycor() < r_paddle.ycor():
    #         ball.setheading(225)
    #
    #     elif r_paddle.ycor() < ball.ycor() < r_paddle.ycor() + 50:
    #         ball.setheading(135)
    #
    #     else:
    #         ball.setheading(180)

screen.exitonclick()
