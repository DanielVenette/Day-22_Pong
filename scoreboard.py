from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.left_score, False, 'center', ("Courier", 40, 'bold'))
        self.goto(100, 230)
        self.write(self.right_score, False, 'center', ("Courier", 40, 'bold'))

    def right_player_point(self):
        self.right_score += 1
        self.update_score()

    def left_player_point(self):
        self.left_score += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"Game Over", False, 'center', ("Courier", 40, 'bold'))

    def countdown(self):
        for number in range(3, -1, -1):
            self.home()
            self.write(number, False, 'center', ("Courier", 40, 'bold'))
            time.sleep(1)
            self.clear()
            self.update_score()
        self.clear()
        self.update_score()
