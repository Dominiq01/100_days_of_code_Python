from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)

    def increase_r_score(self):
        self.score_r += 1

    def increase_l_score(self):
        self.score_l += 1

    def write_score(self):
        self.clear()
        self.write(f"{self.score_r}    {self.score_l}",
                   align="center", move=False, font=('Courier New', 18, 'bold'))
