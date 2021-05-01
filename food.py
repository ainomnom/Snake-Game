from turtle import Turtle
from random import randint
from settings import SCREEN_SIZE, FOOD_COLOR

STRETCH = 0.5


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=STRETCH, stretch_len=STRETCH)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-int(SCREEN_SIZE / 2 - 20), int(SCREEN_SIZE / 2 - 20))
        random_y = randint(-int(SCREEN_SIZE / 2 - 20), int(SCREEN_SIZE / 2 - 20))
        self.goto(random_x, random_y)
