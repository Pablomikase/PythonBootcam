from turtle import Screen
from pongPaddle import Paddle
from pongBall import Ball
from pongScoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Super PONG game")
screen.tracer(0)


left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350,0)
my_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on = True
my_ball.random_move()

while game_is_on:
    my_ball.random_move()
    screen.update()
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()
    if my_ball.distance(right_paddle) < 50 and my_ball.xcor() > 340:
        my_ball.bounce_x()
    if my_ball.distance(left_paddle) < 50 and my_ball.xcor() < -340:
        my_ball.bounce_x()

    if my_ball.xcor() > 380:
        my_ball.reset_position()
        scoreboard.l_point()

    if my_ball.xcor() < -380:
        my_ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
