from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_X_POS = 300
END_X_POS = -310
TOTAL_INITIAL_CARS = 10
car_pack = []


class CarManager:

    def __init__(self):
        self.create_car_pack()

    def create_car_pack(self):
        for x in range(TOTAL_INITIAL_CARS):
            self.add_car_to_the_pack()

    def add_car_to_the_pack(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        self.place_car_in_the_starting_position(new_car)
        car_pack.append(new_car)

    def place_car_in_the_starting_position(self, car):
        car.goto(STARTING_X_POS + random.randint(0, 600), random.randint(-250, 250))

    def move_cars(self):
        for car in car_pack:
            car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())

    def replace_car_if_is_in_last_position(self):
        for car in car_pack:
            if car.xcor() < END_X_POS:
                self.place_car_in_the_starting_position(car)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.add_car_to_the_pack()

    def is_any_car_crushing_with_a(self, player):
        for car in car_pack:
            if car.distance(player) < 15:
                return True
