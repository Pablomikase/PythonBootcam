from turtle import Turtle, Screen

# Variables definition
tortu = Turtle()
my_screen = Screen()
default_step = 10
default_degree = 10


def move_forwards():
    tortu.forward(default_step)


def move_backwards():
    tortu.backward(default_step)


def turn_left():
    tortu.left(default_degree)


def turn_right():
    tortu.right(default_degree)


my_screen.listen()

my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.exitonclick()