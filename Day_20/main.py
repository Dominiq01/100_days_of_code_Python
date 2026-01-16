from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
start_x = 0
snake = []
for _ in range(3):
    body_part = Turtle(shape="square")
    body_part.color("white")
    body_part.penup()
    body_part.goto(x=start_x, y=0)
    start_x -= 20
    snake.append(body_part)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    prev_pos = snake[0].pos()
    for segment_num in reversed(range(0, len(snake))):
        snake[segment_num].goto(prev_pos)
        prev_pos = snake[segment_num].pos()






screen.exitonclick()