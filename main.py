import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WINNING_SCORE = 3

# set up screen (600x800)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
# do not refresh screen automatically
screen.tracer(0)

# center line
line_painter = Turtle()
line_painter.pencolor("white")
line_painter.pensize(1)
line_painter.hideturtle()
line_painter.penup()
line_painter.goto(0, -300)
line_painter.pendown()
line_painter.setheading(90)
dash_length = 10
for _ in range (int(620/(dash_length*2))):
    line_painter.forward(dash_length)
    line_painter.penup()
    line_painter.forward(dash_length)
    line_painter.pendown()

# create scoreboard:
scoreboard = Scoreboard()

# create paddles:
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create ball and initial direction
ball = Ball()

# listen for key strokes:
screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_is_on = True

# initial countdown
screen.update()
scoreboard.countdown()

game_speed = 0.0005
speed_change = False

while game_is_on:
    #print(game_speed)
    screen.update()
    ball.move()
    time.sleep(game_speed)
    # detect wall collision and change ball direction
    if abs(ball.ycor()) >= 290:
        ball.wall_bounce()
    # detect paddle collision
    if 345 > abs(ball.xcor()) > 335:
        if l_paddle.distance(ball) < 51 or r_paddle.distance(ball) < 51:
            ball.paddle_bounce()
            if not speed_change:
                game_speed *= 0.9
                speed_change = True
    else:
        speed_change = False
    # detect left-player-point
    if ball.xcor() > 400:
        scoreboard.left_player_point()
        r_paddle.goto((350, 0))
        l_paddle.goto((-350, 0))
        ball.home()
        game_speed = 0.0005
        screen.update()
        if scoreboard.left_score < WINNING_SCORE:
            scoreboard.countdown()
        else:
            ball.home()
            scoreboard.game_over()
            game_is_on = False
    # detect right-player-point
    if ball.xcor() < -400:
        scoreboard.right_player_point()
        r_paddle.goto((350, 0))
        l_paddle.goto((-350, 0))
        ball.home()
        game_speed = 0.0005
        screen.update()
        if scoreboard.right_score < WINNING_SCORE:
            scoreboard.countdown()
        else:
            ball.home()
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()
