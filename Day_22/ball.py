from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.setheading(45)
        # self.topWall = False
        # self.bottomWall = False
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)
    # def bounce(self):
    #     x = self.xcor()
    #
    #     if self.topWall:
    #         if x > 0:
    #             self.setheading(315)
    #         else:
    #             self.setheading(225)
    #     elif self.bottomWall:
    #         if x > 0:
    #             self.setheading(45)
    #         else:
    #             self.setheading(135)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def reset_pos(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1
