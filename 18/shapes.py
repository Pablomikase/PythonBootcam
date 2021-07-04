from turtle import Turtle

tortu = Turtle()

for x in range (3,8):
    angle =360-  360/x
    for y in range(x):
        tortu.forward(100)
        tortu.right(angle)