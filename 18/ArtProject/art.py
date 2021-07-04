import turtle
from turtle import Turtle
import random

turtle.colormode(255)
tortu = Turtle()
color_list = [(67, 90, 135), (28, 35, 62), (66, 25, 68), (132, 67, 116), (123, 154, 202), (54, 48, 105), (101, 37, 91), (200, 129, 175), (108, 108, 180), (185, 88, 150), (10, 48, 39), (244, 215, 239), (205, 214, 240), (173, 175, 231), (222, 138, 111), (61, 156, 174), (36, 123, 106), (231, 164, 213), (158, 74, 52), (246, 220, 209), (48, 176, 160), (25, 82, 91), (19, 90, 71), (204, 93, 76), (79, 204, 187), (236, 170, 159), (239, 251, 249), (114, 222, 212), (127, 219, 231), (238, 203, 118)]
tortu.pensize(10)
tortu.penup()
myScreen = turtle.Screen()
tortu.speed("fastest")

x_start_position = -500
y_start_position = -500

for x in range (0,1000, 50):
    for y in range (0,1000, 50):
        tortu.setx(x_start_position + x)
        tortu.sety(y_start_position + y)
        tortu.dot(random.choice(color_list))