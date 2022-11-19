from turtle import Turtle
import random

UP = 1
DOWN = -1
RIGHT = 1
LEFT = -1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_dir = random.choice([RIGHT, LEFT])
        self.y_dir = random.choice([UP, DOWN])

    def move(self):
        new_x = self.xcor() + .3 * self.x_dir
        new_y = self.ycor() + 1 * self.y_dir
        self.goto(new_x, new_y)

    def wall_bounce(self):
        if self.ycor() >= 290:
            self.y_dir = DOWN
        if self.ycor() <= -290:
            self.y_dir = UP

    def paddle_bounce(self):
        if self.xcor() >= 0:
            self.x_dir = LEFT
        if self.xcor() <= 0:
            self.x_dir = RIGHT
