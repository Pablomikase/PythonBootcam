import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Logica de cars
    car_manager.move_cars()
    car_manager.replace_car_if_is_in_last_position()

    if player.is_turtle_in_last_position():
        player.restart_position()
        scoreboard.point()
        car_manager.level_up()

    if car_manager.is_any_car_crushing_with_a(player):
        player.restart_position()
        scoreboard.game_over()

screen.exitonclick()
