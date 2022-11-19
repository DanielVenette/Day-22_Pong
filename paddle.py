from turtle import Turtle


class Paddle(Turtle):

    # set up paddle
    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(coordinates)

    def move_up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 20)
            print(self.ycor())
            # screen.update()

    def move_down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 20)
            print(self.ycor())
            # screen.update()
