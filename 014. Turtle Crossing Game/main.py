"""
Main game loop for the Turtle Crossing game.
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# Game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


# Controls
screen.listen()
screen.onkey(player.go_up, "Up")


# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_car()
    car_manager.move_cars()

    # Collision check
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

    # Level up
    if player.reset_position():
        car_manager.level_up()
        scoreboard.increase_level()


# Exit on click
screen.exitonclick()
