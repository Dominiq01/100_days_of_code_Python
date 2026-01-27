from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.resizemode("user")
        self.width(20)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(x=position[0], y=position[1])
        self.color("white")

    def move_paddle_up(self):
        self.setheading(90)
        self.fd(20)

    def move_paddle_down(self):
        self.setheading(270)
        self.fd(20)