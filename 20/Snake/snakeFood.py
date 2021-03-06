from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_food_position()

    def refresh_food_position(self):
        random_position_x = random.randint(-280, 280)
        random_position_y = random.randint(-280, 280)
        self.goto(random_position_x, random_position_y)
