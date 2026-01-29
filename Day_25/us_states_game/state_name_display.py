from turtle import Turtle


class StateNameDisplay(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()


    def display_name(self, state_coords, state_name):
        self.goto(state_coords)
        self.write(state_name)
