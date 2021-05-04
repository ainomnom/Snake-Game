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
        with open("high_score.txt") as high_score:
            self.high_score = int(high_score.read())
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align=TEXT_ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.display_score()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.display_score()

    def game_over(self):
        self.reset()
        self.goto(0, 0)
        self.write("GAME OVER", align=TEXT_ALIGNMENT, font=FONT)
