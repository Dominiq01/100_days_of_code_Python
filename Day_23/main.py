import time
from turtle import Screen

from Day_23.scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
game_is_on = True
cars = car_manager.cars

screen.listen()
screen.onkeypress(key="Up",fun=player.move)

def spawn_car():
    if game_is_on:
        car_manager.create_car()
        screen.ontimer(spawn_car, 500)

spawn_car()

while game_is_on:
    scoreboard.print_level()
    time.sleep(0.1)
    screen.update()
    for car in cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.print_game_over()
        car.fd(car_manager.move_distance)

    if player.check_win():
        scoreboard.increase_level()
        car_manager.increase_move_distance()



screen.exitonclick()