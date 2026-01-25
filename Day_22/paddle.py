from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.paddle.penup()
        self.paddle.speed("fastest")
        self.paddle.shape("square")
        self.paddle.resizemode("user")
        self.paddle.width(20)
        self.paddle.turtlesize(stretch_wid=1, stretch_len=5)
        self.paddle.setheading(90)
        self.paddle.goto(x=position[0], y=position[1])
        self.paddle.color("white")

    def move_paddle_up(self):
        self.paddle.setheading(90)
        self.paddle.fd(20)

    def move_paddle_down(self):
        self.paddle.setheading(270)
        self.paddle.fd(20)