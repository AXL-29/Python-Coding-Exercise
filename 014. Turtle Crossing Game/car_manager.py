"""
Handles car creation, movement, and speed control.
"""

import random
from turtle import Turtle


# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_CHANCE = 3

class CarManager(Turtle):
    """Manage cars: create, move, remove, and speed up."""

    def __init__(self):
        """Initialize car manager."""
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_counter = 0

    def create_car(self):
        """Create a new car at random y position."""
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(320, random.randint(-240, 260))
        car.setheading(180)
        self.cars.append(car)

    def spawn_car(self):
        """Spawn a car based on spawn counter."""
        self.spawn_counter += 1
        if self.spawn_counter >= SPAWN_CHANCE:
            self.create_car()
            self.spawn_counter = 0

    def move_cars(self):
        """Move cars and remove those off-screen."""
        for car in self.cars[:]:
            car.forward(self.car_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    def level_up(self):
        """Increase car speed for next level."""
        self.car_speed += MOVE_INCREMENT
