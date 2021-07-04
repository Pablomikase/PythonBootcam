import turtle
from turtle import Turtle
import random

turtle.colormode(255)
turtle.speed("fastest")
tortu = Turtle()


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for degree in range(0,360, 2):
    tortu.color(generate_random_color())
    turtle.pencolor(generate_random_color())
    turtle.right(degree)
    turtle.circle(100)