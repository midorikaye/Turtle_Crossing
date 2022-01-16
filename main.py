import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()
i = 0
FINISH_LINE_Y = 280
REFLESH_FREQ = 6

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.move()
    i += 1
    if i % REFLESH_FREQ == 0:
        cars.more_car()
    cars.remove_car()

    if turtle.ycor() >= FINISH_LINE_Y:
        turtle.goal()
        scoreboard.addscore()
        cars.step += 10
        REFLESH_FREQ -= 2

    if cars.collision(turtle):
        scoreboard.gameover()
        game_is_on = False

    screen.listen()
    screen.onkey(fun=turtle.player_go, key='Up')

screen.exitonclick()
