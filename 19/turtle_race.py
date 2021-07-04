from turtle import Turtle, Screen
import random

tortu = Turtle()
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Haz tus apuestas", prompt="Qué tortuga ganará la carrera? Ingresa un color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
starting_x_point = -230
starting_y_point = -100
is_the_race_active = True
winner = ""


# function definition
def create_turtle(color):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    return new_turtle


def create_set_of_turtles():
    for turtle_color in colors:
        turtles.append(create_turtle(turtle_color))


def set_turtles_position():
    global starting_y_point
    for my_turtle in turtles:
        my_turtle.goto(x=starting_x_point, y=starting_y_point)
        starting_y_point += 50


def generate_a_random_distance():
    return random.randint(0, 5)


def go_forward(this_turtle):
    this_turtle.forward(generate_a_random_distance())


def release_turtles():
    while is_the_race_active:
        for this_turtle in turtles:
            go_forward(this_turtle)
        check_if_the_race_continue()


def check_if_the_race_continue():
    global turtles
    global is_the_race_active
    for turtle in turtles:
        x_pos = turtle.xcor()
        if x_pos > 99:
            print(f"The turtle {turtle}")
            is_the_race_active = False


def set_the_winner():
    global winner
    for current_turtle in turtles:
        if current_turtle.xcor() > 99:
            winner = current_turtle.fillcolor()


create_set_of_turtles()
set_turtles_position()
release_turtles()
set_the_winner()
print(f"The winner is the: {winner}")
if user_bet == winner:
    print("YOU WON :D")
else:
    print("you LOOSE :(")

screen.exitonclick()
