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
    
    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(320, random.randint(-260, 280))
        new_car.setheading(180)
        self.cars.append(new_car)
    
    def spawn_car(self):
        if random.randint(1, SPAWN_CHANCE) == 1:
            self.create_car()

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)
        
