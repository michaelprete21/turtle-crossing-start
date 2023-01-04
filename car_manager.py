from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
car_coordinates = [(300, 250), (300, 200), (300, 150), (300, 100), (300, 50), (300, -50), (300, -100),
                   (300, -150), (300, -200)]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def move_cars(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)

    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setposition(random.choice(car_coordinates))
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1.5, stretch_len=2.5)
        self.all_cars.append(new_car)

    def clear_fleet(self):
        for car in self.all_cars:
            car.setpos(10000, 10000)
        self.all_cars = []

