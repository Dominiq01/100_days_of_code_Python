from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-290, 260)

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def increase_level(self):
        self.level += 1

    def print_game_over(self):
        self.home()
        self.write("GAME OVER", font=FONT, align="center")
