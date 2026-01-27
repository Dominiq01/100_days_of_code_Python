import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.fd(self.move_distance)

    def increase_move_distance(self):
        self.move_distance += MOVE_INCREMENT

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.goto(x=320, y=random.randint(-300, 300))
        self.cars.append(new_car)
