from turtle import Screen
import time
from snake import Snake
from snakeFood import Food
from snakeScoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Juego de la culebrita")
screen.tracer(0)
segments = []
game_is_on = True

my_snake = Snake()
my_food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.getHead().distance(my_food) < 15:
        my_snake.extend_snake()
        my_food.refresh_food_position()
        scoreboard.increase_score()

    if my_snake.getHead().xcor() > 280 or my_snake.getHead().xcor() < -280 or my_snake.getHead().ycor() > 280 or my_snake.getHead().ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for segment in my_snake.segments[1:]:
        if my_snake.getHead().distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
