from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
STARTING_NUMS_OF_CARS = 10


class CarManager():
    def __init__(self):
        self.car = []
        self.cars()
        self.step = STARTING_MOVE_DISTANCE

    def cars(self):
        for i in range(0, STARTING_NUMS_OF_CARS):
            self.newcar()

    def move(self):
        for i in range(0, len(self.car)):
            self.car[i].forward(self.step)

    def newcar(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(280, 20 * random.randint(-25, 25))
        new_car.setheading(180)
        self.car.append(new_car)

    def more_car(self):
        self.newcar()

    def remove_car(self):
        for i in self.car:
            if i.xcor() <= -330:
                i.clear()
                self.car.remove(i)

    def collision(self, player):
        for i in self.car:
            if i.distance(player.position()) <= 20:
                return True
