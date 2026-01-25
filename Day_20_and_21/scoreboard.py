from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.print_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(x=0, y=280)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Arial', 12, 'normal'))

    def add_to_score(self):
        self.score += 1

    def print_score(self):
        self.clear()
        self.write(f"Score:  {self.score}", False, align="center", font=('Arial', 12, 'normal'))