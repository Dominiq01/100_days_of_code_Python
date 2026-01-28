from turtle import Screen
import time

from Day_20_and_21.scoreboard import Scoreboard
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.head_north)
screen.onkey(key="Down", fun=snake.head_south)
screen.onkey(key="Left", fun=snake.head_west)
screen.onkey(key="Right", fun=snake.head_east)

while game_is_on:
    scoreboard.print_score()
    screen.update()
    time.sleep(.1)
    snake.move()
    distance = food.distance(snake.head)
    head_x = int(snake.head.xcor())
    head_y = int(snake.head.ycor())
    if distance < 15:
        food.refresh()
        scoreboard.add_to_score()
        snake.extend_body()
    if head_x > 290 or head_x < -300 or head_y > 300 or head_y < -290:
        scoreboard.reset()
        snake.reset()
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()