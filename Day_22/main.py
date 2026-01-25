from turtle import Screen
from Day_22.paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

game_is_on = True


screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_paddle_up)
screen.onkey(key="Down", fun=r_paddle.move_paddle_down)
screen.onkey(key="w", fun=l_paddle.move_paddle_up)
screen.onkey(key="s", fun=l_paddle.move_paddle_down)
while game_is_on:
    screen.update()


screen.exitonclick()