import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_CHANCE = 3

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_counter = 0

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(320, random.randint(-240, 280))
        new_car.setheading(180)
        self.cars.append(new_car)
    
    def spawn_car(self):
        self.spawn_counter += 1
        if self.spawn_counter >= SPAWN_CHANCE:
            self.create_car()
            self.spawn_counter = 0

    def move_cars(self):
        for car in self.cars[:]:  # iterate over a copy
            car.forward(self.car_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT