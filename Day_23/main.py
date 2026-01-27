import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
game_is_on = True
cars = car_manager.cars

screen.listen()
screen.onkeypress(key="Up",fun=player.move)

while game_is_on:
    car_manager.create_car()

    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.fd(car_manager.move_distance)

    # if player goes beyond y > 300 it means he won and is going to the next level



screen.exitonclick()