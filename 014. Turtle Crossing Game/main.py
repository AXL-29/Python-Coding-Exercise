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

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 25:
            game_is_on = False
    
    if(player.reset_position()):
        car_manager.level_up()

screen.exitonclick()
