from turtle import Screen
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


game_is_on = True


snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.head_north)
screen.onkey(key="Down", fun=snake.head_south)
screen.onkey(key="Left", fun=snake.head_west)
screen.onkey(key="Right", fun=snake.head_east)

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()



screen.exitonclick()