from turtle import Turtle

SNAKE_LENGTH = 3

class Snake:
    def __init__(self):
        self.start_x = 0
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def move_forward(self):
        self.head.fd(20)

    def head_north(self):
        if int(self.head.heading()) == 270:
            return
        self.head.setheading(90)

    def head_south(self):
        if int(self.head.heading()) == 90:
            return
        self.head.setheading(270)

    def head_east(self):
        if int(self.head.heading()) == 180:
            return
        self.head.setheading(0)

    def head_west(self):
        if int(self.head.heading()) == 0:
            return
        self.head.setheading(180)

    def create_snake(self):
        for _ in range(SNAKE_LENGTH):
            body_part = Turtle(shape="square")
            body_part.color("white")
            body_part.penup()
            body_part.goto(x=self.start_x, y=0)
            self.start_x -= 20
            self.snake.append(body_part)

    def move(self):
        prev_pos = self.snake[0].pos()

        for segment_num in range(0, len(self.snake)):
            curr_pos = self.snake[segment_num].pos()
            self.snake[segment_num].goto(prev_pos)
            prev_pos = curr_pos

        self.move_forward()