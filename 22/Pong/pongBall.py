from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.y_step = 0.5
        self.x_step = 0.5

    def random_move(self):

        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_step *= -1

    def bounce_x(self):
        self.x_step *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()