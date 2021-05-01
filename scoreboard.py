from turtle import Turtle
from settings import SCREEN_SIZE, TEXT_ALIGNMENT, FONT


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(SCREEN_SIZE / 2 - 40)
        self.current_score = 0
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.current_score}", align=TEXT_ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=TEXT_ALIGNMENT, font=FONT)
