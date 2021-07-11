from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_DIR = 90
DOWN_DIR = 270
RIGHT_DIR = 0
LEFT_DIR = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def getHead(self):
        return self.segments[0]

    def up(self):
        if self.segments[0].heading() != DOWN_DIR:
            self.segments[0].setheading(UP_DIR)

    def down(self):
        if self.segments[0].heading() != UP_DIR:
            self.segments[0].setheading(DOWN_DIR)

    def left(self):
        if self.segments[0].heading() != RIGHT_DIR:
            self.segments[0].setheading(LEFT_DIR)

    def right(self):
        if self.segments[0].heading() != LEFT_DIR:
            self.segments[0].setheading(RIGHT_DIR)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())