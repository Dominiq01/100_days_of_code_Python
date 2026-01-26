from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.setheading(0)
        self.topWall = False
        self.bottomWall = False

    def move(self):
        self.fd(10)

    def bounce(self):
        x = self.xcor()

        if self.topWall:
            # if x > 0:
            #     self.setheading(315)
            # else:
            self.setheading(225)
        elif self.bottomWall:
            # if x > 0:
            #     self.setheading(45)
            # else:
            self.setheading(135)
