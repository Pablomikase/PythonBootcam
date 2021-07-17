from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.restart_position()
        self.setheading(90)

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_turtle_in_last_position(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def restart_position(self):
        self.goto(STARTING_POSITION)
