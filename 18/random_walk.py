import turtle
from turtle import Turtle
import random

turtle.colormode(255)
tortu = Turtle()
tortu.pensize(10)
colors = ["red", "blue", "black", "green", "yellow", "grey", "pink"]
degrees =[0, 90, 180, 270]

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

for _ in range(200):
    tortu.color(generate_random_color())
    tortu.forward(30)
    tortu.right(random.choice(degrees))