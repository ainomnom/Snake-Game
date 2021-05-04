from turtle import Turtle

SEGMENT_LENGTH = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            x = -SEGMENT_LENGTH * i
            y = 0
            initial_position = (x, y)
            self.add_segment(initial_position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start = length of snake - 1, stop = 0, step = -1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(SEGMENT_LENGTH)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if abs(self.head.heading() - UP) != 180:
            self.head.setheading(UP)

    def down(self):
        if abs(self.head.heading() - DOWN) != 180:
            self.head.setheading(DOWN)

    def left(self):
        if abs(self.head.heading() - LEFT) != 180:
            self.head.setheading(LEFT)

    def right(self):
        if abs(self.head.heading() - RIGHT) != 180:
            self.head.setheading(RIGHT)
